# merge_datasets.py
import pandas as pd

# Load original dataset
df1 = pd.read_csv('malicious_phish.csv')
df1['label'] = df1['type'].apply(lambda x: 0 if x == 'benign' else 1)
df1 = df1[['url', 'label']]
df1.columns = ['url', 'label']
print(f"Original dataset: {len(df1)} rows")

# Load LegitPhish — 1.0 = legitimate, 0.0 = phishing
df2 = pd.read_csv('url_features_extracted1.csv')
df2 = df2[['URL', 'ClassLabel']]
df2.columns = ['url', 'label']
df2['label'] = df2['label'].apply(lambda x: 0 if x == 1.0 else 1)  # flip: 1.0=legit=0, 0.0=phish=1
print(f"LegitPhish dataset: {len(df2)} rows")

# Merge and drop duplicates
combined = pd.concat([df1, df2]).drop_duplicates(subset='url').reset_index(drop=True)
print(f"Combined dataset: {len(combined)} rows")
print(f"Label distribution:\n{combined['label'].value_counts()}")

combined.to_csv('combined_dataset.csv', index=False)
print("Saved to combined_dataset.csv")