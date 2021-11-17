#source helpd to solve the  project :
#http://introtopython.org/while_input.html 
#https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data
#https://github.com/Aritra96/bikeshare-project
#https://github.com/philribbens


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }


#list of data (city,month,days)
month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_list  = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

 

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ('')
    while city not in CITY_DATA:
         print('Choose a city name:  chicago , new york city ,washington')
         city = input().lower()
         if city not in CITY_DATA:
             print('That\'s not vaild please try agin ...')
    # get user input for month (all, january, february, ... , june)
    month = ('')
    while month not in month_list:
         print('Choose a month or select all : all, january, february, \n march, april, may, june')
         month = input().lower()
         if month not in month_list:
             print('That\'s not vaild please try agin with ...')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ('')
    while day not in day_list:
         print('Choose a day or select all: all, monday, tuesday, wednesday,\n friday, saturday, sunday')
         day = input().lower()
         if day not in day_list:
             print('That\'s not vaild please try agin with ...')
   


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_list.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month

    common_month =df['month'].mode()[0]
    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]       
    # display the data 
    print(' The most common month : ',common_month)
    print(' \n The most common day  : ',common_day)
    print(' \nThe most common hour  : ',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station']
    mode_start = start_station.mode()[0]
    # display most commonly used end station
    end_station = df['End Station']
    mode_end = end_station.mode()[0]
    # display most frequent combination of start station and end station trip
    combo = (start_station + end_station).mode()[0]
    # display the data 
    print(' Popular used start station :',mode_start)
    print('\n Popular used end station ',mode_end)
    print('\n Frequent used station is ',combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is ',total_travel)


    # display mean travel time
    mean_travel_time =  df['Trip Duration'].mean()
    print('The average of travel time is :',mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
   
    start_time = time.time()
    # varibale we use in the loop 
    # Display counts of user types
    # loop to chick if city is chicago or new_york_city 
    print('\nUser type count:')
    count_of_user_type = print(df['User Type'].value_counts())

    try:
            print(df['Gender'].value_counts())
            print('Birth date count ')
            print('\nThe most commn year :',df['Birth Year'].mode()[0])
            print( '\nThe most recent year:',df['Birth Year'].max())
            print( '\nThe most earliest year: ',df['Birth Year'].min())
    except:
            print('No gender or Birth Date in  Washington ')


              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dispaly_head_rows(df):
    """
    this function take ask user if want to see
    the first 5 row of the data and output 
    will be in the dataframe (df)
    and ask him if he want to see another 5 row 
    """
    more = 0
    user_input = input('Enter  Yes for display the data or No for continue : ').lower()
    rows = df.head()
    while user_input == 'yes' :
        print('Display the first 5 rows',rows)
        break
    # loop to add  more rows the sturcture idea of loop from aritra96  source
    while user_input == 'yes':
        print('Want to view more data : ')
        more +=5
        second_input = input().lower()
        if second_input =='yes':
            print(df[more:more+5])
        else:
            break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dispaly_head_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
