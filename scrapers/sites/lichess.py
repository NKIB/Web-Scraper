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
    