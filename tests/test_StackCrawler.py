from unittest import TestCase
from stackcrawler.Entry import Entry
from stackcrawler.EntryFilter import EntryFilter
from stackcrawler.StackCrawler import StackCrawler
from stackcrawler.HackerNewsParser import HackerNewsParser


class TestStackCrawler(TestCase):

    def test_fetch_entries_from_hacker_news(self):
        stack_crawler = StackCrawler(parser=HackerNewsParser(), filter=EntryFilter())

        entries = stack_crawler.fetch_entries_from_HTML(url='https://news.ycombinator.com/')
        self.assertEqual(30, len(entries))
        self.assertEqual(1, entries[0].order_number)
        self.assertEqual(30, entries[29].order_number)

        entries = stack_crawler.fetch_entries_from_HTML(url='https://news.ycombinator.com/', limit=25)
        self.assertEqual(25, len(entries))
        self.assertEqual(1, entries[0].order_number)
        self.assertEqual(25, entries[24].order_number)



