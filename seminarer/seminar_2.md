{% include navbar_open.html %}

## Seminar 2 - Tilbud og etterspørsel - økonomisk politikk   

Det er lurt å bruke egnet verktøy for å løse disse oppgavene.   

### Oppgave 1   

Gjør oppgavene fra [Core Project 7](https://www.core-econ.org/doing-economics/book/text/07-01.html#introduction){:target="blank"}. Her møter du igjen Suit sin modell for tilbud av og etterspørsel etter vannmeloner. Se foreløpig bort fra oppgave 3c i delkap 7.1 (overskuddsbetraktninger kommer vi tilbake til i kap 9). Her lærer du noe mer om hvordan man fremstiller tilbud og etterspørsel basert på faktisk data, tolkning av empiriske resultater, og hvordan man modellerer skift i kurvene.       

R-koden et gitt i gjennomgangen av oppgaven. Klarer du det samme med Python?

### Oppgave 2   

Her skal vi se på virkningen av å ilegge en vare en avgift. Betrakt fremstillingen av markedet for oppdrettslaks i læreboka s. 101-104. Etterspørsel er gitt ved


\begin{equation}
   x^{D}= 500 -3.2p
\end{equation}

og tilbud:


\begin{equation}
   x^{S}= -100 + 4.3p
\end{equation}

I boka ser forfatterne på en avgift på 4kr per enhet som produsenten må betale. Les denne analysen nøye.  
a) Hvordan endres analysen dersom avgiften legges på kjøpere? Forklar intuisjonen bak ditt svar.   
b) Tenk deg nå at avgiften er på $\tau$kr per enhet ilagt produsenter uten at dette tallfestes. Beregn likevektsverdier på prisen som konsumenten betaler, produsentpris, samt kvantum omsatt. Likevektsprisen før avgiften ble innført er 80kr; betaler kjøpere eller selgere mesteparten av avgiften? Forklar intuisjonen bak ditt svar. (Se ellers oppgave 3 for mer om dette).    
c) Skatteproveny blir beregnet som avgiftssats ganget med omsatt kvantum. Finn et uttrykk for dette, og tegn en figur med proveny på y-aksen og avgiftssatsen på x-aksen.   
d) Hva er en fornuftig avgrensning for avgiftssatsen? Beregn avgiftssatsen som maksimerer provenyet.


### Oppgave 3   

I Oppgave 2 så vi at selv om avgiften er pålagt selgere, veltes en del av dette over på kjøpere. I denne oppgaven skal vi undersøke hvor mye av avgiften som må betales av selgere og kjøpere. La etterspørsel og tilbud være gitt ved


\begin{equation}
   x^{D}= a -bp
\end{equation}



\begin{equation}
   x^{S}= -\alpha + \betap
\end{equation}

hvor alle parametre er positive tall.   
a) La $a=504, b=2, \alpha=100, \beta=4.3$. Hvor mye av en produsentavgift på $\tau=4$ må betales av kjøpere og selgere nå? Tegn en figur som viser denne likevekten, og sammenlikn svaret med eksempelet i Fig 3.22 i læreboka (tegn gjerne begge eksemplene i samme figur). Hvilke konklusjoner trekker du foreløpig om hva det er som kan påvirke fordelingen av avgiften mellom de to sidene av markedet? Hva er intuisjonen bak resultatet?
b) En avgift på $\tau$kr per enhet solgt pålegges selgerne i dette markedet. Regn ut likevektsprien for kjøpere, selgere og kvantum omsatt som en funksjon av $\tau$. Sjekk at løsningen for $\tau =0$ er det samme som du fant i seminar 1, oppgave 1e).   
c) La oss kalle likevektsprisen til konsumenten $p^{\*D}(\tau)$, og til produsenten $p^{\*S}(\tau)=p^{\*D}(\tau)-\tau$. Gitt en avgift på $\tau$kr per enhet, må kjøpere betale andel

\begin{equation}
   A^{KONS}=\frac{p^{\*D}(\tau)-p^{\*D}(0)}{\tau}
\end{equation}

mens selgere må betale en andel $A^{SELG}=1-A^{KONS}$. Forklar dette (tegn gjerne en figur for å hjelpe til med forklaringen). Regn ut $A^{KONS}, A^{SELG}$. Hvordan avhenger disse størrelsene av modellens parametre ($a,b,\alpha,\beta$)?   
d) Bruk din analyse for å forklare følgende setning fra læreboka (s. 103): "Teorien forteller oss at det er elastisiteten eller prisfølsomheten til etterspørselen og tilbudet som er avgjørende for hvor stpr andel av avgiften konsumentene og produsentene må betale".



### Oppgave 4   

Kommer - om maks og min priser







