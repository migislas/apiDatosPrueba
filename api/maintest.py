from src.Test.testingcsvColumns import testCSVoppenning
import unittest



def suite():
    suite = unittest.TestSuite()
    suite.addTest(testCSVoppenning('testingColumnsTypes'))
    suite.addTest(testCSVoppenning('testingColumnsNames'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(suite())