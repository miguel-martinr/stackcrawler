from typing import List
from .Parser import Parser
from bs4 import BeautifulSoup, element
from .HackerNewsEntry import HackerNewsEntry


class HackerNewsParser(Parser):

    def _parse_entry(self, entry_id: str, raw_entry: element.Tag, raw_entry_info: element.Tag):

        def _get_entry_points(entry_info: element.Tag):
            if entry_info is None:
                return None

            score_element = entry_info.select_one('span.score')
            return int(score_element.text.split()[0]) if score_element else None

        def _get_entry_comments_count(entry_info: element.Tag, entry_id: str):
            if entry_info is None:
                return None

            a_elements = [a for a in entry_info.select(f'a[href="item?id={entry_id}"]') if 'comments' in a.text]
            return int(a_elements[0].text.split()[0]) if len(a_elements) > 0 else None

        title_element = raw_entry.select_one('td.title > span.titleline > a')
        order_element = raw_entry.select_one('td.title > span.rank')

        points = _get_entry_points(raw_entry_info)
        comments_count = _get_entry_comments_count(raw_entry_info, entry_id)

        return HackerNewsEntry(
            title=title_element.text if title_element else None,
            order_number=int(order_element.text.replace('.', '')) if order_element else None,
            points=points,
            comments_count=comments_count,
        )

    def parse_entries_from_HTML(self, html_content: str, limit: int) -> List[HackerNewsEntry]:
        bs = BeautifulSoup(html_content, 'html.parser')

        entries = []

        try:
            raw_entries = [(entry.get("id"), entry, entry.find_next_sibling())
                           for entry in list(bs.select('tr.athing'))]

            for entry_id, raw_entry, entry_info in raw_entries[:limit]:
                entries.append(
                    self._parse_entry(entry_id, raw_entry, entry_info)
                )

            return entries

        except Exception as e:
            raise Exception(f'An error occurred while parsing entries: {e}')
