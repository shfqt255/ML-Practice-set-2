# Pakistan City Population Predictor
# Simple and beginner-friendly code

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Fetch data from Wikipedia
print("Fetching data from Wikipedia...")
print("-" * 50)

url = "https://en.wikipedia.org/w/index.php?title=List_of_cities_in_Pakistan_by_population&variant=en"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table', {'class': 'wikitable'})

# Step 2: Extract data from table
cities_data = []

rows = table.find_all('tr')[1:]  # Skip header row

for row in rows:
    cells = row.find_all('td')
    
    if len(cells) >= 8:
        # Get city name
        city_name = cells[1].get_text().strip()
        
        # Get populations (remove commas and convert to numbers)
        pop_2023 = cells[2].get_text().strip().replace(',', '').split('\n')[0]
        pop_2017 = cells[3].get_text().strip().replace(',', '').split('\n')[0]
        pop_1998 = cells[4].get_text().strip().replace(',', '').split('\n')[0]
        pop_1981 = cells[5].get_text().strip().replace(',', '').split('\n')[0]
        pop_1972 = cells[6].get_text().strip().replace(',', '').split('\n')[0]
        pop_1961 = cells[7].get_text().strip().replace(',', '').split('\n')[0]
        pop_1951 = cells[8].get_text().strip().replace(',', '').split('\n')[0]
        
        # Convert to integers (handle empty values)
        def clean_number(text):
            try:
                return int(''.join(filter(str.isdigit, text)))
            except:
                return 0
        
        pop_2023 = clean_number(pop_2023)
        pop_2017 = clean_number(pop_2017)
        pop_1998 = clean_number(pop_1998)
        pop_1981 = clean_number(pop_1981)
        pop_1972 = clean_number(pop_1972)
        pop_1961 = clean_number(pop_1961)
        pop_1951 = clean_number(pop_1951)
        
        # Only add if 2023 population exists
        if pop_2023 > 0:
            cities_data.append({
                'City': city_name,
                '1951': pop_1951,
                '1961': pop_1961,
                '1972': pop_1972,
                '1981': pop_1981,
                '1998': pop_1998,
                '2017': pop_2017,
                '2023': pop_2023
            })

# Step 3: Create DataFrame
df = pd.DataFrame(cities_data)

print("Data fetched successfully!")
print(f"Total cities found: {len(df)}")
print("\nAvailable cities:")
for i, city in enumerate(df['City'], 1):
    print(f"{i}. {city}")

print("\n" + "=" * 50)

# Step 4: Get user input
city_name = input("\nEnter city name (e.g., Karachi, Lahore): ").strip()
prediction_year = int(input("Enter prediction year (e.g., 2040): "))

# Find the city in dataframe
city_row = df[df['City'].str.contains(city_name, case=False, na=False)]

if city_row.empty:
    print(f"\nCity '{city_name}' not found!")
    print("Please check the spelling and try again.")
else:
    city_row = city_row.iloc[0]
    
    print("\n" + "=" * 50)
    print(f"PREDICTION FOR {city_row['City'].upper()}")
    print("=" * 50)
    
    # Step 5: Prepare data for Linear Regression
    years = [1951, 1961, 1972, 1981, 1998, 2017, 2023]
    populations = [
        city_row['1951'],
        city_row['1961'],
        city_row['1972'],
        city_row['1981'],
        city_row['1998'],
        city_row['2017'],
        city_row['2023']
    ]
    
    # Remove zero values
    valid_data = [(year, pop) for year, pop in zip(years, populations) if pop > 0]
    valid_years = [item[0] for item in valid_data]
    valid_populations = [item[1] for item in valid_data]
    
    # Step 6: Train Linear Regression Model
    X = np.array(valid_years).reshape(-1, 1)  # Years as features
    y = np.array(valid_populations)  # Population as target
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Step 7: Make prediction
    predicted_population = model.predict([[prediction_year]])[0]
    predicted_population = int(predicted_population)
    
    # Calculate percentage change from 2023
    pop_2023 = city_row['2023']
    percentage_change = ((predicted_population - pop_2023) / pop_2023) * 100
    
    # Step 8: Display results
    print(f"\nHistorical Population Data:")
    print("-" * 50)
    for year, pop in zip(valid_years, valid_populations):
        print(f"{year}: {pop:,}")
    
    print("\n" + "=" * 50)
    print("PREDICTION RESULTS")
    print("=" * 50)
    print(f"City: {city_row['City']}")
    print(f"Prediction Year: {prediction_year}")
    print(f"Predicted Population: {predicted_population:,}")
    print(f"2023 Population: {pop_2023:,}")
    print(f"Percentage Change from 2023: {percentage_change:+.2f}%")
    
    # Step 9: Create chart
    print("\nGenerating population trend chart...")
    
    # Create predictions for chart (from first year to prediction year)
    all_years = list(range(valid_years[0], prediction_year + 1, 5))
    if prediction_year not in all_years:
        all_years.append(prediction_year)
    
    predicted_values = model.predict(np.array(all_years).reshape(-1, 1))
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    
    # Plot actual data
    plt.plot(valid_years, valid_populations, 'go-', linewidth=2, markersize=8, label='Actual Population')
    
    # Plot prediction line
    plt.plot(all_years, predicted_values, 'b--', linewidth=2, label='Predicted Trend')
    
    # Mark the prediction point
    plt.plot(prediction_year, predicted_population, 'r*', markersize=20, label=f'Prediction for {prediction_year}')
    
    # Formatting
    plt.xlabel('Year', fontsize=12, fontweight='bold')
    plt.ylabel('Population', fontsize=12, fontweight='bold')
    plt.title(f'Population Trend and Prediction for {city_row["City"]}', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Format y-axis to show millions
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1_000_000:.1f}M'))
    
    plt.tight_layout()
    plt.show()
    
    print("\nChart displayed successfully!")
    print("=" * 50)