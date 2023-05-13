
from sites.lichess import Lichess

from driver import instantiate_driver


def main():
    driver = instantiate_driver()

    lichess = Lichess(driver)
   # moves = lichess.repertoireCreater("https://lichess.org/analysis")
    moves = lichess.cloothDecision("https://www.dmi.dk/lokation/show/DK/2618425/K%C3%B8benhavn/")

    print(moves)

    driver.close()


if __name__== "__main__" :
    main()

    
