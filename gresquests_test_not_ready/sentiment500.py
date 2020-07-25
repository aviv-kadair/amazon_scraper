import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

payload = "text=great%20value%20in%20its%20price%20range!"
headers = {
    'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
    'x-rapidapi-key': "59e71f2ca2msh163b97bedf8febbp1d0d70jsn7f90e95f54ab",
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
