# Mappeoppgave 1  -   Sok-1006


1. Epple og MacCallum (2006) har estimert tilbud og etterspørsel i markedet for kylling. Les [avsnittene som er merket med gult](https://uit-sok-1006-v22.github.io/innleveringer/chicken_economicinquiry merket.pdf){:target="blank"}, og forklar likning (1) og (2) s. 375.

2. Epple og McCallum estimerer likning (1) og (2) og presenterer resultatene i likning (7) og (4) på side 376/7. Gi en forklaring av koeffisientene i disse likningene; hvorfor var forfatterne ikke fornøyd med disse likningene som en spesifikasjon av tilbud og etterspørsel?   

3. Til slutt ender forfatterne opp med likning (14) som beskriver (invers) etterspørsel og likningene (15) og (16) som representerer invers tilbud på henholdsvis lang og kort sikt. 
    1. Hva er etterspørselens priselastisitet fra likning (14) og hva er tolkningen av denne?
    2. Dersom storfekjøtt øker med to prosent, inntekt med fem prosent og mengde faller med fire prosent, hva er da den marginale konsumenten i gjennomsnitt villig til å betale for kylling?

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

