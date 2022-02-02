{% include navbar_open.html %}
# Sok-1006 Mikroøkonomi   

## Seminar 5 - Produksjon III: Produsentens tilpasning på kort og lang sikt   

   

### Oppgave 1   

Økonom Y har samlet inn data fra produksjon i bedriften Dereks Dingser, og har estimert følgende likning:


\begin{equation}
    ln x = ln e+\frac{1}{2} ln N + \frac{1}{3} ln K
\end{equation}

hvor $e$ er Eulers tall.   
a) Hva kan du si om skalsegenskapene til produksjonen i denne bedriften?   
b) Bruk likning (1) til å skrive en Cobb-Douglas produktfunksjon for Dereks Dingser.   
c) På kort sikt har bedriften tilgang til begrenset kapital $K\_0$. Prisen per enhet kapital er fast $r$, mens én time med arbeidskraft koster $w$. Dingser selges for en fast pris på $p$ kr per enhet.
På kort sikt kan Derek velge hvor mange timer arbiedskraft som tilsettes for å maksimere overskuddet til bedriften. 
Skriv ut fortjenesten til bedriften, og finn ut hvor mye arbeidskraft det er som maksimerer overskuddet: $N^{\*}(p,w,r K\_0)$. 
Daglig leder Derek er noe skeptisk til om dette er et maksimum. Kan du overbevise han?    
d) Hvordan endres bedriftens etterspørselen etter arbeidskraft når de eksogene variablene $N^{\*}(p,w,r K\_0)$endres? Forklar intuisjonen bak dine funn.   
e) Finn bedriftfens kostnadsfunksjon på kort sikt, og vis Derek hvor mye dingser han bør tilby til markedet til enhver pris (dvs tegn tilbudsfunksjonen på kort sikt).   
f) 
b) I en ny figur tegn totale gjennomsnittskostnader på kort sikt, variabler gjennomsnittskostnader på kort sikt, og grensekostnaden på kort sikt. Kommenter og forklar forholdet mellom  total og variabel gjennomsnittskostnad og grensekostnaden.   
c) På lang sikt kan Derek leie inn arbeidskraft og kapital slik at produksjonskostnaden blir minimert for hvert produksjonsnivå. Tegn produksjonsisokvanter i en figur som viser hvordan han kan kombinere produksjonsfaktorene for å produsere $x=10, x=30, x=50$ dingser. Vis at den optimale kombinasjonen av arbeidskraft og kapital som minimerer produksjonskostnaden for alle produsksjonsnivå (dvs substitumalen) er gitt ved $K=\frac{350}{500}N=\frac{w}{r}N$. Tegn substitumalen inn i figuren. Hvorfor er den optimale kombinasjonen kun avhengig av den relative prisen på produksjonsfaktorene, og ikke parametre fra produktfunksjonen (dvs produksjonselastisitetene)? Tegn inn isokostnadskurver og vis dermed at skjæringspunktet mellom isokvanten og substitumalen er det kostnadsminimerende valget.   
d) Gitt svaret ditt fra c) beregn den totale produksjonskostnaden på lang sikt (dvs summen av faktorkostnadene og den faste kostnaden). Kommenter resultatet.   
e) Beregn den totale gjennomsnittskostnaden på langt sikt og tegn dette i en figur med produsert mengde (x) på den horisontale aksen. Tegn også inn den totale gjennomsnittskostnad på kort sikt for kapitalmenger $K=10, K=25, K=50$ Forklar forholdet mellom gjennomsnittskostnaden på kort og lang sikt.   




### Oppgave 2   

En bedrift kan produsere et gode (x) ved å kombinere arbeidskraft (N) og kapital (K) som følger


\begin{equation}
   x = f(N,K)=ZN^aK^{b}
\end{equation}

hvor a, b og Z er positive tall.   
a) Gitt faktorpriser w på arbeidskraft og r på kapital beregn det optimale forholdet mellom produksjonsfaktorene for en kostnadsminimerende bedrift. Under hvilke omstendigheter bruker bedriften mer kapital enn arbeidskraft? Forklar intuisjonen bak dette resultatet.    
b) Vis at (1) kan skrives som 


\begin{equation}
  ln x = ln Z+a ln N + b ln K
\end{equation}


