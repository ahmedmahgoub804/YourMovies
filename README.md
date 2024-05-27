# YOUR Movies
#### Video Demo:  https://www.youtube.com/watch?v=RoQxj_zzEjc
#### Description:
The project is a web App use Movies database to have data of all the movies and show it
You can explore the popular, Top Rated, Now Playing and Upcoming movies and look at thousands of movies
You can also search for a movie using its name 
if you logged in You will have access to a watch-list and you can add or remove movies from it anytime  
The project uses HTML, CSS, Bootstrap and JS in the front-end
The project uses Python in the back-end
and it uses sqlite commands to deal with the database

the static folder contain icon and the css file
the templates folder contains html files:
    layout.html: the main build of the site which exist in all pages
    login.html and register.html 
    index.html: which contain the home page
    allmovies.html: which contain all the site sections like popular, upcoming and the search part .....
    movie.html: contain the movie data

app.py:
    containing the back-end functionality of the site
    the program uses Flask, redirect, render_template, request, session
    and it uses werkzeug.security to make sure that every password stay hashed

    it uses session to keeps track of users to make sure every user gets its watchlist

    the app has many routes:
        "/":
            leads to the homepage and it have data of different type of movies in it 
            it has 6 movies from every section

        "/allmovies":
            this route gets from the user the section he want to access and uses it to display the movies desired by the user
        
        "/movie":
            this route is used to get from the user the id of the movie and then give the user access to all its details

        "/search":
            this route is used when the uses the search in the navbar and give back the movies that got from the searcing

        "/watchlist":
            this route is used for every user to get the data of its watch list from the database
        
        "/login":
            this route is used from the user to login with his user name and password so the user have more accessibility to the site functions
        
        "/logout":
            logs the user out of the site

        "/register":
            this route is used from the new users to register a new user account

help.py:
    contain functions that we use to talk to the api database and export these functions to app.py

    it includes three functions that deals with the api database

    the first one is Lookup
        this function gets data of the movies by using the category and the page number 

    the second one is lookmovie
        this function gets the details of the movie by using the movie id in the api database

    the third one is search
        this function gets a string of words and send it to the api to get the data of all movies containing this words and back with the movies

movies.db:
    database have to tables one for the users data and the other for each user watch-list

requirements.txt:
    contains the requirements of the flask application that the app needs to be run