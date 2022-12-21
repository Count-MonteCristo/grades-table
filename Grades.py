#!/usr/bin/python
#File Name: Grades.py
#Author: Luis Navarro

#Header
print("==========================================================================================")
print("                                 Developer: Luis Navarro                                  ")
print("==========================================================================================")
print("                               School Name: Ronald Reagan High School                     ")
print("                                   Teacher: Mr. Monty Slowashky                           ")
print("                                     Grade: 10                                            ")
print("                             Semester/Year: Summer 2021                                   ")
print("==========================================================================================")
print("%-19s %-9s %-6s %-8s %-10s %-8s %-12s %-6s %-10s" % ("Student Name", "English", "Math",
                                                            "History", "Geography", "Science",
                                                            "Programming", "Total", "Rank"))
print("==========================================================================================")

#Data - Student Grades
names = ["Alice Arnold"
         ,"Cory Brown"
         ,"Sean Douglas"
         ,"Pete Douglas"
         ,"Mary Fleming"
         ,"Joel Jacob"
         ,"Jeremy Ghouse"
         ,"Hansie Holder"
         ,"Loyola Ingenious"
         ,"Gary Jackson"
         ,"Russell Wilson"
         ,"Dustan Kellart"
         ,"Carl Malone"
         ,"Samuel Peterson"
         ,"Alec Stewart"]

data = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

file = open("grades_input.dat", "r")

for line in file:

    linedata = line.split(' ')
    row = int(linedata[0][0:2])
    col = int(linedata[0][2:4])
    val = float(linedata[1]);
    data[row][col] = val

sumRankA = 0
sumRankB = 0
sumRankC = 0
sumRankD = 0
sumRankF = 0

for i in range(len(data)):

    total = sum(data[i])

    if(total >= 540.0):
        rank = "A"
        sumRankA += 1
    elif(total >= 480.0 and total < 540.0):
        rank = "B"
        sumRankB += 1
    elif(total >= 420.0 and total < 480.0):
        rank = "C"
        sumRankC += 1
    elif(total >= 360.0 and total < 420.0):
        rank = "D"
        sumRankD += 1
    elif(total < 420.0):
        rank = "F"
        sumRankF += 1
    
    print('{:16s}'.format(names[i])
              + '{:10.2f}{:9.2f}{:8.2f}{:10.2f}{:10.2f}{:11.2f}'.format(*data[i])
              + '{:10.2f}'.format(total)
              + '   ' + rank)

print("------------------------------------------------------------------------------------------")

#Data - Totals
sumE = sum([i[0] for i in data])
sumM = sum([i[1] for i in data])
sumH = sum([i[2] for i in data])
sumG = sum([i[3] for i in data])
sumS = sum([i[4] for i in data])
sumP = sum([i[5] for i in data])

total = 0.0

for i in range(len(data)):
    for j in range(len(data[i])):
        total += data[i][j]

print('{:16s}'.format("Grand Totals")
        + '{:10.2f}'.format(sumE)
        + '{:9.2f}'.format(sumM)
        + '{:8.2f}'.format(sumH)
        + '{:10.2f}'.format(sumG)
        + '{:10.2f}'.format(sumS)
        + '{:11.2f}'.format(sumP)
        + '{:10.2f}'.format(total))

print("------------------------------------------------------------------------------------------")

#Data - Averages
avgE = sumE / len(names)
avgM = sumM / len(names)
avgH = sumH / len(names)
avgG = sumG / len(names)
avgS = sumS / len(names)
avgP = sumP / len(names)
avgT = total / len(names)

print('{:16s}'.format("Averages")
        + '{:10.2f}'.format(avgE)
        + '{:9.2f}'.format(avgM)
        + '{:8.2f}'.format(avgH)
        + '{:10.2f}'.format(avgG)
        + '{:10.2f}'.format(avgS)
        + '{:11.2f}'.format(avgP)
        + '{:10.2f}'.format(avgT))

#Data - Sum of Ranks
print("==========================================================================================")
print("                    Ranks    A's: " + str(sumRankA)
                            + "    B's: " + str(sumRankB)
                            + "    C's: " + str(sumRankC)
                            + "    D's: " + str(sumRankD)
                            + "    F's: " + str(sumRankF))

print("=====================================End of Report========================================")
