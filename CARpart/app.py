# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from car import Car
from config import WEB_PORT
from esc import ESC
from led import LED
import esc
import threading
import time
import psutil
#from printf import PRINTF
import os

app = Flask(__name__)

led = LED()
car = Car()
esc = ESC()
#printf = PRINTF()

handle_map = {
    'forward': car.forward,
    'left': car.left,
    'right': car.right,
    'pause': car.stop,
    'backward': car.backward,
    'on': esc.on,
    'off': esc.off,
    #'on': printf.add,
    #'off': printf.dec,
    'work': led.work,

}



exitFlag = 0
class myThread1 (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.state = threading.Condition()
        self.paused = False
        #self.paused= threading.Condition(threading.Lock())
        
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print ("Starting " + self.name)
        led_run(self.name, self.counter, 1)
        print ("Exiting " + self.name)
        #while True:
        #    with self.pause_cond:
        #        while self.paused:
        #            self.pause_cond.wait()
        #        led_run(self.name, self.counter, 1)


        
    def resume(self):
        #self.paused = False
        #self.pause_cond.notify()
        #self.pause_cond.release()
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting
            print('resume')

    def pause(self):
        #self.paused=True
        #self.pause_cond.acquire()
        with self.state:
             self.paused = True  # make self block and wait
             print("pause")

class myThread2 (threading.Thread):   
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   
        print ("Starting " + self.name)
        run_app(self.name, self.counter, 1)
        print ("Exiting " + self.name)
    #def resume(self):
        #with self.state:
        #    self.paused = False
        #    self.state.notify()  # unblock self if waiting
        #    print('resume')

    #def pause(self):
    #    with self.state:
    #        self.paused = True  # make self block and wait
    #        print("pause")


def led_run(threadName,delay,counter):
    while counter:
        if exitFlag:
           thread.exit()
        time.sleep(delay)
        os.system('sudo python light.py')
        #os.system('sudo python printf.py')

def run_app(threadName,delay,counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        app.run(host='0.0.0.0', port=WEB_PORT, debug=False)

       

    
@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':

    #app.run(host='0.0.0.0', port=WEB_PORT, debug=False)
    thread2 = myThread2(2, "Thread-2", 2)    
    thread2.start()
    
    thread1 = myThread1(1, "Thread-1", 1)
    thread1.start()
    #thread1.pause()
    #x=int(input())
    #if x>0:
    #if int(esc.count())>0:
       # thread1.resume()
       # thread1 = myThread1(1, "Thread-1", 1)
       # thread1.start()
        
 
