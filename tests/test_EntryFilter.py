from unittest import TestCase
from stackcrawler.EntryFilter import EntryFilter
from stackcrawler.Entry import Entry


class TestEntryFilter(TestCase):

    # Should be able to filter all previous entries with more
    # than five words in the title ordered by the number of comments first.

    def get_entries(self):
        return [
            Entry(title="Scrollbars Are Becoming a Problem",
                  order_number=1, comments_count=67, points=110),
            Entry(title="First word discovered in unopened Herculaneum scroll by CS student",
                  order_number=2, comments_count=108, points=458),
            Entry(title="Desmos 3D graphing calculator",
                  order_number=3, comments_count=70, points=302),
            Entry(title="REI is Laying Off 275 Employees",
                  order_number=4, comments_count=54, points=685),
            Entry(title="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                  order_number=4, comments_count=None, points=685),
        ]

    def test_filter_by_word_count_5_and_order_by_comments(self):
        entry_filter = EntryFilter()
        entries = self.get_entries()
        expected = [
            Entry(title="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                  order_number=4, comments_count=None, points=685),
                  
            Entry(title="REI is Laying Off 275 Employees",
                  order_number=4, comments_count=54, points=685),
            Entry(title="First word discovered in unopened Herculaneum scroll by CS student",
                  order_number=2, comments_count=108, points=458),
        ]

        filtered_entries = entry_filter.filter_by_word_count_and_order_by_comments(entries)
        self.assertEqual(expected, filtered_entries)

    def test_filter_by_word_count_7_and_order_by_comments(self):
        entry_filter = EntryFilter()
        entries = self.get_entries()
        expected = [
            Entry(title="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                  order_number=4, comments_count=None, points=685),

            Entry(title="First word discovered in unopened Herculaneum scroll by CS student",
                  order_number=2, comments_count=108, points=458),
        ]

        filtered_entries = entry_filter.filter_by_word_count_and_order_by_comments(entries, words_count_gt=6)
        self.assertEqual(expected, filtered_entries)

    def test_filter_by_word_count_5_and_order_by_points(self):
        entry_filter = EntryFilter()
        entries = self.get_entries()
        expected = [
            Entry(title="Scrollbars Are Becoming a Problem",
                  order_number=1, comments_count=67, points=110),
            Entry(title="Desmos 3D graphing calculator",
                  order_number=3, comments_count=70, points=302),
        ]

        filtered_entries = entry_filter.filter_by_word_count_and_order_by_points(entries)
        self.assertEqual(expected, filtered_entries)
