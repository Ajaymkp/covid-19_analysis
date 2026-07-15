# 🦠 COVID-19 Pandemic Data Analysis & Risk Classification

A comprehensive data analysis project using Python and Pandas to analyze global COVID-19 trends, vaccination impact, wave dynamics, and country-level risk classification across 10 analytical tasks.

---

## 📌 Project Overview

This project analyzes a multi-country COVID-19 dataset covering cases, deaths, vaccinations, hospitalization, ICU admissions, and policy data. The goal is to extract meaningful insights and classify countries by risk level using a custom scoring algorithm.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Data manipulation & analysis |
| NumPy | Numerical operations |
| Google Colab | Development environment |

---

## 📂 Project Structure

```
covid19-analysis/
│
├── covid_analysis.py       # Main analysis script (Tasks 1–9)
└── README.md
```

---

## 📊 Tasks Covered

| Task | Description |
|---|---|
| Task 1 | Data Understanding — shape, info, describe |
| Task 2 | Missing Value Handling — mean imputation across 25+ features |
| Task 3 | Country-Wise Analysis — top 5 by cases, deaths, vaccinations |
| Task 4 | Growth Rate Analysis — 7-day case & death growth rates |
| Task 5 | Wave Analysis — highest mortality & positivity rate waves |
| Task 6 | Vaccination Impact — correlation with cases, deaths, positivity |
| Task 7 | Moving Average — 7-day smoothing for US, India, Brazil |
| Task 8 | Correlation Matrix — key COVID metrics correlation analysis |
| Task 9 | High Risk Detection — multi-criteria country risk classification |

---

## 🔍 Key Highlights

- **Missing value imputation** across 25+ numerical columns using column mean
- **7-day moving average** model for smoothing case and death trends
- **Custom risk scoring algorithm** classifying countries as High / Medium / Low risk based on:
  - Positivity rate
  - ICU admissions
  - Hospitalizations
  - Reproduction number (Rt)
- **Correlation analysis** between vaccination rate and new cases / deaths / positivity rate
- **Wave dynamics analysis** to identify waves with highest mortality using time-series grouping

---

## ⚙️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Ajaymkp/covid19-analysis.git
cd covid19-analysis
```

**2. Install dependencies**
```bash
pip install -r pandas
pip install -r numpy
```

**3. Add the dataset**

Place your `covid_processed.csv` file inside a `data/` folder:
```
covid19-analysis/
└── data/
    └── covid_processed.csv
```

**4. Run the analysis**
```bash
python covid_analysis.py
```

---

## 📦 Requirements

```
pandas
numpy
```

---

## 📈 Sample Insights

- Top 5 most affected countries by cumulative cases identified
- Countries with highest 7-day case growth rate ranked
- Vaccination rate shows negative correlation with new cases and deaths
- Multi-criteria risk scoring successfully classifies countries into 3 risk tiers

---

## 👤 Author

**Mukesh Kumar Pandian M**  
Data Engineer | B.Tech Information Technology  
[LinkedIn](https://linkedin.com/in/mukesh-kumar-pandian-m-6833b5387) · [GitHub](https://github.com/Ajaymkp)
