#!/usr/bin/env python3

# generate the ice time history based on time history from Wang Hansheng.((( Wang, H. (2001). Effects of glacial
# isostatic adjustment since the late Pleistocene on the uplift of the Tibetan Plateau. Geophysical Journal
# International,144(2), 448–458. https://doi.org/10.1046/j.1365-246x.2001.00340.x )))
# and Lembeck.(((Lambeck, K., Rouby, H., Purcell, A., Sun, Y., & Sambridge, M. (2014). Sea level and global ice volumes
# from the Last Glacial Maximum to the Holocene. Proceedings of the National Academy of Sciences, 111(43), 15296–15303.
# https://doi.org/10.1073/pnas.1411762111)))

# The recent glacier change results are from Wang Qiuyu
# Wang, Q., Yi, S., & Sun, W. (2021).Continuous estimates of glacier mass balance in High Mountain Asia
# based on ICESat-1,2 and GRACE/GRACE Follow-On data. Geophysical Research Letters, 48, e2020GL090954.
# https://doi.org/10.1029/2020GL090954

# 2021.11.11, now the time history of ice thickness has been flipped, so the last part is actually the first part.
# That is last part is early in loading history, the largest time means the end of the ice loading
# zero means the start of ice loading.

# Since the time is increase from 0 to largest time, So if we want study the effect of old ice, we need the last part,
# rather than the first part.

def trunc_point(time, thickness, y3):
    """
    find the x coordinate for the third point x3 in the line defined by (x1, y1) and (x2, y2) given y3
    :param time: the list contains the time
    :param thickness: the number list that will be truncated
    :param y3:
    :return: xa,xb
    """

    time = list(time)
    thickness = list(thickness)
    y3 = float(y3)

    first = dict()
    last = dict()
    deleted = dict()

    # find the index when the thickness exactly larger than max ice thickness 'max_ice'
    # index could be one or two.
    trunc_index = list()
    i = 0

    for item in thickness:
        item = float(item)
        if item <= y3:
            i = i + 1
        else:
            trunc_index.append(i)
            break
    # print(i)
    j = -1
    for item in reversed(thickness):
        # print(item)
        if item < y3:
            j = j - 1
        else:
            trunc_index.append(j)
            break
    # print(j)

    first_x1 = float(time[i-1])
    first_y1 = float(thickness[i-1])
    first_x2 = float(time[i])
    first_y2 = float(thickness[i])

    last_x1 = float(time[j])
    last_y1 = float(thickness[j])
    last_x2 = float(time[j+1])
    last_y2 = float(thickness[j+1])

    first_x3 = float(format((y3 - first_y1) * (first_x1 - first_x2) / (first_y1 - first_y2) + first_x1, '.3f'))
    last_x3 = float(format((y3 - last_y1) * (last_x1 - last_x2) / (last_y1 - last_y2) + last_x1, '.3f'))
    # print(first_x3)
    # print(last_x3)

    time.insert(i, first_x3)
    time.insert(j+1, last_x3)
    thickness.insert(i, y3)
    thickness.insert(j+1, y3)

    first['time'] = time[:i+1]
    first['thick'] = thickness[:i+1]
    last['time'] = time[j:]
    last['thick'] = thickness[j:]
    # last['time'] = time[:i+1]
    # last['thick'] = thickness[:i+1]
    # first['time'] = time[j:]
    # first['thick'] = thickness[j:]
    deleted['time'] = time[i+1:j]
    deleted['thick'] = thickness[i+1:j]

    return first, last, deleted


