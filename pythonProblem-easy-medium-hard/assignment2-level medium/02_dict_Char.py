dt = {}
inp = "MoumitaGiriRajaSur"
for ch in inp:
    temp = ch.lower()
    # if(temp not in dt):
    #     dt[temp] = 1
    # else:
    #     dt[temp] = dt[temp] + 1
    dt.get(dt[ch], 0) + 1
print(dt)