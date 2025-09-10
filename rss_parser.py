import requests
import xml.etree.ElementTree as ET


def parse_rss(url):
    parsed_data = {}

    response = requests.get(url)
    response.raise_for_status()

    xml_data = response.text

    xml_root = ET.fromstring(xml_data)

    feed = xml_root.find(".//channel")

    feed_title = (
        feed.find("title").text if feed.find("title") is not None else "No title"
    )
    feed_link = feed.find("link").text if feed.find("link") is not None else "No link"
    feed_description = (
        feed.find("description").text
        if feed.find("description") is not None
        else "No description"
    )

    parsed_data["feed"] = {
        "title": feed_title,
        "description": feed_description,
        "link": feed_link,
    }

    feed_items = xml_root.findall(".//item")

    items = []
    for item in feed_items:
        title = (
            item.find("title").text if item.find("title") is not None else "No title"
        )
        link = item.find("link").text if item.find("link") is not None else "No link"
        description = (
            item.find("description").text
            if item.find("description") is not None
            else "No description"
        )
        pubDate = (
            item.find("pubDate").text
            if item.find("pubDate") is not None
            else "No pubDate"
        )
        items.append(
            {
                "title": title,
                "description": description,
                "link": link,
                "pubDate": pubDate,
            }
        )

    parsed_data["items"] = items

    return parsed_data
