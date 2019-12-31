import unittest
from funcs import *

class TestCases(unittest.TestCase):
   def test_puzzle(self):
   	  puzzle = "WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
   	  line_puzzle = [puzzle[i:i+10] for i in range(0,100,10)]
   	  self.assertEqual(line_puzzle, ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])
   def test_puzzle_2(self):
   	  puzzle = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
   	  line_puzzle = [puzzle[i:i+10] for i in range(0,100,10)]
   	  self.assertEqual(line_puzzle, ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR'])

   def test_words(self):
   	  words = 'UNIX CALPOLY GCC SLO COMPILE VIM TEST'
   	  word_list = words.split()
   	  self.assertEqual(word_list, ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST'])
   def test_words_1(self):
   	  words = 'CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON'
   	  word_list = words.split()
   	  self.assertEqual(word_list, ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON'])

   def test_find_forward_puzzle_1(self):
   	  word = 'UNIX'
   	  line_puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
   	  place = find_forward(word, line_puzzle)
   	  self.assertEqual(place, (9,3))
   def test_find_forward_puzzle_1_a(self):
   	  word = 'GCC'
   	  line_puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
   	  place = find_forward(word, line_puzzle)
   	  self.assertEqual(place, -1)
   def test_find_forward_puzzle_2(self):
   	  word = 'ZEBRA'
   	  line_puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
   	  place = find_forward(word, line_puzzle)
   	  self.assertEqual(place, (1,0))
   def test_find_forward_puzzle_2_a(self):
   	  word = 'RACCOON'
   	  line_puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
   	  place = find_forward(word, line_puzzle)
   	  self.assertEqual(place, (2,2))

   def test_reverse(self):
   	  puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
   	  reverse_puzzle = [puzzle[i][::-1] for i in range(0, 10)]
   	  self.assertEqual(reverse_puzzle, ['EEWTTGHQAW', 'SLEQQVIMBC', 'LIIIWKWXZA', 'VPIPXFLWDL', 'NMAVMTDNOP', 'BOGQYOSDEO', 'TCMMGKCQGL', 'MZUCAOLSCY', 'ZYCXSGMDVX', 'UNFXINUIUU'])
   def test_reverse_2(self):
   	  puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
   	  reverse_puzzle = [puzzle[i][::-1] for i in range(0, 10)]
   	  self.assertEqual(reverse_puzzle, ['BAINRBRAOE', 'HBRBEARBEZ', 'RNOOCCARRA', 'CEHCRRBCAA', 'AKBOZOBANC', 'ACNBBRINOB', 'AIARBCTREE', 'RHRCIRECBA', 'OCCROROIOB', 'RAEKRKAAOB'])


   def test_find_reverse_puzzle_1(self):
   	  word = 'VIM'
   	  reverse_puzzle = ['EEWTTGHQAW', 'SLEQQVIMBC', 'LIIIWKWXZA', 'VPIPXFLWDL', 'NMAVMTDNOP', 'BOGQYOSDEO', 'TCMMGKCQGL', 'MZUCAOLSCY', 'ZYCXSGMDVX', 'UNFXINUIUU']
   	  place = find_backward(word, reverse_puzzle)
   	  self.assertEqual(place, (1,4))
   def test_find_reverse_puzzle_1_a(self):
   	  word = "IDUNNO"
   	  reverse_puzzle = ['EEWTTGHQAW', 'SLEQQVIMBC', 'LIIIWKWXZA', 'VPIPXFLWDL', 'NMAVMTDNOP', 'BOGQYOSDEO', 'TCMMGKCQGL', 'MZUCAOLSCY', 'ZYCXSGMDVX', 'UNFXINUIUU']
   	  place = find_backward(word, reverse_puzzle)
   	  self.assertEqual(place, -1)
   def test_find_reverse_puzzle_2(self):
   	  word = 'BEAR'
   	  reverse_puzzle = ['BAINRBRAOE', 'HBRBEARBEZ', 'RNOOCCARRA', 'CEHCRRBCAA', 'AKBOZOBANC', 'ACNBBRINOB', 'AIARBCTREE', 'RHRCIRECBA', 'OCCROROIOB', 'RAEKRKAAOB']
   	  place = find_backward(word, reverse_puzzle)
   	  self.assertEqual(place, (1,2))


   def test_column_puzzle(self):
   	  line_puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
   	  col_puz = column_puzzle(line_puzzle)
   	  self.assertEqual(col_puz, ['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])
   def test_column_puzzle_2(self):
   	  line_puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
   	  col_puz = column_puzzle(line_puzzle)
   	  self.assertEqual(col_puz, ['EZAACBEABB', 'OERANOEBOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR'])


   def test_find_down_puzzle_1(self):
   	  word = 'CALPOLY'
   	  col_puz = ['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU']
   	  place = find_down(word, col_puz)
   	  self.assertEqual(place, (1,0))
   def test_find_down_puzzle_1_a(self):
   	  word = 'WHYWERENTYOUATELFPRACTICE'
   	  col_puz = ['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU']
   	  place = find_down(word, col_puz)
   	  self.assertEqual(place, -1)
   def test_find_down_puzzle_2(self):
   	  word = 'RABBIT'
   	  col_puz = ['EZAACBEABB', 'OERANOECOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR']
   	  place = find_down(word, col_puz)
   	  self.assertEqual(place, (1,3))

   def test_reverse_column(self):
   	  col_puz = ['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU']
   	  reverse_col_puzzle = reverse_column(col_puz)
   	  self.assertEqual(reverse_col_puzzle, ['UXYLOPLACW', 'UVCGEODZBA', 'IDSQDNWXMQ', 'UMLCSDLWIH', 'NGOKOTFKVG', 'ISAGYMXWQT', 'XXCMQVPIQT', 'FCUMGAIIEW', 'NYZCOMPILE', 'UZMTBNVLSE'])
   def test_reverse_column(self):
   	  col_puz = ['EZAACBEABB', 'OERANOECOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR']
   	  reverse_col_puzzle = reverse_column(col_puz)
   	  self.assertEqual(reverse_col_puzzle, ['BBAEBCAAZE', 'OOCEONAREO', 'AICRNACRBA', 'AOETIBBARR', 'KRRCRORCAB', 'ROIBBZRCER', 'KRCRBOCOBN', 'ECRANBHORI', 'ACHICKENBA', 'RORAAACRHB'])

   def test_find_up_puzzle_1(self):
   	  word = 'COMPILE'
   	  reverse_col_puzzle = ['UXYLOPLACW', 'UVCGEODZBA', 'IDSQDNWXMQ', 'UMLCSDLWIH', 'NGOKOTFKVG', 'ISAGYMXWQT', 'XXCMQVPIQT', 'FCUMGAIIEW', 'NYZCOMPILE', 'UZMTBNVLSE']
   	  place = find_up(word, reverse_col_puzzle)
   	  self.assertEqual(place, (3,8))
   def test_find_up_puzzle_2(self):
   	  word = 'CHICKEN'
   	  reverse_col_puzzle = ['BBAEBCAAZE', 'OOCEONAREO', 'AICRNACRBA', 'AOETIBBARR', 'KRRCRORCAB', 'ROIBBZRCER', 'KRCRBOCOBN', 'ECRANBHORI', 'ACHICKENBA', 'RORAAACRHB']
   	  place = find_up(word, reverse_col_puzzle)
   	  self.assertEqual(place, (1,8))



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()