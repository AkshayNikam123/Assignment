# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZXkShn2iy2znEPJN65JgQszoNfcNLAL

#Python string manipulation

##1. Count the number of times `iNeuron` appears in the string.
###text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"
"""

text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"
text.count("iNeuron")

"""##2.Check if position 5 to 11 ends with the phrase iNeuron. in the string
###txt = "Hello, welcome to FSDS 2.0 at iNeuron."
"""

txt = "Hello, welcome to FSDS 2.0 at iNeuron."
txt[5:11]=="iNeuron"

"""#3.Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is."""

name=input("enter your name:")
name.title()
first_name,middle_name,surname==name.split(" ")
print(f"{first_name[0].upper()}.{middle_name[0].upper()}.{surname[:].title()}")

"""#4.Join all items in a list into a string, using a hash(#) character as separator:"""

LIST = ["My", "name", "is", "Rishav", "Dash"]
"#".join(LIST)

"""#5.Write example for the following string manipulation 
```
-isdecimal()
- islower()
- isupper()
- isalpha()
- isnumeric()
```
"""

num="\n003"
num.isdecimal()

name=input("enter your name")
name.islower()

favourite_sports=input("enter sports")
favourite_sports.isupper()

text="ineuron"
text.isalpha()

number="874589467975"
number.isnumeric()



"""#  6. Indian PAN card format follows the following formats- 
```
  AYEPC7894X
  ABCDE9999Y
  Take user input for PAN_CARD and validate as per the above example.
```
"""

list=[]
PAN_CARD=input("enter pancard number ")
if PAN_CARD[0:5].isupper() and PAN_CARD[5:9].isdecimal() and PAN_CARD[-1].isupper() :
  print("Enter pancard number is correct")
else:
  print("Invalid pancard number")



