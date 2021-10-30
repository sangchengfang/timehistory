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


def mid_point(coor1, coor2, y3):
    """
    find the x coordinate for the third point x3 in the line defined by (x1, y1) and (x2, y2) given y3
    :param coor1:
    :param coor2:
    :param y3:
    :return: x3
    """
    x1 = float(coor1[0])
    y1 = float(coor1[1])
    x2 = float(coor2[0])
    y2 = float(coor2[1])
    y3 = float(y3)

    x3 = format((y3 - y1) * (x1 - x2) / (y1 - y2) + x1, '.3f')
    return x3


def norm_and_trunc(origin_time_his, max_ice, ice_now):
    # normalize and truncate the time history
    origin_time_his = str(origin_time_his)
    max_ice = float(max_ice)
    ice_now = float(ice_now)

    reserved = dict()
    deleted = dict()
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

        # find the index when the thickness exactly larger than max ice thickness 'max_ice'
        i = 0
        for item in new_thick:
            # print(item)
            if item <= max_ice:
                i = i + 1
            else:
                break

        reserved['res_thick'] = new_thick[0:i + 1]
        deleted['del_thick'] = new_thick[i:]
        reserved['res_time'] = time[0:i + 1]
        deleted['del_time'] = time[i:]

        if reserved['res_thick'][-1] > max_ice > reserved['res_thick'][-2]:
            print('right reserved time history')
            coor1 = (reserved['res_time'][-2], reserved['res_thick'][-2])
            coor2 = (reserved['res_time'][-1], reserved['res_thick'][-1])
            last_time = mid_point(coor1, coor2, max_ice)
            # print(last_time)
            # print(reserved)
            # print(deleted)
            reserved['res_thick'].insert(-1, max_ice)
            reserved['res_time'].insert(-1, last_time)
            reserved['res_norm_thick'] = [item / max_ice for item in reserved['res_thick']]
        else:
            print('wrong reserved time history')
        # print(reserved)
        # print(deleted)
        # print(no_truncate)
    return no_truncate, reserved, deleted


def write_file(file, file_truncated):
    file = str(file)
    file_truncated = str(file_truncated)

    with open(file, 'w') as fop:
        for i in range(len(Gno_truncate['time'])):
            fop.write(str(Gno_truncate['time'][i]).ljust(8))
            fop.write(str(Gno_truncate['norm_thick'][i]))
            fop.write('\n')

    with open(file_truncated, 'w') as fop:
        for i in range(len(Greserved['res_time'])):
            fop.write(str(Greserved['res_time'][i]).ljust(8))
            fop.write(str(format(Greserved['res_thick'][i], '.6f').ljust(14)))
            fop.write(str(format(Greserved['res_norm_thick'][i], '.6f')))
            fop.write('\n')


Gno_truncate, Greserved, Gtruncated = norm_and_trunc('Lambeck_TH_selected.dat', 1000.0, 94.24)
write_file('Lamb_norm_TH.dat', 'Lamb_norm_TH1000.dat')

Gno_truncate, Greserved, Gtruncated = norm_and_trunc('Wanghs_TH.dat', 1000.0, 94.24)
write_file('Whs_norm_TH.dat', 'Whs_norm_TH1000.dat')


