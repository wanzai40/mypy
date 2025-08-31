import aiohttp
import asyncio
import os
from urllib.parse import urljoin


async def download_ts(session, base_url, ts_name, save_folder='video'):
    ts_url = urljoin(base_url + '/', ts_name)
    save_path = os.path.join(save_folder, ts_name)

    try:
        async with session.get(ts_url) as resp:
            if resp.status == 200:
                content = await resp.read()
                with open(save_path, 'wb') as f:
                    f.write(content)
                print(f"Downloaded: {ts_name}")
            else:
                print(f"Failed to download {ts_name}: HTTP {resp.status}")
    except Exception as e:
        print(f"Error downloading {ts_name}: {str(e)}")


async def download_all_ts(m3u8_url, concurrency=10):
    # Create video directory if not exists
    os.makedirs('video', exist_ok=True)

    # Get base URL
    base_url = m3u8_url.rsplit('/', 1)[0]

    # Read m3u8 file to get TS file list
    with open('fczlm.m3u8', 'r', encoding='utf-8') as f:
        ts_files = [line.strip() for line in f if not line.startswith('#') and line.strip()]

    # Configure connection pool
    conn = aiohttp.TCPConnector(limit=concurrency)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    async with aiohttp.ClientSession(connector=conn, headers=headers) as session:
        tasks = [download_ts(session, base_url, ts_file) for ts_file in ts_files]
        await asyncio.gather(*tasks)


def merge_ts_files(output_filename='妇联4.mov'):
    folder_path = 'video/'
    file_list = []

    # Get sorted list of TS files
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_list.append(filename)
    file_list_sorted = sorted(file_list)

    # Merge files
    with open(output_filename, 'wb') as outfile:
        for ts_file in file_list_sorted:
            file_path = os.path.join(folder_path, ts_file)
            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())
            # Optional: remove the TS file after merging to save space
            # os.remove(file_path)


async def main():
    m3u8_url = 'https://vip.lzcdn2.com/20220402/1945_f2f055d5/1200k/hls/mixed.m3u8'

    # First download the m3u8 file if needed (uncomment if needed)
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(m3u8_url) as resp:
    #         with open('fczlm.m3u8', 'wb') as f:
    #             f.write(await resp.read())

    # Download all TS files concurrently
    await download_all_ts(m3u8_url)

    # Merge all TS files
    merge_ts_files()


if __name__ == '__main__':
    asyncio.run(main())