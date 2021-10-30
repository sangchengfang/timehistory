
# with open("./time_history1.dat", 'r') as fip:
#     time = []
#     thickness = []
#     for line in fip.readlines():

#         if line[0] == '#':
#             continue

#         data = line.split(' ')
#         # print(data)
#         fop = open('./processed_timehis.dat', 'a')
#         # fop.write(data[0] + ' ')
#         # fop.write(str( abs(float(data[1])) * 362500000 * 1.09 / 729400000 + 94.2364) + '\n')
#         time.append(data[0])
#         thickness.append(str( abs(float(data[1])) * 362500000 * 1.09 / 729400000 + 94.2364))

#     for i in range( len(time) ):
#         fop.write(str(time[i]) + ' ')
#     fop.write('\n')
#     for i in range( len(thickness) ):
#         fop.write(str(thickness[i]) + ' ')
#     fop.write('\n')
#     print(i)

def used():
    with open("./time_his_selected.dat", 'r') as fip:
        time = []
        thickness = []
        thickness_abs = []
        for line in fip.readlines():

            if line[0] == '#':
                continue

            data = line.split(' ')
            # print(data)
            fop = open('./processed_timehis.dat', 'a')
            time.append(data[0])
            # thickness.append(str( abs(float(data[1])) * 94.24 / 0.16 ))
            thickness.append(format( abs(float(data[1])) * 94.24 / 0.16, '.3f'))
            # if float(data[0]) < 11.7:
            #     thickness.append(format( 94.24, '.3f'))
            # else:
            #     thickness.append(format( abs(float(data[1])) * 94.24 / 61.73, '.3f'))
            
            fop_abs = open('./abs_timehis.dat', 'a')
            # thickness.append(str( abs(float(data[1])) * 94.24 / 0.16 ))
            thickness_abs.append(format( abs(float(data[1])), '.3f'))

    for i in range( len(time) ):
        fop.write(str(time[i]) + ' ')
        fop.write('\n')

        for i in range( len(thickness) ):
            fop.write(str(thickness[i]) + ' ') 
        fop.write('\n')
        print(i)

        for i in range( len(time) ):
            fop_abs.write(str(time[i]) + ' ')
            fop_abs.write(str(thickness_abs[i]) + ' ') 
            fop_abs.write('\n')

def lembeck_nomalization(max_value):
    with open("./time_his_selected.dat", 'r') as fip:
        time = []
        thickness = []
        thickness_abs = []
        for line in fip.readlines():

            if line[0] == '#':
                continue
            
            data = line.split(' ')
            fop = open('./lembeck_nomalization.dat', 'a')
            time.append(data[0])
            thickness.append(format( abs(float(data[1])) * float(max_value) / 134.280, '.8f'))
            fop_abs = open(f'./abs_timehis.dat', 'a')
            thickness_abs.append(format( abs(float(data[1])), '.8f'))


        for i in range( len(time) ):
            fop.write(str(time[i]) + ' ')
        fop.write('\n')

        for i in range( len(thickness) ):
            fop.write(str(thickness[i]) + ' ') 
        fop.write('\n')
        print(i)

        for i in range( len(time) ):
            fop_abs.write(str(time[i]) + ' ')
            fop_abs.write(str(thickness_abs[i]) + ' ') 
            fop_abs.write('\n')

    # for i in range( len(thickness) ):
    #     fop_abs.write(str(thickness[i]) + ' ') 
    # fop_abs.write('\n')
    # print(i)

lembeck_nomalization(1)
