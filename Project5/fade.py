# Project 5
# Author: Luis Armendariz and Alex petrov
# instructor: S.Einakian
# CPE 101- 01
import sys
import math


def get_file(file_input):
    valid_input = False

    while valid_input == False:
        try:
            open_file = open(file_input)
            print("Usage: python fade.py <image> <row> <column> <radius>")
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

def groups_of_3(flat_rgb):
 return [flat_rgb[i:i+3] for i in range(0, len(flat_rgb), 3)]
#[['21', '85', '166'], ['21', '53', '111'], ['21', '3', '195']]
# call group


def pixle_place(rgb_list,row,col,radius,width,height):
        r = 0
        c = 0
        pix = 0
        listNew = []
        for x in range(len(rgb_list)):
            scale = pixle_scale(r, c, row, col,radius)
            newpix0 = int(scale * int(rgb_list[pix][0]))
            newpix1 = int(scale * int(rgb_list[pix][1]))
            newpix2 = int(scale * int(rgb_list[pix][2]))
            pix += 1
            listNew.append(newpix0)
            listNew.append(newpix1)
            listNew.append(newpix2)
            c += 1
            if c == width:
                r += 1
                c = 0
                if r == height:
                    break
        return listNew

def row_heading (heading):
 return int(heading[1][0])

def coloumn_heading(heading):
 return int(heading[1][1])

def pixle_scale(r, c, row, col, radius):
    distance = math.sqrt((r - int(row)) ** 2 + (c - int(col)) ** 2)
    mult = (int(radius) - distance) / int(radius)
    if mult < .02:
        mult = .02
    return mult

def new_ppm(scaled):
    with open("fade.ppm", "w") as hidden_file:
             hidden_file.write("P3" + "\n")
             hidden_file.write("493 401" + "\n")
             hidden_file.write("255" + "\n")
             for scale in scaled:
               hidden_file.write(str(scale) + "\n")
