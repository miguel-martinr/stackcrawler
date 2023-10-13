from typing import List
from .Entry import Entry


class EntryFilter:
    def __init__(self):
        pass
    
    def filter_by_word_count_and_order_by_comments(self, entries: List[Entry]) -> List[Entry]:
        return sorted(
            filter(lambda entry: len(entry.title.split()) > 5, entries),
            key=lambda entry: entry.comments_count
        )