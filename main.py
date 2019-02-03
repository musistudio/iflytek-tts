import requests
import json
from urllib.parse import quote
from encrypt import PrpCrypt


class Iflytek(object):

    def tts(self, text, vid):
        url = "http://www.peiyinge.com/web-server/1.0/works_synth_sign"
        pc = PrpCrypt('G%.g7"Y&Nf^40Ee<')
        data = '{"channel": "%s","synth_text_hash_code":"%s"}' % ('10000001', pc.md5(text))
        s = pc.encrypt(data)
        data = {
            "req": s
        }
        res = requests.post(url="http://www.peiyinge.com/web-server/1.0/works_synth_sign", data=data)
        data = json.loads(pc.decrypt(res.json()['body']))
        # print(data)
        self.getMp3File(data["time_stamp"], data["sign_text"], vid, text)

    def getMp3File(self, ts, sign, vid, content):
        url = "http://proxy.peiyinge.com:17063/synth?ts={}&sign={}&vid={}&volume=0&speed=0&content={}".format(ts, sign, vid, quote(content))
        res = requests.get(url)
        with open("tts.mp3", "wb") as f:
            f.write(res.content)


iflytek = Iflytek()
iflytek.tts('几点了', '67100')
