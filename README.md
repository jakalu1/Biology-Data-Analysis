# Time Series Data Analysis
with Pandas, Matplotlib, and Linear Regression

This project demonstrates how to perform basic time series analysis and predictive modeling using Python's pandas, matplotlib, and scikit-learn libraries.

Functionality:

1. Data Generation:
* The script generates a dataset that contains dates for the entire year of 2022 and associates a sequential value with each day (e.g., January 1st = 1, January 2nd = 2, ... December 31st = 365).
* The dataset is saved as a CSV file named date_metadata.csv in a specified directory.

2. Time Series Visualization:
* The saved data is loaded from the CSV file.
* A line plot is generated to visualize the daily values over time using matplotlib.

3. Predictive Analysis:
* A Linear Regression model is used to predict future values for the next 30 days based on the historical data.
* The actual and predicted values are plotted on a graph to show the time series and forecasted data.

4. Files:
* date_metadata.csv: The generated file containing the date-related metadata for the year 2022.

5. Libraries Used:
* pandas: For generating, organizing, and managing the dataset.
* matplotlib: For visualizing the time series data.
* scikit-learn: For building a Linear Regression model to predict future values.

6. Steps to Run:
a. Ensure the required libraries (pandas, matplotlib, and scikit-learn) are installed.
b. Run the script to generate the dataset and save it as a CSV file.
c. The script then loads the CSV, performs time series visualization, and uses Linear Regression to predict future values.

7. Code Overview:
* Data Creation: Generates a date range for 2022 and associates a sequential value for each day.
* CSV Export: Saves the DataFrame as a CSV file in the specified file path.
* Visualization: Displays the actual time series data using a line plot.
* Prediction: Uses Linear Regression to predict and visualize future values for the next 30 days.

**Important Notes:**
* Please note that around line 13 of metadatacreator.py and around line 9 of timeseriesanalysis.py, the file paths used must be specific to your system for saving and loading the CSV file.
