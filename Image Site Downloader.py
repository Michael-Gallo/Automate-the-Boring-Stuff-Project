#! python3
#Image_Site_Downloader.py  -    Downloads All Images for a category on imgur
import bs4,webbrowser, requests, os ,sys, logging
logging.basicConfig(level = logging.DEBUG, format = ' %(levelname)s- %(message)s')
logging.debug(os.getcwd())
#Make folder to store images and change directory to that folder
folderName= 'Images'
Directory= os.path.join(sys.path[0],folderName)
os.makedirs(Directory, exist_ok=True)
os.chdir(Directory)
logging.debug(os.getcwd())
logging.debug(os.path.dirname(folderName))
#Take search term from Sys Arg
searchTerm = sys.argv[1]
baseURL = 'https://imgur.com/search?q='  #Category Query Goes After Base URL
#Request page for search term
pageRes = requests.get(baseURL+searchTerm)
pageRes.raise_for_status()
#Extract Image out of page
soup = bs4.BeautifulSoup(pageRes.text,features = 'html.parser')
imageElems = soup.select('.image-list-link > img')
for i in range(len(imageElems)):
    imageURL = ('http://'+imageElems[i].get('src')[2:])
    imageRes= requests.get(imageURL)
    print('Downloading image %d...' % (i))
    imageFile = open((str(i)+'.jpg'),'wb')
    for chunk in imageRes.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()


