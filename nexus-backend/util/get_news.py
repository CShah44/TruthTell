### Web scrape the url from newsfetcher
import requests
from bs4 import BeautifulSoup

def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

# stringA = "https://medium.com/geekculture/web-scraping-with-python-a-complete-step-by-step-guide-code-5174e52340ea#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImFiODYxNGZmNjI4OTNiYWRjZTVhYTc5YTc3MDNiNTk2NjY1ZDI0NzgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDM1MjA0NzY2NDQxOTgwNDg3MTQiLCJlbWFpbCI6Imt2ZWxpZGFuZGFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTczNTgyMzYwNywibmFtZSI6IlZlbGlkYW5kYSBLcmlzaG5hIFNhaSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKeENrSjIwbkcxWGprQVJwUXllMjYwVUFLYVEwZXRPa3JMdVUyMl9aMU54Z0xrSVc0PXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IlZlbGlkYW5kYSIsImZhbWlseV9uYW1lIjoiS3Jpc2huYSBTYWkiLCJpYXQiOjE3MzU4MjM5MDcsImV4cCI6MTczNTgyNzUwNywianRpIjoiMTE1OTg3ZGFiMTVhYzdlZWFlZjA3NzRkODdjYjdhMjkzNjA0MDliYyJ9.PijxIbdAtecQ5LPnANLUiqybh4rvHNAWtw1paTSkEDKWLtJ4gLG4TS_xnpH1vcctK0fJGrrPMSYwUDzU04_bpDC6FJM5huf8ek6Diq-u0NxMsPEuSwRz4vTzCI9J0zZIT8YVTXq31L3KxNTbD-omCVc9Mtd9kwFcCRojutzWjL7dyeU-FrY2CTWOPVhGanZ8TgEXWS77BU5LfLHiIslOVM32OxG4RsyPBoT6IGnSsmMnAZLOc6OP33yZ6gB9PA_mLomUlwLOSdQZLmBq5zKqJ_Gg8whsZrg8EtdT3mhZV0WvzHftNzLUMrsaH6qsOR2vE7XVONoOLm6oeZSpQcawZA"

# get_news(stringA)
