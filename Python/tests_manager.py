#!usr/bin/env python

import sys
import csv

database = []


with open('stats.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
	for row in spamreader:
		item = ', '.join(row)
		tokens = item.strip().split(",")
		entry = {
				'test_name':tokens[1],
				'school_name':tokens[5],
				'student_name':tokens[8],
				'grade':int(tokens[11])
		}
		print entry
		database.append(entry)





"""with open('stats.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['test_name'], row['person'], row['grade'])
"""