import csv
import json
import wikipedia
import requests
from tqdm import tqdm


data = []

WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='

def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results = 1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title = result[0])
        title = wkpage.title
        response  = requests.get(WIKI_REQUEST+title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']
        return img_link        
    except:
        return 0


with open('./data_cscs/personal_male.csv','r') as file:
    reader = csv.reader(file)
    for row in tqdm(reader):
        dict = {
        "name":"",
        "fullName":"",
        "dob":"",
        "country":"",
        "birthPlace":"",
        "nationalTeam":"",
        "teams":"",
        "battingStyle":"",
        "bowlingStyle":"",
        "display_photo":""
        }
        x = list(dict.keys())

        if (int(row[2].split('-')[-1]) > 1970):
            img = get_wiki_image(row[0])
            if img:
                row.append(img)
                with open("dataset_v2.csv", "a") as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(row)
            else:
                continue




stats = {}
with open('./data_cscs/ODI data.csv','r') as file:
    reader = csv.reader(file)
    for row in tqdm(reader):
        arr = list(row[3:len(row)-1])
        stats[tolower()]




