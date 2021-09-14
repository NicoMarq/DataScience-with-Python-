import scrapy

#creo un spider
#es el bot que se encargara de recorrer la pagina
class AmazonproductSpider(scrapy.Spider):
    #nombre bot
    name = 'amazonproduct'
    #donde va a trabajar
    allowed_domains = ['www.amazon.com']
    #puedo usar una sola direccion,o usar varias en esta lista
    #ver la documentacion para ver como se haria con mas de 1
    start_urls = ['https://www.amazon.com/s?k=iphone12pro+max']

    #la funcion que se encarga de interpretar la pagina capturada
    #y obtener los datos concretos
    #de ahi que un parametro es response, request response...
    def parse(self, response):
         
        #usar el inspector de Google o la extension Selector Gadget
        #para saber donde demonios esta el elemento que quiero capturar
        #::text me trae el texto que es el dato, no el elemento HTML/CSS
        #extract lo captura y guarda en la variable
        producto=response.css(
            'span.a-text-normal::text'
            ).extract()
        
        precio=response.css(
            'span.a-price-whole::text'
            ).extract()
    
        #yield devuelve un diccionario con los datos
        yield {
                 'producto':producto,
                 'precio':precio,

            }
