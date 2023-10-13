from unittest import TestCase
from stackcrawler.HackerNewsParser import HackerNewsParser
from stackcrawler.HackerNewsEntry import HackerNewsEntry



class TestHackerNewsParser(TestCase):
  

  def test_parse_entries_from_HTML(self):
    html_content = open('./tests/news_ycombinator_sample.html', 'r').read()
    expected = [
      HackerNewsEntry(
       order_number=1,
       title='Scrollbars Are Becoming a Problem',
       comments_count=67,
       points=110 
      ),

      HackerNewsEntry(
        order_number=2,
        title="First word discovered in unopened Herculaneum scroll by CS student",
        comments_count=108,
        points=458
      ),

      HackerNewsEntry(
        order_number=3,
        title="Signal Identification Wiki",
        comments_count=None,
        points=5
      )
    ]

    hn_parser = HackerNewsParser()
    entries = hn_parser.parse_entries_from_HTML(html_content)
    self.assertEqual(expected, entries[:3])