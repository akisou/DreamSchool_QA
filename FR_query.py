# import pandas as pd
from selenium import webdriver  # selenium=3.3.0
import sys
import datetime


def load_currency_code():
    # pandas version
    # currency_file = pd.read_csv('./currency_code.txt', sep=' ')
    # return dict(zip(currency_file['code'], currency_file['currency']))

    # simple version
    code2currency = dict()
    with open('./currency_code.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words = line[:-1].split(' ')
            if len(words) > 1:
                code2currency[words[1]] = words[0]
    return code2currency


def get_forex_rate(date, currency_code):
    # load currency 文件
    code2currency = load_currency_code()
    if currency_code not in code2currency.keys():
        print('code is wrong!')
        return None

    date = str(date)
    today = [int(elem) for elem in str(datetime.date.today()).split('-')]
    if len(date) != 8 or int(date[:4]) < 1950 or int(date[:4]) > today[0] \
            or int(date[4:6]) < 1 or int(date[4:6]) > 12 or int(date[6:]) < 1 or int(date[6:]) > 31:
        print('date is wrong!')
        return None
    date = date[:4] + '-' + date[4:6] + '-' + date[6:]

    # 创建一个Chrome WebDriver实例
    driver = webdriver.Chrome()

    # 构造查询的URL
    url = f"https://www.boc.cn/sourcedb/whpj/"

    # 打开网页
    driver.get(url)

    # 加载页面
    # time.sleep(3)

    # 找到货币选择框并选择指定的货币代号
    currency_select = driver.find_element_by_name("pjname")
    currency_select.send_keys(code2currency[currency_code])

    # 找到时间并选择指定的日期
    start_date = driver.find_element_by_name("erectDate")
    start_date.send_keys(date)
    end_date = driver.find_element_by_name("nothing")
    end_date.send_keys(date)

    # 点击查询按钮
    query_button = driver.find_element_by_xpath("//*[@id='historysearchform']/div/table/tbody/tr/td[7]/input")
    query_button.click()

    # 等待页面加载
    # time.sleep(3)

    # 找到现汇卖出价并输出
    forex_rate = driver.find_element_by_xpath("/html/body/div/div[4]/table/tbody/tr[2]/td[4]").text
    # length = len(forex_rate) - 1
    # index = random.randint(2, length)

    # 关闭浏览器
    driver.quit()

    return forex_rate


if __name__ == "__main__":
    # 获取命令行参数
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2]

    # 获取现汇卖出价并输出
    forex_rate = get_forex_rate(date, currency_code)
    if forex_rate:
        print(forex_rate)
        with open('result.txt', 'w') as f:
            f.write(forex_rate + '\n')
    else:
        print('no data')
