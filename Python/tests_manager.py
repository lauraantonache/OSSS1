#!usr/bin/env python

import sys
import csv

database = []
test = []
crt_test = ""
with open('stats.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
    for row in spamreader:
        item = ', '.join(row)
        tokens = item.strip().split(",")
        if crt_test == tokens[1]:
            entry = {
                'test_name': tokens[1],
                'school_name': tokens[5],
                'student_name': tokens[8],
                'grade': tokens[11]
            }
            test.append(entry)
        else:
            #print test
            database.append(test)
            crt_test = tokens[1]
            entry = {
                'test_name': tokens[1],
                'school_name': tokens[5],
                'student_name': tokens[8],
                'grade': tokens[11]
            }
            test = [entry]

#print database[1]


for i in range (len(database)):
    max = 0
    max_item = {
        'test_name': "none",
        'school_name': "none",
        'student_name': "none",
        'grade': "0"
    }
    #print database[i]
    for item in database[i]:
        print item
        crt_grade = int(item['grade'])
        if crt_grade > max:
            max = crt_grade
            max_item = item
    print max

