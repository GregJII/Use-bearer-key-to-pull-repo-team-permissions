import requests
import csv 
import json

def teams_access(b):
    headers = {
        "Authorization": "Bearer Key"
    }
    team_url = f'https://api.github.com/repos/TestPythonScript/{b}/teams'
    team_resp = requests.get(team_url, headers=headers)
    team_data = team_resp.json()

    return team_data


def run():
    with open('repos.csv', 'r') as f:
        reader = csv.reader(f)
        for column in reader:
            print(column)
            b = column[2]
            print(b)
            team_data = teams_access(b)
            print(team_data)

#    with open('teams.csv', 'a') as f:
#        writer = csv.writer(f)
#        writer.writerow([b, team_data])

    with open('teams.json', 'a') as f:
        data = {'repository': b, 'teams': team_data}
        json.dump(data, f)


if __name__ == '__main__':
    run()
