#Import all libraries
#open the url and read the api response
#identify each data point in you rjson and print it to a spreadsheet

import csv
import json
import datetime

#requests: allow sus to open websites using a url
#beautifulsoup4: helps us read the html and css code of websites
#pandas: enables parsing of millions of data rows, modification of those, and applying math to it and exporting results

import requests

channel_id1 = "UCJFp8uSYCjXOMnkUyb3CQ3Q"
channel_id2 = "UCpko_-a4wgz2u_DgDgd9fqA"
youtube_api_key = "AIzaSyAi_uIqNPhRYWtoqP96aHVoB3eJwH47rQ0"

def make_csv(page_id):
    base = "https://www.googleapis.com/youtube/v3/search?"
    fields = "&part=snippet&channelId="
    api_key = "&key=" + youtube_api_key
    api_url = base + fields + page_id+ api_key
    api_response = requests.get(api_url)
    videos = json.loads(api_response.text)

    #retrive data points from json to put into a spreadsheet
    videos = json.loads(api_response.text)

    with open("youtube_videos.csv", "w", encoding = "utf-8") as csv_file:
        csv_writer = csv.writer(csv_file) #allows us to write rows of data into the file. 

    csv_writer.writerow(["publishedAt", "title", "description", "thumbnailurl"])
    has_another_page = True
    while has_another_page:
        if videos.get("items") is not None:
            for video in videos.get("items"):
                video_data_row = [
                video["snippet"]["publishedAt"], video["snippet"]["title"].encode("utf-8"),video["snippet"]["description"].encode("utf-8"),video["snippet"]["thumbnails"]["default"]["url"].encode("utf-8")
            ]
            csv_writer.writerow(video_data_row)
        if "nextPageToken" in videos.keys():
            next_page_url = api_url+"&pageToken="+videos["nextPageToken"]
            next_page_posts = requests.get(next_page_url)
            videos = json.loads(next_page_posts.text)
        else:
            print("no more videos!")
            has_another_page = False

make_csv(channel_id1)
make_csv(channel_id2)

""" 

api_url = "https://www.googleapis.com/youtube/v3/search?channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet&key=AIzaSyAi_uIqNPhRYWtoqP96aHVoB3eJwH47rQ0&q=cake"
api_response = requests.get(api_url) #use requests library to connect to the internet, make the api call to the specified url
videos = json.loads(api_response.text) # recieve the api's response, the .loads method translates plain api_Response text into json keys and vals

#creates csv file, called youtube_videos and does "w" or writes as opposed to "r" or "a"(read or add)
with open("youtube_videos.csv", "w", encoding = "utf-8") as csv_file:
    csv_writer = csv.writer(csv_file) #allows us to write rows of data into the file. 
    csv_writer.writerow(["publishedAt", "title", "description", "thumbnailurl"])#writers all the headers as this first row. 

    #video information is inside of values under "items" key. 
    if videos.get("items") is not None:
        for video in videos.get("items"):
            video_data_row = [
            video["snippet"]["publishedAt"], video["snippet"]["title"],video["snippet"]["description"],video["snippet"]["thumbnails"]["default"]["url"]
        ]
        csv_writer.writerow(video_data_row)

#api providers build in ways to slow down data-grabbing process. youtube limits data we can request w/pagination, diving data into multiple json objects
      
  """