from channels.generic.websocket import WebsocketConsumer
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ChatConsumer(WebsocketConsumer):

    browser=''
    i=0
    def connect(self):
        # 连接时触发
        print("开始连接")
        self.accept()
        # self.send(text_data=json.dumps({"message": "message"}))
    def disconnect(self, code):
        # 关闭连接时触发
        # print('关闭连接')
        #
        # try:
        #     self.browser.quit();
        # except Exception as e:
        #     print("关闭出错啦=====================\n", e)
        #     self.browser.quit()
        self.close()
        print('关闭连接')

    def receive(self, text_data=None, bytes_data=None):
        # 收到消息后触发
                # 前端页面使用send()发送数据给websocket，由该函数处理
        # 真个ChatConsumer类会将所有接收到的消息加上一个"聊天"的前缀发送给客户端
        # 设置谷歌驱动器的环境
        # self._build_model()
        options = webdriver.ChromeOptions()
        # 设置chrome不加载图片，提高速度
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 创建一个谷歌驱动器
        self.browser = webdriver.Chrome('/Applications/chromedriver', chrome_options=options)
        print("==========",text_data)
        if(text_data=='close'):
            print('关闭连接1')
            self.close()
            self.browser.quit()

        print("收到消息===============")
        try:
            self.i += 1
            print("次数==============================" +str(self.i))


            url = 'http://wap.cnki.net/touch/web/guide'

            # 声明一个全局列表，用来存储字典
            data_list = []
            print("发送消息")
            # 请求url
            self.browser.get(url)
            # 显示等待输入框是否加载完成
            WebDriverWait(self.browser, 1000).until(
                EC.presence_of_all_elements_located(
                    (By.ID, 'keyword')
                )
            )
            # 找到输入框的id，并输入python关键字
            self.browser.find_element_by_id('keyword').click()
            self.browser.find_element_by_id('keyword_ordinary').send_keys('python')
            # 输入关键字之后点击搜索
            self.browser.find_element_by_class_name('btn-search ').click()
            # print('quit')
            # self.browser.quit()

            # print(browser.page_source)
            # 显示等待文献是否加载完成
            WebDriverWait(self.browser, 1000).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, 'g-search-body')
                )
            )
            self.send("202")

            # 声明一个标记，用来标记翻页几页
            count = 1
            while True:
                # 显示等待加载更多按钮加载完成
                WebDriverWait(self.browser, 1000).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, 'c-company__body-item-more')
                    )
                )
                # 获取加载更多按钮
                Btn = self.browser.find_element_by_class_name('c-company__body-item-more')
                # 显示等待该信息加载完成
                WebDriverWait(self.browser, 1000).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH,
                         '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))
                    )
                )
                # 获取在div标签的信息，其中format(2*count-1)是因为加载的时候有显示多少条
                # 简单的说就是这些div的信息都是奇数
                divs = self.browser.find_elements_by_xpath(
                    '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))
                # 遍历循环
                for div in divs:
                    # 获取文献的题目
                    name = div.find_element_by_class_name('c-company__body-title').text
                    # 获取文献的作者
                    author = div.find_element_by_class_name('c-company__body-author').text
                    # 获取文献的摘要
                    content = div.find_element_by_class_name('c-company__body-content').text
                    # 获取文献的来源和日期、文献类型等
                    text = div.find_element_by_class_name('c-company__body-name').text.split()
                    if (len(text) == 3 and text[-1] == '优先') or len(text) == 2:
                        # 来源
                        source = text[0]
                        # 日期
                        datetime = text[1]
                        # 文献类型
                        literature_type = None
                    else:
                        source = text[0]
                        datetime = text[2]
                        literature_type = text[1]
                    # 获取下载数和被引数
                    temp = div.find_element_by_class_name('c-company__body-info').text.split()
                    # 下载数
                    download = temp[0].split('：')[-1]
                    # 被引数
                    cite = temp[1].split('：')[-1]

                    # 声明一个字典存储数据
                    data_dict = {}
                    data_dict['name'] = name
                    data_dict['author'] = author
                    data_dict['content'] = content
                    data_dict['source'] = source
                    data_dict['datetime'] = datetime
                    data_dict['literature_type'] = literature_type
                    data_dict['download'] = download
                    data_dict['cite'] = cite
                    self.send(json.dumps({"paperInfo":[data_dict]}, ensure_ascii=False))
                    data_list.append(data_dict)
                    print(data_dict)
                # 如果Btn按钮（就是加载更多这个按钮）没有找到（就是已经到底了），就退出
                if not Btn:
                    break
                else:
                    Btn.click()
                # 如果到了爬取的页数就退出
                if count == 0:
                    break

                count += 1

                # 延迟两秒，我们不是在攻击服务器
                time.sleep(2)
        except Exception as e:
            print("出错啦=====================\n",e)
            self.browser.quit()

