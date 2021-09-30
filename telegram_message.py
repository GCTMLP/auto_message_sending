from appium import webdriver

def send_message(desire_caps, socket, tel, mes):
  
    try:
        wd = webdriver.Remote(socket, desired_caps)
        wd.implicitly_wait(2)
        wd.find_elements_by_class_name('android.widget.TextView')[1].click()
        wd.find_elements_by_accessibility_id('New Message')[0].click()
        wd.find_elements_by_accessibility_id('Create New Contact')[0].click()
        elements_enter = wd.find_elements_by_class_name('android.widget.EditText')
        elements_enter[0].send_keys('1')
        wd.find_elements_by_class_name('android.widget.TextView')[1].click()
        wd.find_elements_by_accessibility_id('Search')[0].click()
        wd.find_elements_by_class_name('android.widget.EditText')[0].send_keys('russia')
        wd.find_elements_by_class_name('android.widget.TextView')[0].click()
        elements_enter[3].send_keys(tel)
        wd.find_elements_by_accessibility_id('Done')[0].click()
        wd.find_elements_by_class_name('android.widget.EditText')[0].send_keys(mes)
        wd.find_elements_by_accessibility_id('Send')[0].click()
        wd.back()
        wd.back()
        wd.back()
        return True
    except:
        return False

def main():
    desired_caps = dict(
        platformName = 'Android',
        deviceName = 'Android Emulator',
        platformVersion= '8.1',
        automationName= 'UiAutomator2',
        udid= '0.0.0.0:5557',
        unicodeKeyboard = True)
    socket = 'http://127.0.0.1:4723/wd/hub'
    tel = '79999999999'
    mes = 'hello'
    send_message(desire_caps, socket, tel, mes)

if __name__ == "__main__":
    main()