import json
import pandas as pd

file = open('dados\\dados2025.json', encoding='utf-8')
data = json.load(file)

#print(data)

df = pd.DataFrame.from_dict(data)

print(df)

file.close()