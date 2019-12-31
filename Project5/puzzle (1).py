
# Project 5
# Author: Luis Armendariz and Alex petrov
# instructor: S.Einakian
# CPE 101- 01
import sys

def get_file():
    file_input = sys.argv[1]
    valid_input = False

    while valid_input == False:
        try:
            open_file = open(file_input)
            print("Usage: python puzzle.py image_file.ppm")
            valid_input = True

        except Exception as error:
            print("Unable to open <{}>".format(file_input))
            exit()
    if valid_input == True:
        return file_input

# makes the file into a list
def clean_file(file_input):

    filein = open(file_input, 'r')
    listin = [line.strip().split(' ') for line in filein.readlines()]
    return listin
#[['P3'], ['500', '375'], ['255'], ['21'], ['85'], ['166'], ['21'], ['53'], ['111'], [$

def split_list_heading(file_input):
    heading = file_input[:3]
    return heading
#[['P3'], ['500', '375'], ['255']]

def split_list_rgb(file_input):
    rgb = file_input[3:]
    return rgb
#[['21'], ['85'], ['166'], ['21'], ['53'], ['111'], ['21'], ['3']]
#return rgb list

def split_list_flat(rgb_list):
    flat_rgb = []
    for rgb in rgb_list:
        for i in rgb:
            flat_rgb.append(i)
    return flat_rgb
# ['21', '85', '166', '21', '53', '111', '21', '3', '195']

def puzzle_solve(flat_rgb):
    listNew = []
    for x in range(0, len(flat_rgb), 3):
        mult = int(flat_rgb[x]) * 10
        if mult > 255:
           mult = 255
        flat_rgb[x + 1] = flat_rgb[x + 2] = mult
        listNew.append(mult)
        listNew.append(flat_rgb[x + 1])
        listNew.append(flat_rgb[x + 2])
    return listNew

def new_ppm(group_rgb, heading):
    with open("hidden.ppm", "w") as hidden_file:
             hidden_file.write("P3" + "\n")
             hidden_file.write("500 375" + "\n")
             hidden_file.write("255" + "\n")
             for rgb in group_rgb:
               hidden_file.write(str(rgb) + "\n")
