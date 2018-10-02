'''
Created on Sep 29, 2018

@author: Thana Sithisombath
'''
import requests

test = requests.get("http://www.hipstercode.com")

outfile = open("test.txt", "w")
test.encoding = "ISO-8859-1"

outfile.write(str(test.text))
