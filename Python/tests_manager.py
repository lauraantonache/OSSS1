#!usr/bin/env python

import sys
import csv

database = []
test = []
crt_test = ""
with open('stats.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        item = ', '.join(row)
        tokens = item.strip().split(",")
        if crt_test == tokens[0]:
            print "debug"
            entry = {
                'test_name': tokens[0],
                'school_name': tokens[2],
                'student_name': tokens[3],
                'grade': tokens[4]
            }
            test.append(entry)
        else:
            #print test
            database.append(test)
            crt_test = tokens[1]
            entry = {
                'test_name': tokens[0],
                'school_name': tokens[2],
                'student_name': tokens[3],
                'grade': tokens[4]
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
        if item['grade'] != ' ':
            crt_grade = int(item['grade'])
            if crt_grade > max:
                max = crt_grade
                max_item = item
    #print "Maximul obtinut la testul %s este %d " % (max_item['test_name'], max)
