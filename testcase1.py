import requests
from bs4 import BeautifulSoup, GuessedAtParserWarning

#------------------------------------------------------------------------------
class Parse_Web_Content:

    def __init__(self, host_url):
        self.host_url = host_url

    #--------------------------------------------------------------------------
    def get_content(self, url):
        try:
            response = requests.get(url)
            self.content = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"Error while parsing host url {e}")

    #--------------------------------------------------------------------------
    def get_urls_using_class(self, class_name):
        urls_dict = {}
        for a_tag in self.content.find_all('a', class_=class_name):
            urls_dict[a_tag.text] = self.host_url+a_tag['href']
        return urls_dict

    #--------------------------------------------------------------------------
    def validate_urls(self, urls):
        for name, url in urls.items():
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{name} menu status code is {response.status_code} "\
                        "Hence the link is valid")

            else:
                print(f"{name} menu status code {response.status_code} which "\
                        "is not equal to 200. Hence the link is invalid")

    #--------------------------------------------------------------------------
    def get_product_from_menu(self, menu):
        pass

#------------------------------------------------------------------------------
if __name__ == '__main__':
    host_url = "https://www.flaconi.de"
    cls = Parse_Web_Content(host_url)

    print("1) Main navigation menu - check if all links from the main "\
            "navigation menu are valid links and return 200 HTTP response "\
            "status codes\n\n")

    #Get website content
    cls.get_content(host_url)

    #Get main menu links
    menu_class = ['Navigationstyle__MenuLink-sc-1r9fvyg-3 gpeuWL']
    menu_links = cls.get_urls_using_class(menu_class)

    #Validate links
    cls.validate_urls(menu_links)

    print('\na) Hover over MAKE-UP main nav menu\n\n')
    #Get sub menu links
    sub_menu_name = "Make-up"
    sub_menu_link = {name:link for name,link in menu_links.items() if name == sub_menu_name}

    cls.get_content(sub_menu_link[sub_menu_name])

    sub_menu_class = ['Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse',
                        'Linkstyle__A-sc-5bdtqf-0 dQURyc \
                        Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse',
                        'Navigationstyle__ItemLink-sc-1r9fvyg-16 dRpPSG']
    sub_menu_links = cls.get_urls_using_class(sub_menu_class)

    cls.validate_urls(sub_menu_links)