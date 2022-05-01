import unittest
from ..app.models import Source


class SourceTest(unittest.TestCase):
  def setUp(self):
    '''
    set up method to run before every test
    '''
    self.new_source = Source("reuters", "Reuters")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Source))