import requests
# question 1
def getTotalGoals(team, year):
    # Write your code here
    total_goals = 0
    try:
        page = 1
        while True:
            response1 = requests.get(
                f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}')
            response2 = requests.get(
                f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}')
            # print(response2.json())

            data1 = response1.json()
            data2 = response2.json()

            total_goals += sum(int(match['team1goals']) for match in data1['data'])
            total_goals += sum(int(match['team2goals']) for match in data2['data'])

            if page < data1['total_pages']:
                page += 1
            else:
                break

        # print(total_goals)
        return total_goals

    except requests.exceptions.RequestException as req_err:
        print(req_err)


# Question 2

def getNumDraws(year):
    # Write your code here
    total_draw_matches = 0

    try:
        page = 1
        goals = range(0, 10)
        while True:
            response = None
            data = {}
            for g in goals:
                response = requests.get(
                    f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={g}&team2goals={g}&page={page}')
                # print(response.content)

                data = response.json()

                total_draw_matches += data['total']

            if page < data['total_pages']:
                page += 1
            else:
                break

        return total_draw_matches
    except requests.exceptions.RequestException as req_err:
        print(req_err)