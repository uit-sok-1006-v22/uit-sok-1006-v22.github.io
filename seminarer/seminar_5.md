{% include navbar_open.html %}
# Sok-1006 Mikroøkonomi   

## Seminar 5 - Produksjon III: Produsentens tilpasning på kort og lang sikt   

   

### Oppgave 1   

Økonom Y har samlet inn data fra produksjon i bedriften Dereks Dingser, og har estimert følgende likning:


\begin{equation}
    ln x = ln Z \frac{1}{2} ln N + \frac{1}{3} ln K
\end{equation}

   
a) Hva kan du si om skalaegenskapene til produksjonen i denne bedriften?   
b) Bruk likning (1) til å skrive en Cobb-Douglas produktfunksjon for Dereks Dingser.   
c) På kort sikt har bedriften tilgang til begrenset kapital $K\_0$. Prisen per enhet kapital er fast $r$, mens én time med arbeidskraft koster $w$; bedriften har ingen faste kostnader. Dingser selges for en fast pris på $p$ kr per enhet.
På kort sikt kan Derek velge hvor mange timer arbeidskraft som tilsettes for å maksimere overskuddet til bedriften. 
Skriv ut fortjenesten til bedriften, og finn ut hvor mye arbeidskraft det er som maksimerer overskuddet: $N^{\*}(p,w,r, K\_0)$. 
Daglig leder Derek er noe skeptisk til om dette er et maksimum. Kan du overbevise ham?    
d) Hvordan endres bedriftens etterspørselen etter arbeidskraft når de eksogene variablene $Np,w,r K\_0$ endres? Forklar intuisjonen bak dine funn.   
e) Finn bedriftfens kostnadsfunksjon på kort sikt, og vis Derek hvor mye dingser han bør tilby til markedet til enhver pris (dvs tegn tilbudsfunksjonen på kort sikt).   
f) På en strategisamling kommer et innspill om at bedriften burde planlegge for fremtiden, og ikke bare se på kortsiktige løsninger. Styret gir deg oppdraget: "På lang sikt bør bedriften Dereks Dingser ansette arbeidskraft og kapital i optimale mengder for å maksimere bedriftens overskudd. Identifisér optimale mengder av disse produksjonsfaktorer på lang sikt".        
g) Styret går videre i sitt oppdrag, og vil ha deg til å beregne bedriftens tilbudsfunksjon på lang sikt. De ber deg i tillegg utføre ulike scenarioanalyser: Hva skjer med tilbudskurven for dingser dersom: (i) $p$ faller med 25%, (ii) $w$ øker med 10%, (iii) $r$ øker med 10%. Forklar intuisjonen bak dine funn for de styremedlemmene som ikke har en økonomifaglig bakgrunn.   




### Oppgave 2   

