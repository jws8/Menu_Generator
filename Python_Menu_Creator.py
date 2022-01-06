#Date: 1/5/2022
#Author: Joshua W Smith (github.com/jws8)

#Menu Creator and Random Menu Item Generator: prompts user for additional items
#Upon app close returns a random menu item 
import random, os, sys
#create list for menu items
menu_items = []

#read_file() splits entire text contents into a list seperated by commas
# and appends that list to menu_items list
def read_file():
    with open("menu_items.txt") as f:
        for line in f:
            menu_items.append(line.split(","))
#prompts user for new item, updates menu item list and text file.
#generates random menu item upon close
def prompt():  
    while True:
        ans = input("item: ")
        if ans == "":
            #generate random choice out of menu items 
            #& exit prompt loop
            rans = random.choice(menu_items[0])
            print(rans)
            break
        #update file with new item
        write_file(ans)
        #update menu items with new item
        menu_items.append(ans)
#writes new item (ans) to text file
def write_file(ans):
    with open("menu_items.txt", "a") as f:
            f.write(ans + ",")

#Run
read_file()
print(menu_items)
prompt()




        