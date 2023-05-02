#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Krina Patel
Lauren Montion
Tara Joshi
DS 2500 PROJECT 2
DUE: 4/27/2022

"""

import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  
from statistics import mode
from collections import Counter


def filter_movies(df):
    
    # filter file for only movies (no shows)
    movies_df = df[df.type == 'Movie']
    
    # drop unnecessary columns
    dropped = movies_df.drop(["show_id"], axis = 1)
    
    return dropped

def filter_tomatoes(df):
    
    # filter file for only Netflix movies
    netflix_df = df[df.Netflix > 0]

    # drop unnecessary columns
    dropped = netflix_df.drop(["ID", "Type", "Disney+", "Prime Video", "Hulu", "Year"], axis = 1)
    
    return dropped

def merge_files(titles, tomatoes):
    
    # rename "title" column to match on both files to prepare to merge
    titles.rename(columns = {'title':'Title'}, inplace = True)
    
    # merge both files on the "title" column
    merged_data = titles.merge(tomatoes,on=["Title"])
    
    return merged_data

def split_date(df):
    
    # single out date column and separate out month column
    netflix_date = df[['date_added']].dropna()
    
    # separate month column
    netflix_date['Month'] = netflix_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])
    
    # merge both datasets back together-- adding new "Month" column to original 
    merged_data = netflix_date.merge(df,on=["date_added"])
    
    return merged_data

def top_movies(df):
    
    # rename rotten tomatoes column title
    df.rename(columns = {'Rotten Tomatoes':'RottenTomatoes'}, inplace = True)
    
    # filter out only the movies that were rated above 70/100 on rotten tomatoes
    top_movies = df[df.RottenTomatoes > "70/100"]
    
    return top_movies

def remove_dupes(df):
    
    # get rid of duplicate rows
    # get rid of duplicates
    nodupes_df = df.drop_duplicates(subset=['Title'])
    
    return nodupes_df

def ratings_dist(df):

    # show each unique value in rating column and counts of each rating
    rating_counts = df.groupby('rating')['Title'].nunique()

    return rating_counts

def graph_rating_dist(df):
    
    # graph bar graph showing the number of top rated netflix movies there 
    # are for each rating 
    plt.figure(figsize=(12,10))
    plt.title("Rating Distribution of Netflix Movies")
    rating_dist_plot = sns.countplot(x="rating", data=df, palette="Set2", order=df['rating'].value_counts().index[0:15])
    
    return rating_dist_plot

def months_dist(df):

    # show each unique value in rating column and counts of each rating
    release_months_counts = df.groupby('Month')['Title'].nunique()

    return release_months_counts

def graph_month_dist(df):
    
    # graph bar graph showing the number of top rated netflix movies there 
    # are released in each month
    plt.figure(figsize=(12,10))
    plt.title("Release Month Distribution of Netflix Movies")
    month_dist_plot = sns.countplot(x="Month", data=df, palette="Set2", order=df['Month'].value_counts().index[0:15])
    
    return month_dist_plot

def graph_country_dist(df):

    # show number of movies produces in top 5 netflix movie producing countries 
    # & produce a bar graph that shows how many movies the top countries have
    # produced.
    
    # turn country column into a list 
    list_of_countries = df["country"].to_list()
        
    # find the mode
    # country producing the most movies
    most_produced_movies = mode(list_of_countries)
    print("the country that produces the most movies on Netflix is:\n", most_produced_movies)
    
    
    # sort list_of_countries by frequency
    list_of_frequencies = [item for items, c in Counter(list_of_countries).most_common()
                                          for item in [items] * c]

    # remove duplicates from frequencies list
    country_lst = []
    for i in list_of_frequencies:
        if i not in country_lst:
            country_lst.append(i)
            
    # from cleaned frequencies list, take top 5 countries
    new_country_lst = country_lst[:5]
    print("the top 5 countries (most to least) producing most Netflix movies are:\n", new_country_lst)
    
    # count & print the number of movies produced in each of the top 5 countries
    
    country1movies = df['country'].value_counts()[new_country_lst[0]]
    print("the number of movies produced in", new_country_lst[0], "is", country1movies)
    
    country2movies = df['country'].value_counts()[new_country_lst[1]]
    print("the number of movies produced in", new_country_lst[1], "is", country2movies)
    
    country3movies = df['country'].value_counts()[new_country_lst[2]]
    print("the number of movies produced in", new_country_lst[2], "is", country3movies)
    
    country4movies = df['country'].value_counts()[new_country_lst[3]]
    print("the number of movies produced in", new_country_lst[3], "is", country4movies)
    
    country5movies = df['country'].value_counts()[new_country_lst[4]]
    print("the number of movies produced in", new_country_lst[4], "is", country5movies)
    
    # filter dataset for only rows from top 5 countries
    new_country_df = df[df['country'].isin(new_country_lst)] 

    # plot bar graph showing number of netflix movies released in each of the top 
    # 5 countries using filtered dataset
    plt.figure(figsize=(12,10))
    plt.title("Release Country Distribution of Netflix Movies")
    country_dist_plot = sns.countplot(x="country", data=new_country_df, palette="Set2", order=new_country_df['country'].value_counts().index[0:15])
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    
    return country_dist_plot




def avg_durations(df):
        
    # plot line graph for movie durations
    
    # separate time and "min" from duration column 
    # make new column for only "min" to prep to do mean calculation
    d_list = []

    for durations in df["duration"]:
        split = durations.split(" min")[0]
        split2 = float(split.strip())
        d_list.append(split2)

    df["duration_min"] = d_list
    
    # find average from new duration column
    duration_sum = df["duration_min"].sum()
    duration_mean_min = duration_sum / len(df)
    duration_mean_hours = duration_mean_min / 60

    print(f"The mean duration of Netflix movies rating 70/100 or above on Rotten Tomatoes is "
      f"{duration_mean_min} minutes, or {duration_mean_hours} hours.")
    
    return df

def plot_durations(df):
    
    # filter dataset for two columns needed for duration line plot
    new_df = df[['release_year', 'duration_min']]
    
    # make separate figure
    plt.figure()
    
    # plot lineplot for release year v movie duration 
    sns_plot = sns.lineplot(x="release_year", y="duration_min", data = new_df).set(title = "Release Year Vs. Movie Duration", 
                                                xlabel = "Release Year",
                                                ylabel = "Movie duration (in minutes)")
    return sns_plot


def main():
    
    # open netflix titles dataset
    netflix_df = pd.read_csv('netflix_titles.csv')
    
    # filter titles dataset for only movies - don't want to work with the shows
    titles_filtered = filter_movies(netflix_df)
    
    # open rotten tomatoes dataset
    tomatoes_df = pd.read_csv('MoviesOnStreamingPlatforms.csv')
    
    # remove all rows with movies not on netflix, and unnecessary columns
    # from tomatoes dataset
    tomatoes_filtered = filter_tomatoes(tomatoes_df)
    
    # merge the files
    netflix_tomatoes_merged = merge_files(titles_filtered, tomatoes_filtered)
    
    # split date column to take out month
    netflix_tomatoes_w_month_col = split_date(netflix_tomatoes_merged)

    # only looking at top rated movies (over 70/100)
    top_movies_netflix = top_movies(netflix_tomatoes_w_month_col)
    
    # remove duplicate rows
    # get rid of duplicates
    netflix_tomatoes_final_df = remove_dupes(top_movies_netflix)
    
    # number of netflix movies in each rating category
    rating_distribution = ratings_dist(netflix_tomatoes_final_df)    
    print("the rating distribution of Netflix movies is:\n", rating_distribution)
    
    # graph rating distribution plot
    graph_rating_dist(netflix_tomatoes_final_df)
    
    # number of netflix movies released in each month distribution
    month_distribution = months_dist(netflix_tomatoes_final_df)
    print("the release month distribution of Netflix movies is:\n", month_distribution)
    
    # graph month distribution plot
    graph_month_dist(netflix_tomatoes_final_df)
    
    # country distribution graph & number of movies produced in the top 5 countries  
    graph_country_dist(netflix_tomatoes_final_df)

    # find average length of best rated movies
    duration_df = avg_durations(netflix_tomatoes_final_df)
    
    # graph line plot of durations
    plot_durations(duration_df)
    

main()