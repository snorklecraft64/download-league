import time
import os

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
    prefs = {"download.default_directory" : os.path.dirname(os.path.realpath(__file__)), 
             'download.prompt_for_download': False,
             'download.directory_upgrade': True,
             'safebrowsing.enabled': True}
    #example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
    options.add_experimental_option("prefs",prefs);
    driver = webdriver.Chrome(service=service, options=options)
    try:
        # Open the web page and wait for it to load.
        driver.get(page_url)
        time.sleep(load_wait_time)
        # Execute the JS script and wait for it to finish.
        result = driver.execute_script(js_script)
        time.sleep(script_wait_time)
        return result
    finally:
        driver.quit()

if __name__ == '__main__':
    # download standings from most recent week
    url = "https://www.leaguesecretary.com/bowling-centers/orleans-bowling-center/bowling-leagues/fat-purse-tuesday-ii-spring/league/standings/136652"
    print(execute_script_on_url(url, "$(\"#gridStanding\").data(\'kendoGrid\').saveAsExcel()", 3, 1))