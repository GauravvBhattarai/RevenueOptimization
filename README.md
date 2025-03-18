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

# F. Outcome and Analysis

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

The pricing strategy combined with other promotional techniques would increase Annual Revenue by £2.3M (a ROI of 312%). Revenue per Seat Mile would be £0.42, a 23% increase from the base figure. The dynamic pricing strategy on different fare classes would also help in capacity building, specifically, reducing empty seats by 16% and improving first-class utilization by 22%. Customer experiences will get better despite higher prices following the value proposition of LNER. In the short term, the optimization would help in immediate revenue increment during the Festive Fringe in Edinburgh including improved yield management and capacity utilization. In the long run, it will enhance LNER’s pricing strategy framework, demand forecasting capability, and understanding of customer behaviour and set a benchmark for other special events. Some ideas for future optimizations would be to roll out dynamic pricing immediately and update inventory management systems every 4 hours. 

Looking at the outcomes, it can be seen that Demand Forecasting Enhancement can be done by:
- Granular Segmentation: Segment customers based on booking behaviors, demographics, and travel purposes. This allows for tailored pricing strategies that cater to specific customer needs.
- Real-Time Data Integration: Incorporate real-time data sources, such as social media trends and local events, to adjust forecasts dynamically.

Advanced Pricing Strategies enhancement tools:
- Dynamic Pricing Models: Implement machine learning algorithms that adjust prices based on real-time demand fluctuations, competitor pricing, and remaining capacity.
- Personalized Offers: Utilize customer data to provide personalized pricing or bundled offers, enhancing perceived value and willingness to pay.

Techniques for Capacity Management:
- Flexible Scheduling: Adjust train frequencies and capacities based on predicted demand surges during the festival period.
- Seat Inventory Control: Allocate seat quotas to different fare classes dynamically, ensuring optimal revenue from each segment.

Marketing and Promotions campaigns can be based on:
- Targeted Campaigns: Develop marketing campaigns aimed at high-value customer segments identified through data analysis.
- Partnerships: Collaborate with event organizers to offer combined travel and event packages, making LNER the preferred choice for festival-goers.

# G. Business Implications

- Revenue Growth: By implementing these strategies, LNER can further boost revenue beyond the initial 13.2% increase, solidifying its financial position.
- Customer Satisfaction: Personalized and dynamic pricing can enhance customer satisfaction by offering value-aligned options, potentially increasing repeat business.
- Competitive Advantage: Advanced revenue management positions LNER ahead of competitors, attracting a larger share of the market during peak periods.
- Operational Efficiency: Optimized capacity management ensures resources are utilized effectively, reducing operational costs.

# H. Conclusion 

Expanding upon the initial revenue optimization model, LNER has the potential to unlock significant additional revenue streams by adopting a data-driven, dynamic approach to pricing, capacity management, and customer segmentation. The projected 13.2% increase in revenue is just the beginning. By integrating real-time demand forecasting, dynamic pricing models, and personalized marketing strategies, LNER can enhance both short-term profitability and long-term customer loyalty. Beyond revenue growth, these strategies also provide operational benefits. More efficient seat inventory management and demand-driven scheduling ensure that resources are utilized effectively, reducing unnecessary costs and maximizing seat occupancy. Additionally, customer experience is a critical factor—offering personalized pricing and travel packages can improve satisfaction and loyalty, leading to repeat business and positive word-of-mouth.  

From a strategic perspective, the implementation of these revenue optimization techniques will position LNER as a forward-thinking, competitive leader in the rail travel industry. By continuously refining its pricing and capacity models through data analysis and machine learning, the company can adapt to evolving market conditions, seasonal fluctuations, and customer preferences. Looking ahead, LNER should consider further technological enhancements, such as AI-driven demand prediction models and real-time competitor benchmarking, to refine its revenue strategies. Moreover, forming partnerships with event organizers and leveraging loyalty programs could serve as additional revenue drivers. Ultimately, by adopting a holistic and adaptive revenue management strategy, LNER can ensure sustainable financial growth while maintaining customer-centric service excellence.

# I. References

Lazar, T. and Naylor, R. 2023. Festivals Edinburgh Economic Impact of Edinburgh Festivals Image credits.
LNER 2023. Responsible Business Report 2023/24.
Office of Rail and Road 2015. Impact Assessment of the CMA’s Options for Increasing On-Rail Competition [Online]. Available from: www.arup.com.
Office of Rail and Road 2024. Passenger rail performance [Online]. [Accessed 6 January 2025]. Available from: https://dataportal.orr.gov.uk/statistics/performance/passenger-rail-performance/.
Office of Rail and Road 2023. Rail fares index.
