# openMovieDL
A simple Python script to get movie download links from open directories

## What?
This script gets movie/TV series download links from open directories on the web

## How?
It first scrapes Google search results, then goes to open directories and scrapes them.
If a direct download link is found, it is added to the list of URLs. 

## Why?
For lazy people who can't search all the different websites to get download links.

*Note*: Author not intend any copyright violations. Please use at your own discretion.


## How to use?

### Clone the repo to local machine 
*In a command prompt or terminal window*
`git clone https://github.com/prashantsengar/openMovieD.git`

Or **Download as ZIP** from the above menu (Clone or Download) and extract the contents

### Change to the directory 
*In a command prompt/terminal window*
`cd openMovieDL`


### Install the requirements 
*In a command prompt/terminal window*
`pip3 -r requirements.txt`

### Run the script 
*In a command prompt/terminal window*
`python3 dl.py`


## Changes that can be made
- Change the TLD in `search(q, stop=20, tld='co.in')` to your country TLD if you wish (.com if google.com, .co.uk etc)
- Add websites that are not open directories and come in top search results in `any(x in j for x in ['imdb','economictimes','news','money','businesstoday','indiatoday','ndtv','india','koimi'])`

## What next?
- Create a config file for the changes
- Search other search engines
- Get complete info about the link


