# Phishing Detection System — Project Documentation

**Course Project | Group of 3 | 1-Week MVP**
**Stack: Django + Python**

---

## 1. Project Overview

A web application that accepts a URL as input and predicts whether it is a **phishing** or **legitimate** link using heuristic feature extraction and a machine learning classifier.

---

## 2. Scope (MVP Only)

| In Scope | Out of Scope |
|---|---|
| URL input via web form | Browser extension |
| Feature extraction from URL string | Email scanning |
| ML model prediction (pre-trained) | Real-time crawling/screenshot |
| Result display (safe / phishing) | User accounts / history |
| Basic Django frontend | REST API / mobile support |

---

## 3. System Architecture

```
User → Django Frontend (form)
           ↓
       Django View
           ↓
    Feature Extractor (Python)
           ↓
    ML Model (scikit-learn, loaded at startup)
           ↓
    Prediction → Rendered Result Page
```

No separate backend service needed — the ML model runs inside the Django process.

---

## 4. Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Django 4.x |
| Language | Python 3.10+ |
| ML Library | scikit-learn |
| Feature Extraction | Python (`re`, `urllib`, `tldextract`) |
| Dataset | UCI Phishing Websites / Kaggle phishing URLs |
| Frontend | Django templates + Bootstrap 5 |
| DB | SQLite (default, no custom models needed for MVP) |

---

## 5. Django Project Structure

```
phishing_detector/
├── manage.py
├── phishing_detector/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── detector/
│   ├── views.py          ← main logic
│   ├── urls.py
│   ├── forms.py          ← URLInputForm
│   ├── feature_extractor.py  ← extracts features from URL
│   ├── model/
│   │   └── phishing_model.pkl  ← pre-trained model saved via joblib
│   └── templates/
│       └── detector/
│           ├── index.html
│           └── result.html
└── requirements.txt
```

---

## 6. Features Extracted from URL

These are computed purely from the URL string — no HTTP request needed.

| # | Feature | Description |
|---|---|---|
| 1 | `url_length` | Total character length of URL |
| 2 | `has_ip` | 1 if URL uses IP address instead of domain |
| 3 | `has_at_symbol` | 1 if `@` present in URL |
| 4 | `has_double_slash` | 1 if `//` appears after position 7 |
| 5 | `subdomain_count` | Number of subdomains |
| 6 | `has_https` | 1 if scheme is HTTPS |
| 7 | `domain_length` | Length of registered domain |
| 8 | `path_length` | Length of URL path |
| 9 | `hyphen_in_domain` | 1 if `-` appears in domain |
| 10 | `digit_ratio` | Ratio of digits to total URL length |
| 11 | `special_char_count` | Count of `%`, `=`, `?`, `&` in URL |
| 12 | `tld_in_path` | 1 if a TLD like `.com` appears in the path |

These 12 features are sufficient for a working MVP model.

---

## 7. Module Details

### 7.1 `feature_extractor.py`

```python
import re
from urllib.parse import urlparse
import tldextract

def extract_features(url: str) -> list:
    parsed = urlparse(url)
    ext = tldextract.extract(url)

    features = [
        len(url),
        1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc) else 0,
        1 if '@' in url else 0,
        1 if '//' in url[7:] else 0,
        len(ext.subdomain.split('.')) if ext.subdomain else 0,
        1 if parsed.scheme == 'https' else 0,
        len(ext.domain),
        len(parsed.path),
        1 if '-' in ext.domain else 0,
        sum(c.isdigit() for c in url) / len(url),
        sum(url.count(c) for c in ['%', '=', '?', '&']),
        1 if any(t in parsed.path for t in ['.com', '.net', '.org']) else 0,
    ]
    return features
```

### 7.2 `views.py`

```python
import joblib
import os
from django.shortcuts import render
from .forms import URLInputForm
from .feature_extractor import extract_features

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'phishing_model.pkl')
model = joblib.load(MODEL_PATH)  # loaded once at startup

def check_url(request):
    result = None
    url = None
    if request.method == 'POST':
        form = URLInputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            features = extract_features(url)
            prediction = model.predict([features])[0]
            result = 'Phishing' if prediction == 1 else 'Legitimate'
    else:
        form = URLInputForm()
    return render(request, 'detector/index.html', {'form': form, 'result': result, 'url': url})
```

### 7.3 `forms.py`

```python
from django import forms

class URLInputForm(forms.Form):
    url = forms.URLField(
        label='Enter URL',
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com', 'class': 'form-control'})
    )
```

---

## 8. ML Model Training (Offline Script)

Run this once locally to generate `phishing_model.pkl`. Not part of the Django app.

```python
# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from feature_extractor import extract_features

df = pd.read_csv('phishing_dataset.csv')  # columns: url, label (0=legit, 1=phish)

X = [extract_features(url) for url in df['url']]
y = df['label'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

print(classification_report(y_test, clf.predict(X_test)))
joblib.dump(clf, 'detector/model/phishing_model.pkl')
print("Model saved.")
```

**Recommended dataset:** [Kaggle — Malicious and Benign URLs](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) or the UCI Phishing Websites dataset.

---

## 9. Work Division (3 Members, 1 Week)

| Member | Responsibility |
|---|---|
| Member 1 | Dataset collection, model training script, `.pkl` generation, model evaluation |
| Member 2 | Django app setup, `feature_extractor.py`, `views.py`, `urls.py` wiring |
| Member 3 | Frontend templates (index + result pages), Bootstrap styling, form validation |

### Day-by-Day Plan

| Day | Task |
|---|---|
| Day 1 | Project setup, Django scaffold, divide work |
| Day 2 | Dataset ready; feature extractor written and tested |
| Day 3 | Model trained and `.pkl` saved; Django view wired up |
| Day 4 | Frontend templates done; end-to-end flow working |
| Day 5 | Testing with real URLs; bug fixes |
| Day 6 | Documentation finalized; demo prepared |
| Day 7 | Buffer / submission |

---

## 10. Setup Instructions

```bash
# Clone / create project
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install django scikit-learn joblib tldextract pandas

# Start Django project
django-admin startproject phishing_detector .
python manage.py startapp detector

# After wiring everything, run server
python manage.py runserver
```

---

## 11. Requirements (`requirements.txt`)

```
django>=4.2
scikit-learn>=1.3
joblib>=1.3
tldextract>=3.4
pandas>=2.0
```

---

## 12. Limitations (Acknowledged for Submission)

- Model accuracy depends on dataset quality
- URL-only analysis; does not fetch or render the page
- No real-time threat intelligence feed
- No WHOIS or DNS lookup (kept out of MVP scope)
- Model may misclassify newly registered legitimate domains

---

## 13. Future Enhancements (Beyond MVP)

- Add DNS/WHOIS-based features
- Integrate VirusTotal API for live checking
- Store scan history per session
- Export results as PDF report
- Deploy to cloud (Render / Railway)

