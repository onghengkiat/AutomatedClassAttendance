# AutomatedClassAttendance
---
It is a mini project built by using Selenium to automate the process of signing class attendance of my university. 

**PS: I am a good boy :P, I didn't use it.**

Procudure to use it:
1) Edit the TakeAttendance.py. Fill in the scehedule, username and password according to the format given. The begin and end time is the 24 hours format time.
2) Make sure your computer has pip installed. 
3) Make sure your computer has Selenium installed. Else, either run pip install selenium or pip3 install selenium. 
Alternative way for it is you can run "source env/bin/activate" to activate the virtual environment that I have prepared.
4) Make sure you have the chrome drive file inside here. The current program is using chrome driver for chrome version 86 and linux OS.

If your chrome is not version 86 or your computer is not having linux OS, get the suitable chrome driver from the website below : 

https://chromedriver.chromium.org/downloads

You can check your chrome version by clicking the 3 dots on the top right corner, and then click "help". Lastly click "About google chrome".
If you have to download another chrome driver. 

Make sure to change the path below in TakeAttendance.py at line 38 to point it to your chrome driver.

driver = webdriver.Chrome("chromedriver_linux64/chromedriver")

5) You can try to deploy it to a server and let it run between a period of time to automate the take attendance process :D
