import scrapy
from scrapy import Request

class LemondeSpider(scrapy.Spider):
    name = "lemondev3"
    allowed_domains = ['lemonde.fr']
    start_urls = ['https://www.lemonde.fr/international/']

    def parse(self, response, **kwargs):
        # Parcours tous les éléments de navigation pour extraire les liens
       articles = response.css(".river .teaser")
       
       if not articles:
            self.logger.warning("Aucun article trouvé sur cette page : %s", response.url)
        
       for article in articles:
            title = self.clean_spaces(article.css("h3::text").extract_first())
            image = article.css("img::attr(data-src)").extract_first()
            description = article.css("p::text").extract_first()

            if title:
                self.logger.info(f"Titre extrait : {title}")
            else:
                self.logger.warning(f"Aucun titre trouvé pour l'article sur {response.url}")

            yield {
                "title": title,
                "image": image,
                "description": description
            }

    def clean_spaces(self, string):
        """Nettoie les espaces supplémentaires dans une chaîne."""
        if string:
            return " ".join(string.split())
        return ""
