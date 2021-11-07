import feather
import os

researchPath = os.environ['RESEARCH_PATH']
featherPath = f'{researchPath}\\4-Data Management\\test.feather'
df = feather.read_dataframe(featherPath)
print(df.head())