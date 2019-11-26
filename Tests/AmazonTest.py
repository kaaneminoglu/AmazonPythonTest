import time
from Common import WebElement

AmazonWebElement = WebElement.WebElement()
AmazonWebElement.getPage()
AmazonWebElement.signIn()
time.sleep(5)
AmazonWebElement.Search()
AmazonWebElement.AddList()
