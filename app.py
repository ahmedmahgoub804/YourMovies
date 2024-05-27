from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from help import lookup, lookmovie, search
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///movies.db")

@app.route("/")
def index():

    # Get all movies data
    data = [
        {
            "name":"Top Rated",
            "value": lookup("top_rated","1"),
            "type": "top_rated"
        },
        {
            "name":"Popular",
            "value": lookup("popular","1"),
            "type": "popular"
        },
        {
            "name":"Now Playing",
            "value": lookup("now_playing","1"),
            "type": "now_playing"
        },
        {
            "name":"Upcoming",
            "value": lookup("upcoming","1"),
            "type": "upcoming"
        }
    ]
    return render_template("index.html",data=data)


@app.route("/allmovies")
def allmoives(): 

    # Get request data 
    type = request.args.get("type")
    page = request.args.get("page", "1")
    
    # Get movies from api
    data = lookup(type,page)

    # Making sure not to pass the number of pages
    if int(page) > 500 or not data:
        return redirect(f"/allmovies?type={type}")

    return render_template("allmovies.html",data=data,type=type,page=page,int=int)


@app.route("/movie")
def moive():
    
    # Get request Data
    id = request.args.get("id")

    # Get movie from api
    data = lookmovie(id)

    # Know if movie already in the watchlist
    watched = 0
    if session.get("user_id") != None:
        watched = db.execute("select * from history where user_id=? and movie_id = ?",session["user_id"],id)

    return render_template("movie.html",data=data,watched=watched)


@app.route("/search")
def searching():

    # Get the search query 
    query = request.args.get("query")
    page = request.args.get("page", "1")
    
    # Get the matched movies
    data = search(query,page)

    if not query:
        return redirect(f"/")
    # Making sure not to pass the number of pages
    if int(page) > 500 or not data:
        return redirect(f"/search?query={query}")
    
    return render_template("allmovies.html",data=data,query=query,page=page,int=int)   


@app.route("/add", methods=["GET", "POST"])
def add():


    if request.method == "POST":
    
        # Add movie to watchlist
        id = request.form.get("id")
        db.execute("INSERT INTO history (user_id,movie_id) VALUES (?,?)", session["user_id"],id)
    else:

        # Remove from watchlist
        id = request.args.get("id")
        db.execute("DELETE FROM history WHERE user_id=? and movie_id=?", session["user_id"],id)
    
    return redirect("/watchlist")

@app.route("/watchlist")
def watchlist():
    
    # Get all movies in the user watchlist
    movies = db.execute("select movie_id AS id from history where user_id=?",session["user_id"])
    
    # Making a data structure of it to be able to show in allmovies.html
    data = []
    for i in movies:
        chunk = lookmovie(i["id"])
        data.append(chunk)

    return render_template("allmovies.html",data=data,int=int,page=1)

@app.route("/login", methods=["GET", "POST"])
def login():

    error = request.args.get("q")
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return redirect("/login?q=Please Enter Username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return redirect("/login?q=Please Enter Password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return redirect("/login?q=Invalid Login")
        
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html",error=error)



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    
    error = request.args.get("q")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")
        checkUser = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Check for validation
        if not username or not password or not cpassword:
            return redirect("/register?q=Please Fill All Data")
        if not (password == cpassword):
            return redirect("/register?q=Passwords Did Not Match")
        if not (len(checkUser) == 0):
            return redirect("/register?q=Username Is Taken")

        # Add user to the database
        db.execute("INSERT INTO users (username , hash) VALUES (? , ?)", username, generate_password_hash(password))
        
        # Log the user in
        session["user_id"] = db.execute("SELECT * FROM users WHERE username = ?", username)[0]["id"]
        
        return redirect("/")

    return render_template("register.html",error=error)