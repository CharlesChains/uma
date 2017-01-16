from selenium import webdriver
wd = webdriver.Firefox()
wd.get("https://www.instagram.com")
username = "charleschains"
password = "caracas"
import time
time.sleep(4)
wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a").click()
wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[1]/input").send_keys(username)
wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/input").send_keys(password)
loginbut=wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")
loginbut.click()
#Empieza la posta
time.sleep(10)
try:
    #cerramos la porquería esa de usar app
    x = wd.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/button")
    assert x.text == "Close"
    x.click()
except:
    pass
    

def follower_xpath(follower_num):
    return "html/body/div[2]/div/div[2]/div/div[2]/ul/li["+str(follower_num)+"]/div/div[1]/div/div[1]/a"
    
try:
    #Si tenemos sugeridos vamos pa allá
suggested = wd.find_element_by_xpath(".//*[@id='react-root']/section/main/section/ul/li[1]/div/h2")
time.sleep(1)
assert suggested.text == "SUGGESTIONS FOR YOU"
primer_sugerido = wd.find_element_by_xpath(".//*[@id='react-root']/section/main/section/ul/li[2]/div/div[1]/div[1]/div/div[1]/a").click()
time.sleep(1)
followers = wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/header/div[2]/ul/li[2]/a")
time.sleep(1)
cant_followers = wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/header/div[2]/ul/li[2]/a/span").text
time.sleep(1)
cant_followers = int(cant_followers)
time.sleep(1)
followers.click()
time.sleep(1)
import random
rando_follower = wd.find_element_by_xpath(follower_xpath(random.randrange(1,cant_followers)))
rando_follower.click()
try: #Porque si son privado, son puto
    private_message_xpath = ".//*[@id='react-root']/section/main/article/div/h2"                      
    wd.find_element_by_xpath(private_message_xpath)
except: 
    pass
    
    wd.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div/div[1]/div/a[1]/div[2]").click()
    corazoncito = wd.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/a/span")
    corazoncito.click()
    import time
    time.sleep(200)
except:
    print("Cabe que sean puto y sean privado, o que el corazon no me late")
except:
    print("Mira vieja, no nos sugiere nada, instagram puto")
    