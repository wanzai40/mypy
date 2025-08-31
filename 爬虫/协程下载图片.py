import  asyncio
import os

import aiohttp

urls = [
    'https://vcg03.cfp.cn/creative/vcg/800/new/VCG21gic18853778.jpg',
    'https://vcg03.cfp.cn/creative/vcg/800/new/VCG211388638247.jpg',
    'https://vcg02.cfp.cn/creative/vcg/800/new/VCG211379951298.jpg'
]

async def download(url):
    name = url.rsplit('/',1)[1]
    path = os.path.join('./img', name)
    async with aiohttp.ClientSession() as session:          #（session）相当于requests
        async with session.get(url) as resp:                #相当于resp=requests.get(url)
            with open(path, 'wb') as f:     #rsplit('/',1)[1]---从右边切，切1次，取【1】的
                f.write(await resp.content.read())          #读取内容是异步，需要await 挂起


async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())