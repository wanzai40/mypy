import requests
import json
import time
import asyncio
import aiohttp
import asyncio
import aiofiles


'''
1.同步操作:访问getCatalog 拿到所有章节的cid和名称
2,异步操作:访问getChaptercontent 下载所有的文章内容
'''
# url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'

async def downlode(b_id,cid,title ):
    data = {
    'book_id' : b_id,
    'cid' : f'{b_id}|{cid}' ,
    'need_bookinfo': 1}

    data = json.dumps(data)
    url = 'https://dushu.baidu.com/api/pc/getChapterContent?data='+data
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(f'txt/{title}.txt','w',encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])          #因为用到了aiofiles，他是个异步，所以要用await



async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:      #item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        print(cid,title)
        #准备异步任务
        tasks.append(asyncio.ensure_future(downlode(b_id,cid,title)))
    await asyncio.gather(*tasks)            #加了await之后就要加上async




if __name__ == '__main__':
    b_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    asyncio.run(getCatalog(url))

