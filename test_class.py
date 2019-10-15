

# Import the 'modules' that are required for execution
 
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
#Fixture for Firefox
#@pytest.fixture(scope="class")
#def driver_init(request):
    #ff_driver = webdriver.Firefox()
    #request.cls.driver = ff_driver
    #yield
    #ff_driver.close()
 
#Fixture for Chrome
#@pytest.fixture(scope="class")
#def chrome_driver_init(request):
    #chrome_driver = webdriver.Chrome()
    #request.cls.driver = chrome_driver
    #yield
    #chrome_driver.close()


 
#@pytest.mark.usefixtures("driver_init")
#class BasicTest:
    #pass
#class Test_URL(BasicTest):
        #def test_open_url(self):
            #self.driver.get("https://weathershopper.pythonanywhere.com/")
            #print(self.driver.title) 
            #sleep(5)

#@pytest.mark.usefixtures("chrome_driver_init")
#class Basic_Chrome_Test:
    #pass
#class Test_URL_Chrome(Basic_Chrome_Test):
        #def test_open_url(self):
            #self.driver.get("https://weathershopper.pythonanywhere.com/")
            #print(self.driver.title)
            #sleep(5)



# Import the 'modules' that are required for execution
 
#Fixture for Firefox
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
 
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://weathershopper.pythonanywhere.com/")
            self.driver.save_screenshot("C:\\Users\\Rahul Bhave Qxf2\\code\\rahul-qxf2\\pytest_weathershopper\\screenshots\\WeatherShopper.png")
            print(self.driver.title)
            sleep(5)

    
