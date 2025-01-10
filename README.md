<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 90px">

# Project 5: New York State of Energy - Renewable Energy by 2030

*Team: Muhammad Haseeb Anjum, Graham Haun, Melissa Marshall, Deval Mehta, Damar Shipp*

## Table of Contents
1) [Overview](#Overview) 
2) [Data Dictionary](<#Data Dictionary>)
3) [Requirements](#Requirements)
4) [Executive Summary](<#Executive Summary>)
    1) [Purpose](<#Purpose>)
    2) [Data Handling](<#Data Handling>)
    3) [Analysis](#Analysis)
    4) [Findings and Implications](<#Findings and Implications>)
    5) [Next Steps](#Next-Steps)

## Overview
According to the [New York State Energy Plan](https://energyplan.ny.gov/), the State of New York intends to reduce greenhouse gas emissions to 85% of their 1990 levels by 2050. To this end, the State must produce and maintain renewable energy infrastructure to gradually replace the existing carbon-based energy systems in place on a similar, if not accelerated, timescale. In particular, the various climatological zones of New York State are amenable to wind, solar, and hydroelectric power. In order to determine the best locations for each source of energy, we must consider a variety of factors, from typical weather to cost to land use agreements.

We employ k-means clustering and time-series analysis to classify the state into distinct climatological zones, so that we might simplify the process for the State Energy Planning Board to determine which land use agreements should be considered for each type of renewable energy source. We then perform a predictive time-series analysis to demonstrate that our proposed plan will continue to serve the State into the near future, in alignment with the state's benchmark goals in 2030.

We collect weather data over a 20-year period from 2005 to 2024 using the [open-meteo api](https://open-meteo.com/). Open-meteo collects daily weather data at 05:00 GMT. In addition, we've collected population data and energy consumption data for the State of New York through 

## Data Dictionary
Two datasets are required to successfully replicate our work: the daily weather data from Open-Meteo and the energy consumption data for New York State from ______

Daily Weather Data
| Information | Data Type | Description | Notes |
|---|---|---|---|
| `date` | `string` | Date on which the data was collected. | Converted to a `datetime` object for time series analysis. |
| `daylight_duration` | `float` | Length of time between sunrise and sunset, measured in seconds. |  |
| `sunshine_duration` | `float` | Length of time for which the sun was visible, measured in seconds. |  |
| `rain_sum` | `float` | Total rainfall, measured in millimeters. |  |
| `snowfall_sum` | `float` | Total snowfall, measured in millimeters. |  |
| `precipitation_hours` | `float` | Length of time during which precipitation occured. |  |
| `wind_speed_10m_max` | `float` | Maximum wind speed at 10 meters above ground. |  |
| `wind_gusts_10m_max` | `float` | Maximum wind gusts at 10 meters above ground. |  |
| `latitude` | `float` | Latitude coordinate. |  |
| `longitude` | `float` | Longitude coordinate. |  |
| `precipitation_total` | `float` | Sum of `rain_sum` and `snowfall_sum`. | Engineered. |
| `location` | `tuple` | (`latitude`, `longitude`) | Engineered. |

Energy Consumption Data
| Information | Data Type | Description | Notes |
|---|---|---|---|
| `Name` | `string` | Zone for which data is collected. |  |
| `Load` | `float` | Total energy consumption, measured in KwH. |  |
| `Date` | `string` | Date on which the date was collected. | Converted to a `datetime` object for time series analysis. |

## Requirements

### Hardware
12 threads needed for time series KMeans Clustering Model
### Software
| Library | Module | Purpose |
| --- | --- | --- |
| `numpy` || Ease of basic aggregate operations on data.|
| `pandas` || Read our data into a DataFrame, clean it, engineer new features, and write it out to submission files.|
| `matplotlib` | `pyplot`| Basic plotting functionality.|
| `seaborn` || More control over plots.|
| `prophet` || [Procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.](https://facebook.github.io/prophet/)|
| `sklearn` | `cluster`| `KMeans` for KMeans clustering.|
|  | `metrics`| `silhouette_score` for determining the silhouette score.|
|  | `preprocessing`| `StandardScaler` for scaling data.|
|  | `pipeline`| `Pipeline` to set up a pipeline for models.|
|  | `decomposition`| `PCA` to reduce dimensionality of the data.|
| `tslearn` | `clustering`| `TimeSeriesKMeans` for a KMeans model that accounts for a historic change.|
| `zipefile` | | To extract files from a zip file.|
| `os` | | Access operating level commands within python.|
| `random` | | To generate random seeds for easier analysis of models.|
| `time` | | To delay the data collection script to avoid minutely and hourly api limits.|
| `retry_requests` | | `retry` Helps handle HTTP timeouts or network errors.|
| `openmeteo_requests` | | Required for the open-meteo api.|
| `requests_cache` | | cahce HTTP requests to reduce the need for repeated network calls.|
## Executive Summary

### Purpose
We require three key pieces of information in order to best inform the Energy Planning Board of the best regions to considering building solar, wind, and hydroelectric energy collection facilities and distribution centers:

- The climatological regions of New York State
- The demand for energy across the State
- The cost of building and maintainngg said structures.



### Data Handling

### Analysis

### Findings and Implications

### Next Steps