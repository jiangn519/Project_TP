from main_classes import RegistreGitInfos, GitInfo
from mod_web import scrap_github
from mod_bd import cree_tab, obtenir_connexion, insertion_table, recherche

def main():
    search = str(input('rentrer votre mot cle de recherche GitHub :'))
    listing = RegistreGitInfos()
    scrap_github(search, listing)
    #cree_tab()
    #insertion_table(listing)
    recherche()


if __name__ == '__main__':
    main()
