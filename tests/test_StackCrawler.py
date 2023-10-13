from unittest import TestCase
from stackcrawler.StackCrawler import StackCrawler




class TestStackCrawler(TestCase):
  
      def test_fetch_entries(self):
          stack_crawler = StackCrawler()
          entries = stack_crawler.fetch_entries(url=" https://news.ycombinator.com/", limit=30)
          self.assertEqual(30, len(entries))
          self.assertEqual(1, entries[0].order_number)
          self.assertEqual(30, entries[29].order_number)
          
          