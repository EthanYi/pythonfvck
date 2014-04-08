#!/usr/bin/env python
#-*-coding:utf-8-*-
import time  
import thread
import threading

#---------------------------------------------------
def timer(no, interval):  
    cnt = 0  
    while cnt<10:  
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt+=1  
    thread.exit_thread()  
     
   
def test(): #Use thread.start_new_thread() to create 2 new threads  
    thread.start_new_thread(timer, (1,1))  
    thread.start_new_thread(timer, (2,2))

#---------------------------------------------------
class timer1(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())  
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
   
def test1():  
    thread1 = timer1(1, 1)  
    thread2 = timer1(2, 2)  
    thread1.run()  
    thread2.run()  
    time.sleep(10)  
    thread1.stop()  
    thread2.stop()  
    return

#---------------------------------------------------
mylock1 = thread.allocate_lock()  #Allocate a lock  
num1=0  #Shared resourc
def add_num(name):  
    global num1  
    while True:  
        mylock.acquire() #Get the lock   
        # Do something to the shared resource  
        print 'Thread %s locked! num=%s'%(name,str(num1))  
        if num1 >= 5:  
            print 'Thread %s released! num=%s'%(name,str(num1))  
            mylock.release()  
            thread.exit_thread()  
        num1+=1  
        print 'Thread %s released! num=%s'%(name,str(num1))  
        mylock.release()  #Release the lock.  
  
def test3():  
    thread.start_new_thread(add_num, ('A',))  
    thread.start_new_thread(add_num, ('B',))

#-------------------------------------------------
mylock2 = threading.RLock()  
num2=0  
   
class myThread(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.t_name = name  
          
    def run(self):  
        global num2  
        while True:  
            mylock.acquire()  
            print '\nThread(%s) locked, Number: %d'%(self.t_name, num2)  
            if num2>=4:  
                mylock.release()  
                print '\nThread(%s) released, Number: %d'%(self.t_name, num2)  
                break  
            num2+=1  
            print '\nThread(%s) released, Number: %d'%(self.t_name, num2)  
            mylock.release()  
              
def test4():  
    thread1 = myThread('A')  
    thread2 = myThread('B')  
    thread1.start()  
    thread2.start()

#---------------------------------------
class Producer(threading.Thread):  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  
   
    def run(self):  
        global x  
        con.acquire()  
        if x > 0:  
            con.wait()  
        else:  
            for i in range(5):  
                x=x+1  
                print "producing..." + str(x)  
            con.notify()  
        print x  
        con.release()  
  
class Consumer(threading.Thread):  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  
    def run(self):  
        global x  
        con.acquire()  
        if x == 0:  
            print 'consumer wait1'  
            con.wait()  
        else:  
            for i in range(5):  
                x=x-1  
                print "consuming..." + str(x)  
            con.notify()  
        print x  
        con.release()  
   
 def test5(): 
    con = threading.Condition() 
    x=0  
    print 'start consumer'  
    c=Consumer('consumer')
    print 'start producer'  
    p=Producer('producer')  
    p.run()  
    c.run()  
    p.join()  
    c.join()  
    print x
    
if __name__=='__main__':  
    test1()  