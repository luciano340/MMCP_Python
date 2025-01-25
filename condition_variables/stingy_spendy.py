import time
from threading import Thread, Lock, Condition


class StingySpendy:
    money = 100
    mutex = Condition()

    def stingy(self):
        for i in range(1000000):
            with StingySpendy.mutex: 
                self.money += 10
                StingySpendy.mutex.notify()
        print("Stingy Done")

    def spendy(self):
        for i in range(500000):
            with StingySpendy.mutex:
                while self.money < 20:
                    StingySpendy.mutex.wait()
                self.money -= 20

                if self.money < 0:
                    print("You don't have any money!", self.money)
        print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)