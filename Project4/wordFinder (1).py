# Program 4
#
# Name:Luis Armendariz and Alex Petrov
# Instructor: S. Einakian
# Section:01
from funcs import*

# gives names to functions from funcs 
line_puzzle = puzzel()
wordlist = words()
rev_puzzle = reverse(line_puzzle)
column_puzzle = column_puzzle(line_puzzle)
reverse_column = reverse_column(column_puzzle)

# prints the puzzle to the user
print("Puzzle:")
print("")
ten_by_ten(line_puzzle)
print("")

# goes for each word given by user
for word in wordlist:
 forward = find_forward(word,line_puzzle)
 backward = find_backward(word,rev_puzzle)
 down = find_up(word,column_puzzle)
 up = find_up(word,reverse_column)
# prints based on what the function is found by and if it is found at all
 if forward != -1:
     print("{}: (FORWARD) row: {} column: {}".format(word, forward[0], forward[1]))
 elif backward != -1 :
     print("{}: (BACKWARD) row: {} column: {}".format(word,backward[0],backward[1])) 
 elif down != -1:
     print("{}: (DOWN) row: {} column: {}".format(word,down[0], down[1])) 
 elif up != -1:
     print("{}: (UP) row: {} column: {}".format(word,up[0]+3, up[1]))
 elif up == -1 or down == -1 or backward == -1 or foward == -1:
     print ("{}: word not found".format(word))
