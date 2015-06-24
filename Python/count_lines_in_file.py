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

min = 11
max = -1
maxname = ""
maxfstname = ""
minname = ""
minfstname = ""
for idx, line in enumerate(list(fp)):
    unit = line.split("\t")
    grade = int(unit[3])
#    print unit
#    print "grade = ", grade
    if min == grade:
        minperson.append(' '.join([unit[0], unit[1]]))
    if min > grade:
        minname = unit[0]
        minfstname = unit[1]
        min = grade
        minperson = [' '.join([unit[0], unit[1]])]
    if max == grade:
        maxperson.append(' '.join([unit[0], unit[1]]))
    if max < grade:
        maxname = unit[0]
        maxfstname = unit[1]
        max = grade
        maxperson = [' '.join([unit[0], unit[1]])]
print "Cel cu nota cea mai mare este: ", maxperson
print "Cel cu nota cea mai mica este: ", minperson


if __name__ == "__main__":
    sys.exit(main())
