# Trends_In_Top-Rated_Netflix_Movies
Python program that analyzes Netflix movies against Rotten Tomatoes ratings to conclude the ideal characteristics a movie should have to receive the most optimal rating and engagement

** works best in Anaconda Spyder **


# Problem Statement and Background

Netflix was founded by Marc Randolph and Reed Hastings in Scotts Valley, California in 1997.
When it first started, it was a movie rental company, and users ordered their movies on the
Netflix website to receive DVDs in the mail, then they would mail them back when they were
finished. Today, Netflix streams movies and shows online and has over 207 million paid
subscribers in over 190 countries worldwide. It has a range of TV series, documentaries, and
feature films across different genres, languages, and even its own original productions(Netflix
Originals). As of 2022, Netflix has 13,612 unique titles and has an estimated total viewer pool of
over 300 million worldwide. The company has also saved up to $1 billion a year via its
personalized recommendation engine. However, although Netflix seems very strong, successful,
and growing, it has lost more than one million subscribers to Disney Plus. By the end of 2021,
Netflix closed the year with 221.8 million subscribers – it fell short of the company’s forecast for
new subscribers in Q4, of 8.5 new million subscribers with 8.3 million subscribers.
Our problem statement reads, what characteristics a movie needed to get the most optimal
engagement on Netflix? By investigating the trends of successful Netflix movies (best rated), our
goal was to find the ideal conditions under which to release a movie on Netflix, defined by the
following metrics: maturity rating, length, release month, and country produced. Knowing this
information would help the company increase subscriber count by releasing more movies with
the best chance of optimal engagement, in turn increasing their revenue.

# Introduction to the Data
We used two different csv files in our project, and both came from Kaggle.com. We downloaded
them directly from the Kaggle website and used Google Sheets/Excel to open and read the data:

● “netflix_titles.csv”: contained a list of tv shows and movies available on Netflix as of
2019 (however it was updated in 2021); collected from Flixable, a third-party Netflix
search engine; included the column names: “show_id”, “type”, “title”, “director”, “cast”,
“country”, “date_added”, “release_year”, “rating”, “duration”, “listed_in”, and
“description”.

● “MoviesOnStreamingPlatforms.csv”: scraped from the Rotten Tomatoes website;
provided a list of ratings of all movies available on various streaming platforms (last
updated in 2021); it included the column names: “ID”, “Title”, “Year”, “Age”, “Rotten
Tomatoes”, “Netflix”, “Hulu”, “Prime Video”, “Disney+”, and “type”.

# Number of data points
We found two datasets and then merged them to make one containing all the necessary
information we would be using in our research. The first one we used is called
“netflix_titles.csv” and it contains 12 columns and 8810 rows. The second we used is called
“MoviesOnStreamingServices.csv” and it contains 10 columns and 9516 rows. When we merged
the data, we made a new csv called “NETFLIX_TOMATOES_FINAL.csv” and it contains 16
columns and 367 rows.

# Relevant Information from the Dataset
We made the new dataset, “NETFLIX_TOMATOES_FINAL.csv”, in order to have access to the
most relevant information. We started by filtering the “netflix_titles.csv” and
“MoviesOnStreamingServices.csv” files for only Netflix movies and dropped any unnecessary
columns. We then merged the two files by the movie titles, and from this dataset, we then further
filtered it to look at only those movies rated above 70/100 on Rotten Tomatoes. We used our
final, “NETFLIX_TOMATOES_FINAL.csv” to answer our problem statement. We were mostly
focused on the title of the movies, the country they were produced in, their maturity rating (G,
PG, etc.), their Rotten Tomatoes rating, and the date they were released on. These specific
columns helped us answer the following questions:
1. What is the average length of the top rated movies on Netflix?
2. Which country has the highest number of top movies produced?
3. What is the rating distribution of Netflix movies?
4. What month are the most/least movies released?
This helped us in crafting our recommendation for the best conditions under which to release a
movie on Netflix.

