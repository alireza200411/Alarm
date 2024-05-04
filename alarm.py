def clock():
    """
    This function is a wake-up alarm that receives two inputs:
            first clock : Current time
            second clock : The time you set to wake up
    """
    time1 = input('format -> hh:mm:ss\nenter the first clock: ')
    time2 = input('format -> hh:mm:ss\nenter the second clock: ')
    list_time1_string = time1.split(":")
    list_time2_string = time2.split(":")
    dic1 = {}
    dic2 = {}

    list_time1_number = []
    list_time2_number = []

    for data in list_time1_string:
        new = int(data)
        list_time1_number.append(new)

    for data2 in list_time2_string:
        new2 = int(data2)
        list_time2_number.append(new2)

    dic1['hour1'] = list_time1_number[0]
    dic1['min1'] = list_time1_number[1]
    dic1['sec1'] = list_time1_number[2]

    dic2['hour2'] = list_time2_number[0]
    dic2['min2'] = list_time2_number[1]
    dic2['sec2'] = list_time2_number[2]

    if dic1['min1'] == 0 and dic1['sec1'] == 0:
        if dic1['hour1'] > dic2['hour2']:
            ans_h = (24 - dic1['hour1']) + dic2['hour2']

            return (f'{ans_h}:{dic2["min2"]}:{dic2["sec2"]}')
        else:
            ans_h = dic2['hour2'] - dic1['hour1']
            return (f'{ans_h}:{dic2["min2"]}:{dic2["sec2"]}')

    if dic1['min1'] != 0 or dic1['sec1'] != 0:
        ans_s = 60 - dic1['sec1']
        if ans_s < 60:
            dic1['min1'] += 1
        else:
            pass

        ans_m = 60 - dic1['min1']
        if ans_m < 60:
            dic1['hour1'] += 1
        else:
            pass

        if dic1['hour1'] > dic2['hour2']:
            ans_h = (24 - dic1['hour1']) + dic2['hour2']

        else:
            ans_h = dic2['hour2'] - dic1['hour1']

        if dic2['sec2'] != 60:
            ans_s += dic2['sec2']
            if ans_s > 60:
                m = ans_s // 60
                ans_s = ans_s % 60
                ans_m += m

        if dic2['min2'] != 0:
            ans_m += dic2['min2']
            if ans_m > 60:
                h = ans_m // 60
                ans_m = ans_m % 60
                ans_h += h

        return (f'{ans_h}:{ans_m}:{ans_s}')
