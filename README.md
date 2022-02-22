

How to create new project:

> scrapy startproject crawl_bao
> 
> scrapy genspider example example.com

How to run a crawl

> scrapy crawl cafef -s JOBDIR=crawls/cafef-1 -O cafef.csv -s DOWNLOADER_CLIENT_TLS_METHOD=TLSv1.0