# CO₂ Emissions Explorer

A Streamlit-based web app for exploring and forecasting CO₂ emissions per capita.

## Project Overview

* **Case Studies**: Historical trends for Wyoming (WY), North Dakota (ND), and Alaska (AK).
* **Prediction**: Interactive forecasting based on coal & natural gas production, per capita income, urbanization, and renewable energy usage.
* **HASS Reflection**: Social and ethical analysis on environmental justice and responsibility.

## 📂 File Structure

```bash
LAST_DTP/
├── app.py
├── case_service.py         # Load & filter merged data for case studies
├── data_service.py         # Fit & apply state-specific regression models
├── assets/
│   ├── All main data (1998 to 2023).xlsx   # Input data for charts & models
├── pages/                    # Streamlit multipage directory
│   ├── 02_case_studies.py    # Case studies page
│   ├── 03_prediction.py      # Prediction interface
│   └── 04_hass_reflection.py # Qualitative reflection page
├── tests/
│   ├── test_data_service.py
│   └── test_case_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Kopi-O-Kosong-Beng/DTP-MU-Project/tree/main
cd LAST_DTP
```

### 2. Create and activate a virtual environment

```bash
# Install virtualenv (to your user site)
pip3 install --user virtualenv

# Create the env
~/.local/bin/virtualenv .venv

# Activate it
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

Open your browser at the URL printed (usually [http://localhost:8501](http://localhost:8501/)).

## 🧪 Testing

Run unit tests with pytest:

```bash
pytest
```

## 📄 Usage

* **Home**: Intro & navigation.
* **Case Studies**: View historical CO₂ trends for WY, ND, AK.
* **Prediction**: Input your parameters and click **Run Prediction**.
* **HASS Reflection**: Explore environmental justice themes.

## 📦 Deployment

* Suitable for platforms supporting Python & Streamlit (Heroku, Streamlit Cloud, Azure).
* Ensure `assets/` and `.env` (if any secrets) are included in deployment.

## 🤝 Contribution

Contributions and improvements are welcome:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request
