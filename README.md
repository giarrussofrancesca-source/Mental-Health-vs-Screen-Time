# Screen Time vs Mental Health negli adolescenti
Quali effetti sono associati all'utilizzo di dispositivi elettronici negli adolescenti tra i 12 e i 16 anni? Esiste una relazione tra tempo trascorso sullo schermo, carenza di sonno e sintomi depressivi? Ci sono differenze tra maschi e femmine?

## Dataset:
Fonte: **Screen Time vs Mental Health (ML-Ready)**
- Kaggle, derivato dallo studio peer-reviewed di Hökby et al. (2025, PLOS Global Public Health).
**Descrizione**: 4.810 adolescenti svedesi (12-16 anni) con dati sul tempo trascorso sullo schermo, qualità del sonno e sintomi depressivi.

## Tecniche utilizzate:
- **Python / pandas**: esplorazione dati, pulizia, filtri, aggregazioni e colonne calcolate;
- **SQL (SQLite)**: query con GROUP BY/HAVING, CTE, window function (RANK, AVG OVER);
- **Power BI**: dashboard interattiva con colonne calcolate DAX, misure, slicer e pagina riepilogativa.

## Risultati principali:
L'analisi ha messo in evidenza una netta differenza tra maschi e femmine: queste registrano un punteggio medio di sintomi depressivi quasi doppio rispetto ai maschi.
Oltre il 60% degli adolescenti non riposa il numero di ore raccomandato di 8-10 ore (National Sleep Foundation).

Non emerge una relazione lineare diretta tra tempo trascorso sullo schermo e sintomi depressivi. I valori del dataset riguardanti il tempo trascorso sullo schermo sono discontinui, rendendo più complesso individuare un pattern chiaro; un'analisi statistica come un test di correlazione permetterebbe di quantificare con maggiore precisione l'eventuale associazione tra le due variabili.

## Limiti del dataset:
- Il tempo trascorso sullo schermo non è misurato in modo lineare, limitando la possibilità di individuare eventuali correlazioni.
- I dati non mostrano relazioni di causa-effetto: un punteggio di depressione più alto associato ad un utilizzo maggiore di dispositivi elettronici non implica che l'uno causi l'altro.
- Il campione è composto solo da adolescenti svedesi: i risultati non sono necessariamente generalizzabili ad altre popolazioni.

### Link:
[Screen Time vs Mental Health (ML Ready)](https://www.kaggle.com/datasets/kylefengkfeng209/screen-time-vs-mental-health-ml-ready)