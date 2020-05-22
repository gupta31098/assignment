import datetime

def solution():
    isValid = False
    while not isValid:
        date_1 = input("Type first Date yyyy-mm-dd: ")
        value_1 = input("Enter first value: ")
        date_2 = input("Type second Date yyyy-mm-dd: ")
        value_2 = input("Enter second value: ")
        try:  # strptime throw an exception if input date doesn't match the pattern
            d1 = datetime.datetime.strptime(date_1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date_2, "%Y-%m-%d")
            isValid = True

        except:
            print("Try again in yyyy-mm-dd pattern\n")
        if (isValid == True):
            if (d1.year == d2.year and d1.month == d2.month):
                # checking for value which is greater then 0 and less than 1000000
                # checking for valid years
                if (int(value_1) < 1000000 and int(value_2) < 1000000 and int(value_1) > 0 and int(value_2) > 0):
                    if (d1.year > 1970 and d1.year < 2100 and d2.year > 1970 and d2.year < 2100):
                        if (d2.day != d1.day):  # checking for same days
                            x = int(d2.day) - int(d1.day)
                        else:
                            x = 1
                        v = int(value_2) - int(value_1)

                        avg = v / x
                        val = int(value_1)
                        dec_final = {}  # final empty dict

                        for day in range(int(d1.day), int(d2.day) + 1):

                            if (day != d1.day):  # checking if days are same
                                val = val + avg
                            vall1 = str(d1.year) + "-" + str(d1.month) + "-" + str(day)

                            dec_final[vall1] = int(val)
                        print(dec_final)
                    else:
                        print("enter valid years 1970 < year < 2020")
                        solution()

                else:
                    print("Enter valid values(0 > value > 1000000)")
                    solution()

            else:
                print("year and month must be same")
                solution()
solution()