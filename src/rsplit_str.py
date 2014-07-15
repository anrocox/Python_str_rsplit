#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

How to split a string defining a separator and looking from the end of string
in python?

¿Como dividir un string, definiendo un separador y buscando desde el final del
string en python?
'''

#create a str
s = 'blue;red;green;black;white;gray'
print(s)

#generates a list of the words contained in 's', using as the delimiter
#the ';' character.
l = s.rsplit(';')
print(l)

#can define the number of occurrences to split. Looking from the end to the
#beginning of the string.
l = s.rsplit(';', 3)
print(l)
