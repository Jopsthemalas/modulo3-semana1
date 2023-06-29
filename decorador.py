def decorator_imprime (func):
    def imprime (capital,taxa,tempo):
     print ("resultado é :")
     resultado=func(capital,taxa,tempo)
  
    return imprime
      
    
        

@decorator_imprime
def juros_simples (capital,taxa,tempo):
    resultado= capital*(taxa/100)*tempo
    print (resultado)

    
juros_simples (1000,5,6)