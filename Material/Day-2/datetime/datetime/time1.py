import datetime

t = datetime.time(1, 2, 3,1234)
print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo
raw_input('any key ')
