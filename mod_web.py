from urllib import request

from requests import get
from bs4 import BeautifulSoup
from main_classes import GitInfo
import random

def scrap_github(filter, listing):

    proxies = ["43.241.141.21:35101", "181.205.41.210:7654", "1.179.148.9:55636", "5.183.71.145:39305",
               "103.152.238.82:8080"]
    header = {
        'User-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    random_proxy = random.choice(proxies)
    page = 1
    while True:
        proxies = {"http": "http://" + random_proxy}
        git = 'https://github.com/search?p=' + str(page) + '&q=' + filter
        url = get(git, headers=header, proxies=proxies)
        print('page:', page)

        html_soup = BeautifulSoup(url.text, 'html.parser')
        repertoire = html_soup.find_all('li',
                                        class_='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source')
        number = 0
        for rep in repertoire:
            number += 1
            print('////////////////////////////////////////////////////////////////////')
            print('number: ', number)

            titre = rep.a.text
            star = rep.find('a', class_='Link--muted').text

            hub = 'https://github.com/' + titre
            url2 = get(hub)
            html_soup2 = BeautifulSoup(url2.text, 'html.parser')
            aspect = html_soup2.find_all('div', class_='BorderGrid BorderGrid--spacious')
            topics = ""
            description = ""
            links = ""
            ver = ""
            rels = ""
            sponsors = ""
            packs = ""
            users = ""
            contributors = ""
            langs = ""
            for apt in aspect:
                tags = apt.find_all('a', class_='topic-tag topic-tag-link')

                if tags is None:
                    topics = "N/A"
                else:
                    for t in tags:
                        topics = topics + t.text
                desc = apt.p
                if desc is None:
                    description = "N/A"
                else:
                    description = desc.text
                link = apt.a

                if link is None:
                    links = "N/A"
                else:
                    for lin in link:
                        links = links + lin.text
                version = apt.find('span', class_='css-truncate css-truncate-target text-bold mr-2')
                if version is None:
                    ver = "N/A"
                else:
                    ver = version.text
                releases = apt.find('relative-time')
                if releases is None:
                    rels = "N/A"
                else:
                    rels = releases['datetime']

                sponsor = apt.find_all('span', class_='flex-self-center')
                if sponsor is None:
                    sponsors = "N/A"
                else:
                    for spon in sponsor:
                        sponsors = sponsors + spon.text

                packages = apt.find('a', href='/orgs/pandas-dev/packages?repo_name=pandas')
                #### j’ai pas trouve de repertoire qui contient des packages ####
                if packages is None:
                    packs = "N/A"
                else:
                    packs = packages.text

                use = apt.find_all('img', class_='avatar avatar-user')
                if use is None:
                    users = "N/A"
                else:
                    for user in use:
                        users = users + user['alt']

                contrib = apt.find_all('li', class_='mb-2 mr-2')
                if contrib is None:
                    contributors = "N/A"
                else:
                    for contributor in contrib:
                        contributors = contributors + contributor.a.img['alt'] + ' '

            print(
                "{}, {}, {},{}, {}, {},{}, {}, {},{}, {}".format(titre.replace("\n", ""), star.replace("\n", ""), topics.replace("\n", ""), description.replace("\n", ""), links.replace("\n", ""), ver.replace("\n", ""), rels.replace("\n", ""),
                                                                     sponsors.replace("\n", ""), packs.replace("\n", ""), users.replace("\n", ""), contributors.replace("\n", "")))
            listing.ajouter_info(
                GitInfo(titre.replace("\n", ""), star.replace("\n", ""), topics.replace("\n", ""), description.replace("\n", ""), links.replace("\n", ""), ver.replace("\n", ""), rels.replace("\n", ""), sponsors.replace("\n", ""), packs.replace("\n", ""), users.replace("\n", ""), contributors.replace("\n", "")))

        if page > 10:
            break
        page += 1


