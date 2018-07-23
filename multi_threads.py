#! /usr/bin/env python3

import requests
import logging
import json
from timeit import default_timer as timer
from multiprocessing import Pool as ThreadPool

def url_list():

    url_list = [
        'https://en.wikipedia.org/wiki/Main_Page',
        'https://en.wikipedia.org/wiki/Cape_sparrow',
        'https://en.wikipedia.org/wiki/Southern_Africa',
        'https://en.wikipedia.org/wiki/Continent',
        'https://en.wikipedia.org/wiki/Ural_River',
        'https://en.wikipedia.org/wiki/Albrecht_D%C3%BCrer',
        'https://en.wikipedia.org/wiki/Holy_Roman_Empire',
        'https://en.wikipedia.org/wiki/Translatio_imperii',
        'https://en.wikipedia.org/wiki/Lombards',
        'https://en.wikipedia.org/wiki/Austria'
    ]

    return url_list


def download_page(index, url):

    fetched = requests.get(url)
    logging.info((index, url))

    return fetched


def synchronous_thread():

    start = timer()

    source = url_list()
    for i, url in enumerate(source):
        fetched = download_page(i, url)
        logging.info(fetched)

    end = timer()

    return end - start


def multi_threads():

    # https://camtsmith.com/articles/2018-01/multithreading-and-multiprocessing
    start = timer()

    source = url_list()
    enum = [(i, url) for (i, url) in enumerate(source)]

    pool = ThreadPool(15)
    pool.starmap(download_page, enum)

    end = timer()

    return end - start


def main():
    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s|%(lineno)d|  %(message)s'
    )

    sync = synchronous_thread()
    logging.info(f'Synchronous run time: {sync}')

    async = multi_threads()
    logging.info(f'ASynchronous run time: {async}')


if __name__ == '__main__':
    main()