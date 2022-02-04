from json import loads
from re import search
from typing import Tuple, Union

from bs4 import BeautifulSoup
from requests import get


def download(url:str) -> Union[Tuple[str, str], Tuple[None, None], None]:
    if "pin.it" in url:
        url = get(url).url
        
    pin_id = search(r"/pin/([^/]+)", url).group(1)
    url = f"https://www.pinterest.com/pin/{pin_id}"

    html = get(url).text
    soup = BeautifulSoup(html, "html.parser")
    find_json = soup.find(
        'script',
        {
            'id': '__PWS_DATA__',
            'type': 'application/json'
        }
    )
    
    json_content:dict = loads(find_json.string)
    if (json_content:= json_content["props"]["initialReduxState"].get("pins", None)):
        json_content:dict = json_content.get(pin_id, None)
        
        if (gif := json_content.get("embed")):
            return ("gif", gif["src"])
        
        elif (video := json_content.get("videos")):
            return ("video", video["video_list"]["V_720P"]["url"])
        
        elif (image := json_content.get("images")):
            return ("image", image["orig"]["url"])
        
        else:
            return None
    
    else:
        return None
