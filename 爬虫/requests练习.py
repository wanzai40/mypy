import  requests

# url = 'http://baidu.com'
# # s = input()
# heard = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
# }
#
# resp = requests.get(url,headers=heard)
# # print(resp.text)

#############################################
url2 = 'https://fanyi.baidu.com/sug'

s = input()

dic = {
        'kw' : s
}
header3 = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
cookic = {
        "Cookie":"BIDUPSID=63D4625E4B8E7A0606D2F21046128756; PSTM=1603200156; H_WISE_SIDS=61027_61218_60851_61353_61362_61373_61391_61392_61389_61423_61428; BAIDUID=629AB13A925EE40BECD33A79B77438ED:FG=1; H_WISE_SIDS_BFESS=61027_61218_60851_61353_61362_61373_61391_61392_61389_61423_61428; BDUSS=BMdHM2M0RzMjR0ak1yWGcxNWwxUDdORkg1aGp6VjctRjhYfjN2Y1I5LWxJdnRuSVFBQUFBJCQAAAAAAAAAAAEAAADnP~5YyrG54m90bQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKWV02elldNnWT; BDUSS_BFESS=BMdHM2M0RzMjR0ak1yWGcxNWwxUDdORkg1aGp6VjctRjhYfjN2Y1I5LWxJdnRuSVFBQUFBJCQAAAAAAAAAAAEAAADnP~5YyrG54m90bQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKWV02elldNnWT; H_PS_PSSID=60271_61027_62325_62346_62372_62423_62427_62497_62457_62454_62452_62451_62543_62619_62635; BAIDUID_BFESS=629AB13A925EE40BECD33A79B77438ED:FG=1; ab_sr=1.0.1_MWEwYTQyMjRmY2Q5NGM3NmU2MDY2OGU5YjhlNzVmN2Q2NWE1OTMzZmZmNTQ3YjdkZWU5NWZjZTA2MGRlNjFkMWQ2NDQ0ZGVjM2YxNGQwNjEwY2UwYzZkNDVmNDFkMTM3YWQ5ZThhZTNkODZlMjkzMjgzZGUwZTY1OTM1ODdmY2M5NzUyMTJkYWQwZDQ5NmJiM2ExYzkwYTkzNzc1YmFkNg==; RT='z=1&dm=baidu.com&si=5ecba343-998d-47a6-9622-6962ef6b9964&ss=m8mhb6l8&sl=4&tt=sjp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=jpdl"}

resp2= requests.post(url2,data=dic,cookies=cookic,headers=header3)
print(resp2.json())     #将服务器返回的内容直接处理成JSON也就是字典


##########################################
# url3 = 'https://movie.douban.com/typerank'
# param = {
#         "type":"11",
#         "interval_id":"100%3A90",
#         "action":"",
#         "start":"0",
#         "limit":"20",
# }
# header3 = {
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
# }
# cook = {
#         'cookie':'ll="118254"; bid=CzXlBY7iHdY; __utma=30149280.739292639.1742787332.1742787332.1742787332.1; __utmc=30149280; __utmz=30149280.1742787332.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=30149280.1.10.1742787332; __utma=223695111.804065538.1742787335.1742787335.1742787335.1; __utmb=223695111.0.10.1742787335; __utmc=223695111; __utmz=223695111.1742787335.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1742787335%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=43be526c6a166183.1742787335.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __yadk_uid=jsfvd7lDM8kYPLyijcLICZY6KUuncuuN; _vwo_uuid_v2=DDB047BE67228423AB1AFBA3F769B5A90|9bdfe841a48ecef4e8db1dd28b1a8b97'
# }
# resp3 = requests.get(url=url3,headers=header3,params=param,cookies=cook)
#
# if resp3.text:
#     try:
#         print(resp3.json())
#     except requests.exceptions.JSONDecodeError:
#         print("响应体不是有效的JSON格式")
# else:
#     print("响应体为空")
# resp3.close()