# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:57:25 2018

@author: UARTman
"""
import random


dots=[]
roads=[]



class Dot:
    def __init__(self,idt):
        self.idt=idt
        self.roads=[]


class Road:
    def __init__(self,a,b,l):
        self.a=a
        self.b=b
        self.l=l
        a.roads.append(self)
        b.roads.append(self)
    def oend(self,dot):
        return dots[self.a.idt+self.b.idt-dot.idt]


def genlen(minn=1,maxx=10):
    return random.randrange(minn,maxx+1)

def RandRoads(dot,m=-1):
    x=dots[:]
    x.remove(dot)
    for i in dot.roads:
        x.remove(i.oend(dot))
    k=len(x)
    if m==-1:
        m=random.randrange(0,k)
    for i in range(0,m):
        l=random.randrange(0,len(x))
        ll=x[l]
        Road(dot,ll,genlen())
        x.pop(l)

def Generate(d,r):
    for i in range(0,d):
        dots.append(Dot(i))
    for i in dots:
        RandRoads(i)
        
def Visual():
    for i in roads:
        print(i.a,' ',i.b,' ',i.l)
        














