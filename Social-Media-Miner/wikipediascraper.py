import csv 
import time

from bs4 import BeautifulSoup 
import requests

#Your identification
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", "from":"zheyuli2012@gmail.com"}

rows = []

#open the website
urls = ["https://en.wikipeda.org/wiki/Category:Women_computer_scientists", "https://en.wikipeda.org/w/index.php?title=Category:women_computer_scientists&pagefrom=Lin%2C+Ming+C.%OAMing+C.+Lin#mw-pages"]

# url = "https://en.wikipeda.org/wiki/Category:Women_in_computing"
# page = requests.get(url)
# page_content = page.content 
# #parse the page with Beautiful Soup 
# soup = BeautifulSoup(page_content, "html.parser")
# content = soup.find("div", class_= "mw-category")
# all_groupings = content.find_all("div", class_ = "mw-category-group")

def scrape_content(url):
    time.sleep(2)
    page = requests.get(url, headers = headers)
    page_content = page.content

    #parse the page through BeautifulSouplibrary
    soup = BeautifulSoup(page_content, "html.parser")
    content = soup.find("div", class_= "mw-category") #class_ is a reserved keyword
    all_groupings = content.find_all("div", clas_ = "mw-category-group")
    for grouping in all_groupings:
        names_list = grouping.find("ul")
        category = grouping.find("h3").get_text()
        alphabetical_names = names_list.find_all("li")
        for alphabetical_name in alphabetical_names:
            #get the name
            name = alphabetical_name.text
            #get the link
            anchortag = alphabetical_name.find("a", href = True)
            link = anchortag["href"]
            #get the letter
            letter_name = category
            #make a data dictionary that will be written into the csv 
            row = {"name":name, "link":link,"letter_name":letter_name}
            rows.append(row)
    for url in urls:
        scrape_content(url)
    
    #make a new csv into which we will write all the rows
    with open("all-women-computer-scientists.csv", "w+") as csvfile:
        #these are the header names:
        fieldnames = ["name", "link", "letter_name"]
        #this creates your csv
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        #this writes in the first row, which are the headers
        writer.writeheader()

        #this loops through your rows(the array you set at the beginning and have updated throughout)
        for row in rows:
            #this takes each row and writes it into your csv
            writer.writerow(row)


