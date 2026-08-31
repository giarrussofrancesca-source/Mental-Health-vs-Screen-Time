import sqlite3
import pandas as pd
df = pd.read_csv(r"C:\Users\Francesca\Desktop\screen_time_mental_health.csv")
#analisi forma del dataset, tipi di dato e statistiche descrittive. Conteggio di adolescenti depressi.
print(df.shape)
print(df.dtypes)
print(df.describe())
print(df["depressed"].value_counts())
#verifica di eventuali valori nulli
print(df.isnull().sum())
#adolescenti con depressione più marcata, maschi vs femmine
df_depressed = df[df["bdi_total"] > 20]
print(df_depressed)
print(df_depressed["sex"].value_counts())
#media di tempo trascorso sugli schermi, ore di sonno e livello di depressione, maschi vs femmine
print(df.groupby("sex")[["screen_time_index", "avg_sleep_hours", "bdi_total"]].mean())
#caricamento csv in tabella sql
df_sql = sqlite3.connect ("df.db")
df.to_sql("df", df_sql, if_exists = "replace", index = False)
#confronto sesso vs depressione media 
query = pd.read_sql("SELECT sex, AVG(bdi_total), COUNT (*) FROM df GROUP BY sex ORDER BY AVG(bdi_total) DESC", df_sql)
print(query)
#analisi delle ore di sonno su più di 500 persone
second_query = pd.read_sql("SELECT sex, AVG(avg_sleep_hours), COUNT (*) FROM df WHERE avg_sleep_hours < 7.5 GROUP BY sex HAVING COUNT (*) > 500", df_sql)
print(second_query)
#cte per aggregare i dati sulla salute mentale per genere e filtrare i gruppi ad alto punteggio medio
cte = pd.read_sql("""WITH stats_per_sesso AS(
    SELECT sex, AVG(bdi_total) AS media_bdi,
    COUNT(*) AS n
    FROM df
    GROUP BY sex
)
SELECT *
FROM stats_per_sesso
ORDER BY media_bdi
DESC""", df_sql)
#cte per selezionare gruppi di genere con media bdi superiore a 7
second_cte = pd.read_sql("""WITH stats_per_sesso AS(
    SELECT sex, AVG(bdi_total) AS media_bdi,
    COUNT(*) AS n
    FROM df
    GROUP BY sex
)
SELECT *
FROM stats_per_sesso
WHERE media_bdi > 7
ORDER BY media_bdi
DESC""", df_sql)
#creazione colonna calcolata per ore di sonno
df["sleep_category"] = df["avg_sleep_hours"].apply(
    lambda x : "insufficient" if x < 8 else ("adequate" if x <= 10 else "excessive")
)
print(df["sleep_category"].value_counts())
#window function per calcolare il rank di bdi_total all'interno di ogni gruppo sex
rank_total_bdi = pd.read_sql("SELECT subject_id, sex, bdi_total, RANK () OVER (PARTITION BY sex ORDER BY bdi_total DESC) AS rank_bdi FROM df", df_sql)
print(rank_total_bdi)
#differenza tra livello inviduale di depressione e media per sesso
avg_bdi = pd.read_sql("SELECT subject_id, sex, bdi_total, AVG(bdi_total) OVER (PARTITION BY sex) AS avg_sex FROM df", df_sql)
print(avg_bdi)
diff_avg_sex = pd.read_sql("""SELECT *, bdi_total - avg_sex AS difference FROM(SELECT subject_id, sex, bdi_total, AVG(bdi_total) OVER (PARTITION BY sex) AS avg_sex FROM df)""", df_sql)
print(diff_avg_sex)
#replica in pandas del rank calcolato in SQL, con method='min' per gestire i pari nello stesso modo di RANK()
sql_rank = df.groupby("sex")["bdi_total"].rank(ascending = False, method = 'min') 
print(sql_rank)
df_sql.close()