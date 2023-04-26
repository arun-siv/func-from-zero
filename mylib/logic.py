import wikipedia


def wiki(name="War Goddess", length=1):
    """this is a wiki fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
