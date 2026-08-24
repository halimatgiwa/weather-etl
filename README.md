# Weather Data ETL Pipeline Using Python & OpenWeather API

## Project Overview

This project demonstrates the development of a simple **ETL (Extract, Transform, Load) pipeline** using Python and real-time weather data from the OpenWeather API.

The pipeline extracts weather information for multiple cities, transforms the API response into a structured Pandas DataFrame, performs basic analysis, and loads the processed data into a CSV file for future analysis.

The project was completed as part of **Week 7: Data Pipelines & Automation** at AnalystLab Africa.

---

## Data Source

**OpenWeather API**

The OpenWeather API provides real-time weather information for locations around the world.

Weather data was collected for the following cities:

* Lagos
* London
* New York

The API was used to retrieve:

* City Name
* Temperature
* Humidity
* Weather Condition
* Wind Speed
* Date and Time

---

## ETL Process

### 1. Extract

The pipeline connects to the OpenWeather API using Python's `requests` library.

Weather data is retrieved for three cities: Lagos, London, and New York.

The API response is converted from JSON into a format that can be processed using Python.

### 2. Transform

The extracted weather information is organized into a structured Pandas DataFrame.

The transformation process includes:

* Selecting relevant weather fields
* Renaming columns for clarity
* Converting the API timestamp into a readable date and time format
* Organizing the information into a clean tabular dataset
* Preparing the dataset for analysis

### 3. Load

The transformed dataset is saved as:

`weather_data.csv`

The CSV file provides a reusable dataset that can be opened in Excel, Power BI, Python, or other data analysis tools.

---

## Tools Used

* **Python** – ETL pipeline development
* **Pandas** – Data transformation and analysis
* **Requests** – API connection and data extraction
* **Jupyter Notebook** – Development and demonstration
* **OpenWeather API** – Weather data source
* **GitHub** – Source code and project documentation

---

## Project Structure

```text
weather-etl/
│
├── weather_etl.py
├── weather_etl.ipynb
├── weather_data.csv
├── README.md
├── .gitignore
└── .env
```

> **Security Note:** The OpenWeather API key is stored locally in an environment file and is not included in the public repository.

---

## Steps Taken

1. Created an OpenWeather API account.
2. Generated an API key.
3. Connected to the OpenWeather API using Python.
4. Selected three cities for data collection.
5. Extracted real-time weather information.
6. Selected relevant fields from the API response.
7. Organized the extracted information using Pandas.
8. Converted the API timestamp into a readable datetime format.
9. Created a clean weather dataset.
10. Saved the processed dataset as a CSV file.
11. Compared weather measurements across the selected cities.
12. Documented the ETL pipeline and findings.
13. Published the project source code on GitHub.

---

## Basic Analysis

The processed dataset was analyzed to compare weather conditions across the selected cities.

The analysis focused on:

* City with the highest temperature
* City with the highest humidity
* City with the highest wind speed
* Weather conditions recorded for each city

### Key Findings

The analysis identified differences in temperature, humidity, wind speed, and weather conditions across Lagos, London, and New York.

The exact results depend on the weather data returned by the OpenWeather API at the time of extraction because weather conditions change in real time.

---

## Key Learning Outcomes

This project provided practical experience in building a basic data pipeline from an external API to a structured dataset.

Key lessons learned include:

* How to retrieve data from an external REST API using Python
* How to work with JSON API responses
* How to structure and transform raw data using Pandas
* How to convert timestamps into readable datetime values
* How to save processed data for future analysis
* How ETL pipelines prepare raw data for analytical use
* The importance of protecting API credentials when working with public repositories
* How to document and version-control a data project using Git and GitHub

---

## Conclusion

This project demonstrates a complete basic ETL workflow:

**Extract → Transform → Analyze → Load**

The pipeline successfully retrieves real-time weather data, transforms it into a clean and structured dataset, performs basic comparisons, and stores the processed data in CSV format.

The project also demonstrates the importance of separating sensitive API credentials from publicly shared source code.

---

## Author

**Halimat Giwa**

B.Sc. Petroleum Chemistry | Energy Data Analyst

GitHub: https://github.com/halimatgiwa
