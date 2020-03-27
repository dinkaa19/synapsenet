from selenium import webdriver

# Парсинг баланса, орнг, кпп с сайта synapsenet.ru
list_balans = []
ogrn_list = []
kpp_list = []


def find_ogrn():
    #   Скачиваем файл с сайта и добавлюем путь к нему https://github.com/mozilla/geckodriver/releases/
    driver = webdriver.Firefox(executable_path=r'C:\Py_selenum\geckodriver.exe')
    #   Алгоритм берет "ИНН" из таблицы и сканирует таблицу
    for i in lotereya_4['ИНН']:
        list_2 = []
        driver.get("https://synapsenet.ru/searchorganization/proverka-kontragentov")
        elem = driver.find_element_by_xpath('//*[@id="org-search-input"]')
        elem.send_keys(str(i))
        elem_2 = driver.find_element_by_id('org-search-button')
        elem_2.click()
        #         Огрн
        orgn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ul/li[1]')
        orgn_1 = orgn.text
        ogrn_2 = orgn_1.split(' ')[2]
        ogrn_list.append(str(ogrn_2))
        #         Кпп
        kpp = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ul/li[3]')
        kpp_1 = kpp.text
        kpp_2 = kpp_1.split(' ')[2]
        kpp_list.append(str(kpp_2))
        #       Достаем баланс(2018 или 2017 год), учтены все нюансы
        try:
            elem_3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[11]/table/tbody/tr[2]/td[2]')
            elem_3_1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[11]/table/tbody/tr[2]/td[1]')
            if (elem_3_1.text == "2018") or (elem_3_1.text == '2017'):
                list_2.append(elem_3.text)
                num = int(list_2[0].replace(' ', '')) * 1000
                num = str(num)
                list_balans.append(num)
            #                 print(num)
            else:
                list_balans.append('Нет актуальных данных')
        except:
            list_balans.append('Нет актуальных данных')
            continue
        print(i)
    #     Заполняем столбцы "Баланс" "ОГРН" "КПП"
    for i in list_balans:
        index = list_balans.index(i)
        lotereya_4['Баланс'][index] = str(i)

    for i in ogrn_list:
        index = ogrn_list.index(i)
        lotereya_4['ОГРН'][index] = str(ogrn_list[index])

    for i in kpp_list:
        index = kpp_list.index(i)
        lotereya_4['КПП'][index] = str(kpp_list[index])

    driver.close()