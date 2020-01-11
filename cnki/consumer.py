from channels.generic.websocket import WebsocketConsumer
import json
from spider.paper_spider_by_app import start_spider_by_app

class ChatConsumer(WebsocketConsumer):


    def connect(self):
        # 连接时触发
        print("开始连接")
        self.accept()
        print('self.channel_name',self.channel_name)

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
        self.result.revoke(terminate=True)
        self.close()
        print('关闭连接')

    def receive(self, text_data=None, bytes_data=None):
        print("收到消息")
        print("==========",text_data)
        print(json.loads(text_data)['message'])
        print('self.channel_name',self.channel_name)
        self.keyWords=json.loads(text_data)['message']
        self.result = start_spider_by_app.delay(self.keyWords, self.channel_name)

        # start_spider_by_app.delay(self)

    def send_message(self, event):
        print(event)
        print('self.result',self.result)
        self.send(json.dumps({
            "paperInfo": event["message"]
        }))