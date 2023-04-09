import re
import os
import requests
from time import sleep
import urllib.request
import undetected_chromedriver as uc

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


class TwitterScraper:
    def __init__(self):
        arguments = [
        "--disable-blink-features=AutomationControlled",
        "--disable-infobars",
        "--disable-features=WebRtcHideLocalIpsWithMdns",
        "--headless",
        "--no-sandbox",
        f"--window-size=1920,1080 * 4",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-blink-features=AutomationControlled",
        "--disable-features=VizDisplayCompositor",
    ]
        
        options = uc.ChromeOptions()

        # Add mandatory arguments to the ChromeOptions object
        for arg in arguments:
            options.add_argument(arg)

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)

    def login(self, my_user_mail, my_user_twitter, password):
        # Iniciar sesión en Twitter
        # Search login
        self.driver.get("https://www.twitter.com/")
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a",
        ).click()
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div").click()

        # send user email and click next
        search = self.driver.find_element(By.TAG_NAME, "input")
        search.send_keys(my_user_mail)
        next = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]",
        )
        next.click()
        sleep(2)

        # send user_twitter and click next
        search = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
        )
        search.send_keys(my_user_twitter)
        next = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div",
        )
        next.click()
        sleep(2)
        # send password and get in

        search = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        search.send_keys(password)
        next = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div",
        )
        next.click()
        self.driver.implicitly_wait(10)

    def search_users_urls(self, user):
        # Buscar la página de usuario en Twitter y devolver su URL
        
        search = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input",
        )
        search.send_keys(user)
        sleep(3)
        go_to = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/span/span[1]",
        )
        go_to.click()
        sleep(2)
        url_actual_page = self.driver.current_url
        return url_actual_page
    
    def get_photos(self):
        urls_imagenes = []
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/nav/div/div[2]/div/div[3]/a",
        ).click()
       
        for each_post in list(range(1, 10)):
            try:   
                self.driver.execute_script("window.scrollBy(0, 500);")

                xpath = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/a/div/div[2]/div/img'
                print(xpath)
                element = self.driver.find_element(By.XPATH, xpath)
                urls_imagenes.append(element.get_attribute("src"))
                print(urls_imagenes)
                self.driver.execute_script("window.scrollBy(0, 500);")

            except:
                try:
                    # XPATH para post con dos imágenes
                    xpath2 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/div/a/div/div/img'
                    element = self.driver.find_element(By.XPATH, xpath2)
                    urls_imagenes.append(element.get_attribute("src"))
                    
                    xpath3 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div/a/div/div/img'
                    element = self.driver.find_element(By.XPATH, xpath3)
                    urls_imagenes.append(element.get_attribute("src"))
                    print(urls_imagenes)
                    self.driver.execute_script("window.scrollBy(0, 500);")
                except:
                    try:
                        
                        # XPATH para post con tres imágenes
                        xpath4 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/div/a/div/div/img'
                        element = self.driver.find_element(By.XPATH, xpath4)
                        urls_imagenes.append(element.get_attribute("src"))
                        
                        xpath5 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/a/div/div/img'
                        element = self.driver.find_element(By.XPATH, xpath5)
                        urls_imagenes.append(element.get_attribute("src"))
                        print(urls_imagenes)
                        self.driver.execute_script("window.scrollBy(0, 500);")
                        
                        xpath6 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[2]/a/div/div/img'
                        element = self.driver.find_element(By.XPATH, xpath6)
                        urls_imagenes.append(element.get_attribute("src"))
                        print(urls_imagenes)
                        self.driver.execute_script("window.scrollBy(0, 500);")
                    except:
                        # post 4 imgs 
                        try:
                                # XPATH para post con cuatro imágenes
                            xpath7 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/div[1]/div/a/div/div/img'
                            element = self.driver.find_element(By.XPATH, xpath7)
                            urls_imagenes.append(element.get_attribute("src"))
                            
                            xpath8 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/img'
                            element = self.driver.find_element(By.XPATH, xpath8)
                            urls_imagenes.append(element.get_attribute("src"))
                            
                            xpath9 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div/a/div/div/img'
                            element = self.driver.find_element(By.XPATH, xpath9)
                            urls_imagenes.append(element.get_attribute("src"))
                            

                            xpath10 = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{each_post}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[2]/div/a/div/div/img'
                            element = self.driver.find_element(By.XPATH, xpath10)
                            urls_imagenes.append(element.get_attribute("src"))
                            print(urls_imagenes)
                            self.driver.execute_script("window.scrollBy(0, 500);")

                        except Exception as e:
                                print('Dejaron de ser post de 4')
                        
        lista_nueva = [elemento.replace("small", "large").replace("360x360", "large").replace("900x900",'large') for elemento in urls_imagenes]

        print(lista_nueva)
        return lista_nueva


    def download_photos(self, urls):

        IMAGES_FOLDER = 'chocolatito'
        if not os.path.exists(IMAGES_FOLDER):
            os.makedirs(IMAGES_FOLDER)
        for i, url in enumerate(urls):
            nombre_archivo = f'imagen_{i}.jpg'
            ruta_archivo = os.path.join(IMAGES_FOLDER, nombre_archivo)
            urllib.request.urlretrieve(url, ruta_archivo)

    def quit(self):
        # Cerrar el navegador
        self.driver.quit()


