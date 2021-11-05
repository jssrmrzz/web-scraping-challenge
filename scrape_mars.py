# Imports
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # Latest Mars News
    # Visit url: https://redplanetscience.com/
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3)
    soup = bs(html, 'html.parser')

    # Scrape the Mars News Site and for the latest News Title 
    newsTitle = soup.find('div', {'class': 'content_title'}).get_text()

    #newsTitle = soup.find('div', class_ = 'content_title').get_text()
    print(newsTitle)

    # Scrape the Mars News Site and for the Paragraph Text
    newsPara = soup.find('div', {'class': 'article_teaser_body'}).get_text()
    print(newsPara)

    # JPL Mars Space Images
    browser = init_browser()

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    featured_image_url = "https://spaceimages-mars.com/image/featured/mars1.jpg"

    # Mars Facts

    browser = init_browser
    url = 'https://galaxyfacts-mars.com/'
    #browser.visit(url)
    marsDF = pd.read_html('https://galaxyfacts-mars.com/')[0]

    # Mars Hemispheres

    browser = init_browser()
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    hemiSoup = bs(html, 'html.parser')
    hemiURL = hemiSoup.find_all('div', {'class': 'item'})

    # Create dictionary to store urls
    hemiURLDict = []
    for hemi in hemiURL:
        hemisURL = hemi.find('a')['href']
        hemiURLDict.append(hemisURL)
    
    title = hemiURLDict
    title

    img_url = hemiURL
    img_url

    hemiURLDict.append({'title': title, 'img_url': img_url})

    browser.quit()
    return hemiURLDict
