from typing import List
from .Entry import Entry


class EntryFilter:
    def __init__(self):
        pass

    def _filter_by_words_count(
      self,
      filter_fn: callable,
      entries: List[Entry],
    ):
        return filter(
            lambda entry: filter_fn(len(entry.title.split())),
            entries
        )


    def filter_by_word_count_and_order_by_comments(self, entries: List[Entry], words_count_gt: int = 5) -> List[Entry]:
        """
          Filters entries whose length is greater than `words_count_gt` and sorts them by comments count

          - `words_count_gt`: Words count greather than... Default: 5
        """
        return sorted(
            self._filter_by_words_count(lambda words_count: words_count > words_count_gt, entries),
            key=lambda entry: entry.comments_count
        )

    def filter_by_word_count_and_order_by_points(self, entries: List[Entry], words_count_le: int = 5) -> List[Entry]:
        """
          Filters entries whose length is less than or equal to `words_count_le` and sorts them by points

          - `words_count_le`: Words count less than or equal to... Default: 5
        """
        return sorted(
            self._filter_by_words_count(lambda words_count: words_count <= words_count_le, entries),
            key=lambda entry: entry.points
        )

