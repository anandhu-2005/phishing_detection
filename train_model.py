import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import sys
import os
from detector.feature_extractor import extract_features 
# ── Make sure feature_extractor is importable ─────────────────────────────
sys.path.append(os.path.join(os.path.dirname(__file__), 'detector'))
from feature_extractor import extract_features

# ── 1. Load the dataset ───────────────────────────────────────────────────
print("Loading dataset...")
df = pd.read_csv('combined_dataset.csv')
print(f"  Total rows: {len(df)}")

# ── 2. Extract features from each URL ─────────────────────────────────────
# This is the slow step — it loops through every URL
print("Extracting features (this may take a minute)...")
X = []
for i, url in enumerate(df['url']):
    try:
        X.append(extract_features(str(url)))
    except Exception:
        X.append([0] * 12)          # fallback: zeros if URL is malformed
    if i % 50000 == 0:
        print(f"  {i}/{len(df)} done...")

y = df['label'].tolist()

# ── 3. Split into training set and test set ───────────────────────────────
# 80% for training, 20% for testing
# random_state=42 means you get the same split every time you run it
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"  Training samples: {len(X_train)}")
print(f"  Test samples:     {len(X_test)}")

# ── 4. Train the model ────────────────────────────────────────────────────
# RandomForest = many decision trees voting together → very reliable
print("Training model...")
clf = RandomForestClassifier(
    n_estimators=100,    # 100 trees — good balance of speed vs accuracy
    random_state=42,
    n_jobs=-1            # use all CPU cores to speed up training
)
clf.fit(X_train, y_train)
print("  Training done.")

# ── 5. Evaluate ───────────────────────────────────────────────────────────
print("\n── Evaluation Results ──")
y_pred = clf.predict(X_test)

# classification_report shows precision, recall, F1 for each class
print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing']))

# confusion matrix: [[TN, FP], [FN, TP]]
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(f"  True Legit  (correct): {cm[0][0]}")
print(f"  False Alarm (wrong):   {cm[0][1]}")
print(f"  Missed Phish (wrong):  {cm[1][0]}")
print(f"  True Phish  (correct): {cm[1][1]}")

# ── 6. Save the model ─────────────────────────────────────────────────────
os.makedirs('detector/model', exist_ok=True)
joblib.dump(clf, 'detector/model/phishing_model.pkl')
print("\nModel saved to detector/model/phishing_model.pkl")