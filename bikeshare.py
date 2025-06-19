import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_input(prompt, valid_options, error_message):
    """Helper function to get and validate user input."""
    user_input = input(prompt).lower()
    while user_input not in valid_options:
        print(error_message)
        user_input = input(prompt).lower()
    return user_input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # Get user input for city
    city = get_user_input(
        "Which city do you want to explore? Choose one:\nChicago\nNew York City\nWashington\n  ",
        CITY_DATA.keys(),
        "Invalid input! Please choose from: Chicago, New York City, or Washington"
    )
    
    # Get user input for month
    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    month = get_user_input(
        f"\nFilter {city}'s data by month?\nJanuary, February, March, April, May, June, or 'all': ",
        months,
        "Invalid input! Please choose a valid month or 'all'"
    )
    
    # Get user input for day
    days = ('saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all')
    day = get_user_input(
        f"\nFilter {city}'s data by day?\nEnter day name or 'all': ",
        days,
        "Invalid input! Please enter a valid day or 'all'"
    )
    
    print('-'*40)
    return city,month,day

#########################################################################################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe.
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # Filter by month if applicable.
    if month != 'all' :
        # Use the index of the months tuple to get the corresponding integer.
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = months.index(month) + 1
        
        # Filter by month to create the new dataframe.
        df = df[df['month'] == month]

    # Filter by day of week if applicable.
    if day != 'all' :
        # Filter by day of week to create the new dataframe.
        df = df[df['day'] == day.title()]
        
    
    return df

#########################################################################################
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel.

    Args:
        df (DataFrame): The DataFrame to analyze.
        month (str): The month to filter by, or "all".
        day (str): The day to filter by, or "all".
    """
    
    months = ('january', 'february', 'march', 'april', 'may', 'june')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculating the most common month:
    if month == 'all' :
        most_common_month = df['month'].mode()[0]
        print("The most common month: {}".format(months[most_common_month - 1]))
        
    # Calculating the most common day of week:
    if day == 'all' :
        most_common_day = df['day'].mode()[0]
        print("The most common day: ",most_common_day)
        
    # Calculating the most common start hour:
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour: ",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        df (DataFrame): The DataFrame to analyze.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculating the most commonly used start station:
    most_commonly_used_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station: ",most_commonly_used_start_station)
    
    # Calculating the most commonly used end station:
    most_commonly_used_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station: ",most_commonly_used_end_station)
    
    # Calculating the most frequent combination of start station and end station trip:
    df["Most Frequent Trip"] =  df["Start Station"] + "   >>   " + df["End Station"]
    most_frequent_trip = df["Most Frequent Trip"].mode()[0]
    print("The most frequent trip is: ",most_frequent_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        df (DataFrame): The DataFrame to analyze.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculating the total travel time:
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is: ",total_travel_time)

    # Calculating the average travel time:
    mean_travel_time =  df["Trip Duration"].mean()  
    print("The average travel time is: ",mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def user_stats(df):
    """Displays statistics on bikeshare users.

    Args:
        df (DataFrame): The DataFrame to analyze.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Extracting the unique columns :
    df_columns = df.columns
    
    # Calculating counts of user types:
    counts_of_user_types = df["User Type"].value_counts()
    print("The counts of user types: ",counts_of_user_types)
    
    # Evaluating & Calculating counts of gender:
    if 'Gender' in df_columns :
        counts_of_gender = df['Gender'].value_counts() 
        print("counts of gender: ", counts_of_gender)
    else :
        print("No availab data for gender in Washington! ")
              
    
    # Evaluating & Calculating earliest, most recent, and most common year of birth:
    if 'Birth Year' in df_columns :
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year =  df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        
        print("The earliest birth year: ",int(earliest_birth_year))
        print("The recent birth year: ",int(most_recent_birth_year))
        print("The most common year of birth: ",int(most_common_year_of_birth))
    else :
        print("No availab data for birth year in Washington! ")
              
       
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def display_raw_data(city):
    """
    Displays 5 lines of raw data at a time when prompted by the user.

    Args:
        (str) city - name of the city to display raw data from
    """
    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check...')
    
    start_index = 0
    
    while True:
        response = input("Would you like to see 5 rows of raw data? (yes/no): ").lower()
        
        if response == 'yes':
            print(df.iloc[start_index:start_index + 5])
            start_index += 5
            
            # Check if we've reached the end of the data
            if start_index >= len(df):
                print("No more data to display.")
                break
                
        elif response == 'no':
            print('\nThank you!')
            break
        else:
            print('Invalid input. Please enter "yes" or "no".')
                
#########################################################################################
def main():
    """
    Main function to run the bikeshare data analysis program.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('   THANK YOU   ')
            break


if __name__ == "__main__":
	main()