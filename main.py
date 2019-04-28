import requests
import json
from urllib.parse import quote
from encrypt import PrpCrypt
import datetime

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
        # name = "tts_{}.mp3".format(i)
        now_time = datetime.datetime.now()  # get current time
        FormatTime=now_time.strftime("%Y-%m-%d&&%H:%M:%S") # transfer show format
        name = "tts_{}.mp3".format(FormatTime)
        # with open("tts.mp3", "wb") as f:
        with open(name, "wb") as f:
            f.write(res.content)


iflytek = Iflytek()

# ---------------------中文主播---------------------
# iflytek.tts('你好我是云润TTS!', '65070') #65070 //小俊
# iflytek.tts('你好我是云润TTS!', '65090') #65090 //彬哥
# iflytek.tts('你好我是云润TTS!', '68080') #65080 //程程
# iflytek.tts('你好我是云润TTS!', '65080') #65320 //小薛
# iflytek.tts('你好我是云润TTS!', '65040') #65040 //小英
# iflytek.tts('你好我是云润TTS!', '65010') #65010 //小洋
# iflytek.tts('你好我是云润TTS!', '68080') #65110 //小光
# iflytek.tts('你好我是云润TTS!', '65110') #65340 //小南
# iflytek.tts('你好我是云润TTS!', '64010') #64010 //坤叔
# iflytek.tts('你好我是云润TTS!', '65360') #65360 //瑶瑶
# iflytek.tts('你好我是云润TTS!', '15675') #15675 //小宇
# iflytek.tts('你好我是云润TTS!', '62020') #62020 //小芳
# iflytek.tts('你好我是云润TTS!', '62060') #62060 //百合仙子
# iflytek.tts('你好我是云润TTS!', '65310') #65310 //飞飞
# iflytek.tts('你好我是云润TTS!', '62070') #62070 //韦香主
# iflytek.tts('你好我是云润TTS!', '60150') #60150 //老马
# iflytek.tts('你好我是云润TTS!', '65250') #65250 //大灰狼
# iflytek.tts('你好我是云润TTS!', '62010') #62010 //小华
# iflytek.tts('你好我是云润TTS!', '62010') #65270 //原野
# # ---------------------特色语音合成---------------------
iflytek.tts('你好我是云润TTS!', '67230') #67230 //葛二爷
# iflytek.tts('你好我是云润TTS!', '60170') #60170 //萌小新
# iflytek.tts('你好我是云润TTS!', '60120') #60120 //小桃丸
# iflytek.tts('你好我是云润TTS!', '67100') #67100 //颖儿
#
# # ---------------------方言主播---------------------
# iflytek.tts('你好我是云润TTS!', '68060') #68060 //小蓉
# iflytek.tts('你好我是云润TTS!', '10003') #10003 //小梅
# iflytek.tts('你好我是云润TTS!', '68030') #68030 //小坤
# iflytek.tts('你好我是云润TTS!', '68010') #68010 //小强
# iflytek.tts('你好我是云润TTS!', '68040') #68040 //晓倩
# iflytek.tts('你好我是云润TTS!', '68120') #68120 //玉儿
# iflytek.tts('你好我是云润TTS!', '68080') #68080 //小莹
#
# # ---------------------英文主播---------------------
# iflytek.tts('你好我是云润TTS!', '69055') #69055 //Mr.奥
# iflytek.tts('你好我是云润TTS!', '69020') #69020 //凯瑟琳
# iflytek.tts('你好我是云润TTS!', '69010') #69010 //John
# iflytek.tts('你好我是云润TTS!', '69030') #69030 //Steve
# # ---------------------童声主播---------------------
# iflytek.tts('你好我是云润TTS!', '60130') #60130 //楠楠

