from urllib import request

from requests import get
from bs4 import BeautifulSoup

from main_classes import GitInfo


def scrap_github(filter, listing):
    page = 1

    while True:
        git = 'https://github.com/search?p=' + str(page) + '&q=' + filter
        url = get(git)
        print(url.text[:50])

        html_soup = BeautifulSoup(url.text, 'html.parser')
        repertoire = html_soup.find_all('li',
                                        class_='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source')

        for rep in repertoire:
            print('////////////////////////////////////////////////////////////////////')

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
                        contributors = contributors + contributor.a.img['alt']

                languages = apt.find_all('li', class_='d-inline')
                if languages is None:
                    langs = "N/A"
                else:

                    for lang in languages:

                        lan = lang.a
                        # if lan.span is None:
                        #     print(lan)
                        # else:
                        #     print('-----------')
                        #     print(lan.span.text)
                        if lang.span.text is None:
                            langs = langs + lan.a.text
                        else:
                            langs = langs + lan.span.text
            print("*" * 50)
            print(
                "{}, {}, {},{}, {}, {},{}, {}, {},{}, {}, {}".format(titre, star, topics, description, links, ver, rels,
                                                                     sponsors, packs, users, contributors, langs))
            listing.ajouter_info(
                GitInfo(titre, star, topics, description, links, ver, rels, sponsors, packs, users, contributors,
                        langs))
            print(len(aspect))

            print('////////////////////////////////////////////////////////////////////')

            if page > 100:
                break
            page += 1


