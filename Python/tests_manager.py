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
        #print "crt_test", crt_test
        #print "token[0]:", tokens[0]
        if crt_test == tokens[0]:
            #print "debug"
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
            crt_test = tokens[0]
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
    test_name_aux = max_item['test_name'].split('(')     
    print "Maximul obtinut la testul %s este %d " % (test_name_aux[0], max)



for i in range (len(database)):
    schools = []
    for item in database[i]:
        crt_test = item['test_name']
        crt_school = item['school_name']
        crt_grade = int(item['grade'])
        flag = 0
        for iterator in schools:
            if crt_school == iterator[0]:
                if iterator[1] < crt_grade:
                    iterator[1] = crt_grade
                flag = 1
        if flag == 0:
            schools.append([crt_school, crt_grade])
    test_name_aux = crt_test.split('(')     
    print "Maximul obtinut la testul %s" % crt_test.split('(')[0]
    for school in schools:
        print "Scoala %s, Maximul %d" % (school[0], school[1])
