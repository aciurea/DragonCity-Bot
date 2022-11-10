## Dragon City Bot

### Goal
- The goal is to automate as much as possible the gameplay.
- Since I have no access to their APIs (at least I don't know how to access them from windows, android or iOS), I created a script that will play for me (collecting resources, fighting, identifing the resources where it needs to click, etc)

### Technology stack
- The project started with autohotkey `https://www.autohotkey.com/` but due to it's limitations I switched the language to Python 3s.

`NOTE`: I am new with python, I am a based JavaScript developer, I am adapting the code to the community guidelines as soons as I am learning new things in Python

### Platforms
- Works only for windows right now but it can also work with bluestacks or any other emulator as soon as the script runs from windows. Images might be updated due to different resolution on emulators
- Didn't try to run the script from other OS (but it should work)

## How it works
- I use Python3 to identify resources on screen. For this I need to take a screenshot (this one is not automated, it has to be manually) and I am using the `imagesearch` [https://pypi.org/project/python-imagesearch/] to get the coordinates on screen. 
- Once the resources are identified I am clicking on this coordinates or I am moving forward with other screenshots.
- The application needs a starting point (in my case the center of the map) and drag the map up and down to collect gold and food.
- The application is zoomed out to maximum.
- The starting point is needed because there might be a lot of missed clicks and thus opening unwanted screens (In the future can be fixed, be closing those screens and try again to move the map on other coordonates [`x` + step, `y` +step])
- The application has a lot of screenshots with buttons, resources and this is happening because some of the screenshots looks the same at first view but in reality are not the same (have extra shadows, borders, maybe different colors) and `imagesearch` will fail
- TODO: added screenshot with the map


### Features
- Collect gold
- Collect and farm food
- Breeding and hatching
- Battles: (TODO update with links and more documentation)
    - Arena battles
    - Quest battles
    - League battles
- Divine Tree:
    - recall dragons
    - trading hub
    - summon new dragons
    - empower (to be implemented)
- Watching rewards and automatically close them
- Buying orbs (only the one with gold)
- Heroic Race (Work in progress)
    - Battle
    - Action based on need (Breeding, Hatching, or Feeding)

### Heroic Race 
- Lap1: minTime = 25 minutes
- Lap2: minTime = 58 minutes
- Lap3: minTime = 1h 30 min
- Lap4: minTime = 5h 50min
##### 9h

- Lap5: minTime = 7h (battle dragons)
- Lap6: minTime = 11h (battle dragons)
- Lap7: minTime = 10h
- Lap8: minTime = 10h 15min
- Lap9: minTime = 11h
- Lap10: minTime = 14h
- Lap11: minTime = 19h 40 min
- Lap12: minTime = 19h 40 min
- Lap13: minTime = 20h 40 min
- Lap14: minTime = 31h 40 min
- Lap15: minTime = 26h
- Lap15: minTime = 30h
- 

## TOTAL ============================
