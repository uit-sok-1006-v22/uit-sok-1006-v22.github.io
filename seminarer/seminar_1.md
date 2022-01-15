{% include navbar_open.html %}
# Sok-1006 Mikroøkonomi   

## Seminar 1 - Tilbud og etterspørsel   

Det kan være lurt å løse oppgave 1 og 2 ved hjelp av Python.   

### Oppgave 1   

a) Hva viser markedets etterspørsel, og hvilke faktorer og variabler påvirker den?   
b) En lineær etterspørselsfunksjon skrives som 

\begin{equation}
   x^{D}=a-bp
\end{equation}


hvor _p_ er prisen på varen, _x_ er kvantum, og _a_ og _b_ er positive parametre.
Tegn denne funksjonen i en figur, og vis hvordan den påvirkes av de endringene du diskuterte under a). Hva fanger opp parametrene _a_ og _b_?   
c)  Hva viser markedets tilbud, og hvilke faktorer og variabler påvirker den?   
d) En lineær tilbudsfunksjon skrives som 

\begin{equation}
   x^{S}=-\alpha+\beta p
\end{equation}

hvor $\alpha>0, \beta>0$.
Tegn denne funksjonen i en figur, og vis hvordan den påvirkes av de endringene du diskuterte under c). Hva fanger opp parametrene $\alpha, \beta$?   
e) Hva karakteriserer en markedslikevekt? Bruk (1) og (2) og finn likevekten.  
f) Regn ut og vis i fire figurer hvordan endringer i i) _a_, ii) _b_, iii) $\alpha$ og iv) $\beta$ påvirker tilbud, etterspørsel, likevektsprisen og -kvantumet. Forklar intuisjonen bak dine resultater.      


### Oppgave 2   

a) Tenk deg nå at markedets etterspørsel er gitt ved 

\begin{equation}
   x^{D}= kp^{-r}
\end{equation}

hvor _k_ og _r_ er positive parametre. Anta at $ k=1 $ og $ r=0,5$
Tegn dette i en figur sammen med tilbudsfunksjonen 

\begin{equation}
   x^{S}=mp^s
\end{equation}

hvor _m_ og _s_ er positive tall: $m=1$, $s=0,5$.   
b) Regn ut markedslikevekten (i) for de gitte tallene, og (ii) for alle parameterverdier. Vis hvordan tilbuds- og etterspørselsfunksjonene og likevekten påvirkes når modellens parametre endres. Forklar dine resultater.   

### Oppgave 3   
a) Hva viser etterspørselens og tilbudets priselastisitet? Gi en intuitiv forklaring på formelen som brukes for å regne disse ut.   
b) Regn ut etterspørselselastisitetene for (1) og (3).
Tegn figurer for hvert tilfelle som viser hvordan elastisitetene endrer seg når pris øker. Hva skjer med elastistitetene i hvert tilfellet når vi beveger oss langs etterspørselskurven?    
c) Gjør det samme som i b) for tilbudsfunksjonene.   
d) Bedriftens inntekt er gitt ved pris ganget med etterspurt kvantum (som er en funksjon på pris):

\begin{equation}
   R=px^{D}(p)
\end{equation}

Finn betingelser knyttet til etterspørselens priselastisitet som sikrer at en prisøkning fører til at bedriftens inntekt øker. (Dvs når er $\frac{dR}{dp}\>0 $?).   

### Oppgave 4

Betrakt etterspørselsfunksjonen gitt ved (3). Ved å ta naturlige logaritmer (ln) av begge sidene, vis at etterspørselsen kan skrives som:

\begin{equation}
   ln x^{D}=ln k - r ln p
\end{equation}

a) I 1955 estimerte Daniel Suits en modell av vannmelonmarkedet i USA, og kom frem til følgende etterspørselsfunksjon (som er noe forenklet)

\begin{equation}
   ln x^{D}=1.4 ln y - 0.9 ln p
\end{equation}

hvor $x^D$ er etterspørsel per person $y$ er konsumentens inntekt, og $p$ er prisen på vannmeloner. Hvor mye endres etterspørselen når (i) $p$ øker, (ii) $y$ øker?   



### Oppgave 5   

[Cooper (2003)](/seminarer/Cooper.2003.OPECReview.PriceElasticityofDemandforCrudeOil.pdf){:target="blank"} estimerer etterspørselen etter olje i 23 land i perioden 1971-2000. Han legger til grunn følgende likning:

\begin{equation}
   ln D_t=ln\alpha +\beta ln P_t +\gamma ln Y_t +\delta ln D_{t-1} + \epsilon_t
\end{equation}

hvor
- $D_t$ er konsum av olje per innbygger i år t
- $P_t$ er prisen på olje i år t
- $Y_t$ er BNP per innbygger i år t
- $\epsilon$  er et tilfeldig feilledd.

Her er $\beta$ etterspørselsens priselastisitet på kort sikt, mens priselastisiteten på lang sikt er gitt ved $\frac {\beta}{1-\delta}$. Med "lang sikt" menes her $D_t=D_{t-1}$.   
a) Er estimatene av etterspørselens priselastisitet på kort og lang sikt i tråd med økonomisk teori (c.f oppgave 4e)?    
b) På 1970-tallet produserte OPEC landene ca 65% av verdens olje. Hvorfor gjorde denne organisasjon mange forsøk på å redusere tilbudet av olje?   
c) Er det grunn til å tro at silke produksjonsorganisasjoner har en vanskeligere jobb i dag dersom de skal prøve å påvirke oljeprisen? (Se for eksempel [denne artikkelen](https://www.dn.no/olje/oljemarkedet/opec/olje-og-gass/oljeprisen-falt-etter-opec-enighet-om-a-ga-videre-med-produksjonsokning-men-henter-seg-inn-igjen/2-1-1111584){:target="blank"}).


