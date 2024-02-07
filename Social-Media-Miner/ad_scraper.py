import csv
from bs4 import BeautifulSoup

rows = [] #empty array for data storage
foldername = "facebook-chrisli1234567890-06_02_2024-Qn0Y5YT0"

with open("%s/ads/advertisers_you've_interacted_with.html" % foldername) as page:
    soup = BeautifulSoup(page,"html.parser")
    #grabbing needed elements
    contents = soup.find("div", class_ = "_4t5n")
    ad_list = contents.find_all("div", class_ = "uiBoxWhite")

    #extracting contents
    for item in ad_list:
        advert = item.find("div", class_= "_2let").get_text()
        timeaccessed = item.find("div", class_ = "_2lem").get_text()
        #create dictionary for data, append to our .csv file
        row = {
            "advert": advert,"timeaccessed": timeaccessed
        } # the advert and timeaccessed keys are strings that represent types of data we want to collect. 
        rows.append(row)

with open("%s/ads/advertisers_you've_interacted_with.html" % foldername, "w+") as csvfile:
    fieldnames = ["advert", "timeaccessed"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerrow(row)


