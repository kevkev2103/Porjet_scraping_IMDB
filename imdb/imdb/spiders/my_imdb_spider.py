import scrapy


class MyImdbSpiderSpider(scrapy.Spider):
    name = "my_imdb_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls =["https://www.imdb.com/chart/top/"]
    

    def parse(self, response):

        movies = response.css('ul.ipc-metadata-list li.ipc-metadata-list-summary-item')


        for movie in movies:
            movie_url = movie.css('a.ipc-title-link-wrapper::attr(href)').get()
            yield response.follow(movie_url, self.parse_movie)


    def parse_movie(self, response):
            
            yield{
                'titre': response.xpath('//h1[@data-testid="hero__pageTitle"]//span/text()').get(),
                'score':response.xpath('//div[@class ="sc-bde20123-2 cdQqzc"]/span[@class = "sc-bde20123-1 cMEQkK"]/text()').get(),
                'genre':response.xpath('//a[@class = "ipc-chip ipc-chip--on-baseAlt"]/span[@class="ipc-chip__text"]/text()').get(),
                'année':response.css('h1[data-testid="hero__pageTitle"]~ul a::text').get(),
                'durée':response.xpath('//section/div[2]/div[1]/ul/li[3]/text()').get(),
                'description':response.xpath('//p[@data-testid="plot"]/span[@data-testid="plot-l"]/text()').get(),
                'acteurs':response.xpath("(//a[text()='Stars'])[1]/following-sibling::div//li//a/text()").getall(),
                'pays':response.xpath('//li[@data-testid="title-details-origin"]//a//text()').get(), 


            }