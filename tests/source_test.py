import unittest
from app.models import source
  
class sourcesTest(unittest.TestCase):
    '''
    Test Class to the test the behaviour of the news class
    '''


    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://python',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,source)


if __name__ == '__main__':
    unittest.main()