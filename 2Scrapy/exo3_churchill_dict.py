import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations_de_churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill"]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            
            if text_value:
                text_value = text_value.replace('“', '').replace('”', '')
                
            for cit in response.xpath('//div[@class="figsco__fake__col-9"]'):
                author_value = cit.xpath('a/text()').extract_first()

            yield {
                    'text': text_value,
                    'author': author_value
                }
            
# Stocker le fichier dans un JSON   
# scrapy runspider exo3_churchill_dict.py -o data/citation.json -t json