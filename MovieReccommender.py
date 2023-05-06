import pandas as pd

db = pd.read_table('title.basics.tsv.gz', compression = 'gzip', nrows = 10)
print(db)