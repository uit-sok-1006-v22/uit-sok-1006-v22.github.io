
# Sok-1006 Mikroøkonomi

## Mappeoppgave 2    

Denne mappeoppgaven består av ett case. Det er lov å samarbeide i grupper på inntil 3 studenter.    

Tilbakemelding underveis: de som ønsker tilbakemelding kan levere et utkast i Canvas innen 13. mai kl 16.00. Tilbakemelding gis i løpet av uke 20.    

Besvarelsen på mappeoppgaven leveres i Wiseflow innen 30. mai 2022 kl. 13.00.

### Case: Kraftmarkedet i Norge 

Dere skal se på kraftmarkedet i Norge. Noen nyttige kilder som dere kan velge å bruke er     
- [Energifakta Norge](https://energifaktanorge.no/){:target="_blank"}
- [Norges vassdrags- og energidirektorat (NVE)](https://www.nve.no/){:target="_blank"}
- [Statnett](https://www.statnett.no/){:target="_blank"}
- [Slik virker kraftmarkedet](https://energiogklima.no/to-grader/ekspertintervju/ekspertintervjuet-slik-virker-kraftmarkedet/){:target="_blank"}
- [Nord Pool](https://www.nordpoolgroup.com/){:target="_blank"}        

#### A. Bakgrunn       

Du skal lage et notat med tre kapitler som omhandler ulike problemstillinger knyttet til kraftmarkedet i Norge. Notatet er tenkt brukt i undervisningen på et kurs i samfunnsøkonomi for kull 2022 til høsten. Kapittel 1 gir en oversikt over markedet, kapittel 2 presenterer en debatt om effekten av en reduksjon i forbrukeravgiften på strøm, og kapittel 3 gir en økonomisk analyse av ulike støttetiltak for konsumenter på grunn av de høye strømprisene i 2021 og 2022. Analysen vil bestå av tekst, figurer, teknisk analyse og kode som kan forstås av nye studenter; gi intuitive forklaringer på dine resultater.
   

#### B. Oppgave     
##### Kapittel 1 - Slik virker kraftmarkedet      

ca 1000-1500 ord      

###### 1.1 Beskrivelse av det norske kraftmarkedet
Her skal du kartlegge strukturen i kraftmarkedet. Noen momenter som du kan tenke på er for eksempel: hvem er aktørene som produserer og formidler kraft, hvordan settes prisen, hvilke kraftkilder brukes i Norge (og utlandet), inndeling i kraftområder, eksport/import av kraft, avgifter knyttet til kraftproduksjon og forbruk.   

###### 1.2 Etterspørsel etter strøm i Norge
I dette avsnittet skal du se på etterspørsel etter strøm i Norge. Nedenfor finner du noen spørsmål som skal brukes som grunnlag for dette avsnittet. Husk at du skriver et notat, slik at svarene på spørsmålene inngår i en utfyllende tekst.     

[I denne fila](https://uit-sok-1006-v22.github.io/innleveringer/kraft-pris-prod.csv) ligger det data for kraftmarkedet i Norge. Dataene inneholder årlige gjennomsnitt for kraftprisen i Oslo-området (dvs. Østlandet) og Tromsø-området (dvs. Nord-Norge) i EUR/Mwh, og total produksjon av kraft, i tillegg til import og eksport. 

1.2.1 Hent inn dataene, og lag to nye variabler med logaritmen av produksjon og logaritmen av pris i Oslo-området, vis dataene og lag et plott med logartimen av henholdsvis pris i Oslo langs y-aksen og total produksjon langs x-aksen.      

I løpet av 2021 ble to nye kabler til utlandet åpnet. Disse var NorthConnect til Storbritannia og NordLink til Tyskland. Vi skal bruke dataene fra det norske kraftmarkedet til å finne ut omtrent hvilken prisendring vi kan forvente at disse kablene kan ha gitt. Fordi markedet i Europa har endret seg betydelig det siste året, kan vi ikke bare se på prisen før og etter kablene ble åpnet. I stedet estimerer vi en elastisitet, og beregner effekten med den. 

1.2.2 Kjør en regresjon med logaritmen av total produksjon som uavhengig variabel og logaritmen av pris i Oslo som avhengig variabel.     
    1.  Hva er tolkningen av koeffisienten til produksjon her?     
    2.  Hvilken forutsetning er nødvendig for at koeffisienten skal beskrive hvordan konsumentene oppfører seg, og ikke hvordan produsentene oppfører seg? Er det en realistisk forutsetning i dette tilfellet (hint: produsentene kan ikke påvirke hvor mye nedbør det kommer i løpet av ett år eller hvor mye det blåser)     
    3. Legg til en regresjonslinje til plottet du laget i 1.2.1.    
    4. Er koeffisienten du har estimert signifikant eller ikke signifikant?    

1.2.3 Vi kan gjøre noen enkle justeringer for å forbedre påliteligheten til resultatet. Kjør regresjonen på nytt med følgende justeringer:      
    1. prisene i Oslo og Tromsø tilsier at vi kan anse landet som ett marked, bortsett fra for ett bestemt år. Fjern dette året fra datasettet.     
    2. Vi bør ta hensyn til at det har vært en vekst i kapasiteten i utvalgsperioden. Siden regresjonen er på log-form, er det tilstrekkelig å legge til tid (År) som variabel for å ta hensyn til det.       
    
Vi skal nå bruke resultatet for å si noe om effekten av kraftkablene på pris.     

1.2.4 Finn etter beste evne ut hvor mye kablene til Storbritannia og Tyskland kan antas å bli i prosent av total produksjon. Bruk dette tallet til å finne ut hvor mange prosent vi kan forente at prisene vil øke som følge av disse kablene.     

1.2.5 Forklar ved hjelp av mikroøkonomisk teori hvorfor det kan være lurt å bygge slike kabler, til tross for en prisøkning.      


    


##### Kapittel 2 - Aktuell debatt: Vil husholdninger få en lavere strømregning om forbrukeravgiften reduseres?    

ca 500-1000 ord     

Her skal du gi en faglig oppsummering av en debatt som har pågått mellom samfunnsøkonomer i Dagens Næringsliv om effekten av å redusere forbrukeravgiften (også kalt elavgiften) på strøm. Forklar først hva denne avgiften er og hvordan den fastsettes. [Eric Nævdal](https://www.dn.no/innlegg/elavgiften/strom/strompris/innlegg-elavgiftskutt-hjelper-ikke-stromkundene-men-det-gjor-elavgift-pa-eksportstrom/2-1-1065150) påstår at en reduksjon i forbrukeravgiften på strøm ikke vil redusere strømregningen til husholdninger. [Nils-Henrik M. von der Fehr](https://www.dn.no/innlegg/innlegg-navdals-teori-passer-ikke-for-kraftmarkedet/2-1-1070683) mener at dette ikke stemmer.    

Les Nævdals innlegg frem til "Vann- og vindkraft er derfor ideele varer å beskatte", og bruk din bakgrunn i mikroøkonomi til å forklare hans argumenter for ferske studenter (tegn gjerne et eller flere markedskryss for å illustrere). Les deretter von der Fehr sitt innlegg, og tegn et markedskryss som illustrerer hvordan han tenker. Forklar hvorfor han er uenig med Nævdal. Hvem er du enig med, og hvorfor? 

##### Kapittel 3 - Tiltak mot høye strømpriser   

ca 500-1000 ord    

Strømpriser har vært høye, og regjeringen har innført ulike tiltak for å hjelpe husholdninger med å klare å betale strømregningen. [Strømstøtte til husholdninger](https://www.regjeringen.no/no/tema/energi/regjeringens-stromtiltak/id2900232/?expand=factbox2900261) er et slikt tiltak hvor en andel av kraftprisen betales av myndighetene dersom den gjennomsnittlige månedsprisen ligger over en terskelverdi, inntil 5000 KW/t per måned. Hvordan denne støtten ble utregnet for mars 2022 kan dere finne [her](https://www.nve.no/reguleringsmyndigheten/nytt-fra-rme/nyheter-reguleringsmyndigheten-for-energi/stroemstoette-her-er-stoettesatsene-for-mars/).    

I dette kapitlet skal vi se på hvordan en gjennomsnittlig husholdning som bor i et rekkehus på 140 kvm i Oslo tilpasser seg med og uten strømstøtte. En gjennomsnittlig husholdning har 46 000kr i månedlig inntekt (etter skatt), og bruker 22 000 KW/t i strøm per år for denne boligtypen. Legg til grunn gjennomsnittsprisen for strøm i mars 2022 (lenke ovenfor). Inntekten brukes på konsum (C) som har "pris" 1kr (dvs 1 enhet konsum koster 1kr), og strøm.    
(i) tegn en budsjettlinje i figur som viser husholdningens månedlig konsummuligheter i mars 2022 uten strømstøtte. Sett enheter konsum på den vertikale aksen, og enehter strøm på den horisontale.     
(ii) i samme figur tegn budsjettlinjen med støttesatsen for mars 2022.      
(iii) tegn inn noen indifferenskurver som kan tenkes å representere husholdnings preferanser mellom konsum og strøm.    
(iv) Vis husholdningens tilpasningen før og etter støtte i mars. Hvor mye bedre har husholdningen fått det med dette tiltaket?      

Et annet tiltak som regjerningen kan vurdere er å gi hver husholdning et kontantbeløp for mars 2022. Gitt at husholdningen i Oslo får samme kronebeløp i støtte som med en subsidiert kraftpris hva ville den foretrekke? Forklar din analyse her, og intuisjonen bak ditt svar.



#### C. Bedømmelse    
Formålet med denne oppgaven er å utforske hvordan kraftmarkedet fungerer, og formidle funn til nye studenter i samfunnsøkonomi i et notat.
 

Oppgaven bedømmes ut fra følgende kriterier:

1. evne til å forstå og beskrive hvordan markedet fungerer
2. evne til å finne, presentere og tolke relevant data 
3. evne til å gi kortfattede og presise definisjoner av mikroøkonomiske begreper og operasjonalisere disse i en analyse
4. anvendelse av mikroøkonomisk analyse til å vurdere ulike påstander
5. anvendelse av mikroøkonomisk analyse for å utforske samfunnsøkonomiske sammenhenger
6. at analysen henger sammen og at det går en rød tråd gjennom den
7. at forklaringene til figurene er presise og gode
8. formidling til folk som ikke nødvendigvis er økonomer
9. kvaliteten på koden dere bruker til å løse oppgaven
10. presentasjonen av arbeidet (tegn gjerne figurer med Python for eksempel)

 




Lykke til!



