#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from scipy import stats
import warnings


# In[2]:


# Suppress warnings
warnings.filterwarnings("ignore")


# In[3]:


def create_historical_data():
    np.random.seed(42)
    date_range = pd.date_range(start='2023-01-01', periods=365, freq='D')
    base_demand = 100 + 10 * np.sin(np.linspace(0, 3.14 * 2, 365))
    noise = np.random.normal(scale=5, size=365)
    total_passengers = base_demand + noise
    return pd.DataFrame({'date': date_range, 'total_passengers': total_passengers})


# In[4]:


def plot_demand_seasonality(data):
    decomposition = seasonal_decompose(data['total_passengers'], period=7, extrapolate_trend='freq')
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(decomposition.trend, label='Trend')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(decomposition.seasonal, label='Seasonality')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(decomposition.resid, label='Residuals')
    plt.legend()
    plt.tight_layout()
    plt.show()


# In[5]:


def create_forecast(data, forecast_days=30):
    data['total_passengers'].fillna(method='ffill', inplace=True)  # Handle missing values
    model = ExponentialSmoothing(data['total_passengers'], seasonal_periods=7, trend='add', seasonal='add').fit()
    forecast = model.forecast(forecast_days)
    return forecast


# In[6]:


def price_elasticity_analysis(data):
    price_changes = np.linspace(-0.2, 0.2, 5)  # Simulating -20% to +20% price changes
    elasticity = -0.8  # Assumed elasticity coefficient
    results = data.copy()
    results['adjusted_demand'] = results['total_passengers'] * (1 + elasticity * price_changes[2])  # Apply price change
    return results


# In[7]:


def optimize_inventory_allocation(forecast_demand):
    fare_classes = ['Economy', 'Premium Economy', 'Business', 'First Class']
    allocation_ratios = [0.5, 0.3, 0.15, 0.05]  # Example allocation ratios
    allocations = {}
    
    for i, fare_class in enumerate(fare_classes):
        allocations[fare_class] = {
            'allocated_seats': forecast_demand * allocation_ratios[i],
            'demand_mean': forecast_demand * allocation_ratios[i] * 0.15  # Example multiplier
        }
    return allocations


# In[8]:


def main():
    historical_data = create_historical_data()
    plot_demand_seasonality(historical_data)
    forecast_demand = create_forecast(historical_data, forecast_days=30)
    elasticity_results = price_elasticity_analysis(historical_data)
    inventory_allocation = optimize_inventory_allocation(forecast_demand.mean())  # Using mean forecast demand
    
    print("\nInventory Allocation:")
    for key, value in inventory_allocation.items():
        print(f"{key}: {value}")
    
    plt.figure(figsize=(10, 5))
    plt.plot(forecast_demand, label='Forecasted Demand', linestyle='dashed')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


# In[ ]:




