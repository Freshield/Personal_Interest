import time
import cv2
import numpy as np
from playwright.sync_api import Playwright, sync_playwright, expect


def get_layer0_gas_image():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'height': 1000, 'width': 1000})
        page = context.new_page()
        page.goto("https://stargate.finance/transfer")
        page.get_by_text("Check Transfer Gas Estimator").click()
        time.sleep(1.5)

        element = page.wait_for_selector(
            'body > div.MuiDialog-root > div.MuiDialog-container.jss68.MuiDialog-scrollPaper > div > div.MuiDialogContent-root.jss73.jss74 > section > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div', timeout=10000)
        for i in range(30):
            time.sleep(0.5)
            print(element.inner_text())
            if 'MATIC' in element.inner_text():
                break

        print(element.inner_text())
        time.sleep(0.5)
        image_data = page.screenshot(path='example.png')
        # image_data = np.fromstring(image_data, np.uint8)
        # image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        # print(image_data)
        # cv2.imshow('test', image_data)
        # cv2.waitKey(0)

        page.close()

        # ---------------------
        context.close()
        browser.close()

    return image_data


if __name__ == '__main__':
    get_layer0_gas_image()
