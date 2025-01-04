from flask import Flask, render_template, request, redirect, url_for, session, flash
from meta_ai_api import MetaAI
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database setup
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT NOT NULL UNIQUE, 
                       password TEXT NOT NULL, 
                       job_profile TEXT, 
                       industry TEXT)''')
    conn.commit()
    conn.close()

create_database()

# MetaAI initialization
ai = MetaAI()

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session["username"] = user[1]
            session["job_profile"] = user[3]
            session["industry"] = user[4]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.")  # Flash message for invalid login
            return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if "username" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        job_profile = request.form["job_profile"]
        industry = request.form["industry"]
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, job_profile, industry) VALUES (?, ?, ?, ?)", 
                           (username, password, job_profile, industry))
            conn.commit()
            conn.close()
            flash("Successfully registered!")  # Flash message for successful registration
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("Username already exists.")  # Flash message for duplicate username
            return redirect(url_for("register"))
    return render_template("register.html")

@app.route("/dashboard", methods=["GET", "POST"])  
def dashboard():  
    if "username" not in session:
        return redirect(url_for("index"))
    show_profile_form = False 
    return render_template("profile.html", username=session["username"], 
                           job_profile=session["job_profile"], industry=session["industry"],
                           show_profile_form=show_profile_form)  

@app.route("/update_profile", methods=["GET", "POST"])
def update_profile():
    if "username" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        job_profile = request.form["job_profile"]
        industry = request.form["industry"]
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET job_profile=?, industry=? WHERE username=?", 
                       (job_profile, industry, session["username"]))
        conn.commit()
        conn.close()
        session["job_profile"] = job_profile
        session["industry"] = industry
        flash("Profile updated successfully!")  # Flash message for successful update
        return redirect(url_for("dashboard")) 

    show_profile_form = True  
    return render_template("profile.html", username=session["username"], 
                           job_profile=session["job_profile"], industry=session["industry"],
                           show_profile_form=show_profile_form) 

@app.route("/generate_post", methods=["POST"])
def generate_post():
    if "username" not in session:
        return redirect(url_for("index"))

    #  No need to get 'content' from the form
    prompt = f"""Generate a new trending social media post for a {session['job_profile']} in the {session['industry']} industry. Focus only on real-world trends and do not include imaginary thoughts, include emojis and engage the audience. Do not write anything before or after the post.
    Example:
    AI in 2025: What's Next? 🤔
    As we step into the new year, I'm excited to see the impact of Artificial Intelligence on various industries! Did you know that: 
    1. AI-powered chatbots are expected to handle 85% of customer service interactions by 2025? 🤖
    2. The global AI market is projected to reach $190 billion by 2025, growing at a CAGR of 38.1%? 📈
    3. AI-driven content creation is becoming increasingly popular, with 61% of marketers already using AI for content generation? ✍️
    What are your thoughts on the future of AI? Share your predictions and insights! 👇
    #AI #ArtificialIntelligence #MachineLearning #Marketing #Technology #Innovation
    """
    response = ai.prompt(message=prompt)
    post_content = response["message"]
    return render_template("profile.html", username=session["username"], 
                           job_profile=session["job_profile"], industry=session["industry"], 
                           post_content=post_content, show_profile_form=False)

@app.route("/logout")
def logout():
    session.pop("username", None)  # Indent this line
    return redirect(url_for("index"))  # Indent this line

if __name__ == "__main__":
    app.run(debug=True)