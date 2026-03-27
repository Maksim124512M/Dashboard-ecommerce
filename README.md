# Online Retail Dashboard Documentation

This is the official documentation for the **Online Retail (2010–2011)** dashboard built with **Streamlit** and **Plotly**.  

---

## Overview

The dashboard provides:

- Key **KPI metrics**:
  - Average revenue per sale
  - Total revenue
  - Number of sales
- **Monthly revenue trend**
- **TOP-5 products by revenue**
- Clean handling of duplicates in the dataset

---

## Technologies Used

- Python 3.12
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- Excel dataset (`data/online_retail.xlsx`)

---

## Project Structure
```
online_retail_dashboard/
├── data/
│   └── online_retail.xlsx
├── app.py
├── README.md
└── requirements.txt
```
- `data/online_retail.xlsx`: The dataset used for the dashboard.
- `app.py`: The main Streamlit application file.
- `README.md`: This documentation file.
- `requirements.txt`: List of required Python packages.

### Dashboard URL
The dashboard is hosted on Streamlit Cloud and can be accessed at:
[https://dashboard-ecommerce-neceabv5yinwhnabayvum.streamlit.app/](https://dashboard-ecommerce-neceabv5yinwhnabayvum.streamlit.app/)