import os
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import requests
import panda as pd
import time

def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    latestnews = soup.find("div", class_="content_title").text
    paragraphtext= soup.find("div", class_="article_teaser_body").text

    
    url_2= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)

    browser.find_by_id("full_image").click()
    time.sleep(5)

    html2 = browser.html
    soup2 = BeautifulSoup(html2, "html.parser")

    img_url = soup2.find("img", class_="fancybox-image")["src"]

    featured_image_url = "https://www.jpl.nasa.gov" + img_url


    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html3= browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')    

    mars_weather = soup3.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text        

    url_4= "http://space-facts.com/mars/"
    browser.visit(url_4)
    html4= browser.html
    soup4 = BeautifulSoup(html4, "html.parser")  

    marsdata = pd.read_html(url_4)
    
    df_marsdata = marsdata[0]
    df_marsdata.columns=["Mars_Profile","Mars_ProfileValue"]
    df_marsdata.set_index("Mars_Profile",inplace=True)
    marsdata_html=df_marsdata.to_html(justify="left")
    
    url_5= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)

    html5 = browser.html
    soup5 = BeautifulSoup(html5, 'html.parser')
    mars_hemisphere=[]

    for i in range(4):
        time.sleep(5)
        images=browser.find_by_tag("h3")
        images[i].click()
        html5 = browser.html
        soup5 = BeautifulSoup(html5, 'html.parser')
        partial=soup5.find("img",class_="wide-image")["src"]
        image_title=soup5.find("h2", class_="title").text
        img_url="https://astrogeology.usgs.gov"+partial
        dictionary={"title":image_title,"img_url":img_url}
        mars_hemisphere.append(dictionary)
        browser.back()
    
    mars_hemisphere_dict = []
    
    
    
    
    
    
    
    
