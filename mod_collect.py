from urllib import request

from requests import get
from bs4 import BeautifulSoup

git = 'https://github.com/search?q=pandas'
url = get(git)
print(url.text[:50])

html_soup = BeautifulSoup(url.text, 'html.parser')
repertoire = html_soup.find_all('li', class_='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source')

for rep in repertoire:
    print('////////////////////////////////////////////////////////////////////')

    titre = rep.a
    star = rep.find('a', class_='Link--muted')

    print(titre.text)
    print('==========================================')

    print(star.text)
    print('==========================================')

    hub = 'https://github.com/' + titre.text
    url2 = get(hub)
    html_soup2 = BeautifulSoup(url2.text, 'html.parser')
    aspect = html_soup2.find_all('div', class_='BorderGrid BorderGrid--spacious')

    for apt in aspect:
        tags = apt.find_all('a', class_='topic-tag topic-tag-link')
        if tags is None:
            print(tags)
        else:
            for topics in tags:
                print('-----------')
                print(topics.text)

        print('==========================================')
        desc = apt.p
        if desc is None:
            print(desc)
        else:
            print(desc.text)

        print('==========================================')
        link = apt.a
        if link is None:
            print(link)
        else:
            for lin in link:
                print('-----------')
                print(lin.text)

        print('==========================================')
        version = apt.find('span', class_='css-truncate css-truncate-target text-bold mr-2')
        if version is None:
            print(version)
        else:
            print(version.text)

        print('==========================================')
        releases = apt.find('relative-time')
        if releases is None:
            print(releases)
        else:
            print(releases['datetime'])

        print('==========================================')
        sponsor = apt.find_all('span', class_='flex-self-center')
        if sponsor is None:
            print(sponsor)
        else:
            for spon in sponsor:
                print('-----------')
                print(spon.text)

        print('==========================================')
        packages = apt.find('a', href='/orgs/pandas-dev/packages?repo_name=pandas')
        #### j’ai pas trouve de repertoire qui contient des packages ####
        if packages is None:
            print(packages)
        else:
            print(packages.text)

        print('==========================================')
        use = apt.find_all('img', class_='avatar avatar-user')
        if use is None:
            print(use)
        else:
            for user in use:
                print('-----------')
                print(user['alt'])

        print('==========================================')
        contrib = apt.find_all('li', class_='mb-2 mr-2')
        if contrib is None:
            print(contrib)
        else:
            for contributor in contrib:
                print('-----------')
                print(contributor.a.img['alt'])

        print('==========================================')
        languages = apt.find_all('li', class_='d-inline')
        if languages is None:
            print(languages)
        else:
            for lang in languages:
                lan = lang.a
                if lan.span is None:
                    print(lan)
                else:
                    print('-----------')
                    print(lan.span.text)
    print(len(aspect))

    print('////////////////////////////////////////////////////////////////////')

print(type(repertoire))
print(len(repertoire))
