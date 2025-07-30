# QA Automation Framework
## Setup

1. make python virtual enviroment (python -m venv nama_env)
2. activate the virtual env (with cmd=> nama_env/Scripts/activate.bat)
3. Install requirements in virtual enviroment: `pip install -r requirements.txt`
4. Download ChromeDriver (web) & Appium Server (mobile)

## Run Web Tests
pytest web_automation/tests/

## Run Mobile Tests
appium & pytest mobile_automation/tests/
