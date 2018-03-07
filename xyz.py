class temp(object):
        k=0
        def tempin(self):
                self.eno=raw_input('enumber ')
                self.ename=raw_input('ename ')
        def tempout(self):
                temp.k+=1
                print temp.k, self.eno, self.ename

