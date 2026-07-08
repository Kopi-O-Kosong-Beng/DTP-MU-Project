# CO₂ Emissions Explorer

**What actually drives U.S. per-capita CO₂ emissions?** A state-level regression study over a 1,300-observation panel (50 states × 26 years, 1998–2023), packaged as an interactive Streamlit app.

![Python](https://img.shields.io/badge/Python-3.9+-3776ab?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-ff4b4b?logo=streamlit&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest%20·%2010%20passing-brightgreen)

🎬 **[6-minute project video](https://youtu.be/_4QkfWFUnI4)** · 📖 **[Full case study with methodology & honest failure analysis](https://zhifeng-portfolio.vercel.app/projects/co2-modeling)**

---

## The question

Per-capita CO₂ emissions vary nearly **twelve-fold** across U.S. states — 7.7 tonnes/year in New York vs 92.9 in Wyoming. A uniform emissions cap punishes states whose energy systems differ structurally. Can we predict a state's per-capita emissions from five structural variables — renewable energy consumption, coal production, natural gas production, personal consumption expenditure (PCE), and urban population — and use the drivers to argue for targeted climate policy?

## Key findings

A single pooled model across all 50 states turned out to be statistical noise — state-level structure swamps any shared pattern. Rather than force it, we pivoted to case studies of the three highest-emitting states, each with its own multiple linear regression:

| State | Adjusted R² | Significant drivers (5% level) |
|---|---|---|
| Wyoming | **0.98** | Coal production + urban population |
| North Dakota | **0.84** | Coal + gas production, consumption spending |
| Alaska | **0.81** | Consumption spending, gas, urban population |

**There is no one-size-fits-all model.** Coal drives Wyoming and North Dakota; consumption-linked emissions drive Alaska; natural gas *reduces* emissions in one state and raises them in another.

### Validation we're proud of

- **Real out-of-sample testing** — trained on 1998–2019, tested on 2020–2023, with RMSE reported in raw, range-adjusted, and normalized forms.
- **Leakage avoided by design** — relative scaling instead of Z-score standardization, so no future information contaminates training.
- **Honest failure reporting** — Alaska's coefficients lost significance on the training window alone, so we reported N.A. instead of a misleading number; North Dakota's under-prediction was traced to oil-field gas flaring (~15 Mt CO₂ in 2020) that our five variables never captured.

## The app

| Page | What it does |
|---|---|
| **Home** | Intro and navigation |
| **Case Studies** | Historical CO₂-per-capita trends for WY, ND, AK with driver narratives and raw-data preview |
| **Prediction** | Enter the five structural drivers, get a per-capita forecast from the state-specific OLS model (fit via `np.linalg.lstsq`) |
| **HASS Reflection** | The environmental-justice dimension: who bears the burden of emissions |

## Quick start

```bash
git clone https://github.com/Kopi-O-Kosong-Beng/DTP-MU-Project.git
cd DTP-MU-Project

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run Home.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## Project structure

```
├── Home.py                     # Streamlit entry point
├── case_service.py             # Load & filter the merged dataset for case studies
├── data_service.py             # Fit state-specific OLS models, prediction API
├── pages/
│   ├── 02_Case_Studies.py      # Historical trends + driver narratives
│   ├── 03_Prediction.py        # Interactive forecasting UI
│   └── 04_HASS_Reflection.py   # Environmental-justice reflection
├── tests/
│   ├── test_case_service.py    # Data loading, filtering, sorting
│   └── test_data_service.py    # Model structure, prediction sanity checks
├── assets/
│   └── All main data (1998 to 2023).xlsx   # Merged panel dataset
└── requirements.txt
```

## Testing

```bash
python -m pytest
```

Ten tests cover data loading, column contracts, series filtering/sorting, model structure, and a prediction sanity check (zero inputs must return the intercept).

## Data sources

- U.S. Energy Information Administration (EIA) — State Energy Data System
- U.S. Bureau of Economic Analysis (BEA) — personal consumption expenditure
- U.S. Census Bureau — urban population estimates

## Team & attribution

Built for SUTD's Design Thinking Project III by a 5-person team. I was one of two core modelers and the developer of this Streamlit app: together with my teammate I gathered the dataset and built the regression models in Excel — he wrote the core math-algorithm code, and I did the final checking and integrated the models into the app. I also originated the evaluation methodology (adjusted R² and RMSE-variant scoring), wrote the report, and led the model-strengths analysis in the final presentation. Full role breakdown on the [case study page](https://zhifeng-portfolio.vercel.app/projects/co2-modeling).