Daglig leder Derek jobber i en bedrift som lager dingser. Etter mange år har han samlet inn [dette datasettet](https://github.com/uit-sok-1006-v22/uit-sok-1006-v22.github.io/blob/main/seminarer/data_sem_5.csv) som inneholder tall på produksjon, kapitalbruk og anvendelse av arbeidskraft i en bedrift. De er allerede gjort om til logaritmer (variablene 'lnx', 'lnK', 'lnN'), men Derek kommer ikke videre i sin analyse av bedriftens optimale produksjon på kort og lang sikt. Han hyrer deg inn som konsulent, og ber deg estimere følgende produktfunksjon:

\begin{equation}
  ln x = ln Z+a ln N + b ln K
\end{equation}

(noe av koden fra seminar 4 kan være nyttig her).  
Bruk dine estimatene på $a$ og $b$ og $lnZ$ i den følgende analysen (bruk 1 desimalplass).   
a) Hvordan ser bedriftens Cobb-Douglas produktfunksjon ut? Hvilke skalaegenskaper har den?   
b) Bedriftens mål er å maksimere overskudd. Sett opp bedriftens maksimeringsproblem. På kort sikt kan ikke bedriften endre bruken av kapital, slik at kapitalmengden er fast: $K=K\_0$. Gitt lønn $w$ og kapitalpris $r$ må Derek informere bedriftens styre hvor mye arbeidskraft som bør ansettes på kort sikt. Styremedlemmene i bedriften vil helst ha en figur, og ikke et matematisk uttrykk som viser forholdet mellom lønn og optimal arbeidsinnsats; tegn en figur med $N$ på den vertikale aksen og $w$ på den horisontale.    
c) Derek oppsøker styrerommet, fornøyd med løsningen som "han" har funnet. Styreleder C. Kent ser på figuren, og stiller et noe ekkelt spørsmål: "Er du fornøyd med hvordan denne etterspørselsfunksjonen ser ut, Derek?". Slukøret må Derek innrømme at han ikke er helt fornøyd (men han vet ikke hvorfor). Hva kan ha gått galt her? For å undersøke dette kan du (i) prøve å tegne profittfunksjonen (sett for eksempel $p=10, w=1, K\_0=1$) , og (ii) sjekke om den 2. ordens betingelsen for et maksimum er oppfylt. Etter det må du forklare for Derek hva som er problemet, så enkelt som mulig og uten faguttrykk.   
d) Styret har vedtatt en produksjonsplan for de neste 6 måneder, og ber Derek lage en strategi for å oppfylle denne. Gitt det han har opplevd til nå skjønner han ikke hvordan han skal klare dette, og søker råd hos deg. Forlar for daglig leder at det er mulig å lage en optimal strategi på tross av det tidligere svaret.   
e) Daglig leder Derek tenker at han vil klare å maksimere bedriftens overskudd i det lange løp, bare han også får tllpasset kapitalnivået. "Det går ikke med denne produktfunksjon, dessverre" må du fortelle han. Hvorfor ikke?    


### Oppgave 3   
[Arbeidsgiveravgift](https://www.regjeringen.no/no/tema/kommuner-og-regioner/regional--og-distriktspolitikk/differensiert-arbeidsgiveravgift/id2353986/) må betales av bedrifter til staten basert på lønnsutgifter. Dette er bedriftens bidrag til finansieringen av folketrygden, og satsen som må betales er avhengig av hvor bedriften er lokalisert (differensiert arbeidsgiveravgift). En bedrift som er lokalisert i Tromsø selger et produkt for 1000 kr per enhet, og har følgende produktfunksjon:

\begin{equation}
   x = N^a K^b
\end{equation}

med en total kostnad på arbeidskraft (dvs inkludert arbeidsgiveravgiften) på 380 kr per time, og en kapitalkostnad på 500 kr per enhet. Anta at $a=0,5, b=0,25$. Bedriften har faste driftsavhengige kostnader på $F$ kr.    
a) Hva er bedriftens profittmaksimerende etterspørsel etter arbeidskraft og kapital på lang sikt mens den er lokalisert i Tromsø?    
b) Arbeidsgiveravgiften i Tromsø kommune er på 7,9% i 2022. Bedriften vurderer å flytte produksjon til Alta hvor arbeidsgiveravgiften er 0. Hvordan vil dette endre etterspørselen etter arbeidskraft på lang sikt? Endres etterspørselen etter kapitalen selv om dens pris per enhet er fast? Forklar intuisjonen her.   
c) Hvor mye kan bedriften tjene på å flytte fra Tromsø til Alta? (Se bort fra evt. flyttekostnader, og anta samme fastkostnad i Tromsø som i Alta).    
d) Produktet som bedriften lager omsettes på verdensmarkedet, og man har observert store svingninger i pris den senere tiden. Bedriftens styre vil vite hvor mye som bør produseres til enhver pris på lang sikt når markedet har roet seg. Gjennomfør en analyse av dette for lokaliseringen i Tromsø og Alta, og foklar dine resultater. I beregningen kan du anta $F=200$ i begge kommunene.   


 






