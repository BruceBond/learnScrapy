import requests


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=“{}”&ie=utf-8&pn={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    
    def get_url_list(self):
        # url_list = []
        # for i in range(10):
        #     url_list.append(self.url_temp.format(self.tieba_name, i*50))
        # return url_list     
        return [self.url_temp.format(self.tieba_name, i*50) for i in range(1000)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()    

    def save_html(self, html_str, page_num):
        file_path = "{}_第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f: 
            f.write(html_str)





    def run(self):  
        #1.构造url列表
        url_list = self.get_url_list()
        #2.发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            #3.保存到本地
            page_num = url_list.index(url)+1
            self.save_html(html_str,page_num)
        


if __name__ == '__main__':
    tieba_spider = TiebaSpider("插画")
    tieba_spider.run()