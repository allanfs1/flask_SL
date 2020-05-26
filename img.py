#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image

class Img:
  def __init__(self,pacht):
    self.i = Image.open(pacht)
    self.i.show()

  def rotacionar(self,graus):
    self.i = self.i.rotate(graus)
    return self.i
   
  def saveImg(self,caminho,formate):
    path = caminho + formate
    self.i.save(path)
      
  
if __name__ == '__main__':
   img = Img("carro.jpg")
   imgread = img.rotacionar(45)
   imgread.show()
   img.saveImg("carro-novo",".jpg")
