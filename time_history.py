#!/usr/bin/env python3

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

from math import pi


def trunc_point(time, thickness, y3):
    """
    find the x coordinate for the third point x3 in the line defined by (x1, y1) and (x2, y2) given y3
    :param time: the list contains the time
    :param data: the number list that will be truncated
    :param y3:
    :return: xa,xb
    """

    time = list(time)
    thickness = list(thickness)
    y3 = float(y3)

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

    first = dict()
    last = dict()
    deleted = dict()

    first['time'] = time[:i+1]
    first['thick'] = thickness[:i+1]
    last['time'] = time[j:]
    last['thick'] = thickness[j:]
    deleted['time'] = time[i+1:j]
    deleted['thick'] = thickness[i+1:j]

    return first, last, deleted


def norm_and_trunc(origin_time_his, max_ice, ice_now):
    # normalize and truncate the time history
    origin_time_his = str(origin_time_his)
    max_ice = float(max_ice)
    ice_now = float(ice_now)

    no_truncate = dict()

    with open(origin_time_his, 'r') as fip:
        time = list()
        thickness = list()
        for line in fip:
            line = line.split()
            time.append(float(line[0]))
            thickness.append(abs(float(line[1])))
        if len(time) != len(thickness):
            print('Warning, wrong origin time history file, lengths of time and thickness unequal')
        no_truncate['time'] = time

        new_thick = list()
        # new_thick is the origin thickness + nowadays ice thickness in TP
        norm_thickness = list()
        # Normalized new_thick
        for item in thickness:
            item = (item / max(thickness)) * max_ice + ice_now
            new_thick.append(item)
            norm_thickness.append(format(item / (max_ice + ice_now), '.6f'))
        no_truncate['norm_thick'] = norm_thickness
        no_truncate['thick'] = new_thick

    first_part, last_part, deleted = trunc_point(time, new_thick, max_ice)
    first_part['norm_thick'] = [item / max_ice for item in first_part['thick']]
    last_part['norm_thick'] = [item / max_ice for item in last_part['thick']]
    deleted['norm_thick'] = [item / max_ice for item in deleted['thick']]

    # print(first_part)
    # print(last_part)
    # print(deleted)
    # print(no_truncate)

    return no_truncate, first_part, last_part, deleted


def write_file(origin_all, all, first_part, last_part, deleted):
    origin_all = str(origin_all)
    all = str(all)
    first_part = str(first_part)
    last_part = str(last_part)
    deleted = str(deleted)

    with open(origin_all, 'w') as fop:
        for i in range(len(Gall['time'])):
            fop.write(str(Gall['time'][i]).ljust(8))
            fop.write(str(format(float(Gall['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Gall['thick'][i]), '.8f')))
            fop.write('\n')

    with open(all, 'w') as fop:
        for i in range(len(Gfirst_part['time'])):
            fop.write(str(Gfirst_part['time'][i]).ljust(8))
            fop.write(str(format(float(Gfirst_part['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Gfirst_part['thick'][i]), '.8f')))
            fop.write('\n')
        for i in range(len(Glast_part['time'])):
            fop.write(str(Glast_part['time'][i]).ljust(8))
            fop.write(str(format(float(Glast_part['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Glast_part['thick'][i]), '.8f')))
            fop.write('\n')

    with open(first_part, 'w') as fop:
        for i in range(len(Gfirst_part['time'])):
            fop.write(str(Gfirst_part['time'][i]).ljust(8))
            fop.write(str(format(float(Gfirst_part['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Gfirst_part['thick'][i]), '.8f')))
            fop.write('\n')

    with open(last_part, 'w') as fop:
        for i in range(len(Glast_part['time'])):
            fop.write(str(Glast_part['time'][i]).ljust(8))
            fop.write(str(format(float(Glast_part['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Glast_part['thick'][i]), '.8f')))
            fop.write('\n')

    with open(deleted, 'w') as fop:
        for i in range(len(Gdeleted['time'])):
            fop.write(str(Gdeleted['time'][i]).ljust(8))
            fop.write(str(format(float(Gdeleted['norm_thick'][i]), '.8f')).ljust(12))
            fop.write(str(format(float(Gdeleted['thick'][i]), '.8f')))

            fop.write('\n')




Gall, Gfirst_part, Glast_part, Gdeleted = norm_and_trunc('Lambeck_TH_selected.dat', 1000.0, 94.24)
write_file('Lamb_norm_TH.dat', 'Lamb_norm_TH_plateau.dat', 'Lamb_norm_TH_first.dat', 'Lamb_norm_TH_last.dat', 'Lamb_norm_TH_delete.dat')

Gall, Gfirst_part, Glast_part, Gdeleted = norm_and_trunc('Wanghs_TH.dat', 1000.0, 94.24)
write_file('Whs_norm_TH.dat', 'Whs_norm_TH_plateau.dat', 'Whs_norm_TH_first.dat', 'Whs_norm_TH_last.dat', 'Whs_norm_TH_delete.dat')




