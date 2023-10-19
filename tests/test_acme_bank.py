from applitools.selenium import Eyes, Target
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_log_into_bank_account(webdriver: Chrome, eyes: Eyes) -> None:

  webdriver.get("https://examples.sencha.com/extjs/7.7.0/examples/kitchensink/?classic#simple-combo")

  webdriver.switch_to.frame("examples-iframe")

  eyes.check(Target.window().fully().with_name("Full page"))

  dropdown = webdriver.find_element(By.CSS_SELECTOR, ".x-form-arrow-trigger-default")
  dropdown.click()

  eyes.check(Target.window().fully().with_name("Full page after click"))

