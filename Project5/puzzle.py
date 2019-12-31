
# Project 5
# Author: Luis Armendariz and Alex petrov
# instructor: S.Einakian
# CPE 101- 01
import sys

def get_file():
    file_input = input("Enter the name of .ppm file:")
    valid_input = False

    while valid_input == False:
        try:
            open_file = open(file_input)
            print("Usage: python puzzle.py image_file.ppm")
            valid_input = True

        except Exception as error:
            print("Unable to open <{}>".format(file_input))
            file_input = input("Enter the name of .ppm file: ")
    if valid_input == True:
        return file_input

# makes the file into a list
def clean_file(file_input):

    filein = open(file_input, 'r')
    listin = [line.strip().split(' ') for line in filein.readlines()]
    return listin

def clean_up(listin):
    flat_list = []
    for list in listin:
        for group in list:
            for i in group:
               flat_list.append(i)
    return flat_list

def groups_of_3(rgb_list):
    group_rgb = []
    for i in range(0,len(rgb_list),3):
        last_group = rgb_list[i:i+3]
        group_rgb.append(last_group)
    return (group_rgb)

def new_ppm(group_rgb):
    with open("hidden.ppm", "w") as hidden_file:
        for rgb in group_rgb:
            for i in rgb:
             hidden_file.write(i + "\n")

