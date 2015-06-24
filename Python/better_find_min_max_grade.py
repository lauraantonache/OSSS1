#!usr/bin/env python

import sys


"""def hello():
    print "Hello, World!"
"""


def usage():
    print >> sys.stderr, "Usage python %s <filename>" % (sys.argv[0])


def main():
    #print "Program arguments are: ", sys.argv
    #print "No of arg is: ", len(sys.argv)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)


try:
    fp = open(sys.argv[1])
except IOError, e:
    print >> sys.stderr, "Argument is not a valid name"
    sys.exit(2)


#print len(list(fp))
#print "No of lines in file", len(fp.readlines())

students = []
for line in list(fp):
    tokens = line.strip().split('\t')
    student = {
            'first_name':tokens[0],
            'last_name':tokens[1],
            'group':tokens[2],
            'grade' : int(tokens[3])
            }
    students.append(student)

min_student = {
            'first_name': "Min",
            'last_name': "Min",
            'group': "33XXX",
            'grade' : 11
}

max_student = {
            'first_name': "Min",
            'last_name': "Min",
            'group': "33XXX",
            'grade' : 0
}


for s in students:
    if s['grade'] > max_student['grade']:
        max_student = s
    if s['grade'] < min_student['grade']:
        min_student = s
print min_student
print max_student



max_grade = 0
min_grade = 11
for s in students:
    if s['grade'] == max_grade:
        max_students.append(s)
    if s['grade'] > max_grade:
        max_students = [s]
        max_grade = s['grade']
    if s['grade'] == min_grade:
        min_students.append(s)
    if s['grade'] < min_grade:
        min_students = [s]
        min_grade = s['grade']
    
print min_students
print max_students


if __name__ == "__main__":
    sys.exit(main())
