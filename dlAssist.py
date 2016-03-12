'''
dlAssist will download all files of a given file type from a webpage.
Please make sure the site is trusted before executing

Designed to help download of lecture slides, homeworks, etc.

Will download files into a folder on the Desktop
'''
#will use beautifulsoup to parse html
import requests
from urllib.parse import urlparse
import bs4
import os

#prompt input of url and file type
url = input('Enter site url: ')
fileType = input('Enter file type (ie. pdf, txt, ppt, etc.): ')

#prompt folder name for download
folderName = input('Enter download folder name: ')

#create anchor tag list
html = requests.get(url).content
soup = bs4.BeautifulSoup(html, 'lxml')
tags = soup('a')

#remove path from url
u = urlparse(url)
url = '://'.join(u[0:2]) + '/'

#construct folder path
folder = os.path.expanduser('~') + '/Desktop/' + folderName

#create folder if it does not exist
if not os.path.exists(folder):
    os.mkdir(folder)
folder += '/'

#default assumes no username/password required
username, password = None, None

#print out all tags of selected file type
for tag in tags:
    link = tag.get('href', None)
    if link.split('.')[-1] == fileType:
        fileURL = url + link
        req = requests.get(fileURL, auth=(username, password))
        #prompt for username/password input if authorization required
        #will loop until correct username/password entered
        while req.status_code == 401:
            print('Authorization required')
            username = input('Enter username: ')
            password = input('Enter password: ')
            req = requests.get(fileURL, auth=(username, password))

        #set file name and path
        fileName = link.split('/')[-1]
        filePath = folder + fileName

        #assume default to not overwrite existing files
        confirm = 'n'
        #confirm overwriting a file that exists
        if os.path.exists(filePath):
            confirm = input(fileName + ' exists in folder. Overwrite? (y/n): ')
            if confirm == 'n':
                print('Download of ' + fileName + ' skipped')
                continue

        #write file to folder
        with open(filePath, 'wb') as f:
            print('Downloading ' + fileName)
            f.write(req.content)

print('Downloads complete')