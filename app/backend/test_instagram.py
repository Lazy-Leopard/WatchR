import unittest
import time
from instagram import instgrm

class TestInsta(unittest.TestCase):
  def test_instgrm(self):
    result=instgrm("invalidusernameeeeeeeeeeeeeeeeee")
    time.sleep(2.5)
    self.assertIsNone(result)
    result=instgrm("_shoury.a_")
    self.assertEqual(result["code"],200)
  
  
  unittest.main(argv=[''],verbosity=2, exit=False)

   

