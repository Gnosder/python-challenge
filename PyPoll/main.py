import csv, os

path = os.path.join("Resources", "election_data.csv")
with open(path) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    # declare vars
    totalVotes = 0
    candidatesDict = {} # Key = Name, Value = Votes
    percentVotes = []
    winner = 'Error'
    winnerVotes = 0

    header = next(csvReader)

    for row in csvReader:
        totalVotes = totalVotes + 1
        if row[2] not in candidatesDict:
            candidatesDict[row[2]] = 1
        else:
            candidatesDict[row[2]] = candidatesDict[row[2]] + 1

    # winner
    for name in candidatesDict:
        if candidatesDict[name] > winnerVotes:
            winner = name
            winnerVotes = candidatesDict[name]

    

 # Export report to terminal and txt file
print(f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
''')

for name in candidatesDict:
    print(name + ": " + str((round(candidatesDict[name] / totalVotes, 2)) * 100) + "% (" + str(candidatesDict[name]) + ")")


print(f'''
-------------------------
Winner: {winner}
-------------------------
''')

# Export to txt file
savePath = os.path.join("Analysis", "Analysis.txt")

analysis = open(savePath, "w")
analysis.write(f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
''')
for name in candidatesDict:
    analysis.write(name + ": " + str((round(candidatesDict[name] / totalVotes, 2)) * 100) + "% (" + str(candidatesDict[name]) + ")\n")
analysis.write(f'''
-------------------------
Winner: {winner}
-------------------------
''')
