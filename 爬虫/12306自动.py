import time

import requests
import json
from DrissionPage import ChromiumPage
from DrissionPage.common import Actions
from DrissionPage.common import Keys
from pypinyin import pinyin ,Style
def change(chaina):
    text = pinyin(chaina, style=Style.NORMAL)
    return ''.join([i[0] for i in text])

dp = ChromiumPage()

dp.get('https://kyfw.12306.cn/otn/resources/login.html')
dp.ele('x://html/body/div[1]/div[2]/div[2]/ul/li[2]/a').click()
dp.wait.load_start()
# dp.wait.load_complete()

# dp.wait.ele_displayed('css:#link_for_ticket')  # 直到匹配的元素可见

# page.ele('x://a[text()="继续"]').click(by_js=True, wait=1)
# wait=1 表示先等 1 秒再触发点击
time.sleep(5)
dp.get('https://kyfw.12306.cn/otn/leftTicket/init')
action = Actions(dp)
action.move_to('css:#fromStationText').click().type('wuhan')
dp.ele('css:#fromStationText').input(Keys.ENTER)

action.move_to('css:#toStationText').click().type('shanghai')
dp.ele('css:#toStationText').input(Keys.ENTER)

dp.ele('css:#train_date').clear()
dp.ele('css:#train_date').input('2025-09-01')

dp.ele('css:#query_ticket').click()