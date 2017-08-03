import sys

if __name__ == '__main__':
    for i in range(1, int(sys.argv[1])+1):
        if i % 3 == 0 and i % 5 == 0:
            print "foobar"
        elif i % 3 == 0 :
            print "foo"
        elif i % 5 == 0:
            print "bar"
        else:
            print i