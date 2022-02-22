from datetime import datetime
from scrapy.spiders import SitemapSpider
from crawl_bao.items import ArticleItem


class CafeFSpider(SitemapSpider):
    name = 'cafef'
    sitemap_urls = ['https://cafef.vn/sitemaps.chn']

    def _get_sitemap_body(self, response):
        return super()._get_sitemap_body(response) or response.body

    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry['lastmod'], '%Y-%m-%d')
            if date_time.year >= 2022 and ('sitemaps' not in entry['loc'] or 'news-' in entry['loc']):
                yield entry

    def parse(self, response):
        yield ArticleItem(
            category=response.css('a.cat::text').get(),
            title=response.css('h1.title::text').get(),
            time=response.css('p.dateandcat span::text').get(),
            recap=response.css('div.w640.fr.clear h2.sapo::text').get(),
            content='\n'.join(response.css('div#mainContent p::text').getall()),
            author=response.css('p.author::text').get(),
            source=response.css('p.source::text').get(),
            url=response.url
        )
