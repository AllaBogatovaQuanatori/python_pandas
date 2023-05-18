import pandas as pd

if __name__ == '__main__':
    power_data = pd.read_csv('csv/power.csv')

    filtered_data = power_data[
        (power_data['country'].isin(['Latvia', 'Lithuania', 'Estonia'])) &
        (power_data['category'].isin([4, 12, 21])) &
        (power_data['year'].between(2005, 2010)) &
        (power_data['quantity'] >= 0)]

    total_consumption = filtered_data['quantity'].sum()
    print("Total consumption of Baltic countries :", total_consumption)
