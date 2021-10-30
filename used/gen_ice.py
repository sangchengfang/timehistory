#!/usr/bin/env python3

# generate the ice time of Tibet Plateau based on glacier change results from Wang Qiuyu
# Wang, Q., Yi, S., & Sun, W. (2021).Continuous estimates of glacier mass balance in High Mountain Asia
# based on ICESat-1,2 and GRACE/GRACE Follow-On data. Geophysical Research Letters, 48, e2020GL090954. 
# https://doi.org/10.1029/2020GL090954

from math import pi

fop = open('./tp_ice.dat', 'w')
fop.write('82\n\n')
fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        # m = re.match("^Number of observations:\s*(\d+)",line)
        # line.split('\n\t')
        data = line.split(' ')
        # print(line)
        # print(data)
        fop = open('./tp_ice.dat', 'a')
        fop.write('10 0 6\n')
        fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
        fop.write('1000\n')
        fop.write('92 3\n')
        fop.write('0 0.017 19.6 92\n')
        if float(data[2]) > 0:
            fop.write(str(float(data[2]) * 17 * 4/pi) + ' 0' + ' 1000 0\n\n')
        else:
            fop.write('0 ' + str(abs(float(data[2])*17*4/pi)) + ' 1000 0\n\n')
        # fop.writelines(data)
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 65 < float(data[0]) < 83 and 33 < float(data[1]) < 40:
            fop = open('./small_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('2000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 2) + ' 0' + ' 2000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 2)) + ' 2000 0\n\n')
        else:
            pass
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 70 < float(data[0]) < 75 and 35 < float(data[1]) < 40:
            fop = open('./smaller_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('5000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 5) + ' 0' + ' 5000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 5)) + ' 5000 0\n\n')
        else:
            pass
        fop.close()#!/usr/bin/env python3

# generate the ice time of Tibet Plateau based on glacier change results from Wang Qiuyu
# Wang, Q., Yi, S., & Sun, W. (2021).Continuous estimates of glacier mass balance in High Mountain Asia
# based on ICESat-1,2 and GRACE/GRACE Follow-On data. Geophysical Research Letters, 48, e2020GL090954.
# https://doi.org/10.1029/2020GL090954

from math import pi

fop = open('./tp_ice.dat', 'w')
fop.write('82\n\n')
fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        # m = re.match("^Number of observations:\s*(\d+)",line)
        # line.split('\n\t')
        data = line.split(' ')
        # print(line)
        # print(data)
        fop = open('./tp_ice.dat', 'a')
        fop.write('10 0 6\n')
        fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
        fop.write('1000\n')
        fop.write('92 3\n')
        fop.write('0 0.017 19.6 92\n')
        if float(data[2]) > 0:
            fop.write(str(float(data[2]) * 17 * 4/pi) + ' 0' + ' 1000 0\n\n')
        else:
            fop.write('0 ' + str(abs(float(data[2])*17*4/pi)) + ' 1000 0\n\n')
        # fop.writelines(data)
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 65 < float(data[0]) < 83 and 33 < float(data[1]) < 40:
            fop = open('./small_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('2000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 2) + ' 0' + ' 2000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 2)) + ' 2000 0\n\n')
        else:
            pass
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 70 < float(data[0]) < 75 and 35 < float(data[1]) < 40:
            fop = open('./smaller_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('5000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 5) + ' 0' + ' 5000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 5)) + ' 5000 0\n\n')
        else:
            pass
        fop.close()#!/usr/bin/env python3

# generate the ice time of Tibet Plateau based on glacier change results from Wang Qiuyu
# Wang, Q., Yi, S., & Sun, W. (2021).Continuous estimates of glacier mass balance in High Mountain Asia
# based on ICESat-1,2 and GRACE/GRACE Follow-On data. Geophysical Research Letters, 48, e2020GL090954.
# https://doi.org/10.1029/2020GL090954

from math import pi

fop = open('./tp_ice.dat', 'w')
fop.write('82\n\n')
fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        # m = re.match("^Number of observations:\s*(\d+)",line)
        # line.split('\n\t')
        data = line.split(' ')
        # print(line)
        # print(data)
        fop = open('./tp_ice.dat', 'a')
        fop.write('10 0 6\n')
        fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
        fop.write('1000\n')
        fop.write('92 3\n')
        fop.write('0 0.017 19.6 92\n')
        if float(data[2]) > 0:
            fop.write(str(float(data[2]) * 17 * 4/pi) + ' 0' + ' 1000 0\n\n')
            # 17 : 17 years
        else:
            fop.write('0 ' + str(abs(float(data[2])*17*4/pi)) + ' 1000 0\n\n')
        # fop.writelines(data)
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 65 < float(data[0]) < 83 and 33 < float(data[1]) < 40:
            fop = open('./small_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('2000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 2) + ' 0' + ' 2000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 2)) + ' 2000 0\n\n')
        else:
            pass
        fop.close()

with open("./glacier_thickness_trend_for_chengfang.txt", 'r') as fip:
    for line in fip.readlines():
        data = line.split(' ')
        # print(data)
        if 70 < float(data[0]) < 75 and 35 < float(data[1]) < 40:
            fop = open('./smaller_tp_ice.dat', 'a')
            fop.write('10 0 6\n')
            fop.write(data[0] + ' ' + str(90-float(data[1])) + ' 0.5\n')
            fop.write('5000\n')
            fop.write('92 3\n')
            fop.write('0 0.017 19.6 92\n')
            if float(data[2]) > 0:
                fop.write(str(float(data[2]) * 17 * 4/pi * 5) + ' 0' + ' 5000 0\n\n')
            else:
                fop.write('0 ' + str(abs(float(data[2]) * 17 * 4/pi * 5)) + ' 5000 0\n\n')
        else:
            pass
        fop.close()