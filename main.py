from stackcrawler.StackCrawler import StackCrawler
from stackcrawler.EntryFilter import EntryFilter
from stackcrawler.HackerNewsParser import HackerNewsParser


# This is a demo of how to use the stackcrawler package
def main():
    stack_crawler = StackCrawler(parser=HackerNewsParser(), filter=EntryFilter())
    entries = stack_crawler.fetch_entries_from_HTML(url='https://news.ycombinator.com/', limit=25)    
    print(entries)
    print(stack_crawler.filter.filter_by_word_count_and_order_by_comments(entries))
    print(stack_crawler.filter.filter_by_word_count_and_order_by_points(entries))

if __name__ == '__main__':
    main()