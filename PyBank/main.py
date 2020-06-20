import csv, os

# Open and read budget_data.csv
path = os.path.join("Resources", "budget_data.csv")
with open(path) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    totalMonths = -1
    netProfit = 0
    avgProfit = 0
    greatestProfit = 0
    greatestProfitMonth = ''
    lowestProfit = 0
    loweestProfitMonth = ''

    next(csvReader)

    for row in csvReader:
        totalMonths = totalMonths + 1
        netProfit = netProfit = row[1]
        if row[1] > str(greatestProfit):
            greatestProfit = row[1]
            greatestProfitMonth = row[0]
        elif row[1] < str(lowestProfit):
            lowestProfit = row[1]
            loweestProfitMonth = row[0]

    avgProfit = int(netProfit) / int(totalMonths)

# Export report to terminal and txt file
print(f'''
Financial Analysis
------------------
Total Months: {totalMonths}
Total: {netProfit}
Average Change: {avgProfit}
Greatest Increase in Profits: {greatestProfitMonth} ({greatestProfit})
Greatest Decrease in Profits: {loweestProfitMonth} ({lowestProfit})''')

# Export to txt file
savePath = os.path.join("Analysis", "Analysis.txt")

analysis = open(savePath, "w")
analysis.write(f'''
Financial Analysis
------------------
Total Months: {totalMonths}
Total: {netProfit}
Average Change: {avgProfit}
Greatest Increase in Profits: {greatestProfitMonth} ({greatestProfit})
Greatest Decrease in Profits: {loweestProfitMonth} ({lowestProfit})''')
