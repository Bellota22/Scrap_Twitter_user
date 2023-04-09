import requests
import random
import pandas as pd
from dotenv import load_dotenv

from bs4 import BeautifulSoup

from utils import TwitterScraper
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserCredentials(BaseModel):
    my_user_email: str = Field(
        ...,
        max_length=40,
        example ='user@email.com'
        
    )

    my_user_twitter: str = Field(
        ...,
        max_length=20,
        example = "user"
    )
    
    password: str = Field(
        ...,
        max_length=20,
        example='rodrigoselacome42'
    )

    person_scrap: str = Field(
        ...,
        max_length=20,
        example='@person_scrap3 o "random"'
    )

@app.post("/scrape-twitter")
async def scrape_twitter(user_credentials: UserCredentials):
    random_persons = ['Shiro_sun_', 'FluffyNako', 'lulu_tan__']
    my_user_email = user_credentials.my_user_email
    my_user_twitter = user_credentials.my_user_twitter
    password = user_credentials.password
    person_scrap = user_credentials.person_scrap
    scraper = TwitterScraper()
    if person_scrap == 'random':
        person_scrap = random.choice(random_persons)
    else:
        random_persons.append(person_scrap)
        
    print(person_scrap)
    scraper.login(my_user_email, my_user_twitter, password)
    print(1)
    scraper.search_users_urls(person_scrap)
    print(2)
    url_photos = scraper.get_photos()

    photos = scraper.download_photos(url_photos)

    return {"person_scraped": person_scrap}