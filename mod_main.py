from main_classes import RegistreGitInfos
from mod_web import scrap_github


def main():
    listing = RegistreGitInfos()
    scrap_github("panda", listing)


if __name__ == '__main__':
    main()
