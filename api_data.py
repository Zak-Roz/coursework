import requests
from view import View
view = View()

url = "https://visual-crossing-weather.p.rapidapi.com/history"

# querystring1 = {
#     "startDateTime":"2002-01-01T00:00:00",
#     "aggregateHours":"6",
#     "location":"Kiev,UA",
#     "endDateTime":"2002-12-31T00:00:00",
#     "unitGroup":"us",
#     "dayStartTime":"9:00:00",
#     "contentType":"csv",
#     "dayEndTime":"21:00:00",
#     "shortColumnNames":"0"
#     }

headers = {
    'x-rapidapi-key': "000e7bfe94msha144e6cc241e4bcp1e2214jsnb7b7168d2442",
    'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com"
    }

def get_():
    defaults = view.choose_d()
    # print(defaults)
    response = []
    for default in defaults:
        querystring = {
            "startDateTime":f"{default['start_date']}",
            "aggregateHours":f"{default['times']}",
            "location":f"{default['location']}",
            "endDateTime":f"{default['end_date']}",
            "unitGroup":"us",
            "dayStartTime":"9:00:00",
            "contentType":"csv",
            "dayEndTime":"21:00:00",
            "shortColumnNames":"0"
            }
        # print(querystring)

        res = requests.request("GET", url, headers=headers, params=querystring)
        response.append(res)
        view.line()
        print(res.text)
        view.line()
    return response