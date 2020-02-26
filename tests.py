'''
This is an example test script. 
In its current state this will not run
'''

import unittest
#import module

class TestModule(unittest.TestCase):

    def test_add(self): 
        result = module.add(4,6) #this would be a test
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main() #this will kick off all the unit tests 
