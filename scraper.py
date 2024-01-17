import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    url = 'https://news.ycombinator.com/item?id=38842977'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_='ind', indent=0)
    comments = [element.find_next(class_='comment') for element in elements]

    keywords = {"javascript": 0, "typescript": 0, "react": 0, "python": 0,
                "fastapi": 0, "django": 0, "c#": 0, "dotnet": 0, "asp.net": 0}

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")
        words = {word.strip(".,/:;!@-_") for word in words}

        for keyword in keywords:
            if keyword in words:
                keywords[keyword] += 1

    print(keywords)
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel = ("Programming Languages")
    plt.ylabel = ("Number of Mentions")
    plt.show()


if __name__ == '__main__':
    main()
