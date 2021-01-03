import os
import pickle
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('PRIVATE KEY')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)
tone_analyzer.set_service_url(
    'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/ebd854a7-cb37-4e28-8069-95ebba735e06')

cnn = dict()
hp = dict()
fox = dict()
bb = dict()

print("Analyzing CNN...")
for fname in os.listdir(r'.\cnn'):
    date = fname.split("_")[1]
    with open("cnn/" + fname, "r", encoding='utf-8') as f:
        text = f.read().replace('\n', '')
        ta = tone_analyzer.tone(
            {'text': text},
            sentences=False,
            content_type='application/json'
        ).get_result()
        for tone in ta['document_tone']['tones']:
            tDict = cnn.get(date)
            if tDict:
                tList = tDict.get(tone['tone_name'])
                if tList:
                    tList.append(tone['score'])
                else:
                    tDict[tone['tone_name']] = [tone['score']]
            else:
                cnn[date] = {tone['tone_name']: [tone['score']]}

print("Analyzing HuffPost...")
for fname in os.listdir(r'.\huffpost'):
    date = fname.split("_")[1]
    with open("huffpost/" + fname, "r", encoding='utf-8') as f:
        text = f.read().replace('\n', '')
        ta = tone_analyzer.tone(
            {'text': text},
            sentences=False,
            content_type='application/json'
        ).get_result()
        for tone in ta['document_tone']['tones']:
            tDict = hp.get(date)
            if tDict:
                tList = tDict.get(tone['tone_name'])
                if tList:
                    tList.append(tone['score'])
                else:
                    tDict[tone['tone_name']] = [tone['score']]
            else:
                hp[date] = {tone['tone_name']: [tone['score']]}

print("Analyzing Fox...")
for fname in os.listdir(r'.\fox'):
    date = fname.split("_")[1]
    with open("fox/" + fname, "r", encoding='utf-8') as f:
        text = f.read().replace('\n', '')
        ta = tone_analyzer.tone(
            {'text': text},
            sentences=False,
            content_type='application/json'
        ).get_result()
        for tone in ta['document_tone']['tones']:
            tDict = fox.get(date)
            if tDict:
                tList = tDict.get(tone['tone_name'])
                if tList:
                    tList.append(tone['score'])
                else:
                    tDict[tone['tone_name']] = [tone['score']]
            else:
                fox[date] = {tone['tone_name']: [tone['score']]}

print("Analyzing Breitbart...")
for fname in os.listdir(r'.\breitbart'):
    date = fname.split("_")[1]
    with open("breitbart/" + fname, "r", encoding='utf-8') as f:
        text = f.read().replace('\n', '')
        ta = tone_analyzer.tone(
            {'text': text},
            sentences=False,
            content_type='application/json'
        ).get_result()
        for tone in ta['document_tone']['tones']:
            tDict = bb.get(date)
            if tDict:
                tList = tDict.get(tone['tone_name'])
                if tList:
                    tList.append(tone['score'])
                else:
                    tDict[tone['tone_name']] = [tone['score']]
            else:
                bb[date] = {tone['tone_name']: [tone['score']]}

for date in cnn:
    for tone in cnn[date]:
        toneScores = cnn[date][tone]
        toneAvg = sum(toneScores) / len(toneScores)
        cnn[date][tone] = toneAvg
for date in hp:
    for tone in hp[date]:
        toneScores = hp[date][tone]
        toneAvg = sum(toneScores) / len(toneScores)
        hp[date][tone] = toneAvg
for date in fox:
    for tone in fox[date]:
        toneScores = fox[date][tone]
        toneAvg = sum(toneScores) / len(toneScores)
        fox[date][tone] = toneAvg
for date in bb:
    for tone in bb[date]:
        toneScores = bb[date][tone]
        toneAvg = sum(toneScores) / len(toneScores)
        bb[date][tone] = toneAvg

pickle.dump(cnn, open("cnn.p", "wb"))
pickle.dump(hp, open("hp.p", "wb"))
pickle.dump(fox, open("fox.p", "wb"))
pickle.dump(bb, open("bb.p", "wb"))
