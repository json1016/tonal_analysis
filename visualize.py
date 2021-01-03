import matplotlib.pyplot as plt
import pickle

TONE_NAMES = ["Analytical", "Anger", "Confident", "Fear", "Joy", "Sadness", "Tentative"]
Y_LIM_LOWER = 0.5
cnn = pickle.load(open("cnn.p", "rb"))
hp = pickle.load(open("hp.p", "rb"))
fox = pickle.load(open("fox.p", "rb"))
bb = pickle.load(open("bb.p", "rb"))

cnn_dates = cnn.keys()
hp_dates = hp.keys()
fox_dates = fox.keys()
bb_dates = bb.keys()

all_dates = ['10-25-20', '10-26-20', '10-27-20', '10-28-20', '10-29-20', '10-30-20', '10-31-20',
             '11-01-20', '11-02-20', '11-03-20', '11-04-20', '11-05-20', '11-06-20', '11-07-20',
             '11-08-20', '11-09-20', '11-10-20', '11-11-20', '11-12-20', '11-13-20', '11-14-20',
             '11-15-20', '11-16-20', '11-17-20', '11-18-20', '11-19-20', '11-20-20', '11-21-20']

cnn_tones = dict()
for date in cnn_dates:
    tone_scores = cnn[date]
    for tone in TONE_NAMES:
        sList = cnn_tones.get(tone)
        if sList:
            sList.append(tone_scores.get(tone, Y_LIM_LOWER))
        else:
            cnn_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]

hp_tones = dict()
for date in hp_dates:
    tone_scores = hp[date]
    for tone in TONE_NAMES:
        sList = hp_tones.get(tone)
        if sList:
            sList.append(tone_scores.get(tone, Y_LIM_LOWER))
        else:
            hp_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]

fox_tones = dict()
for date in fox_dates:
    tone_scores = fox[date]
    for tone in TONE_NAMES:
        sList = fox_tones.get(tone)
        if sList:
            sList.append(tone_scores.get(tone, Y_LIM_LOWER))
        else:
            fox_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]

bb_tones = dict()
for date in bb_dates:
    tone_scores = bb[date]
    for tone in TONE_NAMES:
        sList = bb_tones.get(tone)
        if sList:
            sList.append(tone_scores.get(tone, Y_LIM_LOWER))
        else:
            bb_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]

all_cnn_tones = dict()
for date in all_dates:
    for tone in TONE_NAMES:
        sList = all_cnn_tones.get(tone)
        if date in cnn:
            tone_scores = cnn[date]
            if sList:
                sList.append(tone_scores.get(tone, Y_LIM_LOWER))
            else:
                all_cnn_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]
        else:
            if sList:
                sList.append(Y_LIM_LOWER)
            else:
                all_cnn_tones[tone] = [Y_LIM_LOWER]

all_hp_tones = dict()
for date in all_dates:
    for tone in TONE_NAMES:
        sList = all_hp_tones.get(tone)
        if date in hp:
            tone_scores = hp[date]
            if sList:
                sList.append(tone_scores.get(tone, Y_LIM_LOWER))
            else:
                all_hp_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]
        else:
            if sList:
                sList.append(Y_LIM_LOWER)
            else:
                all_hp_tones[tone] = [Y_LIM_LOWER]

all_fox_tones = dict()
for date in all_dates:
    for tone in TONE_NAMES:
        sList = all_fox_tones.get(tone)
        if date in fox:
            tone_scores = fox[date]
            if sList:
                sList.append(tone_scores.get(tone, Y_LIM_LOWER))
            else:
                all_fox_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]
        else:
            if sList:
                sList.append(Y_LIM_LOWER)
            else:
                all_fox_tones[tone] = [Y_LIM_LOWER]

all_bb_tones = dict()
for date in all_dates:
    for tone in TONE_NAMES:
        sList = all_bb_tones.get(tone)
        if date in bb:
            tone_scores = bb[date]
            if sList:
                sList.append(tone_scores.get(tone, Y_LIM_LOWER))
            else:
                all_bb_tones[tone] = [tone_scores.get(tone, Y_LIM_LOWER)]
        else:
            if sList:
                sList.append(Y_LIM_LOWER)
            else:
                all_bb_tones[tone] = [Y_LIM_LOWER]

plt.figure(figsize=(9, 5))
for tone in TONE_NAMES:
    plt.plot(cnn_dates, cnn_tones[tone], label=tone)
plt.ylim(Y_LIM_LOWER, 1)
plt.xticks(rotation=30)
plt.ylabel("Score")
plt.suptitle("CNN")
plt.legend()
plt.savefig("graph_cnn.png")
plt.show()
plt.close()

plt.figure(figsize=(9, 5))
for tone in TONE_NAMES:
    plt.plot(hp_dates, hp_tones[tone], label=tone)
plt.ylim(Y_LIM_LOWER, 1)
plt.xticks(rotation=30)
plt.ylabel("Score")
plt.suptitle("Huffington Post")
plt.legend()
plt.savefig("graph_hp.png")
plt.show()
plt.close()

plt.figure(figsize=(9, 5))
for tone in TONE_NAMES:
    plt.plot(fox_dates, fox_tones[tone], label=tone)
plt.ylim(Y_LIM_LOWER, 1)
plt.xticks(rotation=30)
plt.ylabel("Score")
plt.suptitle("FOX")
plt.legend()
plt.savefig("graph_fox.png")
plt.show()
plt.close()

plt.figure(figsize=(9, 5))
for tone in TONE_NAMES:
    plt.plot(bb_dates, bb_tones[tone], label=tone)
plt.ylim(Y_LIM_LOWER, 1)
plt.xticks(rotation=30)
plt.ylabel("Score")
plt.suptitle("Breitbart")
plt.legend()
plt.savefig("graph_bb.png")
plt.show()
plt.close()

for tone in TONE_NAMES:
    plt.figure(figsize=(9, 5))
    plt.plot(all_dates, all_cnn_tones[tone], label="CNN")
    plt.plot(all_dates, all_hp_tones[tone], label="HuffPost")
    plt.plot(all_dates, all_fox_tones[tone], label="FOX")
    plt.plot(all_dates, all_bb_tones[tone], label="Breitbart")
    plt.ylim(Y_LIM_LOWER, 1)
    plt.xticks(rotation=30)
    plt.ylabel("Score")
    plt.suptitle(tone)
    plt.legend()
    plt.savefig(tone + ".png")
    plt.show()
    plt.close()
