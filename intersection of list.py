# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:12:01 2020

@author: kgitn
"""


def intersection(l1,l2):
    return list(set(l1)&set(l2))
l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
print('intersection of l1 and l2 list is: ',intersection(l1,l2))




#removing 24 from the list
list=[12,24,35,24,88,120,155]
for x in list:
    if x==24:
        list.remove(x)
print(list)

#list=[12,24,35,24,88,120,155]
#list=[x for x in list if x!=24]
#print (list)

#without list comprehension
list=[12,24,35,24,88,120,155]
l=[]
for x in list:
    if x!=24:
        l.append(x)
print(l)



