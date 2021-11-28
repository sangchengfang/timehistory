#!/usr/bin/env python3

# get the flipped time for TABOO task 3.

# for every thme, just substracted the largest time and get absolute value.

def flip_time(time_his_file, flipped_time_file):
    """

    :param time_his_file: time history  file
    :return:
    """

    time_his_file = str(time_his_file)
    flipped_time_file = str(flipped_time_file)
    time = list()
    flipped_time = list()
    thickness = list()

    with open(time_his_file, 'r') as fip:
        # data = fip.readlines()
        for line in fip:
            line = line.split()
            time.append(float(line[0]))
            thickness.append(line[1])

        # print(time)
        # print(thickness)
        largest_time = max(time)
        # print(largest_time)

        for item in time:
            flipped_time.append(abs(item - largest_time))
        print(flipped_time)
        flipped_time.reverse()
        thickness.reverse()
        print(flipped_time)

    with open(flipped_time_file, 'w') as fop:
        length = len(flipped_time)

        if length != len(thickness):
            print('wrong!!! time and thickness should have same numbers')

        for i in range(length):
            fop.write(str(format(flipped_time[i], '.4f')).ljust(8))
            fop.write(thickness[i])
            fop.write('\n')

# flip_time('Wanghs_TH.dat', 'Wanghs_TH_flipped.dat')
flip_time('Lambeck_TH_selected_abs.dat', 'Lambeck_TH_selected_abs_flipped.dat')