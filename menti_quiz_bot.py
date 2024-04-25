import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def ask_openai(question, choices):
    headers = {
    	# Change OPENAI_API_KEY with your OpenAI API Key
        'Authorization': 'Bearer OPENAI_API_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Answer just with the correct choice.\nQuestion: {question}\nChoices: {choices}\n"}
        ]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)
    if response.status_code == 200:
        # Print the full response for debugging
        # print("Full API Response:", response.json())
        try:
            # Adjust this path to correctly parse the response from chat completions
            return response.json()['choices'][0]['message']['content'].strip()
        except KeyError:
            print("Error in API response format:", response.json())
            return None
    else:
        print("Failed to fetch answer from OpenAI:", response.status_code, response.text)
        return None

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the quiz URL
# Replace the QUIZ_URL with the correct one
driver.get("https://www.menti.com/QUIZ_URL")

try:
    # Locate the question element
    question_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1 span"))
    )
    question = question_element.text

    # Locate the answer elements
    answer_elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[aria-label]"))
    )
    answers = [element.get_attribute('aria-label') for element in answer_elements]
    
    # Use OpenAI API to determine the correct answer
    correct_answer_text = ask_openai(question, answers)
    if correct_answer_text:
        # Print the suggested correct answer
        print("Suggested Correct Answer:", correct_answer_text)
        # Find the matching answer and click it
        for answer_element in answer_elements:
            if correct_answer_text == answer_element.get_attribute('aria-label'):
                answer_element.click()
                break
finally:
    driver.quit()

