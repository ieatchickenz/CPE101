# Program 4
#
# Name:Luis Armendariz and Alex petrov
# Instructor: S. Einakian
# Section:01
'''
Some of the suggested functions are shown bellow.
You can create as many functions as you need.
You can even ignore the suggested functions.
But you are not allow to write the whole project in One Function!
'''

def puzzel():
    puzzle = input("Enter puzzle: ")
    line_puzzle = [puzzle[i:i+10] for i in range(0,100,10)]
    return line_puzzle
# splits string of letters into list contaning 10 elements
# returns ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
# call this line_puzzel
# string ---> list
def ten_by_ten(line_puzzle):
    for i in range(0, 10):
        print(line_puzzle[i])
# prints it as a 10 by 10 letter puzzle

def words():
 words = input("Enter words: ")
 return words.split()
# gets words that want to be found and seperates them into a list
# returns ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST']
# call it wordlist
# string ---> list
#def one_word(wordlist):
 #for word in range(0, 10):
  #return wordlist[word]
#makes word so it can bes test one word at a time* may not work

def find_forward(word,line_puzzle):
    for i in range(len(line_puzzle)):
      if word in line_puzzle[i]:
        col = i
        row = line_puzzle[i].index(word)
        return col,row
      else:
       i += 1
    return -1
# returns (9,3)
# gets the index of the row and col
def reverse(line_puzzle):
    return [line_puzzle[i][::-1] for i in range(0, 10)]
# returns['EEWTTGHQAW', 'SLEQQVIMBC', 'LIIIWKWXZA', 'VPIPXFLWDL', 'NMAVMTDNOP', 'BOGQYOSDEO', 'TCMMGKCQGL', 'MZUCAOLSCY', 'ZYCXSGMDVX', 'UNFXINUIUU']
# call the return rev_puzzle
# gives a reversed version of the line_puzzle

def find_backward(word,rev_puzzle):

    for i in range(len(rev_puzzle)):
      if word in rev_puzzle[i]:
        col = i
        row = (rev_puzzle[i].index(word)) -1
        return col,row

      else:
       i += 1
    return -1
# find the word in the backward puzzle list
# returns (1,4)
# finds the index of row and col

def column_puzzle(line_puzzle):
    puzzle_columns = []
    for row in range(0,10):
        column_temp = ""
        for column in range(0,10):
            column_temp += line_puzzle[column][row]
        puzzle_columns.append(column_temp)
    return puzzle_columns
# returns['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU']
# makes a column list to be used for up and down
# make column_puzzle

def find_down(word,colunm_puzzle):
    for i in range(len(colunm_puzzle)):
      if word in colunm_puzzle[i]:
        row = i
        col = colunm_puzzle[i].index(word)
        return col,row

      else:
       i += 1
    return -1
# retuns (1, 0)
# Finds word in the column_puzzle list

def reverse_column(column_puzzle):
    return [column_puzzle[i][::-1] for i in range(0, 10)]
#returns reverse column_puzzle
# returns ['UXYLOPLACW', 'UVCGEODZBA', 'IDSQDNWXMQ', 'UMLCSDLWIH', 'NGOKOTFKVG', 'ISAGYMXWQT', 'XXCMQVPIQT', 'FCUMGAIIEW', 'NYZCOMPILE', 'UZMTBNVLSE']

def find_up(word,reverse_column):
    for i in range(len(reverse_column)):
      if word in reverse_column[i]:
        row = i
        col = reverse_column[i].index(word)
        return col,row

      else:
       i += 1
    return -1
