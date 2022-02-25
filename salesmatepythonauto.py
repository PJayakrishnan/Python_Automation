import pyautogui

from win32api import GetSystemMetrics

import os

print("Adding new customers in Salesmate +")

pyautogui.FAILSAFE=False

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

print("Clicking on the bottom left to launch the start menu")
pyautogui.click(0,height)

print("Selecting the SalesMate+ Application")
pyautogui.typewrite(" SalesMate + ")

print("Pressing enter key to launch SalesMate + and wait 10s")
pyautogui.press("enter",1,15)

print("Presings enter again to close the pop up in salesmate+")
pyautogui.press("enter")

print("pressing shift + a to open accept payment menu item")
pyautogui.hotkey('shift','a')

print("Typing 1 as customer number to find customer Jayakrishnan")
pyautogui.typewrite("1")

print("Pressing enter 2 timer to get cursor to payment recieved field")
pyautogui.press("enter",2,1)

print("Type a payment amount of Rs 30")
pyautogui.typewrite("30")

print("Pressing enter to accept the payment")
pyautogui.press("enter",1,1)

print("Pressing enter to close the pop up")
pyautogui.press("enter",1,1)

print("Pressing enter to close the pop up")
pyautogui.press("enter",1,1)

