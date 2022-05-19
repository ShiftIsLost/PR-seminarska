import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

osnovka = pd.read_csv('../podatki/os_razredi_spol_vpis_bg.csv', sep=' ', encoding='cp1250')
osnovka = osnovka.loc[osnovka['STAROST'] == 'Starost - SKUPAJ']
osnovka = osnovka.loc[osnovka['VRSTA VPISA'] == 'Vrsta vpisa - SKUPAJ']
osnovka = pd.DataFrame(osnovka)
osnovka = osnovka[osnovka['RAZRED'] != 'Razred - SKUPAJ']

razredi = dict()

for razred in osnovka['RAZRED']:
    if razred not in razredi:
        razredi[razred] = [dict(), dict()]

i = 0
for razred in razredi.keys():
    n_raz = osnovka.loc[osnovka['RAZRED'] == razred]
    n_raz = pd.DataFrame(n_raz)
    tmpm = n_raz.loc[osnovka['SPOL'] == 'Moški']
    tmpm = pd.DataFrame(tmpm)
    tmpz = n_raz.loc[osnovka['SPOL'] == 'Ženske']
    tmpz = pd.DataFrame(tmpz)
    tmpm = tmpm.iloc[: , 4: ]
    tmpz = tmpz.iloc[: , 4: ]
    n_raz = n_raz.iloc[: , 4: ]
    for leto in n_raz.columns:
        razredi[razred][0]['ucenci ' + leto] = int(tmpm[leto]) # moski
        razredi[razred][1]['ucenke ' + leto] = int(tmpz[leto]) # zenske
raz = '2. razred'
moski = razredi[raz][0]
# moski = list(moski.values())
print(moski)
zenske = razredi[raz][1]
zenske = list(zenske.values())

# plt.bar(*zip(*moski.items()))
# plt.bar(*zip(*zenske.items()))
# plt.title(raz)
# plt.gcf().autofmt_xdate()
# plt.show()
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(*zip(*moski.items()))
plt.show()


