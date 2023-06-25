import requests

class fipe :
     
    def __init__(self , marca_id):
     self.marca_id = marca_id
     self.modelos = []
     self.index_atual = 0

    def __iter__ (self):
     return self
    
             
    def __next__ (self):
       
     if self.index_atual >= len(self.modelos):
      raise StopIteration
    
     modelo = self.modelos[self.index_atual]
     self.index_atual += 1
     return {
             'codigo':modelo['codigo'],
            'nome':modelo['nome'] }
    
    def pegar_modelos (self):
      
      url =f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'

      headers ={'user-agent': 'jose'}

      response = requests.get(url,headers=headers)
      response.raise_for_status()
      data = response.json()

      tipo_de_modelo = data ['modelos']

      self.modelos = tipo_de_modelo


marca_id = input ("qual tabela gostaria ?")

iterator = fipe (marca_id) 
iterator.pegar_modelos()

for veiculo in iterator:
 print (veiculo['codigo'], veiculo['nome'])
    