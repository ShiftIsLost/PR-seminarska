# IZOBRAZBA V SLOVENIJI
Skupina: PR21MMKJP

Seminarska naloga raziskuje razlike v izobrazbi in brezposelnosti, ter prisotnost spolov na določenih akademskih področjih.

## Podatki
Večino podatkov smo pridobili iz statističnega urada. To so podatki o brezposelnosti, zaposlitvenem statusu, delovno aktivnem prebivalstvu, izobrazbi po občinah in vrsti izobrazbe. Problem s podatki iz statističnega urada je, da niso pravilno urejeni. Največji problem predstavlja časovno porazdelitev, ki je v stolpcih pomešana z nekim odcekom meritve(npr. starost 15-24 in leto 2010). To bo potrebno rešiti na nek eleganten način, ki bi bile lahko več dimenzionalne tabele. 
Preostale podatke o objavljenih diplomah smo pridobili iz nacionalnega portala odprte znanosti. Kjer smo dobili podatke o akademskih člankih, doktoratih, magisterijih in podobno. Problem pri teh podatkih je da nimamo podanega spola avtorja in področja dela. Ugibanje spola se lahko lotimo tako da ga probamo ugotiviti iz imena. Za področje se pa lahko lotimo na več načinov. Eden je da pogledamo ustanovo na kateri je bilo delo objavljeno, ampak pri tem nastane težava z natančnostjo. Drug pa da delu dodelimo temo glede na njegove ključne besede.

## Postopek obdelave podatkov
Vprašanje 1. Razlike glede na izobraženost po občinah. Katera občina je najbolj izobražena(največ maturantov diplom itd.)? Kaj se zgodi če to normaliziramo glede na prebivalstvo v občini(x maturantov na y prebivalcev)? Obrazloži ugotovitve(npr. ali so občine z manj izobraženim prebivalstvom bolj kmetijsko usmerjene). Primerjaj najbolj in najmanj izobraženo občino skozi čas(rolling avg).
Vprašanje 2. Kakšna je razlika v akademskih dosežkih med spoloma? Ali je kateri od spolov v zaostanku(vizualiziraj)? Kakšna je razlika med spoloma na posamezni stopnji izobrazbe? (še prikaz po regijah/čas)
Vprašanje 3. Ureditev meta podatkov o strokovnih delih. Ugibanje spola in področje dela. Primerjava spola pa posameznih področjih del.
