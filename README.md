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
## Method to Run on Computer/Laptop

**Prerequisites:**

* **A terminal or command prompt:** This is where you'll run the commands. You can use the default terminal on your operating system:
    * **Windows:** Command Prompt or PowerShell
    * **macOS:** Terminal
    * **Linux:**  Usually Bash or Zsh

* **Python 3.7 or higher:**
    * **Windows:** Download from [python.org](https://www.python.org/downloads/) and run the installer.
    * **macOS:**
        ```bash
        brew install python3 
        ```
    * **Linux (Ubuntu/Debian):**
        ```bash
        sudo apt-get update
        sudo apt-get install python3.7 
        ```

* **Node.js and npm:**
    * **Windows/macOS:** Download from [nodejs.org](https://nodejs.org/) and run the installer.
    * **Linux (Ubuntu/Debian):**
        ```bash
        sudo apt-get update
        sudo apt-get install nodejs npm
        ```

* **Git:** 
    * **Windows/macOS:** Download from [git-scm.com](https://git-scm.com/) and run the installer.
    * **Linux (Ubuntu/Debian):**
        ```bash
        sudo apt-get update
        sudo apt-get install git
        ```

**Steps:**

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

5.  **Install Flask and Meta API:**

    ```bash
    pip install Flask meta-ai-api 
    ```

6.  **Install the JavaScript dependencies:**

    ```bash
    npm install linkedin-auto-poster 
    ```

7.  **Run the Flask application:**

    ```bash
    python app.py
    ```

8.  **Open your web browser and go to the provided address** (usually `http://127.0.0.1:5000/`) to access the application.


## Deploying to a Cloud Server

For more reliable access, persistent storage, and better performance, consider deploying your Flask application to a cloud server:

*   **Popular Cloud Platforms:** Heroku, PythonAnywhere, AWS, Google Cloud
*   **Deployment Guides:** Search for "deploy Flask to [cloud platform name]" for specific instructions.