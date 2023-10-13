from typing import List
import requests
from .Parser import Parser
from .EntryFilter import EntryFilter
from .Entry import Entry
class StackCrawler:
    def __init__(self, parser: Parser, filter: EntryFilter):
        self._parser = parser
        self.filter = filter

    def fetch_entries_from_HTML(self, url: str, limit: int = 30) -> List[Entry]:
        html_content = requests.get(url).text
        return self._parser.parse_entries_from_HTML(html_content, limit=limit)
        
