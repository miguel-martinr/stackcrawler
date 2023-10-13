from typing import List
from .Entry import Entry

class Parser:

  def __init__(self):
    pass

  def parse_entries_from_HTML(self, url: str, limit: int) -> List[Entry]:
    raise NotImplementedError('This method must be implemented by a subclass')
  