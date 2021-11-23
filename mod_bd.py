from typing import Any

import sqlite3


def cree_tab():
    conn = obtenir_connexion()
    curseur = conn.cursor()
    cde_tab = '''create table if not existe GITable(
                  repertoire text,
                  stars text,
                  topics text,
                  description text,
                  link text,
                  version text,
                  release int,
                  sponsor text,
                  packages text,
                  user text,
                  contributors text,
                  languages text,
                  )
                  '''
    curseur.execute(cde_tab)

def obtenir_connexion():
    return sqlite3.connect('GHbd.bdf')

def insertion_table(data):
    conn = obtenir_connexion()
    curseur = conn.cursor()
    cde_ins = '''insert into GITable( repertoire text,
                  stars,
                  topics,
                  description,
                  link,
                  version,
                  release,
                  sponsor,
                  packages,
                  user,
                  contributors,
                  languages) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''';
    for ins in data.registre:
        curseur.execute(cde, [ins.titre,
                              ins.star,
                              ins.topic,
                              ins.description,
                              ins.links,
                              ins.version,
                              ins.releases,
                              ins.sponsors,
                              ins.packages,
                              ins.users,
                              ins.contributors,
                              ins.languages])
    conn.commit()
    conn.close()




# recherche

def recherche():
    conn = obtenir_connexion()
    curseur = conn.cursor()
    recherche = str(input('recherche par topic, profile ou language ?:'))

    if recherche is 'topic':
        topic_rec = str(input('topic recherche ?:'))
        rec = '''select topics,
                      stars,
                      description,
                      link,
                      version,
                      release,
                      sponsor,
                      packages,
                      user,
                      contributors,
                      languages where topics =?'''
        curseur.execute(rec, [topic_rec])

    elif recherche is 'profile':
        profile_rec = str(input('profile recherche ?:'))
        rec = '''select topics,
                          stars,
                          description,
                          link,
                          version,
                          release,
                          sponsor,
                          packages,
                          user,
                          contributors,
                          languages where user =?'''
        curseur.execute(rec, [profile_rec])

        rec2 = '''select topics,
                          stars,
                          description,
                          link,
                          version,
                          release,
                          sponsor,
                          packages,
                          user,
                          contributors,
                          languages where contributors =?'''
        curseur.execute(rec2, [profile_rec])

    elif recherche is 'language':
        language_rec = str(input('languages recherche ?:'))
        rec = '''select topics,
                          stars,
                          description,
                          link,
                          version,
                          release,
                          sponsor,
                          packages,
                          user,
                          contributors,
                          languages where languages =?'''
        curseur.execute(rec, [language_rec])


