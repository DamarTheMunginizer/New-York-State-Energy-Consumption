<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 90px">

# Project 5 (Add new title here)

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

We employ clustering methods and neural networks to classify the state into these various climatological zones, so that we might simplify the process for the State Energy Planning Board to determine which land use agreements should be considered for each type of renewable energy source. We then perform a predictive time-series analysis to demonstrate that our proposed plan will continue to serve the State well into the future, in alignment with the state's benchmark goals in 2030, 2040, and 2050.

We collect weather data over a 25-year period from 2000 to 2024 using the [open-meteo api](https://open-meteo.com/). Open-meteo collects daily weather data at 05:00 GMT. 

## Data Dictionary
Two datasets are required to successfully replicate our work: the daily weather data from Open-Meteo and the energy consumption data for New York State from ______

Daily Weather Data
| Information | Data Type | Description | Notes |
|---|---|---|---|
| `date` | `string` | Date on which the data was collected. | Converted to a `datetime` object for time series analysis. |
| `daylight_duration` | `float` | Length of time between sunrise and sunset, measured in seconds. |  |
| `sunshine_duration` | `float` | Length of time for which the sun was visible, measured in seconds. |  |
| `rain_sum` | `float` | Total rainfall, measured in inches. |  |
| `snowfall_sum` | `float` | Total snowfall, measured in inches. |  |
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

### Software
| Library | Module | Purpose |
|---|---|---|

## Executive Summary

### Purpose

### Data Handling

### Analysis

### Findings and Implications

### Next Steps