import requests

url = 'https://www.pearvideo.com/video_1799034'
contId = url.split('_')[1]

videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6816062576941755'

head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',

        'referer':url           #防盗链
}

resp  = requests.get(videoStatus,headers=head)
dic = resp.json()


srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')

with open('img/a.mp4',mode='wb') as f:
    f.write(requests.get(srcUrl).content)
