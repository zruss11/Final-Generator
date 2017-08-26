# base.py
# developer: @eggins

# This gives you a basic understanding of how I set all my new projects up.
# Everything here is what I would use as a base to any python project.

# Please see installation instructions in README for further information
# Coming soon: documentation on every line to show how everything is being done

# initialise all libraries that are needed
import json, requests, os

# custom coded libraries
from classes.logger import logger
log = logger().log
from classes.FinalGenerator import FinalGenerator

# if you plan on using this script, please dont delete the below line
log("[@eggins] PyBase initalised. (github.com/eggins/pybase)", "info")
log("------------------------------------------------------")
log("\tFinal CC Generator [@_zruss_]", "info")
log("------------------------------------------------------")
# yee haw
s = requests.Session()


if not os.path.exists("config.json"):
    log("Config.json not found brother!!!", "error")
    log("Exiting...", "error")
    exit()

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

def createCard(x):

    f = FinalGenerator(s, config)
    FinalAccountData = f.FinalLogin(config)
    while x > 0:
        CardInfo 	 = f.CreateFinalCard(FinalAccountData, x)
        x -= 1

x = config['final']['amount']
log("Brother we are making %s credit cards. Lets Build!" % x, "info")
createCard(x)



