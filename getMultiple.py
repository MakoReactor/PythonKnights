#Funcao por Elias Granja(Era - http://eliasgranja.com )
#Codigo sob a gpl v3
def getMultiple(p,q,n):
	multiplos= []
	for i in range(1,n):
		if(i%p==0 or i%q==0):
			multiplos.append(i)
	return multiplos
