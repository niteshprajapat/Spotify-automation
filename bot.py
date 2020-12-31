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

    EMAIL = "abc@gmail.com"  # add your email address
    NICK_NAME = "XYZ"          # add your name by which spotify tries to remember you


    YEAR =  1234                        # enter your Year of birth
    DAY = 11                            # enter your Date of birth
    Month_name = "January"             # enter your Month of birth    


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
    


    pyautogui.alert("Please Solve reCAPTCHA puzzle!!!. You have 60 seconds.")   # Please solve reCAPTCHA puzzle to continue , this will not done by Bot .
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




    
    # Remember me button is already checked by Spotify in my case, In your case, if not checked then un-comment below 2 lines 
    # Remember_me_Btn = driver.find_element(By.XPATH, '//*[@id="app"]/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label/span').click()
    # sleep(5)

    driver.execute_script("window.scrollBy(0,500)", "")

    LOGIN_BTN = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    sleep(10)

    driver.get("https://open.spotify.com/?_ga=2.11073460.1059300004.1609394928-1863048095.1609394928")
    sleep(5)

    try:
        driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()
        sleep(2)

    except Exception as e:
        print(f"Error : {e}")
        

    def search(song):

        """
        This function search a song which is given by user as an argument. (Song name must be valid) 

        """

        search_box = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a').click()
        sleep(2)
        search_music = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
        search_music.send_keys(song, Keys.ENTER)
        sleep(2)
        music_label = driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]')
        music_label.click()

        sleep(10)
        add_to_liked_songs = pyautogui.prompt("Want to add in Liked songs (Y/N):: ")

        if add_to_liked_songs == "Y" or add_to_liked_songs == "y":
            if not (driver.title == "Remove from Your Library") :
                driver.execute_script("window.scrollBy(0,500)", "")
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[1]/div/div[3]/div/button').click()
                print("Currently playing song is add to 'Liked Song playlist'.")

            else:
                print("Already in 'Liked Song Playlist'. ")


            sleep(5)
            playlist = pyautogui.prompt("Want to see 'Liked Song Playlist' (Y/N):: ")
            
            if playlist == 'Y' or playlist == 'y':
                driver.execute_script("window.scrollBy(0,500)", "")
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]/a/span').click()

            else:
                pass

        elif add_to_liked_songs == 'N' or add_to_liked_songs == 'n':
            pyautogui.alert("Currently playing song is not added in 'Liked Song playlist")
            print("Currently playing song is not added in 'Liked Song playlist'.")
            
            Playlist = pyautogui.prompt("Want to see 'Liked Song Playlist' (Y/N):: ")

            if Playlist == 'Y' or Playlist == 'y':
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]/a/span').click()

            else:
                pass
            
        else:
            pass

        

    # search("Banjarey")  # Enter your song name replace by "Akela Tha"
    # search("Dooriyan(feat. Kaprila)")


    def play_liked_songs():

        """
        This function plays your liked song playlist. This function plays all songs in sequence .
        """
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]/a/span').click()
        sleep(2)
        
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/section/div[3]/div/button').click()
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    play_liked_songs()


    def fav_artist(name):

        """
        This function plays all songs of your favourite Artist. (Songs either shuffled or not)

        """

        sleep(2)

        search_btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a/span').click()
        search_artist = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
        search_artist.send_keys(name, Keys.ENTER)
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div/button[1]').click()

    fav_artist("Ritviz")





Login(password.main_acc_email, password.main_acc_pwd)



    
    

sleep(10)
user_logout_choice = pyautogui.prompt("Want to quit (Y/N) ::")

if user_logout_choice == "Y" or user_logout_choice == "y":
    driver.quit()
    
else:
    pass
    
    