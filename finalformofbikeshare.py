import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the name of the city: ").lower()
        if city not in ['chicago','new york city', 'washington']:
            print("!Please enter a valid city name")
            continue
        else:
            break
    print("Displaying data for: ", city)


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the name of month you want to filter by or all for no filtering: ").lower()
        if month not in ["all", "january", "february", "march", "april", "may", "june"]:
            print("!Please enter a valid month")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the name of day you want to filter by or all for no filtering: ").lower()
        if day not in ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
            print("!Please enter a valid day")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month

    df["day_of_week"] = df["Start Time"].dt.day_name()

    if month != "all":
       months = ["january", "february", "march", "april", "may", "june"]
       month = months.index(month) + 1
       df = df[df["month"] == month]
                                  
                                  
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    mc_month = df["month"].mode()[0]
    print("The most common month: " , mc_month) 
    

    # TO DO: display the most common day of week
    mc_Day = df["day_of_week"].mode()[0]
    print("The most common day of week: ", mc_Day)


    # TO DO: display the most common start hour
    mc_hour = df["hour"].mode()[0]
    print("The most common start hour: ", mc_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_startstation = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", mc_startstation)


    # TO DO: display most commonly used end station
    mc_endstation = df['End Station'].mode()[0]
    print("The most commonly used end station: ", mc_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    mf_combination = (df["Start Station"] +  ":"  + df["End Station"]).mode()
    print("The most frequent combination: ", mf_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt = df["Trip Duration"].sum()
    print("Displaying total travel time: ", ttt)


    # TO DO: display mean travel time
    mtt = df["Trip Duration"].mean()
    print("Displaying mean travel time: ", mtt)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype = df["User Type"].value_counts()
    print("Displaying counts of user types: ", usertype)


    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value.counts()
        print("Displaying counts of gender: ", gender)
    except:
        print("There is no gender column in Washington.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliestyear = df["Birth Year"].min()
        print("Earliest year of birth: ", earliestyear)
        mr_year = df["Birth Year"].max()
        print("Most recent year of birth: ", mr_year)
        mc_year = df["Birth Year"].mode()
        print("Most common year of birth: ", mc_year)
    except:
        print("There is no birth year column in Washington")
    while True:
        raw_data = input("Do you want to view some raw data? type yes or no").lower()
        if raw_data == "yes":
            sampl = df.sample(5)
            print(sampl)
            continue
        elif raw_data == "no":
            break
        else:
            print("!Please enter a valid answer")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    

def main():        
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
	main()

    
