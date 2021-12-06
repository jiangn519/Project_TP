from typing import Any
import sqlite3


def cree_tab():
    conn = obtenir_connexion()
    curseur = conn.cursor()
    cde_tab = '''create table if not exists GITable(
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
                  contributors text
                  )
                  '''
    curseur.execute(cde_tab)

def obtenir_connexion():
    return sqlite3.connect('GHbd.bdf')

def insertion_table(data):
    conn = obtenir_connexion()
    curseur = conn.cursor()
    cde_ins = '''insert into GITable( repertoire,
                  stars,
                  topics,
                  description,
                  link,
                  version,
                  release,
                  sponsor,
                  packages,
                  user,
                  contributors) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''';
    for ins in data.registre:
        curseur.execute(cde_ins, [ins.titre,
                              ins.star,
                              ins.topics,
                              ins.description,
                              ins.links,
                              ins.version,
                              ins.releases,
                              ins.sponsors,
                              ins.packages,
                              ins.users,
                              ins.contributors])
    conn.commit()
    conn.close()




# recherche

def recherche():
    conn = obtenir_connexion()
    curseur = conn.cursor()
    recherche = str(input('recherche par repertoire, topic ou profile?:'))
    r = 0

    while r == 0:
        if recherche == 'topic':
            topic_rec = str(input('topic recherché ?:'))
            rec = '''select repertoire, stars, topics,
                          description,
                          link,
                          version,
                          release,
                          sponsor,
                          packages,
                          user,
                          contributors from GITable where topics =?'''
            curseur.execute(rec, [topic_rec])
            for req in curseur:
                print('''repertoire:{}, stars:{}, topics:{}, description:{}, link:{}, version:{}, release:{},
                          sponsor{}, packages:{}, user:{}, contributors:{}'''.format(req[0], req[1], req[2],
                                                                                  req[3], req[4], req[5],
                                                                                  req[6], req[7], req[8],
                                                                                  req[9], req[10]))
            r = 1

        elif recherche == 'repertoire':
            repertoire_rec = str(input('repertoire recherché ?:'))
            rec = '''select repertoire, stars, topics,
                          description,
                          link,
                          version,
                          release,
                          sponsor,
                          packages,
                          user,
                          contributors from GITable where repertoire =?'''
            curseur.execute(rec, [repertoire_rec])
            for req in curseur:
                print('''repertoire:{}, stars:{}, topics:{}, description:{}, link:{}, version:{}, release:{},
                          sponsor{}, packages:{}, user:{}, contributors:{}'''.format(req[0], req[1], req[2],
                                                                                  req[3], req[4], req[5],
                                                                                  req[6], req[7], req[8],
                                                                                  req[9], req[10]))
            r = 1

        elif recherche == 'profile':
            profile_rec = str(input('profile recherché ?:'))
            rec = '''select repertoire, stars, topics,
                              stars,
                              description,
                              link,
                              version,
                              release,
                              sponsor,
                              packages,
                              user,
                              contributors from GITable where user =?'''
            curseur.execute(rec, [profile_rec])
            for req in curseur:
                print('''repertoire:{}, stars:{}, topics:{}, description:{}, link:{}, version:{}, release:{},
                          sponsor{}, packages:{}, user:{}, contributors:{}'''.format(req[0], req[1], req[2],
                                                                                  req[3], req[4], req[5],
                                                                                  req[6], req[7], req[8],
                                                                                  req[9], req[10]))

            rec2 = '''select repertoire, stars, topics,
                              stars,
                              description,
                              link,
                              version,
                              release,
                              sponsor,
                              packages,
                              user,
                              contributors from GITable where contributors =?'''
            curseur.execute(rec2, [profile_rec])
            for req in curseur:
                print('''repertoire:{}, stars:{}, topics:{}, description:{}, link:{}, version:{}, release:{},
                          sponsor{}, packages:{}, user:{}, contributors:{}'''.format(req[0], req[1], req[2],
                                                                                  req[3], req[4], req[5],
                                                                                  req[6], req[7], req[8],
                                                                                  req[9], req[10]))
            r = 1

        elif recherche == 'annuler':
            r = 1


        else:
            recherche = str(input('''Voulez-vous une recherche par ( repertoire / topic / profile )? insere votre 
                                     reponse ou ( annuler ) pour arreter la recherche :'''))








