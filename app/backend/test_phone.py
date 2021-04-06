import unittest
import time
from phone import phoneinfo

class TestInsta(unittest.TestCase):
  def test_instgrm(self):
    result=phoneinfo("1234")
    
    self.assertIsNone(result)
    time.sleep(2.5)
    result=phoneinfo("918824593585")
    self.assertEqual(result["result"]["valid"],True)
    time.sleep(2.5)
    result=phoneinfo("sdfsdfs")
    
   

  
  
  unittest.main(argv=[''],verbosity=2, exit=False)