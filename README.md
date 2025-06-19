# US Bikeshare Data Analysis

## Date Created
June 19, 2025

## Description
This Python project analyzes bike share system data from three major US cities: Chicago, New York City, and Washington. The interactive program allows users to explore bike sharing patterns by:

- Filtering data by city, month, and day of the week
- Calculating various statistics including:
  - Most common times of travel
  - Popular stations and trip routes
  - Trip duration information
  - User demographics

## Getting Started

### Prerequisites
- Python 3.x
- pandas
- numpy

### Files Used
- `bikeshare.py`: Main Python script containing the analysis code
- `chicago.csv`: Dataset containing Chicago's bikeshare information
- `new_york_city.csv`: Dataset containing New York City's bikeshare information
- `washington.csv`: Dataset containing Washington's bikeshare information

### Running the Program
1. Clone this repository to your local machine
2. Navigate to the project directory
3. Run the script using Python:
   ```
   python bikeshare.py
   ```
4. Follow the interactive prompts to analyze the bikeshare data

## Project Structure
The project consists of several functions that work together to analyze the bikeshare data:
- `get_filters()`: Collects user input for city, month, and day preferences
- `load_data()`: Loads and filters the data based on user input
- Additional functions for statistical calculations and data analysis

## Credits
This project was completed as part of the Udacity Programming for Data Science Nanodegree program.

## Author
[Your Name]

## License
This project is licensed under the MIT License - see the LICENSE file for details

