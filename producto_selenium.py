import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions


def web_manipulation():
    url = 'https://dinem.agroindustria.gob.ar/dinem_fob.fob_consultaproductos.aspx#'

    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    web = Chrome("C:/Users/henrique.miranda/webdriver/chromedriver.exe", chrome_options=opts)

    try:
        web.get(url)

    except ConnectionError as e:
        print(str(e))
        web.close()

    web.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    element = web.find_element_by_xpath('//*[@id="DDO_DIM_PRODUCTO_DESCRICPCIONContainer_btnGroupDrop"]')

    element.click()

    if element:
        try:
            product_input = element.find_element_by_xpath(
                '//*[@id="GRID_DIM_Producto_Descricpcion"]/ul/li[5]/div/div/div/input')
            product_input.send_keys('Maíz')

            try:
                web.implicitly_wait(4)

                print('Connection completed.\n')

                web.find_element_by_xpath(
                    '//*[@id="GRID_DIM_Producto_Descricpcion"]/ul/li[6]/div/ul/li[36]').click()

                web.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)
                web.find_element_by_xpath('//*[@id="GRID_DIM_Producto_Descricpcion"]/ul/li[7]/input').click()

                time.sleep(2)
                web.find_element_by_xpath('//*[@id="vCDIAEXCEL_0001"]').click()
                print('Download Completed.\n')

            except TimeoutError as TE:
                print(str(TE))
                web.close()

        except NoSuchElementException as error:
            print(str(error))
            web.close()

    else:
        web.close()

    """value = web.execute_script('return arguments[0].value', element)
    print('Hidden input value {}'.format(value))

    web.execute_script('''
    var elem = arguments[0];
    var value = arguments[1];.685´/
    element.value = value;
    ''', element, 'Maíz')

    value = web.execute_script('return arguments[0].value', element)
    print('After update, hidden value = {}'.format(value))"""


web_manipulation()
