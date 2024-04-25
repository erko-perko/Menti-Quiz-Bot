# Menti-Quiz-Bot

## Overview
The Mentimeter Quiz Bot is a Python script that automates interaction with Mentimeter quizzes. It uses Selenium for web automation to fetch quiz questions and possible answers from a Mentimeter quiz page, and integrates with OpenAI's GPT-4-turbo API to determine the most likely correct answer.

## Features
- **Web Scraping**: Utilizes Selenium to interact with web elements on the Mentimeter quiz page.
- **AI Integration**: Uses OpenAI's GPT-4-turbo model to intelligently answer quiz questions.
- **Automatic Answer Selection**: Automatically selects the correct answer based on AI's recommendation.

## Prerequisites
Before you can run the Mentimeter Quiz Bot, you need to install the following:
1. **Install Python**
If you haven't already installed Python, download and install it from python.org. Make sure to add Python to your PATH during installation if you're using Windows.

2. **Obtain an OpenAI API Key**
You need an API key from OpenAI to use their models:

Go to OpenAI’s API platform and sign up or log in.
Once logged in, navigate to the API keys section and generate a new key.

3. **Obtain Menti Quiz URL**
Ask the presenter for the link to the Menti quiz.

## Setup
Follow these steps to set up the Mentimeter Quiz Bot on your local machine:

1. **Clone the Repository**
```bash
git clone https://github.com/erko-perko/mentimeter-quiz-bot.git
cd mentimeter-quiz-bot
```

2. **Set Up a Virtual Environment (Optional but Recommended)**
Using a virtual environment helps manage dependencies for different projects and keeps your global installation clean. Here’s how you can set up one:

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Required Libraries**
You'll need to install selenium, webdriver-manager, and requests. You can install these using pip:
```bash
pip install selenium webdriver-manager requests
```
- **Selenium**: Automates the web browser.
- **WebDriver-Manager**: Handles the driver for the browser (in this case Chrome).
- **Requests**: Makes HTTP requests (used to communicate with the OpenAI API).

## Configuration
To configure the script for different quizzes or environments, modify the following variables in the **menti_quiz_bot.py** script:

**QUIZ_URL**: URL of the Mentimeter quiz.
**OPENAI_API_KEY**: Your OpenAI API key (ensure this is kept secure).

## Usage
To run the Mentimeter Quiz Bot, execute the following command in the project directory:

On Windows:
```bash
python menti_quiz_bot.py
```
On macOS and Linux:
```bash
python3 menti_quiz_bot.py
```
## Contribution

### Getting Started
- Fork the repository and clone it locally.
- Configure your repository to track upstream changes.
- Create a new branch for each feature or improvement.

### Submitting Changes
- Push your changes to your fork.
- Open a pull request to the main repository.
- Provide a descriptive title and summary for your pull request.
- Link any relevant issues or discussions.

*Thank you for using or contributing to the Mentimeter Quiz Bot!*

[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?hosted_button_id=VN2Y3KTX28JMC)
<a href="https://twitter.com/intent/tweet?text=Check+out+this+repository!&url=https%3A%2F%2Fgithub.com%2Ferko-perko%2FMenti-Quiz-Bot&hashtags=github+menti+openai+gpt&original_referer=http%3A%2F%2Fgithub.com%2F&tw_p=tweetbutton" target="_blank">
  <img src="http://jpillora.com/github-twitter-button/img/tweet.png"
       alt="tweet button" title="Check out this repository!"></img>
</a>
