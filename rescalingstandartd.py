"""Gizem Ece Yilmaz"""
from random import randint
from math import *
#Data
data = [416, 388, 186, 273, 164, 426, 444, 232, 304, 
434, 184, 442, 337, 285, 430, 488, 409, 284, 399, 410, 
331, 438, 173, 343, 496, 345, 252, 222, 391, 134, 405, 
365, 174, 428, 420, 223, 202, 481, 303, 202, 301, 134, 
163, 163, 125, 111, 247, 276, 302, 125]

#Contract: number number number-> list
#Purpose: generate random numbers
#Examples:
#random(5,1,9)-> [9, 4, 6, 5, 2]

def random(length,start,end):
	mylist=[]
	for i in range(length):
		mylist.append(randint(start, end))
	return mylist

print random(5,1,9)

#Contract: list->list
#Purpose:rescaling the range of features to scale the range in [0, 1] 
#Examples:
#[8,34,31,79,2]->[0.07792207792207792, 0.4155844155844156, 0.37662337662337664, 1.0, 0.0]

def rescaling(lon):
	new=[]
	for i in lon:
		r=float(i-min(lon))/float(max(lon)-min(lon))
		new.append(r)
	return new

print rescaling(data)
print rescaling([8,34,31,79,2])


#Contract: list->number
#Purpose: calculates the mean of the list
#Examples:
#[2,5,3]->3.33

def mean(lon):
	return float(sum(lon))/float(len(lon))
print mean([2,5,3])


#Contract: list->number
#Purpose: calculates the standart deviation of the list
#Examples:
#[2,3,4]->1.0

def standartdeviation(lon):
	liste=[]
	for i in lon:
		liste.append(float((i-mean(lon))**2))
	return sqrt(sum(liste)/float(len(lon)-1))

print standartdeviation([2,3,4])


#Contract:list->list
#Purpose:to standardize the range of independent variables or features of data
#Example:
#[8,34,31,79,2]->[-0.75140793231301, 0.10546076242989612, 0.006591297651868485, 1.5885027341003106, -0.9491468618690653]

def standardization(lon):
	new=[]
	for i in lon:
		z=float(i-mean(lon))/float(standartdeviation(lon))
		new.append(z)
	return new

print standardization(data)
print standardization([8,34,31,79,2])
