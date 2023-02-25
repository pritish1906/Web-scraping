import csv
import json

data = []


with open('personal_male.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        dict = {
        "name":"",
        "fullName":"",
        "dob":"",
        "country":"",
        "birthPlace":"",
        "nationalTeam":"",
        "teams":"",
        "battingStyle":"",
        "bowlingStyle":""
        }

        x = list(dict.keys())
        if int(row[2].split('-')[-1]) > 1970:
            for i in range(0,len(x)):
                dict[x[i]] = row[i]
            data.append(dict)

    # print(data);

json_object = json.dumps(data, indent=4)

# Writing to sample.json
with open("dataset.json", "w") as outfile:
    outfile.write(json_object)


