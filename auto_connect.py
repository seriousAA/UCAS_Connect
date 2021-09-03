from selenium import webdriver
import time
import threading

username='202028009029004' # modify it
password='**********' # modify it
driver_path='/mnt/Research/Sele/chromedriver' # modify it, must use absolute path
record_path='/mnt/Research/Sele/out.log' # modify it, must use absolute path

global timer
global cnt

def erase_record():
    f = open(record_path, 'r+')
    f.seek(0)
    f.truncate()

def check_connection():
    global cnt
    cnt+=1
    if cnt>50000:
        erase_record()
        cnt=0
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    try:
        client = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
        # client.set_window_position(20,40)
        # client.set_window_size(1100,700)
        client.get("http://124.16.81.61/srun_portal_pc?ac_id=1&theme=pro")
        client.implicitly_wait(1)

        def is_element_exist(id):
            s = client.find_elements_by_id(id)
            if len(s) == 1:
                return True
            return False

        if not is_element_exist('logout'):
            client.find_element_by_id('username').clear()
            client.find_element_by_id('password').clear()
            client.find_element_by_id('username').send_keys(username)
            client.find_element_by_id('password').send_keys(password)
            client.find_element_by_id('login-account').click()
            time.sleep(0.5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " : Re Connect.")
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " : Do nothing.")

        client.quit()
        global timer
        timer = threading.Timer(60, check_connection)  # every 60s check the connection
        timer.start()
    except Exception as e:
        print(e)
        timer = threading.Timer(10, check_connection)  # every 60s check the connection
        timer.start()

if __name__ == '__main__':
    cnt=0
    check_connection()
