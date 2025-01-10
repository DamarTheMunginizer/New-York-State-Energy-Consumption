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

## Data Dictionary
We collect weather data over a 20-year period from 2005 to 2024 using the [open-meteo api](https://open-meteo.com/). Open-meteo collects daily weather data at 05:00 GMT. In addition, we've collected energy consumption data for the State of New York from [New York Independent System Operators](https://www.nyiso.com/) and population data from [New York State's public data respository](https://data.ny.gov/Government-Finance/Annual-Population-Estimates-for-New-York-State-and/krt9-ym2k/about_data).

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
- The cost of building and maintaining said structures

To determine the climatological zones and the source of energy to which they are most amenable, we employ k-means clustering and time-series k-means clustering, both to inspect the number of zones and how those zones might change over time.

### Analysis
We initially intended to divide New York State into three clusters: one for each energy source we considered to be compatible with the State. A quick k-means clustering algorithm demonstrated that a hydro-electric cluster is not well-defined, thus we focus on solar and wind. With that knowledge in mind, we engineered a few features to improve the separation between clusters, which are clearly indicated above. We then project all of our features through 2030 using a Prophet model (which handles seasonality, trends, and shocks with ease) before fitting a time-series k-means clustering model to it. We see that our clusters shift as time progresses, relative to the 2020 clusters, but we should note that the Open-Meteo data is faulty on collection. As such, our analysis may need to be revisited with more complete data.

We also projected New York State's energy use through 2030 with a Prophet model. Here the data was more complete and required no feature engineering and our projected data aligns very well with historic changes. We see that the State's energy consumption drops over time, with seasonal upticks during the Summer months. We would expect energy consumption to taper at some point, however our projections show it completely vanishing, which is unrealistic. This is one of the faults with time-series analysis.

As the energy consumption for the State drops, the cost of energy production would as well, as some solar and wind farms can be retired. Our cost analysis is purely based on research in public-facing figures from The United States Department of Energy, the National Renewable Energy Laboratory, The International Renewable Energy Agency, and the United States Energy Information Agency. We do expect that the cost for maintaining solar and wind farms will be impacted by inflation, but not enough to offset the savings presented by the lower cost of use.

### Findings and Implications
Our present analysis suggests that New York State is in a great position to take advantage of wind and solar farms to produce and store energy to service the whole State's needs. The construction, staffing, and maintenance of these new facilities is projected to produce around 250,000 new jobs and save the State trillions in the long term, compared to the present energy infrastructure. As the effects of human-accelerated climate change become more visible, the climatological zones of New York State will muddle as well, with the "solar" zone growing larger.

### Next Steps
Future work would confirm that our proposal accurately assesses and meets New York's energy needs through 2050 and beyond. We do caution, however, that long-term time-series projections tend to be unreliable, though there is a margin of confidence we may able to provide. The New York State Energy Planning Board should proceed to check land use agreements in accordance with our recommendations.