# Social Media Post Generator

This project provides a web application that uses Meta AI to generate social media posts. Users can log in, provide their job profile and industry, and generate relevant posts with a click of a button.

## Features

*   User login and registration
*   Profile management (update job profile and industry)
*   AI-powered post generation using Meta AI
*   Clean and modern UI inspired by the Meta AI website
*   Automated LinkedIn posting (using `linkedin-auto-poster`)

## Technologies Used

*   Python
*   Flask
*   HTML
*   CSS
*   JavaScript
*   Meta AI
*   SQLite
*   npm (for managing JavaScript packages)
*   linkedin-auto-poster (for automating LinkedIn posting)

## How to Run Locally

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Jazzhunks/socialmedia-post-generator.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd socialmedia-post-generator
    ```

3.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Install the JavaScript dependencies:**
    
    * Make sure you have Node.js and npm installed on your system.
    * Navigate to your project's root directory in the terminal.
    * Run the following command:

    ```bash
    npm install linkedin-auto-poster 
    ```

6.  **Run the Flask application:**

    ```bash
    python app.py
    ```

7.  **Open your web browser and go to the provided address** (usually `http://127.0.0.1:5000/`) to access the application.
