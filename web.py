from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

#Scrape into a csv file

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'videolink'])
#grabing info - eg - if we want to grad a title, then pass title as
#an attribute


'''match = soup.title.text
print(match)'''

#grabbing the class textwidget 
'''match = soup.findAll('div', class_ = 'textwidget')
print(match)'''

'''match = soup.find('div', class_ = 'entry-content')
print(match.text)'''

#grabibng headlines summary and content video for the first one
'''
article = soup.find('article')
headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

match = soup.find('div', class_ = 'entry-content')
print(match.text)

videosource = article.find('iframe', class_='youtube-player')['src']
print(videosource)

#getting a video
videosource_id = videosource.split('/')[4].split('?')[0]
print(videosource_id)

#generate youtube link
youtube_link = f'https://youtube.com/watch?v={videosource_id}'
print(youtube_link)

'''
#headlines & summary of all the articles in page 1
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    match = article.find('div', class_='entry-content').p.text
    print(match)

    try:
    
        videosource = article.find('iframe', class_='youtube-player')['src']


        #getting a video
        videosource_id = videosource.split('/')[4].split('?')[0]


        #generate youtube link
        youtube_link = f'https://youtube.com/watch?v={videosource_id}'
    except Exception as e:
        youtube_link = None

#try catch is added, if any info in some post on the page is missing. Eg
    #video link is missing is shown here


    print(youtube_link)
    print()

    csv_writer.writerow([headline, match, youtube_link])

csv_file.close()
    
    










