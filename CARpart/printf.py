import time
import gol

class PRINTF(object):

    def add(self):
        gol.add_value(1)
        print('IS',gol.get_value(1))
            
            
    def dec(self):
        gol.dec_value(1)
        print('IS',gol.get_value(1))

        
if __name__ == '__main__':
    gol._init()
    gol.set_value(1,1)
    print('is',gol.get_value(1))

