import re

import requests


url = 'https://mooc1.chaoxing.com/exam-ans/exam/test/reVersionPaperMarkContentNew?courseId=249868900&classId=114484232&p=1&id=157944487&ut=s&newMooc=true&qbanksystem=1&qbankbackurl=%2Fexam-ans%2Fexam%2Ftest%2Flook%3FcourseId%3D249868900%26classId%3D114484232%26examId%3D6976138%26examAnswerId%3D157944487%26cpi%3D357818587&cpi=357818587&openc=78ee16aa307ebae58a4bae713b9dba81'
head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'referer':'https://mooc1.chaoxing.com/exam-ans/exam/test/reVersionPaperMarkContentNew?courseId=249868900&classId=114484232&p=1&id=157944487&ut=s&newMooc=true&qbanksystem=1&qbankbackurl=%2Fexam-ans%2Fexam%2Ftest%2Flook%3FcourseId%3D249868900%26classId%3D114484232%26examId%3D6976138%26examAnswerId%3D157944487%26cpi%3D357818587&cpi=357818587&openc=78ee16aa307ebae58a4bae713b9dba81',
    'x-tt-logid':'2025061310552119216821809412900',
    'x-dsa-trace-id':'17497833214f1f1f3454ff61ffacdd562ecdf5c6ca'
}
resp = requests.get(url,headers=head)
resp.encoding = 'utf-8'
print(resp.text)