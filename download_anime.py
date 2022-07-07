import requests
import m3u8
import subprocess
import time

def download_m3u8(baseurl, m3u8url, name):
    '''

    Parameters
    ----------
    baseurl : STR
        url of the m3u8 without the part from '/' and on
    m3u8url : STR
        url with the m3u8 file in it (ends with .m3u8)
    name : STR
        name you want to save the file as

    You'll find both a .TS file and a .mp4 file in the same directory where you ran this
    '''
    r = requests.get(m3u8url)
    m3u8_master = m3u8.loads(r.text)
    data = m3u8_master.data
    i = 0
    with open(f"{name}.ts","wb") as f:
        for segment in data['segments']:
            i += 1
            url = '/'.join([baseurl, segment['uri']])
            r = requests.get(url)
            time.sleep(1)
            f.write(r.content)
    subprocess.run(['ffmpeg', '-i', f'{name}.ts', f'{name}.mp4'])
    print(f"File {name} downloaded")
