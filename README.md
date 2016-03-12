# dlAssist

There are many instances where we have to download multiple files from a given
site. One example is when students need to download lecture slides from the
course website. It can be a rather tedious task to manually download each set
of lecture slides individually. dlAssist was created as a way to streamline the
download process.

Requirements
--------

dlAssist is written in Python 3.4 and makes use of the requests and Beautiful
Soup 4 modules. For instructions on how to install Beautiful Soup 4, visit:

    http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

Currently, dlAssist has only been tested in Ubuntu

Current Features
--------

* Downloads all files of a given file type from a given site
* Downloads to a user set folder on the Desktop
* Prompts user for confirmation before overwriting files
* Prompts user for username/password if authentication required for site

Instructions
--------

Run dlAssist from your terminal

    python3 dlAssist.py

You will be prompted to enter the url of the site containing the links to the
files that you wish to download.

    Enter site url: 

You will then need to specify a file type to download.

    Enter file type (ie. pdf, txt, ppt, etc.): 

You will then name the Desktop folder where the files will be downloaded to.

    Enter download folder name:

As the files are being downloaed, if dlAssist encounters an HTTP 401 error, or
authorization error, it will prompt the user for login credentials to the site.

    Authorization required
    Enter username:
    Enter password:

Password input will not be echoed as it is being entered. The user will continue to be prompted until the correct credentials are entered.

When a file is about to be overwritten, a confirmation message will appear.

    'filename' exists in folder. Overwrite? (y/n):

If the file is not to be overwritten, dlAssist will skip to the next file.