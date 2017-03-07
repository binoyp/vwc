import scrapy
import re, os
from scrapy.shell import inspect_response
class yathriSpider(scrapy.Spider):
    name = "yathri"
    
    allowed_domains = ['ramakrishnavivekananda.info']
    def start_requests(self):
        urls = [
            'http://www.ramakrishnavivekananda.info/vivekananda/volume_1/complete_works_v1_contents.htm'
                  ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        patt = re.compile(r'^http://www.ramakrishnavivekananda.info/vivekananda/volume_1/')
        # filename = 'saved-%s.html' % page
        pathlist = response.url.split('/')[4:]
        filename = os.path.join(os.getcwd(),*pathlist)
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(filename, 'wb') as f:
            f.write(response.body)
        # _file = open('Link.txt','a')
        # _file.write(response.url + '\n')
        # _file.close()
        # inspect_response(response, self)
        pageurls = response.xpath('//a/@href')
        for page in pageurls:
            next_page_url = page.extract()
            if next_page_url is not None:
                if patt.match(response.urljoin(next_page_url)):
                    print "\n\n" + next_page_url + "\n\n"
                    yield scrapy.Request(response.urljoin(next_page_url))
            
