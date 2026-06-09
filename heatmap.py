import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from detector.feature_extractor import extract_features
import os

# ── Load model and data ───────────────────────────────────────────────────
model = joblib.load('detector/model/phishing_model.pkl')

df = pd.read_csv('malicious_phish.csv')
df['label'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

df = df.sample(20000, random_state=42)
X = [extract_features(str(url)) for url in df['url']]
y = df['label'].tolist()

os.makedirs('evaluation', exist_ok=True)

# ── Feature Correlation Heatmap ───────────────────────────────────────────
feature_names = [
    'url_length', 'has_ip', 'has_at_symbol', 'has_double_slash',
    'subdomain_count', 'has_https', 'domain_length', 'path_length',
    'hyphen_in_domain', 'digit_ratio', 'special_char_count', 'tld_in_path'
]

df_features = pd.DataFrame(X, columns=feature_names)
df_features['label'] = y

plt.figure(figsize=(10, 8))
sns.heatmap(
    df_features.corr(),
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    square=True
)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('evaluation/correlation_heatmap.png')
plt.show()
print("Saved: evaluation/correlation_heatmap.png")