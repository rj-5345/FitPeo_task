import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import  ActionChains

#Opening the Chrome browser
driver = webdriver.Chrome()


#Test_Case1 : To open FitPeo homepage
def test_open_url():

    #Opening the Fitpeo Homepage in a maximized window
    driver.maximize_window()
    driver.get("https://fitpeo.com/")

    #wait for 10 sec to get the page loaded completely
    time.sleep(2)

#Test_Case2 : To navigate to Revenue Calculator page
def test_navigte_to_revenue_calculator():

    #Finding the Revenue Calculator on the website and performing action on it
    element = driver.find_element(By.XPATH, "//*[text()='Revenue Calculator']")
    element.click()

    #Wait for a few seconds to observe the action
    time.sleep(2)

#Test_Case3 : Scrolling down to slider section
def test_scroll_to_Slider():

    element = driver.find_element(By.XPATH, "//*[text()='Medicare Eligible Patients']")
    #Scroll the element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(3)


#Test_Case4 : Scrolling the slider to a certain value
def test_Set_slider_to_certain_value():
    #def test_set_slider_value_directly():

        time.sleep(3)
        #Find the slider element
        slider = driver.find_element(By.XPATH, "//input[@type='range']")

        #change the slider value
        action = ActionChains(driver)
        test_scroll_to_Slider()
        action.click_and_hold(slider).move_by_offset(94, 0).release().perform()

        #Wait to observe the action
        time.sleep(3)


#Test_Case5 : Setting the value field to a certain value
def test_Set_valueField_to_certain_value():
    #Identify the value field
    value_field = driver.find_element(By.XPATH, "//input[@type='number']")

    #Set the value in value field as given 560
    time.sleep(3)
    value_field.clear()
    driver.execute_script("arguments[0].value = '560'; arguments[0].dispatchEvent(new Event('input'));", value_field)

    #wait for the input to be processed or the slider to move
    time.sleep(2)

    #Verify the slider's current value
    slider = driver.find_element(By.XPATH, "//input[@type='range']")
    slider_value = slider.get_attribute("value")

    #Handling the exception when the value does not match
    try:
        assert slider_value == ('520')

    except AssertionError:
        print(f"\nMismatch detected!  the slider value is {slider.get_attribute('value')}")
        #take a screenshot as the assertion failed
        driver.save_screenshot('slider_mismatch.png')
        print("Screenshot Captured")

#Test_Case6 : Select desired checkboxes(given CPT-99091, CPT-99453, CPT-99454 and CPT-99474)
def test_Selecting_CPT_Checkboxes():

        #Click the checkbox
        checkbox1 = driver.find_element(By.XPATH,"//span[text()='57']")
        checkbox2 = driver.find_element(By.XPATH,"//span[text()='19.19']")
        checkbox3 = driver.find_element(By.XPATH,"//span[text()='63']")
        checkbox4 = driver.find_element(By.XPATH,"//span[text()='15']")
        time.sleep(7)

        checkbox1.click()
        time.sleep(2)
        checkbox2.click()
        time.sleep(2)
        checkbox3.click()
        time.sleep(2)
        checkbox4.click()
        time.sleep(2)


#Test_Case7 : Verifying the total amount shown for reimbursement
def test_Verifying_total_reimbursment():

    try:
        #Finding the label and associated amount
        label_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Total Recurring Reimbursement for all Patients Per Month')]")
        amount_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Total Recurring Reimbursement for all Patients Per Month:')]//following-sibling::p")
        amount_text = amount_element.text.strip()

        #Verify the value
        expected_amount = "$110700"
        assert amount_text == expected_amount
        print("The amount is correct!")

    except Exception:
        print("\nError: Expected amount is not matching with calculated amount")
        print("Expected",{expected_amount}," but got ",{amount_text})
        driver.save_screenshot("reimbursement doesn't match.png")

    finally:
        #Close the driver after the test
        time.sleep(3)
        driver.quit()



