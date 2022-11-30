from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(3)

username = browser.find_element("name","username")
password = browser.find_element("name","password")

username.send_keys("yourNickname")
password.send_keys("yourPassword")

time.sleep(5)

login = browser.find_element("xpath","//*[@id='loginForm']/div/div[3]/button/div")
login.click()
time.sleep(8)

def goMyProfile():
    browser.get("yourProfileLink")
    time.sleep(3)

goMyProfile()

def clickFollowers():
    followers = browser.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]")
    followers.click()
    time.sleep(5)

def getFollowers():
    followers = browser.find_elements("css selector","._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
    time.sleep(5)
    global followersList
    followersList = []
    for follower in followers:
        followersList.append(follower.text)
    followersList = sorted(followersList)
    print(followersList)

def scrollDownFollowers():
    jsCommand = """
    page = document.querySelector("._aano");
    page.scrollTo(0,page.scrollHeight);
    var endPage = page.scrollHeight;
    return endPage;
    """
    endPage = browser.execute_script(jsCommand)
    while True:
        end = endPage
        time.sleep(1)
        endPage = browser.execute_script(jsCommand)
        if end == endPage:
            break

def goFollowing():
    browser.get("https://www.instagram.com/ayselaltuntas99/following/")
    time.sleep(3)

def getFollowing():
    followings = browser.find_elements("css selector","._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
    time.sleep(5)
    global followingsList
    followingsList = []
    for following in followings:
        followingsList.append(following.text)
    followingsList = sorted(followingsList)
    print(followingsList)

def scrollDownFollowing():
    jsCommand = """
        page = document.querySelector("._aano");
        page.scrollTo(0,page.scrollHeight);
        var endPage = page.scrollHeight;
        return endPage;
        """
    endPage = browser.execute_script(jsCommand)
    while True:
        end = endPage
        time.sleep(1)
        endPage = browser.execute_script(jsCommand)
        if end == endPage:
            break

def getUnfollowers():
    unfollowersList = (set(followingsList) - set(followersList))
    unfollowersList = sorted(unfollowersList)
    print(unfollowersList)

clickFollowers()
scrollDownFollowers()
getFollowers()
goMyProfile()
goFollowing()
scrollDownFollowing()
getFollowing()
getUnfollowers()

time.sleep(60)
browser.close()