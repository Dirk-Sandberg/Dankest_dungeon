import sys,select
windtime = 4
i, o, e = select.select( [sys.stdin], [], [], windtime )
print 'first', i
print 'lala'
a, b, c = select.select( [sys.stdin], [], [], windtime )
a = 'foo'
print 'second', a
