#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import PIL  
from io import BytesIO
import requests
import json

class Cliente:
    
 def __init__(self,enderecoAPI="http://localhost",port="5000"):
    self.__enderecoAPI = "{0}:{1}".format(enderecoAPI,port)
   

#method GET o que tem na pagina atual
 def soma(self,a,b):
    url = self.__enderecoAPI + "/vs1/soma"
    data = {"a":a,"b":b}
    r = requests.get(url,params=data)
    return r.json()
    
# get base url
 def getUrl(self,a,b):
    url = self.__enderecoAPI + "/vs1/soma"
    data = {"a":a,"b":b}
    r = requests.get(url,params=data)
    return r.url
  
  
  
  # Post conteudo
 def post_obj(self):
     url =    self.__enderecoAPI + "/vs1/post"
     datas = {"nome":"Allan","senha":123456}
     r = requests.post(url,data = datas)   
     return r.text
    
    
    
    
# get Para obter conteudo
 def gt_obter(self):
    url = self.__enderecoAPI+"/"
    r = requests.get(url)
    return r.text
    
    
    
    
 # get Para obter imagen da pagina
 def getoImg_http(self,url):
     r = requests.get(url)
     i = Image.open(BytesIO(r.content))
     i.show()
   
   
   

if __name__ == '__main__':
     cliente = Cliente()
     print(cliente.post_obj())
     #cliente.getoImg_http("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
     #print(cliente.getUrl(34,34)) 
     
    #save a image using extension 
    #print(cliente.soma(2,3)) 
    #print(cliente.obter())
    #print(cliente.getUrl(34,34)) 
     
    
  
