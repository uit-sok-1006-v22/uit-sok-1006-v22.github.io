# Sok-1006 Mikroøkonomi

## Mappeoppgave 1    

Denne mappeoppgaven består av to case som er like viktig. Det er lov å samarbeide i grupper på inntil 3 studenter. Tilbakemelding underveis: de som ønsker tilbakemelding kan levere et utkast i Canvas innen 25. mars kl 16.00. Tilbakemelding gis i løpet av uke 13.  

## Case 1    

**A. Bakgrunn**       
Du skal anvende det du har lært om markedsanalyse til å forstå et forskningsarbeid om kyllingmarkedet i USA. For å få en dyp forståelse av hva forskerne har gjort prøver man ofte å replisere arbeidet dersom man har tilgang til det samme datasettet som analysen er bygget på. Dette er tilfellet her. Du skal blant annet klare i løpet av oppgaven å tegne Figur 1 og Figur 2 fra artikkelen.    

**B. Instruksjoner**       
Innleveringen skal bestå av en Jupyter notebook med kode, figurer og forklaringer (skriv forklaringene i Markdown).   

**C. Bedømmelse**    
Formålet med denne oppgaven er å bli kjent med hvordan enkle begrep fra mikroøkonomi kan operasjonaliseres i en analyse. Du får trening i å      

a) anvende mikroøkonomiske begrep og bruke disse til å tolke resultater     
b) kode for å replisere noen av resultatene fra analysen   
c) kjøre og forklare en enkel scenarioanalyse.   

En god besvarelse gir kortfattede og presise definisjoner av grunnbegrepene, og klarer å anvende disse begrepene i analysen. Videre vil en god besvarelse inneholde presise forklaringer av figurene som du lager.    

### Case 1 - oppgave og ressurser     


1. Epple og MacCallum (2006) har estimert tilbud og etterspørsel i markedet for kylling. Les [avsnittene som er merket med gult](https://uit-sok-1006-v22.github.io/innleveringer/chicken_economicinquiry merket.pdf){:target="blank"}, og forklar likning (1) og (2) s. 375.

2. Epple og McCallum estimerer likning (1) og (2) og presenterer resultatene i likning (7) og (4) på side 376/7. Gi en forklaring av koeffisientene i disse likningene; hvorfor var forfatterne ikke fornøyd med disse likningene som en spesifikasjon av tilbud og etterspørsel?   

3. Til slutt ender forfatterne opp med likning (14) som beskriver (invers) etterspørsel og likningene (15) og (16) som representerer invers tilbud på henholdsvis lang og kort sikt. Hva er etterspørselens priselastisitet fra likning (14) og hva er tolkningen av denne?


4. Programmer ferdig [denne pythonfila](https://uit-sok-1006-v22.github.io/innleveringer/chicken.py). Det som mangler er å 

    1. programmere inn funksjonene (14). (15) og (16)
    2. å lage en funksjon som finner hvilket kvantum som gir likevekt (tilbud=etterspørsel) 
    2. å plotte funksjonene. 

    Hver av tilbud- og etterspørselsfunksjonene har argumentet `c` først. Dette argumentet kan enten være `sp` (`sympy`) for å regne ut likevekt, eller `np` (`numpy`) for å plotte funksjonene. 
    
    I funksjonen `equate_q` skal du bruke `sympy` til å regne ut hvilket kvantum som gir likhet mellom etterspørsel og langsiktig tilbud. Bruk `sp.Eq`, og la første argument i funksjonene være `sp`.
    
    Når du skal plotte funksjonene, husk at
    
    1. funksjonene skal opphøyes i eksponenten (dvs. du bruker `np.exp()`) for å uttrykkes i nivå
    2. så skal de multipliseres med `cpi`
    3. første argument i tilbuds-/etterspørselsfunksjonene er `np` her, ikke `sp`
    
5. Du skal nå kunne kjøre følgende kode i samme mappe (bruk for eksempel jupyter). En figur med etterspørsel og langsiktig og kortsiktig tilbud skal da plottes. 
    
    ```
    import pandas as pd
    import chicken
    df=pd.read_csv("https://uit-sok-1006-v22.github.io/innleveringer/chickendata.csv",delimiter=";")
    chicken.plot_year(df,1995)
    ```
    
6. Plott figurer for 1960 og 1995, forklar figuren, og gi grunner til denne utviklingen (s380 i artikkelen).   

7. Scenarioanalyse. Lag ytterligere tre plott i samme figur, der du legger til 0.5 til henholdsvis kvantum, inntekt og storfekjøtt. Beskriv ulike hendelser (scenarioer) som kan legges til grunn for hver av disse endringene, og forklar hvordan likevekten påvirkes i hvert tilfelle.

## Case 2    

**A. Bakgrunn**     
[Norges offentlige utredninger 2019:8 "Særavgiftene på sjokolade- og sukkervarer og alkoholfrie drikkevarer"](/innleveringer/nou2019_8_særavgift sukker.pdf) utreder hvorvidt man skulle fortsette med det som var kalt "sukkerskatten" på folkemunne. Du er ansatt som økonomisk rådgiver for å sjekke at innholdet i rapporten er faglig forsvarlig. I denne oppgaven skal du vurdere en påstand, og forklare dine funn for utvalget. Du må huske at ikke alle i utvalget er fagøkonomer.   

**B. Instruksjoner**      
Innleveringen skal bestå av en pdf fil (ca 1000 ord).   

**C. Bedømmelse**     
Formålet med denne oppgaven er å       

a) anvende mikroøkonomiske analyse til å vurdere hvorvidt en påstand stemmer     
b) forklare denne analysen for folk som ikke nødvendigvis er økonomer   
   

En god besvarelse gir kortfattede og presise definisjoner av grunnbegrep som du bruker i analysen. Videre vil en god besvarelse ha en rød tråd gjennom analysen. Illustrerende bruk av figurer belønnes. Figurene bør være klar og godt forklart.    

### Case 2 - oppgave     

I ovennenvnte NOU på side 86 finner vi følgende: *"I et marked med fullkommen konkurranse, vil avgifter (både spesifikke- og prosentvise avgifter) bli fullt overveltet i forbrukerprisen. Det er med andre ord en-til-en-overføring av avgiften."*  Bruk mikroøkonomisk analyse og forklar for utvalget hvorvidt du er enig eller uenig i påstanden her.     


Lykke til!



