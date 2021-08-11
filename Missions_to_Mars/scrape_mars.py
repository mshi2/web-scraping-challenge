#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:

def init_browser():
    #set the chromedriver path
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict={}
# In[3]:


    url = "https://redplanetscience.com/"
    browser.visit(url)


# In[4]:


    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


# # NASA Mars News
# Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[5]:


    news_title = soup.find_all('div', class_ ='content_title')[0].text
    news_p = soup.find_all('div', class_ ='article_teaser_body')[0].text
    print(news_title)
    print(news_p)


# In[6]:


    browser.quit()


# # JPL Mars Space Images - Featured Image

# In[7]:


# Visit the following URL
#set the chromedriver path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://spaceimages-mars.com/"
browser.visit(url)


# In[8]:


#Use splinter to navigate the site and find the image url for the current Featured Mars Image and 
#assign the url string to a variable called featured_image_url.
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find("img", class_="headerimage fade-in")["src"]
featured_image_url = url + image
featured_image_url


# In[9]:


browser.quit()


# # Mars Facts

# In[10]:


#Use Pandas to scrape the table containing facts about the planet
url = 'https://space-facts.com/mars/'
tables_facts = pd.read_html(url)
tables_facts


# In[11]:


#Convert data to dataframe
facts_df = tables_facts[0]
facts_df.columns = ['Parameter', 'Value']
facts_df


# In[12]:


#Convert the data to a HTML table string
html = facts_df.to_html()
print(html)


# # Mars Hemispheres

# In[13]:


#Visit Mars Hemispheres url to obtain high resolution images for each of Mar's hemispheres.

#set the chromedriver path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

hemis_url = "https://marshemispheres.com/"
browser.visit(hemis_url)


# In[14]:


# Collect the urls by  clicking each of the links to the hemispheres

#Retrieve the titles and urls and append to list
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
hemispheres = soup.find_all('div', class_='item')

hemisphere_image_urls = {}
hemisph_title = []
img_urls = []
for hemisphere in hemispheres:
    title = hemisphere.find('h3').text
    main_url = hemis_url + hemisphere.find('a')['href']
    browser.visit(main_url)
    img_html = browser.html
    soup = BeautifulSoup(img_html, 'html.parser')
    image_url = hemis_url + soup.find('img', class_='wide-image')['src']
    hemisphere_image_urls = {
        "title" : title, 
        "img_url" : image_url
    }
    print(hemisphere_image_urls)    


# In[15]:


browser.quit()

