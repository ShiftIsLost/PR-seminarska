import pandas as pd
import matplotlib.pyplot as plt
dijaki_vrsta_izobrazbe = pd.read_csv('podatki/dijaki-vrsta-izobrazbe.csv',sep=',',encoding='cp1250')
podrocja = pd.read_csv('podatki/vrsta_srednje_izobrazbe.csv',sep=',',encoding='cp1250')
#Dijaki po starosti, letnikih, spolu in vrsti izobraževanja, Slovenija, letno
#Link: https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0953221S.px
moski = dict()
zenske = dict()


for col in dijaki_vrsta_izobrazbe.columns:
    if("Moški" in col):
        moski[col] = int(dijaki_vrsta_izobrazbe[col].iloc[0])
    if ("Ženske" in col):
        zenske[col] = int(dijaki_vrsta_izobrazbe[col].iloc[0])

print(moski)
print(zenske)

plt.bar(*zip(*moski.items()))
plt.bar(*zip(*zenske.items()))
plt.gcf().autofmt_xdate()
plt.show()