def norm_and_trunc(origin_time_his, max_ice, ice_now):
    # normalize and truncate the time history

    origin_time_his = str(origin_time_his)
    max_ice = float(max_ice)
    ice_now = float(ice_now)

    origin_all = dict()
    new_thick = list()
    # new_thick is the origin thickness + nowadays ice thickness in TP
    norm_thickness = list()
    # Normalized new_thick

    with open(origin_time_his, 'r') as fip:
        time = list()
        thickness = list()
        for line in fip:
            line = line.split()
            time.append(float(line[0]))
            thickness.append(abs(float(line[1])))
        if len(time) != len(thickness):
            print('Warning, wrong origin time history file, lengths of time and thickness unequal')
        origin_all['time'] = time

        for item in thickness:
            item = (item / max(thickness)) * max_ice + ice_now
            new_thick.append(item)
            # norm_thickness.append(format(item / (max_ice + ice_now), '.6f'))
            # norm_thickness.append(format(item / max_ice, '.6f'))
        # origin_all['norm_thick'] = norm_thickness
        origin_all['thick'] = new_thick

        return origin_all


def norm_time_his(thick):
    thick = list(thick)
    norm_thick = list()

    for item in thick:
        norm_thick.append(item / max(thick))

    return norm_thick


def write_file(time_his, filename):
    filename = str(filename)
    with open(filename, 'w') as fop:
        for i in range(len(time_his['time'])):
            fop.write(str(time_his['time'][i]).ljust(8))
            fop.write(str(format(float(time_his['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(time_his['thick'][i]), '.8f')))
            fop.write('\n')


L_origin_all = norm_and_trunc('Lambeck_TH_selected_abs_flipped.dat', 1000.0, 94.24)
L_origin_all['norm_thick'] = norm_time_his(L_origin_all['thick'])
L_first_part, L_last_part, L_deleted = trunc_point(L_origin_all['time'], L_origin_all['thick'], 1000)
L_first_part['norm_thick'] = norm_time_his(L_first_part['thick'])
L_last_part['norm_thick'] = norm_time_his(L_last_part['thick'])
L_deleted['norm_thick'] = norm_time_his(L_deleted['thick'])

write_file(L_origin_all, 'Lamb_norm_TH.dat')

L_plateau = dict()
for item in ['time', 'thick', 'norm_thick']:
    L_plateau[item] = L_first_part[item] + L_last_part[item]
write_file(L_plateau, 'Lamb_norm_TH_plateau.dat')

if float(L_last_part['time'][0]) != 0:
    first_time = L_last_part['time'][0]
    for i in range(len(L_last_part['time'])):
        L_last_part['time'][i] = format(float(L_last_part['time'][i]) - first_time, '.3f')
write_file(L_last_part, 'Lamb_norm_TH_last.dat')

write_file(L_first_part, 'used/Lamb_norm_TH_first.dat')
write_file(L_deleted, 'used/Lamb_norm_TH_delete.dat')


W_origin_all = norm_and_trunc('Wanghs_TH_flipped.dat', 1000.0, 94.24)
W_origin_all['norm_thick'] = norm_time_his(W_origin_all['thick'])
W_first_part, W_last_part, W_deleted = trunc_point(W_origin_all['time'], W_origin_all['thick'], 1000)
W_first_part['norm_thick'] = norm_time_his(W_first_part['thick'])
W_last_part['norm_thick'] = norm_time_his(W_last_part['thick'])
W_deleted['norm_thick'] = norm_time_his(W_deleted['thick'])

write_file(W_origin_all, 'Whs_norm_TH.dat')

W_plateau = dict()
for item in ['time', 'thick', 'norm_thick']:
    W_plateau[item] = W_first_part[item] + W_last_part[item]
write_file(W_plateau, 'Whs_norm_TH_plateau.dat')

if float(W_last_part['time'][0]) != 0:
    first_time = W_last_part['time'][0]
    for i in range(len(W_last_part['time'])):
        W_last_part['time'][i] = format(float(W_last_part['time'][i]) - first_time, '.3f')
write_file(W_last_part, 'Whs_norm_TH_last.dat')

write_file(W_first_part, 'used/Whs_norm_TH_first.dat')
write_file(W_deleted, 'used/Whs_norm_TH_delete.dat')
