import pandas as pd

# Generate sample date-related metadata
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-12-31'),
    'Value': [i for i in range(1, 366)]  # Sample values for each day
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the file path where (on your system) you want to save the CSV file
file_path = "C:/Users..."

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)
print(f"File saved to: {file_path}")
