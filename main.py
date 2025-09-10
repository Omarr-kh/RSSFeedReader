from rss_parser import parse_rss


def print_feed(rss_feed, limit=5):
    feed = rss_feed["feed"]
    print(f"\n📡 {feed['title']}")
    print(f"🔗 {feed['link']}")
    print(f"📝 {feed['description']}\n")

    for item in rss_feed["items"][:limit]:
        print(f"📰 {item['title']}")
        print(f"   {item['link']}")
        print(f"   {item['pubDate']}\n")


def main():
    url = input("Enter RSS Feed URL: ")
    rss_feed = parse_rss(url)
    print_feed(rss_feed)


if __name__ == "__main__":
    main()
