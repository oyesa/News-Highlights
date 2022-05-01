import unittest
from ..app.models import Article


class ArticleTest(unittest.TestCase):
  def setUp(self):
    '''
    set up method to run before every test
    '''
    self.new_article = Article("Jane Otis", "The Art of being", "Lorem Ipsum Dolor Sit Amet", "https://www.theverge.com/2022/4/5/23011377/germany-servers-russian-darknet-site-hydra-bitcoin", "https://cdn.vox-cdn.com/thumbor/p230_bbmfO1qQ5ZuapX9JJbHPiY=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/11556959/acastro_170621_1777_0001_fin.jpg", "2022-04-05T19:24:01Z", "German authorities have seized $25.2 million USD in Bitcoin\r\nGerman authorities shut down the server infrastructure for the Russian darknet marketplace Hydra, seizing 23 million (~$25.2 million USD) … [+2344 chars]")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Article))


  if __name__ == '__main__':
    unittest.main()
      