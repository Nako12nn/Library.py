# Рекурсія 

#class Recurtion():
  #  def __init__(self, arg):
  #      self.arg = arg

  #  def _recur(self, i):

#def recur(n):
 #   if n == 0 or n == 1:
  #      return 1
   # return n * recur(n - 1)

#print(recur(1))
#print()

def real_money(salary, hours):
    result = salary / hours
    return result
print("salary per hour: ",round(real_money(5000, 172)))
print()

x = 2
print(pow(pow(pow(pow(x,2),2), 2), 2)/ 65536)
print()

import math
v = 9
print(math.sqrt(v))
print()

from multiprocessing import Process
import os

def worker(n):
    print(f"Процес {n}, PID: {os.getpid()}")

if __name__ == "__main__":
    p1 = Process(target=worker, args=(1,))
    p2 = Process(target=worker, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Готово")

print()
from multiprocessing import Pool
import time

def square(x):
    time.sleep(1)  # імітація важких обчислень
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:  # 4 процеси
        results = pool.map(square, range(10))
    print(results)

