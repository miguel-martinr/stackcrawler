from unittest import TestCase
from stackcrawler.StackCrawler import StackCrawler



class TestStackCrawler(TestCase):

  def test_fetch_entries_from_hacker_news(self):
    stack_crawler = StackCrawler()
    
    entries = stack_crawler.fetch_entries(url='https://news.ycombinator.com/')
    self.assertEqual(30, len(entries))