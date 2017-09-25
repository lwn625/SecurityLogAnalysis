import csv
with open('security_log.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        datetime=row[1]
        AMPM=datetime[-2:]
        date=datetime[:9]
        time=datetime[10:17]
        datetime_18=datetime[17:18]
        if datetime_18.isdigit():
            
            print(time)
            print("The hour has two digits")
        # print(date)
        # print(time)
        # print(datetime_18)
        # print(AMPM)
        # print("\n")

