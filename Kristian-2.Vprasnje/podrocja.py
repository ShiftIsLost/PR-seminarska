import pandas as pd
import matplotlib.pyplot as plt

podrocja = pd.read_csv('podatki/podrocje2.csv',sep=',',encoding='cp1250')
#Dijaki po starosti, letnikih, spolu in vrsti izobraževanja, Slovenija, letno
#Link: https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0953221S.px
moski = dict()
zenske = dict()
#Skupaj končno število končane srednje izobrazbe
for col in podrocja.columns:
    if ("Moški" in col):
        moski[col] = int(podrocja[col].iloc[0])
    if ("Ženske" in col):
        zenske[col] = int(podrocja[col].iloc[0])


print(moski)
print(zenske)

plt.bar(*zip(*moski.items()))
plt.bar(*zip(*zenske.items()))
plt.gcf().autofmt_xdate()
plt.show()
