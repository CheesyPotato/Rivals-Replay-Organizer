from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm
import zipfile

__version__ = '1.0.0'
#change every release
def update():

    soup = BeautifulSoup(requests.get('https://github.com/CheesyPotato/Rivals-Replay-Organizer/releases/latest').text, 'html5lib')
    downloadzipfile = 'https://github.com'+soup.find_all('li', {'class': 'd-block py-2'})[0].a['href']

    if downloadzipfile[-9:-4] == __version__:

        return

    response = requests.get(downloadzipfile, stream=True)
    tempdirectory = os.getcwd()
    os.chdir(os.path.dirname(os.getcwd()))



    with open("Rivals Replay Organizer " + downloadzipfile[-9:], "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    zip_ref = zipfile.ZipFile(os.getcwd() + '\\Rivals Replay Organizer ' + downloadzipfile[-9:-4] + '.zip', 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()
    os.remove(os.getcwd() + '\\Rivals Replay Organizer ' + downloadzipfile[-9:])
    os.chdir(tempdirectory)
update()
