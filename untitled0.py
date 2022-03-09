# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:28:52 2022

@author: nick
"""

a = {
     "a":123,
     "b":{ 
          "c":456,   
          "b":789   
             },
     "e":{
           "f":0,  
           "g":{
                  "h":1,
                  "i":2
                   }
             }
     }


key = []
val = []
def check(l): 
    for k in l:
        key.append(k)        
        if type(l[k]) == dict:
            check(l[k])
        else:
            val.append(l[k])
    
check(a)
print(key)
print(val)

    