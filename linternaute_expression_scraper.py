#imports
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import string

#scrapes all of the expressions
#found on the site
def scrape_site():

    expressions = []

    for letter in string.ascii_lowercase:

        expressions.extend(scrape_letter(letter))

    return expressions

#scrapes all of the expressions
#beginning with a given letter
def scrape_letter(letter):

    #first, we need to find the numberof pages there are
    #for this letter

    url = "https://www.linternaute.fr/expression/recherche/"

    letter = letter.lower()

    #start on the first page
    url = url + letter + "/" + str(1) + "/"

    #load the html
    page = urllib.request.urlopen(url)

    soup = bs(page, features="lxml")

    #searches for the page index
    names = soup.body.find_all('td', {"class": "multipage_corps"})

    #if there is more than one page
    if len(names) != 0:

        soup = bs(str(names[0]), features="lxml")

        names = soup.find_all('a')

        num_pages = int(bs(str(names[-1]), "html.parser").text)

    else:

        num_pages = 1



    print("Letter: " , str(letter), " | Number of Pages: ", str(num_pages), sep="")

    #we begin scraping the expressions
    #starting with the first page
    expressions = []

    #make a for-loop here
    for page_num in range(1, num_pages+1):

        print("Scraping Page: ", str(page_num), sep="")

        expressions.extend( scrape_page(letter, page_num) )

    return expressions


#scrapes all of the expressions on  a
#given page number for a given letter
def scrape_page(letter, page_index):

    #Access the html page via url

    url = "https://www.linternaute.fr/expression/recherche/"

    letter = letter.lower()
    page_index = str(int(page_index))

    url = url + letter + "/" + page_index + "/"


    #load the html
    page = urllib.request.urlopen(url)

    soup = bs(page, features="lxml")

    #this will contain all of the French expressions
    expressions = []

    #returns descendants of the 'tr' tag
    names = soup.body.findAll('tr')

    #exludes the first element due to redundancy in the html file
    for name in names[1:]:

        found = re.match('<tr height="22">', str(name))

        if found != None:

            soup = bs(str(name), features="lxml")

            #finds all links in the html
            matchs = soup.findAll("a")

            #only look at the first link since it's the only one that matters
            match = matchs[0]

            #parse the expresion out of the html
            exp = bs(str(match), "html.parser").text

            #lowercase the expression
            exp = exp.lower()

            expressions.append(exp)

    return expressions
