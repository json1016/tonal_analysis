from newspaper import Article
from urllib.parse import urlparse

while True:
    url = input("Feed me a valid url:\n")
    article = Article(url)
    article.download()
    article.parse()

    date = article.publish_date
    domain = urlparse(article.url).netloc
    d = domain.split(".")
    title = article.title
    if date:
        fname = d[1] + " " + date.strftime("%x").replace("/", "-") + " " + title + ".txt"
    else:
        fname = d[1] + " DATE " + title + ".txt"
    fname = fname.replace(" ", "_")
    fname = fname.replace("'", "")
    fname = fname.replace(":", "")
    fname = fname.replace("?", "")
    fname = fname.replace("!", "")
    fname = fname.replace("*", "")
    text = str(article.text)

    f = open(fname, "w", encoding="utf-8")
    f.write(text)
    print(fname)
    print()
    f.close()
