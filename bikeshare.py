import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

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

    while (True):
        city = input("\nEnter the name of the city [chicago(ch)/new york city(ny)/washington(wa)]: ").lower()

        if city == 'ch':
            city = 'chicago'
        if city == 'ny':
            city = 'new york city'
        if city == 'wa':
            city = 'washington'

        if city not in ['chicago', 'new york city', 'washington']:
            print("\nInvalid city name! Please try again....")
        else:
            break;

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month = input("\nEnter the name of the month [all/january(jan)/february(feb)/march(mar)/april(apr)/may/june(jun)]: ").lower()

        if month == 'jan':
            month = 'january'
        if month == 'feb':
            month = 'february'
        if month == 'mar':
            month = 'march'
        if month == 'apr':
            month = 'april'
        if month == 'jun':
            month = 'june'

        if month not in ['all','january','february','march','april','may','june']:
            print("\nInvalid month name! Please try again....")
        else:
            break;

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day = input("\nEnter the day of week [all/sunday(sun)/monday(mon)/tuesday(tue)/wednesday(wed)/thursday(thu)/friday(fri)/saturday(sat)]: ").lower()

        if day == 'sun':
            day = 'sunday'
        if day == 'mon':
            day = 'monday'
        if day == 'tue':
            day = 'tuesday'
        if day == 'wed':
            day = 'wednesday'
        if day == 'thu':
            day = 'thursday'
        if day == 'fri':
            day = 'friday'
        if day == 'sat':
            day = 'saturday'

        if day not in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
            print("\nInvalid day name! Please try again....")
        else:
            break;

    print('-' * 40)
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
    df = pd.read_csv(f"{city.replace(' ', '_')}.csv")

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month, :]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day, :]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f"The most common month is: {df['month'].mode().values[0]}")

    # TO DO: display the most common day of week
    print(f"The most common day of the week: {df['day_of_week'].mode().values[0]}")

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour

    print(f"The most common start hour: {df['start_hour'].mode().values[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"The most common start station is: {df['Start Station'].mode().values[0]}")

    # TO DO: display most commonly used end station
    print(f"The most common end station is: {df['End Station'].mode().values[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['End Station']

    print(f"The most common start and end station combination is: {df['routes'].mode().values[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print(f"The total travel time is: {df['duration'].sum()}")

    # TO DO: display mean travel time
    print(f"The mean travel time is: {df['duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Count of user types: {df['User Type'].value_counts()}")

    # TO DO: Display counts of gender
    if city != 'washington':
        print(f"Count of gender:{df['Gender'].value_counts()}")

    # TO DO: Display earliest, most recent, and most common year of birth
        print(f"The earliest birth year is: {int(df['Birth Year'].min())}")

        print(f"The latest birth year is: {int(df['Birth Year'].max())}")

        print(f"The most common birth year is: {int(df['Birth Year'].mode().values[0])}")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)


def main():
    while(True):
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
