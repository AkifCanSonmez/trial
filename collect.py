import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Configure Chrome optionss
chrome_options = Options()
chrome_options.binary_location = '/usr/bin/chromium'
chrome_options.add_argument('--headless')  # Set headless mode to True

# Install ChromeDriver and configure service
service = Service(ChromeDriverManager().install())

# Create a Chrome driver instance with the specified options
driver = webdriver.Chrome(service=service, options=chrome_options)


# Initializee Chrome driver with configured service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google Images and search for "banana"
driver.get("https://images.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("apple")
search_box.send_keys(Keys.RETURN)

# Ensure the dataset directory exists
dataset_path = 'dataset/muz'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# List all files in the dataset directory
existing_files = [f for f in os.listdir(dataset_path) if os.path.isfile(os.path.join(dataset_path, f))]

# Filter files that follow the naming convention 'image_X.png' and extract their indices
existing_indices = [int(f.split('_')[1].split('.')[0]) for f in existing_files if 'image_' in f and f.endswith('.png')]

# Determine the starting index for new files
starting_index = max(existing_indices) + 1 if existing_indices else 0

# Scrape images
for i in range(starting_index, starting_index + 5):  # Change the range as needed
    # Logic to load and save images goes here, including scrolling if necessary
    # For simplicity, here we're just using a placeholder for the actual image saving logic
    screenshot_path = os.path.join(dataset_path, f'image_{i}.png')
    driver.save_screenshot(screenshot_path)  # This would be replaced with actual image saving logic
    print(f'Saved screenshot to {screenshot_path}')
    time.sleep(2)  # Be respesctful in your scraping

driver.quit()
