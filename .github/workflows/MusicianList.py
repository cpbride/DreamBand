# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:04:23 2020

@author: Christopher Bride
"""

# Python code to demonstrate  
# finding duplicate values from dictionary 

from itertools import chain 

q = input("What instrument do you need: ")
  
# initialising dictionary 
musician_lib = {"Nick Beggs": "Bass", 
                 "Geddy Lee": "Bass", 
                 "John Myung": "Bass",
                 "Steven Wilson": "Guitar",
                 "Neil Peart": "Drums", 
                 "John Petrucci": "Guitar",
                 "Mike Portnoy": "Drums",
                 "Kevin Moore": "Keyboards",
                 "Derek Sherinian": "Keyboards", 
                 "Jordan Rudess": "Keyboards",
                 "Neal Schon": "Guitar",
                 "Steve Perry": "Vox",
                 "Alex Lifeson": "Guitar",
                 "James Labrie": "Vox"
                 }
  
# printing initial_dictionary 
#print("musician_library", str(musician_lib)) 
  
# finding duplicate values 
# from dictionary using set 

if musician_lib.value() == q:
    print(musician_lib.items())

call_list = {} 
for key, value in musician_lib.items(): 
    call_list.setdefault(value, set()).add(key) 
  
  
musicians = set(chain.from_iterable( 
         values for key, values in call_list.items() 
         if len(values) > 1)) 
  
# printing result 
print("You should call", str(musicians)) 