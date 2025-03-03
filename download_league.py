import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def execute_script_on_url(
        page_url,
        js_script,
        load_wait_time=1,
        script_wait_time=0
):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Stop browser windows to pop up.
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    try:
        # Open the web page and wait for it to load.
        driver.get(page_url)
        time.sleep(load_wait_time)
        # Execute the JS script and wait for it to finish.
        driver.execute_script(js_script)
        time.sleep(script_wait_time)
    finally:
        driver.quit()

if __name__ == '__main__':
    # download standings from most recent week
    url = "https://www.leaguesecretary.com/bowling-centers/orleans-bowling-center/bowling-leagues/fat-purse-tuesday-ii-spring/league/standings/136652"
    execute_script_on_url(url, "$(\"#gridBowlerList\").data(\'kendoGrid\').saveAsExcel()", 1, 1)