from selenium import webdriver
import os


chromedriver = "D:\chromedriver.exe"

browser = webdriver.Chrome(chromedriver)
browser.minimize_window()
browser.get('https://the-internet.herokuapp.com/upload')

file_list = os.listdir(r"C:\Users\ramvi\OneDrive\Pictures\test")
list1 = []

def upload(file):
    browser.find_element_by_id('file-upload').send_keys("C:\\Users\\ramvi\\OneDrive\\Pictures\\test\\" + file)
    browser.find_element_by_id('file-submit').click()
    print("Uploaded " + file + " successfully!")
    browser.back()

def add(filename):
    file = open("C:\\Users\\ramvi\\OneDrive\\Pictures\\test\\check.txt", "a")
    file.write(filename)
    file.close()

file1 = open("C:\\Users\\ramvi\\OneDrive\\Pictures\\test\\check.txt", "r")
exist = file1.readlines()
for name in exist:
    list1.append(name.rstrip('\n'))

for f_name in file_list:
    if f_name not in list1:
        add(f_name + "\n")
        upload(f_name)


