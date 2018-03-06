#该模块尚待改善


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time


def is_pixel_equal(image1, image2, x, y):

    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False


def get_gap(image1, image2):

    left = 60
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            if not is_pixel_equal(image1, image2, i, j):
                left = i
                return left
    return left

track = []
driver=webdriver.Firefox()
driver.get('https://account.geetest.com/login')
wait=WebDriverWait(driver,10)

button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_radar_tip')))
button.click()
time.sleep(2)
driver.find_element_by_class_name('geetest_canvas_fullbg').screenshot('a.png')
time.sleep(1)
img1=Image.open('a.png')
driver.find_element_by_class_name('geetest_slider_button').click()
time.sleep(2)
driver.find_element_by_class_name('geetest_canvas_slice').screenshot('b.png')
img2=Image.open('b.png')
left=get_gap(img1,img2)
current = 0
mid = left* 4 / 5
t = 0.2
v = 0
while current < left:
    if current < mid:
        a = 3
    else:
        a = -4
    v0 = v
    v = v0 + a * t
    move = v0 * t + 1 / 2 * a * t * t
    current += move
    track.append(round(move))
slider =wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
ActionChains(driver).click_and_hold(slider).perform()
for x in track:
     ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
time.sleep(0.5)
ActionChains(driver).release().perform()










