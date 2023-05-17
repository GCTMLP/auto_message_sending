from appium import webdriver

def send_message_wtsp(desire_caps, socket, tel, mes):
    """
    the function is intended for automated emulation of human actions
    for sending messages to the messenger whatsapp

    :param desire_caps: emulator parameters
    :param socket: emulator`s socket
    :param tel: recipient's phone number
    :param mes: message text
    :return: bool
    """
    wd = webdriver.Remote(socket, desire_caps)
    wd.implicitly_wait(2)
    wd.find_elements_by_class_name('android.widget.TextView')[2].click()
    try:
        wd.find_element_by_class_name('android.widget.ImageButton').click()
        wd.find_elements_by_id('com.whatsapp:id/contactpicker_row_name')[1]\
            .click()
        wd.find_elements_by_class_name('android.widget.EditText')[0]\
            .send_keys('1')
        wd.find_elements_by_class_name('android.widget.EditText')[2].\
            send_keys(tel)
        wd.find_element_by_id('com.android.contacts:id/editor_menu_save_button')\
            .click()
        wd.back()
        wd.find_elements_by_id('com.whatsapp:id/contactpicker_row_name')[2]\
            .click()
        wd.find_element_by_id('com.whatsapp:id/entry').click()
        wd.find_element_by_id('com.whatsapp:id/entry').send_keys(mes)
        wd.find_element_by_id('com.whatsapp:id/send').click()
        wd.back()
        wd.back()
        wd.back()
        wd.find_elements_by_class_name('android.widget.TextView')[3].click()
        wd.find_elements_by_class_name('android.widget.RelativeLayout')[2]\
            .click()
        wd.find_elements_by_id('com.google.android.dialer:id/contact_name')[1]\
            .click()
        wd.find_element_by_class_name('android.widget.ImageButton').click()
        wd.find_elements_by_id('android:id/title')[1].click()
        wd.find_element_by_id('android:id/button1').click()
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
    send_message_wtsp(desired_caps, socket, tel, mes)

if __name__ == "__main__":
    main()