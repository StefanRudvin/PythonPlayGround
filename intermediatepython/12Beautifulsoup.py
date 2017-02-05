# Scrape multiple websites with beautifulsoup with many processes.
# Spider goes to a page, finds all links and visits all of those urls.

from multiprocessing import Pool
import bs4 as bs
import urllib.request
import random
import requests
import string

# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

# soup = bs.BeautifulSoup(source,'lxml')

# title of the page
# print(soup.title)

# get attributes:
# print(soup.title.name)

# get values:
# print(soup.title.string)

# beginning navigation:
# print(soup.title.parent.name)

# getting specific values:
# print(soup.p)

# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     #print(paragraph.string)
#     print(str(paragraph.text))

# nav = soup.nav
#
# for url in nav.find_all('a'):
#     print(url.get('href'))


def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url

url = random_starting_url()
print(url)


def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a typeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably could not find any useful links. Returning empty list.')
        return []
    except Exception as e:
        print(str(e))
        # Log this somewhere
        return []

def main():
    how_many = 50
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    # Making a list of lists a single list.
    data = [url for url_list in data for url in url_list]
    parse_us = data
    p.close()

    with open('urls.txt','w') as f:
        f.write(str(data))

    # while True:
    #     data = p.map(get_links [link for link in parse_us])
    #     # Making a list of lists a single list.
    #     data = [url for url_list in data for url in url_list]
    #     parse_us = data
    #     p.close()

if __name__ == '__main__':
    main()

