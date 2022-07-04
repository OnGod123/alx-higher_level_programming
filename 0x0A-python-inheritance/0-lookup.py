#!/usr/bin/python3
def lookup(obj):
	"""
	This function returns the list of available attributes and methods of an object

    	Attribute
   	---------
    	obj: This is the object of which attributes and methods are needed

    	Implementation
    	--------------

    	>> class Apple:
    	>>      passs

    	>> lookup(Apple)

    	Return: The list of available attributes and methods of the object
    	"""
    	docList = [x for x in dir(obj)]

    	return docList
