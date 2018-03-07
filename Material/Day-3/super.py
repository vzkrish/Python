class Base(object):
    def __init__(self):
        print "Base created"
    def xyz(self):
	print "another function"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
	super(ChildB, self).xyz()

ChildA() 
ChildB()
