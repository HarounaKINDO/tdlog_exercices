import unittest
from exo2 import *

class TestSolution(unittest.TestCase):
    
    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails")
        )
        
        for string, ending in fixed_tests_True:
            self.assertTrue(solution(string, ending))
            
    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs")
        )
        
        for string, ending in fixed_tests_False:
            self.assertFalse(solution(string, ending))
            
if __name__ == "__main__":
    unittest.main()
