# Project 5
# Author: Luis Armendariz and Alex petrov
# instructor: S.Einakian
# CPE 101- 01

from fade import *
from puzzle import *
import sys


argv =(sys.argv[1])
if sys.argv[1] == "puzzle.py":
                   
 file_input= get_file()
 listin =clean_file(file_input)
 heading = split_list_heading(listin)
 rgb_list = split_list_rgb(listin)
 flat_rgb = split_list_flat(rgb_list)
 listNew = puzzle_solve(flat_rgb)
 new_ppm(listNew, heading)

if sys.argv[1] == "fade.py":
 file= sys.argv[2]
 file_input = get_file(file)
 listin =clean_file(file_input)
 heading = split_list_heading(listin)
 rgb_list = split_list_rgb(listin)
 flat_rgb = split_list_flat(rgb_list)
 row = int(sys.argv[3])
 col = int(sys.argv[4])
 radius = int(sys.argv[5])
 r = row_heading(heading)
 c = coloumn_heading(heading)
 scaled = pixle_place(rgb_list,row,col,radius,r,c)
 new_ppm(scaled)
