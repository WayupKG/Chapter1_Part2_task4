def taimer(hour, minute, second, hour_2, minute_2, second_2):
    convert_second = (hour * 3600) + (minute * 60) + second
    convert_second_2 = (hour_2 * 3600) + (minute_2 * 60) + second_2
    res = convert_second - convert_second_2
    print(abs(res))
taimer(6, 5, 45, 5, 4, 35)