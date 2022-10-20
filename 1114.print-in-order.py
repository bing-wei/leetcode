#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
import threading

class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()

        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def first(self, printFirst) -> None:
        printFirst()
		
        self.lock1.release()


    def second(self, printSecond) -> None:
        self.lock1.acquire()
        
        printSecond()
		
        self.lock2.release()


    def third(self, printThird) -> None:
        self.lock2.acquire()
        printThird()
        
# @lc code=end

