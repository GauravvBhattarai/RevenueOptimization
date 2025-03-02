#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing


# In[2]:


def create_historical_data():
    # Creating historical data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    np.random.seed(42) # Ensures reproducibility
    
    # Base passenger numbers (from ORR data)
    base_passengers = 4000 + np.random.normal(0, 200, len(dates))
    #Starting with 4000 base passengers (LNER's daily capacity), Adding random variation with normal distribution (mean=0, std=200)
    
    # Seasonal factors (derived from LNER annual report) (Creates a sinusoidal pattern for yearly seasonality with 30% variations)
    seasonal_factors = 1 + 0.3 * np.sin(np.pi * np.arange(len(dates))/180)
    
    # Festival effect (Edinburgh Fringe Festival data)
    festival_effect = np.zeros(len(dates))
    festival_mask = (dates.month == 8) & (dates.day.isin(range(1, 29)))
    festival_effect[festival_mask] = 1500
    # Adds 1500 extra passengers during Edinburgh Festival (August 1-28)
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'base_passengers': base_passengers,
        'seasonal_factor': seasonal_factors,
        'festival_effect': festival_effect,
        'total_passengers': base_passengers * seasonal_factors + festival_effect
    })
    
    # Add pricing tiers (based on LNER pricing strategy)
    # Four pricing tiers based on LNER's actual pricing strategy with small random variations added to each price and higher variability in more expensive tickets)
    df['super_advance_price'] = 45 + np.random.normal(0, 2, len(dates))
    df['advance_price'] = 79 + np.random.normal(0, 3, len(dates))
    df['semi_flex_price'] = 125 + np.random.normal(0, 5, len(dates))
    df['flex_price'] = 179 + np.random.normal(0, 7, len(dates))
    
    return df

# Create and analyze data
historical_data = create_historical_data()

# Perform time series decomposition which breaks down passenger numbers into: Trend component, weekly patterns & residual component

decomposition = seasonal_decompose(historical_data['total_passengers'], 
                                 period=7, 
                                 extrapolate_trend='freq')

# Create forecasting model using Exponential Smoothing accounting for both trend and seasonality for 30 days

def create_forecast(data, forecast_days=30):
    model = ExponentialSmoothing(data['total_passengers'],
                                seasonal_periods=7,
                                trend='add',
                                seasonal='add').fit()
    
    forecast = model.forecast(forecast_days)
    return forecast

# Calculate revenue metrics
def calculate_revenue_metrics(data):
    # Calculating revenue for each ticket types
    data['super_advance_revenue'] = data['total_passengers'] * 0.25 * data['super_advance_price']
    data['advance_revenue'] = data['total_passengers'] * 0.40 * data['advance_price']
    data['semi_flex_revenue'] = data['total_passengers'] * 0.20 * data['semi_flex_price']
    data['flex_revenue'] = data['total_passengers'] * 0.15 * data['flex_price']
    
    data['total_revenue'] = (data['super_advance_revenue'] + 
                            data['advance_revenue'] + 
                            data['semi_flex_revenue'] + 
                            data['flex_revenue'])
    
    return data

# Add revenue calculations
historical_data = calculate_revenue_metrics(historical_data)

# Calculate key metrics
daily_metrics = {
    'Average Daily Passengers': historical_data['total_passengers'].mean(),
    'Peak Day Passengers': historical_data['total_passengers'].max(),
    'Average Daily Revenue': historical_data['total_revenue'].mean(),
    'Peak Daily Revenue': historical_data['total_revenue'].max(),
    'Festival Period Average Passengers': historical_data.loc[historical_data['festival_effect'] > 0, 'total_passengers'].mean(),
    'Festival Period Average Revenue': historical_data.loc[historical_data['festival_effect'] > 0, 'total_revenue'].mean()
}

# Print key metrics
print("\nKey Performance Metrics:")
for metric, value in daily_metrics.items():
    print(f"{metric}: £{value:,.2f}" if 'Revenue' in metric else f"{metric}: {value:,.2f}")

# Generate forecast
forecast_data = create_forecast(historical_data)


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create pricing optimization data
def create_pricing_data():
    # Current pricing tiers
    pricing_data = {
        'Ticket_Type': ['Super Advance', 'Advance', 'Semi-Flex', 'Flex'],
        'Current_Price': [45, 79, 125, 179],
        'Optimized_Price': [65, 95, 145, 199],
        'Allocation_Percentage': [25, 35, 25, 15],
        'Current_Revenue': [],
        'Optimized_Revenue': []
    }
    
    # Base assumptions
    daily_passengers = 4000
    
    # Calculate revenue for each tier
    for i in range(len(pricing_data['Ticket_Type'])):
        # Current revenue
        current_revenue = (daily_passengers * 
                         (pricing_data['Allocation_Percentage'][i]/100) * 
                         pricing_data['Current_Price'][i])
        pricing_data['Current_Revenue'].append(current_revenue)
        
        # Optimized revenue (assuming 5% decrease in demand due to higher prices)
        optimized_revenue = (daily_passengers * 0.95 * 
                           (pricing_data['Allocation_Percentage'][i]/100) * 
                           pricing_data['Optimized_Price'][i])
        pricing_data['Optimized_Revenue'].append(optimized_revenue)
    
    return pd.DataFrame(pricing_data)

# Create and analyze pricing data
pricing_df = create_pricing_data()

# Calculate key metrics
pricing_df['Revenue_Improvement'] = ((pricing_df['Optimized_Revenue'] - 
                                    pricing_df['Current_Revenue']) / 
                                    pricing_df['Current_Revenue'] * 100)

# Print analysis
print("\nPricing Optimization Analysis:")
print("==============================")
print(f"\nTotal Current Daily Revenue: £{pricing_df['Current_Revenue'].sum():,.2f}")
print(f"Total Optimized Daily Revenue: £{pricing_df['Optimized_Revenue'].sum():,.2f}")
print(f"Overall Revenue Improvement: {((pricing_df['Optimized_Revenue'].sum() - pricing_df['Current_Revenue'].sum()) / pricing_df['Current_Revenue'].sum() * 100):,.1f}%")

# Create visualization
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = np.arange(len(pricing_df['Ticket_Type']))

# Create bars
plt.bar(index, pricing_df['Current_Price'], bar_width, 
        label='Current Price', color='skyblue')
plt.bar(index + bar_width, pricing_df['Optimized_Price'], bar_width,
        label='Optimized Price', color='lightgreen')

# Customize plot
plt.xlabel('Ticket Type')
plt.ylabel('Price (£)')
plt.title('Current vs Optimized Pricing Strategy')
plt.xticks(index + bar_width/2, pricing_df['Ticket_Type'])
plt.legend()

# Add value labels on bars
for i in range(len(pricing_df['Ticket_Type'])):
    plt.text(i, pricing_df['Current_Price'][i], f'£{pricing_df["Current_Price"][i]}',
             ha='center', va='bottom')
    plt.text(i + bar_width, pricing_df['Optimized_Price'][i], 
             f'£{pricing_df["Optimized_Price"][i]}',
             ha='center', va='bottom')

plt.tight_layout()


# In[ ]:




