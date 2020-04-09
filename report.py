#pylint: disable=invalid-name
prices = open('gas_prices.txt')
lines = prices.readlines()
prices.close()
year = 1994
yeartotal = 0
monthStart = 1
monthTotal = 0
numAvg = 0
yearLow = 8
yearHigh = 0
toPrint = []
months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}
for line in lines:
    gasyear = int(line[6:10])
    month = int(line[0:2])
    price = float(line[11:16])
    if year > 2013:
        break
    if gasyear > year or (year == 2012 and month == 12):
        if numAvg != 0:
            monthAvg = monthTotal / numAvg
        monthTotal = 0
        numAvg = 0
        #print(f"{monthAvg}\n")
        yeartotal += monthAvg
        monthPrint = f"{monthAvg:3.2f}"
        toPrint.append("{0:10} ${1}".format(months[12], monthPrint))
        yearAvg = yeartotal / 12
        print(f"{year}:\n\t Low: ${yearLow:3.2f}, Avg: ${yearAvg:3.2f}, High: ${yearHigh:3.2f}")
        for f in toPrint:
            print("\t\t{0:>10}".format(f))
        yeartotal = 0
        monthStart = 1
        yearLow = 8
        yearHigh = 0
        toPrint = []
        year += 1
    if gasyear == year:
        if month > monthStart:
            if numAvg != 0:
                monthAvg = monthTotal / numAvg
            monthTotal = 0
            numAvg = 0
            #print(f"{monthAvg}\n")
            yeartotal += monthAvg
            monthPrint = f"{monthAvg:3.2f}"
            toPrint.append("{0:10} ${1}".format(months[month-1], monthPrint))
            monthStart += 1
        if price < yearLow:
            yearLow = price
        if price > yearHigh:
            yearHigh = price
        if month == monthStart:
            #print(f"{month} : {price}")
            monthTotal += price
            numAvg += 1

   