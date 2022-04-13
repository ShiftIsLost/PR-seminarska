# RAZLIKE MED SPOLOMA NA AKADEMSKEM PODROČJU V SLOVENIJI
Skupina: PR21MMKJP

Seminarska naloga raziskuje razlike v izobrazbi in brezposelnosti, ter prisotnost spolov na določenih akademskih področjih.

## Podatki
Večino podatkov smo pridobili iz statističnega urada(https://pxweb.stat.si/SiStat/sl). To so podatki o brezposelnosti, zaposlitvenem statusu, delovno aktivnem prebivalstvu, izobrazbi po občinah in vrsti izobrazbe. Problem s podatki iz statističnega urada je, da niso pravilno urejeni. Največji problem predstavlja časovno porazdelitev, ki je v stolpcih pomešana z nekim odcekom meritve(npr. starost 15-24 in leto 2010). To bo potrebno rešiti na nek eleganten način, ki bi bile lahko več dimenzionalne tabele. 
Preostale podatke o objavljenih diplomah smo pridobili iz nacionalnega portala odprte znanosti(https://www.openscience.si/OpenData.aspx). Kjer smo dobili podatke o akademskih člankih, doktoratih, magisterijih in podobno. Problem pri teh podatkih je da nimamo podanega spola avtorja in področja dela. Ugibanje spola se lahko lotimo tako da ga probamo ugotiviti iz imena. Za področje se pa lahko lotimo na več načinov. Eden je da pogledamo ustanovo na kateri je bilo delo objavljeno, ampak pri tem nastane težava z natančnostjo. Drug pa da delu dodelimo temo glede na njegove ključne besede.

## Postopek obdelave podatkov
Vprašanje 1. Razlike glede na izobraženost po občinah. Katera občina je najbolj izobražena(največ maturantov diplom itd.)? Kaj se zgodi če to normaliziramo glede na prebivalstvo v občini(x maturantov na y prebivalcev)? Obrazloži ugotovitve(npr. ali so občine z manj izobraženim prebivalstvom bolj kmetijsko usmerjene). Primerjaj najbolj in najmanj izobraženo občino skozi čas(rolling avg).
Vprašanje 2. Kakšna je razlika v akademskih dosežkih med spoloma? Ali je kateri od spolov v zaostanku(vizualiziraj)? Kakšna je razlika med spoloma na posamezni stopnji izobrazbe? (še prikaz po regijah/čas)
Vprašanje 3. Ureditev meta podatkov o strokovnih delih. Ugibanje spola in področje dela. Primerjava spola pa posameznih področjih del.

### Razlike izobraženosti po občinah
Vprašanja katera občina je najbolj izobražena sem se lotil tako, da sem pridobil podatke o izobrazbi delovno aktivnega prebivalstva Slovenskih občin med letoma 2005 in 2021.
Na podlagi teh podatkov sem ustvaril grafe, ki so mi pokazali kakšni so deleži delovno aktivnega prebivalstva z visokošolsko, srednješolsko oziroma osnovnošolsko izobrazbo v vseh Slovenskih občinah.
Iz grafov je razvidno, da je občina z največjim deležem visokošolskega prebivalstva dolga leta bil Trzin, v zadnjih letih pa je to Kranjska Gora. Blizu je tudi Ljubljana. 
Med letoma 2005 in 2012 je bila občina z najmanjšim deležem prebivalstva z visokošolsko izobrazbo Hodoš. V letu 2021 je na predzadnjem mestu, Zavrč pa je zadnji.
Občina z največjim deležem prebivalstva s srednješolsko izobrazbo je bila med letoma 2005 in 2015 ter v letu 2020 in 2021 Osilnica, med letoma 2016 in 2019 pa je to Zavrč.
Po najaktualnejših podatkih je Ljubljana občina z najmanjšim deležem prebivalstva s srednješolsko izobrazbo. 
Občina z največjim deležem prebivalstva z osnovnošolsko izobrazbo je bil vsa leta (2005 - 2021) Hodoš, občina z najmanjšim deležem takšnega prebivalstva pa je trenutno Kranjska Gora.
Iz podatkov sem ustvaril tudi grafe, ki prikazujejo trend deleža prebivalstva z določeno izobrazbo v petih izbranih Slovenskih mestih (Ljubljana, Maribor, Koper, Celje, Bled). 
Iz dobljenih grafov je razvidno, da delež prebivalstva z osnovnošolsko prebivalstvo v teh mestih pada, delež z visokošolsko izobrazbo pa raste. 
Delež prebivalstva z srednješolsko izobrazbo je v Kopru ter Celju ostal dokaj konstanten, v Bledu, Ljubljani in Maribor pa je upadel.
