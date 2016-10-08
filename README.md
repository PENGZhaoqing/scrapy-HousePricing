# scrapy-hoursepricing

(HousePricing)[https://github.com/PENGZhaoqing/HousePricing]的子项目，目的是实现对房价网站中的基本信息进行抓取

使用了轻量级Scrapy框架，抓取后的数据存为json格式，然后由HousePricing进行解析并储存在数据库中

## 安装

请自行安装Python和Scrapy

## 使用

在终端中运行

```
git clone https://github.com/PENGZhaoqing/scrapy-HousePricing
cd scrapy-HousePricing
scrapy crawl quotes
```

### 抓取数据文件

抓取的数据可以在根目录下的`housedata.json`查看

