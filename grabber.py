from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
#import time
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


def grab_book(url: str):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url=url)
        print(f"Connected successfully to {url}!")
    except:
        print("Failed!")
        driver.close()
    #try:
    element = driver.find_element(By.CLASS_NAME, "btn-user")
    #except :
    #    print(err)
    link = element.get_attribute("href").split("&")
    driver.close()
    driver.quit()
    
    print(link)
    correct_end = "ext=pdf"
    link[-1] = correct_end

    result_link = "&".join(link)
    return result_link
    




if __name__ == "__main__":
    url="https://ru.pdfdrive.com/Освой-самостоятельно-c-по-одному-часу-в-день-d183944321.html"
    grab_book(str(input("Enter")))
