from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Optional: Specify path to chromedriver if needed
# Example: service = Service("C:/path/to/chromedriver.exe")
service = Service()  # uses default if chromedriver is in PATH

options = Options()
options.add_argument("--start-maximized")  # Optional: maximize window

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Example: Open Google
driver.get("https://www.google.com")

# Do something...
print(driver.title)

# Close the browser
driver.quit()
