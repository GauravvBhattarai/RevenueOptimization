# LNER Revenue Optimization Engine

# A. Introduction

This repository contains a comprehensive revenue optimization model developed for London North Eastern Railway (LNER) with a specific focus on maximizing yield during high-demand periods such as the Edinburgh Festival Fringe. The model demonstrates how strategic pricing, inventory management, and demand forecasting can significantly increase revenue while maintaining customer satisfaction levels.

The project implements advanced computational techniques to analyze historical data, forecast future demand patterns, and optimize ticket pricing strategies across different booking timeframes. The model achieved a projected 13.2% revenue improvement and a potential annual revenue increase of £2.3 million.

# B. Key Performance Indicators 

![image](https://github.com/user-attachments/assets/5d49d4bf-3eae-48de-a2ee-99b3440d6610)

# C. Methodology 

1. Route & Timeframe Analysis:
- Route: London Kings Cross to Edinburgh Waverley
- Focus Period: Edinburgh Festival Fringe (August 1-28, 2025)
- Baseline Capacity: 8 daily services with 500 seats per train (4,000 seats daily)

2. Data Collection & Preprocessing
- Historical passenger data from Office of Rail and Road (ORR)
- LNER capacity and pricing tier information
- Seasonal patterns and festival effect calculations
- Customer booking behavior across different timeframes

# D. Model Development

1. Time Series Analysis
- Seasonal decomposition of historical data
- Trend analysis and pattern identification
- Isolation of festival-specific demand surges

2. Demand Forecasting
- Exponential smoothing with trend and seasonality components
- Short and medium-term passenger volume predictions
- Booking pattern analysis by timeframe

3. Revenue Optimization Algorithms
- Implementation of Littlewood's rule for fare optimization
- Dynamic pricing model based on demand elasticity
- Inventory allocation optimization across fare classes

# E. Key Insights and strategies

1. Pricing Strategy
The model identified optimal pricing tiers based on booking timeframes to maximize revenue:

![image](https://github.com/user-attachments/assets/b8cb4711-5355-4ae4-b3ea-76531f0ab085)

According to Littlewood’s rule, revenue is maximized when options are: 
FL ≥ FH * Prob [XH > ΘH] 
FL is the lower fare (in this case the probability is 100%), FH is the higher fare, XH is the demand for a higher fare and ΘH represents the protection level for a higher fare. 

2. Inventory Management

First Class Enhancement: 
- Increased First Class seating capacity from 100 to 125 seats on key routes
- Implemented dynamic upgrade pricing starting at £35, adjusted in real-time based on:
        - Time to departure
        - Remaining seat availability
        - Expected demand patterns
        - Historical upgrade acceptance rates
- AI-powered seat mapping for optimal allocation

Standard Class Optimization
- Rebalanced seat allocation across fare classes based on demand patterns
- Adjusted inventory controls for different booking timeframes
- Implemented constraints on group bookings to maximize yield

3. Innovative Revenue Streams
- Festival Fringe Pass: Unlimited travel ticket priced at £299
        - Limited release of 2,000 passes generating £598,000 additional revenue
        - Enhanced customer loyalty and simplified booking experience
- Partnership Bundling: Combined tickets with festival events and accommodations
        - Revenue sharing model with festival organizers
        - Increased advance bookings and overall yield

# Outcome and Analysis

Economy: {'allocated_seats': 51.03347135856582, 'demand_mean': 7.6550207037848725}

Premium Economy: {'allocated_seats': 30.62008281513949, 'demand_mean': 4.593012422270923}

Business: {'allocated_seats': 15.310041407569745, 'demand_mean': 2.2965062111354615}

First Class: {'allocated_seats': 5.103347135856582, 'demand_mean': 0.7655020703784873}

Average Daily Passengers: 4,115.89

Peak Day Passengers: 5,733.30

Average Daily Revenue: £390,838.09

Peak Daily Revenue: £543,868.19

Festival Period Average Passengers: 4,651.53

Festival Period Average Revenue: £443,143.14

Revenue optimization Technique

Total Optimized Daily Revenue: £439,280.00

Overall Revenue Improvement: 13.2%

## Graphs for Trend, Seasonality and Residuals

![image](https://github.com/user-attachments/assets/1fb0df73-d6cb-4ee3-892a-319f1dd43ad7)

## Demand Forecast

![image](https://github.com/user-attachments/assets/7e5341f9-17d5-4910-b7b0-d46e7538e683)

## Current VS Optimized Revenue

![image](https://github.com/user-attachments/assets/5f5b4c0e-4358-4009-9611-10c288e7c62e)

![image](https://github.com/user-attachments/assets/85ed6f7d-bb6b-45a1-88ac-5b872c1df8fa)





