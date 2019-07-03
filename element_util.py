"""
WebDriverWait:
  wait模块的WebDriverWait类是显性等待类
  __init__:
    driver: 传入WebDriver实例，
    timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）
    poll_frequency: 调用until或until_not中的方法的间隔时间，默认是0.5秒
    ignored_exceptions: 忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，
        则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有NoSuchElementException。
        
  until:
    method: 在等待期间，每隔一段时间（__init__中的poll_frequency）调用这个传入的方法，直到返回值不是False
    message: 如果超时，抛出TimeoutException，将message传入异常
    
  until_not:
    与until相反，until是当某元素出现或什么条件成立则继续执行，
    until_not是当某元素消失或什么条件不成立则继续执行，参数也相同，不再赘述
    
    
expected_conditions:
  selenium.webdriver.support.expected_conditions（模块）
  
  以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’) 
  顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行 
  presence_of_element_located 
  presence_of_all_elements_located
  
  
  以下三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement 
  第一个和第三个其实质是一样的 
  visibility_of_element_located 
  invisibility_of_element_located 
  visibility_of
  
  以下两个条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value 
  text_to_be_present_in_element 
  text_to_be_present_in_element_value
  
  以下条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement 
  frame_to_be_available_and_switch_to_it

  以下条件判断是否有alert出现 
  alert_is_present

  以下条件判断元素是否可点击，传入locator 
  element_to_be_clickable

  以下四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组 
  第三个传入WebElement对象以及状态，相等返回True，否则返回False 
  第四个传入locator以及状态，相等返回True，否则返回False 
  element_to_be_selected 
  element_located_to_be_selected 
  element_selection_state_to_be 
  element_located_selection_state_to_be

  最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了 
  staleness_of

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.implicitly_wait(10)


def wait_element_is_disappear(driver, by):
	"""
	wait for elment to disappear
	:param driver:
	:param by: 传入参数是元组类型的locator 如：(By.ID,"KW")
	:return:True or False
	"""
	flag = None
	try:
		is_disappeared = WebDriverWait(driver, 30, 0.5, (ElementNotVisibleException)). \
			until_not(lambda x: x.find_element(*by).is_displayed())
		if not is_disappeared:
			flag = True
			return flag
	except Exception as e:
		flag = False
	return flag


def wait_element_is_appear(driver, by):
	flag = None
	try:
		is_appeared = WebDriverWait(driver, 30, 0.5, (ElementNotVisibleException)). \
			until(lambda x: x.find_element(*by))
		if is_appeared:
			flag = True
		return flag
	except Exception as e:
		flag = False
	return flag


def wait_element_clickable(driver, by):
	flag = None
	try:
		boolean = WebDriverWait(driver, 30, 0.5). \
			until(EC.element_to_be_clickable(by))
		if boolean:
			flag = True
		return flag
	except Exception as e:
		flag = False
	return flag
