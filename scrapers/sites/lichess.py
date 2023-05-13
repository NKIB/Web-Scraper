from selenium.webdriver.common.by import By

from .scraper import Scraper

class Lichess(Scraper):
    def scrape(self, url):

        # Open URL
        self.driver.get(url)

        # Print title
        print(self.driver.title)

        # Wait for dynamic data to load
        self.driver.implicitly_wait(2)

        # Click on book icon
        book = self.driver.find_element(By.CLASS_NAME, "fbt")
        book.click()
        
        # Wait for stats to show
        self.driver.implicitly_wait(1)
        
        # Get most played move
        moves_box = self.driver.find_element(By.CLASS_NAME, "moves")

        moves = moves_box.find_element(By.TAG_NAME, "tbody")
        
        most_played = moves.find_element(By.TAG_NAME, "tr")
        most_played = most_played.find_elements(By.TAG_NAME, "td")[1].text

        return most_played
    


    def repertoireCreater(self, url):
            # Open URL
        self.driver.get(url)

        # Print title
        print(self.driver.title)

        # Wait for dynamic data to load
        self.driver.implicitly_wait(2)

        # Click on book icon
        book = self.driver.find_element(By.CLASS_NAME, "fbt")
        book.click()
        
        # Wait for stats to show
        self.driver.implicitly_wait(1)
        
        # Get most played move
        moves_box = self.driver.find_element(By.CLASS_NAME, "moves")

        moves = moves_box.find_element(By.TAG_NAME, "tbody")
        
        most_played = moves.find_elements(By.TAG_NAME, "tr")[2]
        most_played = most_played.find_elements(By.TAG_NAME, "td")[0].text

        return most_played
    
    def cloothDecision(self, url):
            
        self.driver.get("https://www.dmi.dk/lokation/show/DK/2618425/København/")
        # Print title
        print(self.driver.title)

        # Wait for dynamic data to load
        self.driver.implicitly_wait(2)

        maxTem_str = self.driver.find_element(by=By.XPATH, 
        value="/html/body/main/section/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/p[3]/span").text
        maxTem_int = int(maxTem_str[0]+maxTem_str[1])
        if maxTem_int > 20 :
            print("Tag en tshirt på")
        elif maxTem_int > 10 and maxTem_int<20 :
            print("tag en trøje på")
        elif maxTem_int < 10 :
            print("tag en jakke på")
            
        return maxTem_int
