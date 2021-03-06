# -*- coding: utf-8 -*-

# Scrapy settings for baidu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
LOG_LEVEL = 'DEBUG'
BOT_NAME = 'baidu'

SPIDER_MODULES = ['baidu.spiders']
NEWSPIDER_MODULE = 'baidu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'


ITEM_PIPELINES = {
    'baidu.pipelines.BaiduPipeline': 30,
}

DOWNLOAD_DELAY = 10  
#LOG_FILE="log.txt"
CONCURRENT_REQUESTS=16
CONCURRENT_REQUESTS_PER_DOMAIN=8
CONCURRENT_REQUESTS_PER_IP=0

M_WANGPANWU_URLS=["http://www.wangpanwu.com/zjgx/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/video/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/mp3/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/bt/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/zip/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/ipa/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/zjgx/apk/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/p/list_%d.html"%(i)  for i in range(1,51)]+ \
              ["http://www.wangpanwu.com/p/fx/list_%d.html"%(i)  for i in range(1,51)]+ \
              []
         



M_SQLDB_CONF={"host":"localhost","port":3306,"user":"wangpan","passwd":"wangpan","db":"wangpan","charset":'utf8'}
M_BAIDU_USER_LIST=[2650954819,]
M_BAIDU_SQL_USER=""
SQLALCHEMY_ENGINE_URL="mysql://wangpan:wangpan@localhost/wangpan"
