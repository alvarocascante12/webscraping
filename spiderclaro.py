import scrapy 
import json
import numpy as np

class SpiderMovies_1(scrapy.Spider):
    name = 'movies_spider'
    
    start_urls=['https://www.clarovideo.com/argentina/vcard/homeuser/']
    Redirect_enabled: 'true'
    header = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'mfwkweb-api.clarovideo.net',
            'Origin': 'https://www.clarovideo.com',
            'Referer': 'https://www.clarovideo.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
       
     

    }
    def parse(self , response):
        url='https://mfwkweb-api.clarovideo.net/services/content/list?quantity=50&order_way=ASC&order_id=50&level_id=GPS&from=0&filter_id=38973&region=argentina&device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=nhb469fu7sj0358qp5dq5nvhd3'
        request = scrapy.Request(url , callback=self.parse_api , headers=self.header)

        yield request

    def parse_api(self , response):
        raw_data = response.body
        url2 = 'https://www.clarovideo.com/argentina/vcard/homeuser/'
        data = json.loads(raw_data)
       
        data = data['response']['groups']
        
        for movie in data:
            movie_code = movie['id']
            movie_url = movie['title_uri']
           
            
            moviesurl = url2 + movie_url +'/'+movie_code
            request = scrapy.Request(moviesurl , self.parse_movies , headers= self.header) 
            yield request

      

    def parse_movies(self , response):
        raw_data = response.body
        data = json.loads(raw_data)
        data = data['response']['groups']
        for movie in data:
            print(movie)
        
        yield {

                'id': data['id'] , 
                'title': data['title_uri'] 
            


        }


class SpiderMovies_2(scrapy.Spider):
    name = 'movies_spider_2'
    
    start_urls=['https://www.clarovideo.com/argentina/vcard/homeuser/']
    Redirect_enabled: 'true'
    header = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'mfwkweb-api.clarovideo.net',
            'Origin': 'https://www.clarovideo.com',
            'Referer': 'https://www.clarovideo.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
       
     

    }
    def parse(self , response):
        url='https://mfwkweb-api.clarovideo.net/services/content/list?quantity=50&order_way=ASC&order_id=50&level_id=GPS&from=0&filter_id=38973&region=argentina&device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=nhb469fu7sj0358qp5dq5nvhd3'
        request = scrapy.Request(url , callback=self.parse_api , headers=self.header)

        yield request

    def parse_api(self , response):
        raw_data = response.body
        url2 = 'https://www.clarovideo.com/argentina/vcard/homeuser/'
        data = json.loads(raw_data)
       
        data = data['response']['groups']
        
        for movie in data:
            movie_code = movie['id']
            movie_url = movie['title_uri']
           
            
            moviesurl = url2 + movie_url +'/'+movie_code
            request = scrapy.Request(moviesurl , self.parse_movies , headers= self.header) 
            yield request

      

    def parse_movies(self , response):
        raw_data = response.body
        data = json.loads(raw_data)
        data = data['response']['groups']
        for movie in data:
            print(movie)
        
        yield {

                'id': data['id'] , 
                'title': data['title_uri'] 
            


        }

