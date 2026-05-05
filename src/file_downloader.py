from bs4 import BeautifulSoup
from navigator import Navigator
from json import loads


FILE_DIRECTORY_PAGE = "/dispatch.php/course/files?cid="
FILE_FLAT_PAGE = "/dispatch.php/course/files/flat?cid="
DOWNLOAD_NEWEST_FILES = "/dispatch.php/course/files/newest_files?cid="


def clone_folder_structure_of_course(navigator: Navigator, cid: str):
    url = navigator.base_url + FILE_DIRECTORY_PAGE + cid
    return clone_folder(navigator, url)
        

def clone_folder(navigator: Navigator, url): 
    response = navigator.get_url(url)
    soup = BeautifulSoup(response.content, "html.parser")
    form = soup.find(id="files_table_form")
    if not form:
        return
    data_files = loads(str(form.get("data-files")))
    data_folders = loads(str(form.get("data-folders")))

    for file in data_files:
        yield file.get("name")
    for folder in data_folders:
        yield {"folder": folder.get("name"), "files": list(clone_folder(navigator, folder.get("url")))}
        
