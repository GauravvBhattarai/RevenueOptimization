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