# Data Science Approaches
We used a wide range of topics we have covered in class in order to get a full scope of the data
we were working with and to completely answer our questions as accurately as possible. We first
implemented the pandas software library to clean up our data and produce clear data frames. In
order to use only the necessary information from both datasets, we merged the two data sets,
creating one data frame containing filtered information. We utilized counter objects as a subclass
of the collections module in Python to prepare our information to be graphed. To analyze our
data we used the Seaborn visualization library to plot all our findings, making new dataframes
for the rating distribution graph and the country production graph.
Results and Conclusions
The rating distribution of the top Netflix movies were
found to assess the optimal target audience for a “hit”
movie- a movie that would do well on rotten
tomatoes. The majority of the Netflix movies from
the dataset were TV-MA (34%), the next top ratings
being R (24%), TV-14 (14%), and PG-13 (14%). The
least amount of top rated Netflix movies was rated
TV-PG (6%), PG (5.5%), TV-G (1.1%), and G
(.55%). The visualization to the right demonstrates
these findings.
The release month distribution from the dataset was also found in order to assess the months
where the least and most movies were released. The months of September, October, November,
and December had the highest percentages of movies released (11%, 11%, 12%, 10%,
respectively), with November at the maximum. The month of February had the least percentage
of movies released, with a low 4%. The plot below was created to visualize this distribution.
Additionally, from most to least movies produced, the
countries producing the most Netflix movies from the
dataset were the United States, India, the United
Kingdom, the United Kingdom and the United States (in
combination), and Spain. The U.S. produced 48% of the
movies, whereas India produced 10%, a considerable
difference. To better understand this distribution, the plot
to the right was created.
In terms of mean duration, the average length of the movies on the dataset was about 110
minutes or 1.84 hours. To analyze how the lengths of top rated Netflix movies have changed over
time, the below visualization was created.
From this plot, it is clear that from about 1997 to
2005, there were sharp spikes in movie duration as
it drastically changed throughout the time period.
However, from about 2005 to 2020, this has leveled
out to about the same as it was in 1970. The length
decreases a bit in 2020 at about 105 minutes but
stays relatively steady, implying the average length
of movies found, 110 minutes, is a good estimation
of recent movie lengths as well.
From this information, it can be analyzed that the top movies on Netflix that are being assessed
on Rotten Tomatoes with 70/100 or above are mainly targeted toward older, more mature
audiences, as TV-MA and rated R appear the most frequently in the dataset. Additionally, movies
produced in the U.S. are more likely to be popular, suggesting this is the optimal location and
audience to target. The months of September, October, November, and December have the
highest percentages of movies released, so they may be the optimal time to release a movie as it
is the holiday season and more people are likely to be watching Netflix. Lastly, the average
length of about 110 minutes for top rated Netflix movies also suggests that for the most
engagement, movies should be a little bit less than two hours.
With all of these analyses in mind, for the most successful movie ratings, we would recommend
someone to produce a movie in the US targeted towards either an older teenage or adult audience
that is about two hours long, and release it during the holiday months/ season.

# Future Work
The results of our work are useful for movie production, writing, or marketing teams when they
are trying to have a successful film release on Netflix. With the information about optimal
audiences, release months, country of production, and movie duration, all taken from the Netflix
movies that are scored 70/100 or more on Rotten Tomatoes, these teams would be able to cater
their films to get high ratings.
Going forward, the next steps would be to analyze which genres on Netflix are rated the highest
on average, and create distribution visuals for this. This would be helpful for the same audience
who is looking to create a hit movie. Additionally, instead of using the top movies based on their
reviews, analyzing movies with the highest box office revenue would be an interesting
perspective to explore because lower ratings do not necessarily mean less profit, as some lower
rated movies have very high engagement. Doing the same analysis with more streaming
platforms would also be a useful next step for broadening the scope of our data.

# Works Cited
Alexander, Julia. “Rotten Tomatoes Scores Don’t Correlate to Box Office Success or Woes,
Research Shows.” Polygon, 11 Sept. 2017,
https://www.polygon.com/2017/9/11/16291038/rotten-tomatoes-scores-movies. Accessed
25 Apr. 2022.
Bhatia, Ruchi. “Movies on Netflix, Prime Video, Hulu and Disney+.” Kaggle,
https://www.kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disn
ey. Accessed 25 Apr. 2022.
Canales, Katie. “Meet the Average Netflix User, a Millennial Woman without a College Degree
Living in the American Suburbs Earning Less than $50,000 a Year.” Insider, 18 Sept.
2021,
https://www.businessinsider.com/typical-netflix-user-subscriber-demographic-millennialage-political-views-income-2021-9. Accessed 25 Apr. 2022.
niharika41298. “🔴Netflix Visualizations, Recommendation, EDA🍿.” Kaggle, 25 Feb. 2021,
https://www.kaggle.com/code/niharika41298/netflix-visualizations-recommendation-eda.
Accessed 25 Apr. 2022.
