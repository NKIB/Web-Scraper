
from sites.lichess import Lichess

from driver import instantiate_driver


def main():
    driver = instantiate_driver()

    lichess = Lichess(driver)
    moves = lichess.scrape("https://lichess.org/analysis")

    print(moves)

    driver.close()



if __name__== "__main__" :
    main()

    
