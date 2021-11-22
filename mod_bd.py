import sqlite3

# connexion sur la BD

conn = sqlite3.connect('GHbd.bdf')
cde_tab = '''create table if not existe GITable(
              repertoire text,
              topics text,
              stars text,
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

# curseur

curseur = conn.cursor()

# creer la table

curseur.execute(cde_tab)

# insertion de donnee

cde_ins = '''insert into GITable( repertoire text,
              topics,
              stars,
              description,
              link,
              version,
              release,
              sponsor,
              packages,
              user,
              contributors,
              languages) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''';
curseur.execute(cde_ins, [a, b, c, d, e, f, g, h, i, j])
conn.commit()

# recherche


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