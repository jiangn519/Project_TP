import requests
import urllib3
from bs4 import BeautifulSoup


class github_crawl():
    def __init__(self):

        self.login_headers = {
            "Referer": "https://github.com/",
            "Host": "github.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        self.login_url = "https://github.com/login"
        self.post_url = "https://github.com/session"

        self.session = requests.Session()

    def parse_loginPage(self):

        html = self.session.get(url=self.login_url, headers=self.login_headers, verify=False)
        Soup = BeautifulSoup(html.text, "html.parser")
        token = Soup.find("input", attrs={"name": "authenticity_token"}).get("value")

        return token

    def get_page(self, page_count):
        page = 0
        count = 0
        url = 'https://github.com/search?q=python'
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find('ul', class_='repo-list').findAll('a', class_='v-align-middle')
        i=1
        for item in items:

            print(item.text.strip())
            i += 1
            # if(i>10):
            #     break






        # while page < page_count:
        #     try:
        #         # specify the url
        #         quote_page = 'https://github.com/search?q=python'
        #         # query the website and return the html to the variable ‘page’
        #         page = urllib3.urlopen(quote_page)
        #         # parse the html using beautiful soap and store in variable `soup`
        #         soup = BeautifulSoup(page, 'html.parser')
        #         # Take out the <div> of name and get its value
        #         name_box = soup.find('a', attrs={'class': 'v-align-middle'})
        #         for name in name_box:
        #             name = name_box.text.strip()  # strip() is used to remove starting and trailing
        #             print(name)
        #
        #         page += 1
        #
        #     except:
        #         pass
        # print(count)

    def login(self, user_name, password, page_count):

        post_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": self.parse_loginPage(),
            "login": user_name,
            "password": password
        }

        logined_html = self.session.post(url=self.post_url, data=post_data, headers=self.login_headers, verify=False)
        if logined_html.status_code == 200:
            self.get_page(page_count)


if __name__ == "__main__":
    page_count = 1
    x = github_crawl()
    x.login("", "", page_count)