#!/usr/bin/env python3
# -*- coding: utf-8 -*-



telefonbuch = dict([('Polizei',110),('Feuerwehr',112),('Behörden',115)])

hinweis = """How can I help you?\n
Please give the number of the options\n
1-->Search for a phone number\n
2-->Add new number\n
3-->Display all numbers\n
4-->Quit
"""

def tele_book():
    print(hinweis) 
    while True:  
        option = input("your optins is:\n")
        if option == '1':
            name = input("Please give the name:\n")
            if name in telefonbuch:
                print(telefonbuch[name])
            else:
                print("There is no num you are looking for.")
                
        elif option == '2':
            k = input("please give the name:\n")
            v = input("Please give the number:\n")
            telefonbuch[k] = v
            print("the telephonenumber of {} is {}.".format(k,telefonbuch[k]))
            print("update succeed!")
            
        elif option == '3':
            for k, v in telefonbuch.items():
                print(k,v)
                
        elif option == '4':
            print("Aufwiedersehen")
            break
        else:
            print("Please give the num 1-4.")
tele_book()