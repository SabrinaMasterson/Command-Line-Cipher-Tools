#Sabrina Masterson
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from cleantext import clean
#from selenium.webdriver.support.select import Select

def testInput(input_send):
    if (input_send.isalpha() == False):
        if ('-' in input_send or ' ' in input_send):
            pass
        else:
            print("\n")
            print("You must use a word or term that can be sent to a search bar")
            #exit()
            return 0
    else:
        return 1

def makeDict(input_send):
    #input_send = "soup"
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.onelook.com/thesaurus")
    time.sleep(2)
    #driver opened to URL

    input_search = driver.find_element(By.ID, "thesinput")
    input_search.send_keys(input_send)
    input_search.send_keys(Keys.RETURN)
    time.sleep(2)
    #input added to web page

    soup = BeautifulSoup(driver.page_source, "lxml")
    time.sleep(2)
    #BeautifulSoup collects html source

    definitions = soup.find("div", class_="def-box-defs")
    if definitions is None:
        print("No definition could be found for your word")
        Print("Because of this, program is exiting as no further content can be found")
        print("Make sure you are inputting a word or phrase that would be searchable in a search engine")
        print("Often shortening the phrase and removing propositions can increase chances of a search result")
        exit()
    else:
        def_text = definitions.get_text()
        def_print = ""

    for text in def_text:
        if (text == u"\U0001F506"):
            text += "\n"
            def_print += text
        elif ';' in text:
            text += "\n"
            def_print += text
        else:
            def_print += text
    #the emoji actually denotes the end of line, so I can split the text on that

    def_print = clean(def_print, no_emoji=True)
    print(def_print + "\n")
    #Definitions printed
    print("\n")
    #it appears that the tabs section will always be the same

    tabs = soup.find("ul", {"id" : "tabs"})
    tabs_len = len(tabs)
    tabs_list = tabs.get_text(separator=' ').split()
    #tabs for each section of the collected words

    for i in range(0, tabs_len):
        z = "zone"
        z = z + str(i+1)
        zone = soup.find("div", {"id" : z})

        if (tabs_list[i] == "All"):
            print("First page of associated words: ")
        else:
            print("First page of associated " + tabs_list[i] + ": ")
        if zone is None:
            print("No words were found for this section")
        else:
            zone_span =  zone.find_all("span")
            no_def = "Definitions"
            word = []
            for items in zone_span:
                items_list = items.get_text(separator=' ')

                if (items_list[0].isalpha() == False):
                    pass
                elif no_def in items_list:
                    index = items_list.index("Definitions")
                    for i in range(index):
                        key = items_list[i].strip()
                        word.append(key)
                    print(''.join(word))
                    word.clear()
                    #it's messy, but it gets only the words I'm looking for
                else:
                    pass
        print("\n")

    #printing of each set of words/phrases, no spaces for password cracking

    driver.quit()


def main():
    done = False
    while done == False:
        print("Would you like to make a password dictionary? ")
        yorn = input("(y/n) ")
        if (yorn == "Y" or yorn == "y" or yorn == "yes"):
             print("Enter word or phrase to search: ")
             input_send = input("Do not add numbers or special characters save for hyphens: ")
             print("\n")
             #test_input = input_send.strip()
             results = testInput(input_send)
             if results == 1:
                 makeDict(input_send)
             elif results == 0:
                pass
        elif (yorn == "N" or yorn == "n" or yorn == "no"):
            print("exiting now.")
            done = True
            break

main()
