from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import password # for storing credentials
import pyautogui

chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.maximize_window()
driver.get("https://www.spotify.com/in/free/?utm_source=in-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_asia_in_premiumbusiness_highintent_brand+contextual-desktop+text+exact+in-en+google&ds_rl=1270915&gclid=EAIaIQobChMIvc6S75nw7QIVrJ1LBR0HRAAAEAAYASAAEgKaPfD_BwE&gclsrc=aw.ds")


driver.delete_all_cookies()
sleep(5)


def Sign_UP():

    """
    This function is used to sign up for Spotify Application.  

    """


    sleep(5)
    sign_up = driver.find_element(By.LINK_TEXT, "Sign up").click() 
    sleep(5)

    EMAIL = "instabottestingemail1@gmail.com"
    NICK_NAME = "Spotify Testing Bot"


    YEAR = 2000
    DAY = 28
    Month_name = "February"


    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()
    sleep(2)

    your_email = driver.find_element(By.ID, "email")
    your_email.send_keys(EMAIL)
    sleep(2)

    confirm_email = driver.find_element(By.ID, "confirm")
    confirm_email.send_keys(EMAIL)
    sleep(2)

    driver.execute_script("window.scrollBy(0,300)", "")
    sleep(2)


    passwrd = driver.find_element(By.ID, "password")
    passwrd.send_keys(password.PASSWORD)
    sleep(2)

    nick_name = driver.find_element(By.ID, "displayname")
    nick_name.send_keys(NICK_NAME)
    sleep(5)

    driver.execute_script("window.scrollBy(0,300)", "")
    sleep(2)

    year = driver.find_element(By.ID, "year")
    year.send_keys(YEAR)
    sleep(2)

    MONTH = Select(driver.find_element(By.ID, "month"))
    MONTH.select_by_visible_text(Month_name)

    day = driver.find_element(By.ID, "day")
    day.send_keys(DAY)

    driver.execute_script("window.scrollBy(0,200)", "")
    sleep(2)

    YOUR_GENDER = input("Enter your Gender (M/F/T) :: ")
    sleep(2)

    if YOUR_GENDER == "m" or YOUR_GENDER == "M" :
        MALE = driver.find_element(By.XPATH, "//*[@id='__next']/main/div[2]/form/div[6]/div[2]/label[1]/span[1]").click()

    elif YOUR_GENDER == "F" or YOUR_GENDER == "f":
        FEMALE = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[6]/div[2]/label[2]/span[1]').click()

    elif YOUR_GENDER == "T" or YOUR_GENDER == "t":
        TRANS = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[6]/div[2]/label[3]/span[1]').click()

    else:
        pass

    TERMS = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[7]/label/span[1]')
    TERMS.click()
    sleep(5)

    driver.execute_script("window.scrollBy(0,300)", "")
    


    pyautogui.alert("Please Solve reCAPTCHA puzzle!!!. You have 60 seconds.")
    sleep(60)

    # Re_captcha = driver.find_element(By.ID, 'recaptcha-anchor')
    # Re_captcha.click()
    # print("Please solve captcha query!!")
    # sleep(60)

    Sign_UP_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[9]/div/button')
    Sign_UP_btn.submit()


# Sign_UP()


def Login(x,y):

    """
    This function is used to Login for Spotify Application. After sign up from above step, all details are used there for login.   

    """


    sleep(2)

    login_btn = driver.find_element(By.LINK_TEXT, "Log in").click()
    sleep(5)

    user_name = driver.find_element(By.ID, 'login-username')
    user_name.send_keys(x)
    sleep(2)


    driver.execute_script("window.scrollBy(0,300)", "")

    pass_word = driver.find_element(By.ID, 'login-password')
    pass_word.send_keys(y)
    sleep(2)




    

    # Remember_me_Btn = driver.find_element(By.XPATH, '//*[@id="app"]/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label/span').click()
    # sleep(5)

    driver.execute_script("window.scrollBy(0,500)", "")

    LOGIN_BTN = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    sleep(10)

    driver.get("https://open.spotify.com/?_ga=2.11073460.1059300004.1609394928-1863048095.1609394928")
    sleep(5)

    driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()
    sleep(2)


    def search(song):

        search_box = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a').click()
        sleep(2)
        search_music = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
        search_music.send_keys(song, Keys.ENTER)
        sleep(2)
        music_label = driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]')
        music_label.click()

        add_to_liked_songs = pyautogui.prompt("Want to add in Liked songs (Y/N):: ")

        if add_to_liked_songs == "Y" or add_to_liked_songs == "y":
            driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[1]/div/div[3]/div/button').click()
            print("Song is add to 'Liked Song playlist'.")
            
            playlist = pyautogui.prompt("Want to see 'Liked Song Playlist' (Y/N):: ")
            
            if playlist == 'Y' or playlist == 'y':
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]/a/span').click()

            else:
                pass

        elif add_to_liked_songs == 'N' or add_to_liked_songs == 'n':
            
            Playlist = pyautogui.prompt("Want to see 'Liked Song Playlist' (Y/N):: ")

            if Playlist == 'Y' or Playlist == 'y':
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]/a/span').click()

            else:
                pass
            
        else:
            pass

    search("Akela Tha")



Login(password.main_acc_email, password.main_acc_pwd)



driver.quit()
    
    
    