# SuperFastPython.com
# example of using a thread timer object
from time import sleep
from threading import Timer
 
# target task function
def task(message):
    # report the custom message
    print(message)
    # timer.start()
 
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
            print('1232') 

# create a thread timer object
timer = RepeatTimer(1, task, args=('Hello world',))
# start the timer object
timer.start()
# block for a moment
sleep(10)
# cancel the thread
print('Canceling the timer...')
timer.cancel()