I  <a href="https://github.com/uit-sok-1006-v22/uit-sok-1006-v22.github.io/blob/main/seminarer/Sem_4_oppgave_2_studenter%20(1).ipynb" target="_self"> denne Jupyter Notebook</a> kan du generere dataobservasjoner på mengde produsert, og mendge arbeidskraft og kapital brukt i prossessen. I denne oppgaven skal du fullføre trinn i notebooken for å estimere Z, a og b for denne produktfunksjon. Kommenter skalautbytteegenskapene til denne produktfunksjonen. Tegn noen produksjonsisokvanter, og vis hvordan skalautbytte påvirker forholdet mellom dem.          
c) Det viser seg at kostnadsfunksjonen for en generell Cobb-Douglas produktfunksjon kan skrives som 


\begin{equation}
   C(w,r,x,Z) = \left ( \frac{x}{Z}) \right )^{\frac{1}{a+b}}w^{\frac{a}{a+b}}r^{\frac{b}{a+b}}\left ( \left ( \frac{a}{b} \right )^{\frac{b}{a+b}}+\left ( \frac{b}{a} \right)^{\frac{a}{a+b}} \right )
\end{equation}

Du behøver ikke vise at dette stemmer (men kan om du klarer!). Gitt at $w=350$ og $r=500$, sett inn verdiene som du fant i del (b) og tegn (i) total kostnaden, (ii) gjennomsnittskostnaden, og (iii) grensekostnaden på lang sikt. Hvilke skalautbytte viser produktfunksjonen som du har estimert?   


### Oppgave 3   

Etter å ha samlet inn data over mange år har en bedrift funnet ut at den har følgende totalkostnadsfunksjon:


\begin{equation}
   C(w,r,x)=2(w r x)^{\frac{1}{2}}
\end{equation}

Bedriftseieren vil vite hvordan hun kan bruke denne informasjonen til å avdekke bedriftens produktfunksjon $x=f(N,K)$.    
a) Shephards Lemma er en setning i mikroøkonomi som vi kan gjøre bruk av her. Tenk deg at bedriften bruker 10 enheter N og 5 enheter K, med faktorpriser w=1 og r=3. Da blir totalkostnaden (1)(10)+(3)(5)=25. Anta nå at prisen på arbeidskraft øker med én enhet slik at den nye kostnaden blir (2)(10)+(3)(5)=35. Kostnadsøkningen er på 10 som er mengden arbeidskraft som er brukt. Likeså om r øker med 1 øker kostnaden med 5 som er mengde kapital brukt. Dette er ikke et matematisk bevis, men vi kan da konstatere Shephards Lemma som sier


\begin{equation}
   L = \frac{\partial C}{\partial w}
\end{equation}

\begin{equation}
   K = \frac{\partial C}{\partial r}
\end{equation}

Beregn (6) og (7) for kostnadsfunksjonen i (5) for å finne forholdet mellom faktorbruk, faktorpriser og produsert mengde: $L(w, r, x), K(w, r, x)$.   
b) Fra $L(w, r, x)$ finn et uttrykk for $\frac{w}{r}$, og sett dette inn i $K(w, r, x)$.   
c) Nå skal du ha en likning som knytter sammen x, N, og K. Løs denne likningen for x, og fortell bedriftseieren hvilken produktfunksjon hun bruker! Sjekk at du har rett ved å verifisere at ditt resultat gir samme kostnad som i (5).     
d) Hvilke skalaegenskaper har denne produktfunksjon?   




### Oppgave 4   

[Denne fila](/seminarer/tesladata.csv) inneholder årlig data fra Tesla på kapitalutgifter (USD), arbeidere, og antall biler laget i perioden 2012-2020.    
a) Plott disse seriene i en figur med tid på den horisontale aksen.   
b) Anta at produktfunksjonen for Tesla er


\begin{equation}
   x = f(N,K)=ZN^aK^{b}
\end{equation}

I <a href="https://github.com/uit-sok-1006-v22/uit-sok-1006-v22.github.io/blob/main/seminarer/seminar_4_tesla_for_studenter.ipynb" target="_self"> denne Jupyter Notebook</a> får du kode til å estimere følgende likning


\begin{equation}
  ln (x/N) = ln Z + (a+b-1)ln N + b ln (K/N)
\end{equation}

Hva viser din analyse om skalautbytte til Tesla?    
c) Er du fornøyd med resultatene fra analysen, eller er det noe som ikke ser helt riktig ut?    
d) Er ditt resultat forenelig med [denne analysen](https://cleantechnica.com/2018/07/22/peeking-behind-teslas-cost-of-materials-curtain/){:target="blank"} av Tesla sine kostnader?   
e) Gitt denne analysen hvilke andre variabler bør inkluderes i (8), og hvordan vil den nye produktfunksjonen se ut (gitt at den er Cobb-Douglas)? 




