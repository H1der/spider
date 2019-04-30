import requests,sys
from bs4 import BeautifulSoup


class downloader(object):

    def __init__(self):
        # self.server = 'https://www.biduo.cc/biquge/'
        self.target ='https://www.biduo.cc/biquge/42_42269/'
        self.names = []
        self.urls = []
        self.nums = 0


    def get_download_url(self):
            req = requests.get(url = self.target)
            req.encoding = 'GBK'
            html = req.text
            div_bf = BeautifulSoup(html,'html.parser')
            texts = div_bf.find(id = 'list') 
            a_bf = BeautifulSoup(str(texts),'html.parser')
            a = a_bf.find_all('a')
            self.nums = len(a)
            for each in a:
                # print(each.string, self.server + each.get('href'))
                self.names.append(each.string)
                self.urls.append(self.target + each.get('href'))
    


    def get_contents(self,target):
        req = requests.get(url=target)
        req.encoding = 'GBK'
        html = req.text
        bf = BeautifulSoup(html,'html.parser')
        texts = bf.find(id = 'content') 
        texts = texts.text.replace('\xa0'*4,'\n\xa0\xa0')
        return texts


    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('开始下载:')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'小说.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已下载:%.2f%%" % float(i/dl.nums*100) +'\r')
        sys.stdout.flush()
    print('下载完成 100.00%')

