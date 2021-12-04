class GitInfo:
    def __init__(self, titre, star, topics, description, links, version, releases, sponsors, packages, users, contributors,):
        self.titre = titre
        self.star = star
        self.topics = topics
        self.description = description
        self.links = links
        self.version = version
        self.releases = releases
        self.sponsors = sponsors
        self.packages = packages
        self.users = users
        self.contributors = contributors



    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.titre, self.star, self.topics, self.description, self.links, self.version, self.releases, self.sponsors, self.packages, self.users, self.contributors)

class RegistreGitInfos:
    def __init__(self):
        self.registre = []

    def ajouter_info(self, git_info):
        self.registre.append(git_info)

    def afficher_infos(self):
        for info in self.registre:
            print(info)
