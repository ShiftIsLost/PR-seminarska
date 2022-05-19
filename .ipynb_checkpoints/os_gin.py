import matplotlib.pyplot as plt
import pandas as pd

osnovka = pd.read_csv('../podatki/os_zakljucili_spol_bg.csv', sep=' ', encoding='cp1250')
ucenci = osnovka.loc[osnovka['SPOL'] ==  'Moški']
ucenke = osnovka.loc[osnovka['SPOL'] ==  'Ženske']
ucenci = pd.DataFrame(ucenci)
ucenke = pd.DataFrame(ucenke)
ucenci = ucenci.drop(['SPOL', 'STAROST'], axis=1)
ucenke = ucenke.drop(['SPOL', 'STAROST'], axis=1)
print(ucenci)
print(ucenke)
moski = dict()
zenske = dict()
for col in ucenci.columns:
    moski['m ' + col] = int(ucenci[col].iloc[0])

for col in ucenke.columns:
    zenske['z ' + col] = int(ucenke[col].iloc[0])

print(moski)
print(zenske)

plt.bar(*zip(*moski.items()))
plt.bar(*zip(*zenske.items()))
plt.gcf().autofmt_xdate()
plt.show()