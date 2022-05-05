import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
  def setUp(self):
    '''
    set up method runs before every test
    '''
    self.new_source = Source('bbc-news', 'BBC News', 'Children killed during cold war', "https://abcnews.go.com", 'general', 'us')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Source))