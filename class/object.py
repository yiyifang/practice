# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:50:02 2022

@author: nick
"""

#python3中兩者並無差異

class Person:
    """
    不帶object
    """
    name = "zhengtong"
 
 
class Animal(object):
    """
    帶有object
    """
    name = "chonghong"
 
if __name__ == "__main__":
    x = Person()
    print("Person", dir(x))
 
    y = Animal()
    print("Animal", dir(y))