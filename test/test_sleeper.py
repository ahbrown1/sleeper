import unittest
import mock
from mock import patch

#import sleeper
from sleeper.sleeper import Sleeper



def mocked_timer_sleep(x):
    print 'mocking %s second sleep'%x 

@mock.patch('time.sleep', side_effect=mocked_timer_sleep)
class SleeperTest(unittest.TestCase):

    def setUp(self):
        print 'In setUp()'
        self.fixture = Sleeper() 


    def tearDown(self):
        print 'In tearDown()'
        del self.fixture

    def test1(self, mock_get):
        print 'in test1()'
        self.failUnlessEqual(self.fixture.wait(30), 0)

    def test2(self, mock_get):
        print 'in test2()'
        self.failUnlessEqual(self.fixture.wait(1), 0)

    def test(self, mock_get):
        print 'in test2()'
        self.failUnlessEqual(1, 0)

if __name__ == '__main__':
    unittest.main()

