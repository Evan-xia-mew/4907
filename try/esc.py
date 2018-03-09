import RPi.GPIO as gpio
import time
	
class ESC(object):
    def __init__(self):
         global i
            
    def on(self):
	    i = 5
         print(i)
	
		 
    def add(self):
         i+=1
		 print(i)
		
		 
	def dec(self):
	     i-=1
		 print(i)
		
				
	def off(self):
         i=0
		 print(i)
    
		 
      
     
