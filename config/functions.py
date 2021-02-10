import requests
import datetime


def get_exchange():
    today = datetime.datetime.now()
    # 주말은 환률 API 미재공되기 때문에 평일 날짜로 조회
    if today.weekday() >= 5:
        diff = today.weekday() - 4
        today = datetime.timedelta(days=diff)
    today = today.strftime('%Y%m%d')
    auth = 'sUnfuhQUL2VmyQUEcA2rqd3YFhh0FRnf'
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url = url.format(auth, today)
    res = requests.get(url)
    data = res.json()
    for d in data:
        if d['cur_unit'] == 'USD':
            return d['tts']
    return
