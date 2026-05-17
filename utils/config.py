import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenshot_dir = "Screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
RESUME_DATA = os.path.join(BASE_DIR, "utils", "resumeData.json")
USERNAME = "potlapaduabdulrahim@gmail.com"
PASSWORD = "Nafirahim#@240125"
BASE_URL = "https://www.naukri.com/"
SKILL_COMPANY_DESIGNATION="Python,Java,Selenium,robotframework"
Location="Hyderabad"
PAGES_TO_APPLY=15
EXPERIENCE_YEARS=3
# RESUME_DATA="C:\\Users\\USER\\PycharmProjects\\NaukariAutomation\\utils\\resumeData.json"
