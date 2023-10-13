from typing import List
from .Entry import Entry


class EntryFilter:
    def __init__(self):
        pass

    def filter_by_word_count_and_order_by_comments(self, entries: List[Entry], words_count_gt: int = 5) -> List[Entry]:
        """
          Filters entries whose length is greater than 5 and sorts them by comments count

          - `words_count_gt`: Words count greather than... Default: 5
        """
        return sorted(
            filter(lambda entry: len(entry.title.split()) > words_count_gt, entries),
            key=lambda entry: entry.comments_count
        )

