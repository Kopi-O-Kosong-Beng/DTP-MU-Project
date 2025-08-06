# CO₂ Emissions Explorer

A Streamlit-based web app for exploring and forecasting CO₂ emissions per capita.

## Project Overview

* **Case Studies**: Historical trends for Wyoming (WY), North Dakota (ND), and Alaska (AK).
* **Prediction**: Interactive forecasting based on coal & natural gas production, per capita income, urbanization, and renewable energy usage.
* **HASS Reflection**: Social and ethical analysis on environmental justice and responsibility.

## 📂 File Structure

```bash
your-project/
├── app.py                   # Entrypoint (Home page)
├── data_service.py          # Data loading & ML model logic
├── utils.py                 # Utility functions (formatting, validation)
├── assets/
│   └── future.png           # App picture
├── pages/                   # Streamlit multipage directory
│   ├── 02_Case_Studies.py   # Case studies
│   ├── 03_Prediction.py     # Prediction interface
│   └── 04_HASS_Reflection.py# Qualitative reflection
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── .gitignore               # Local ignores (e.g. .venv/)
```

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone 
cd co2-explorer
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
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
