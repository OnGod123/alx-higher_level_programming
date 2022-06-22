#!/usr/bin/python3
"""
Module 1-square.py
Defines square class with a private attribute, size
"""


class Square:
	"""
	class Square definition
	Args:
        size : size of a side in square
	"""
	def __init__(self, size):
		"""
        	Initializes square
        	Attributes:
            	size: size of a side of square
        	"""
		self.__size = size
