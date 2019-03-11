opcion=False
while not opcion:
	print 'Choose a dictionary'
	print '1.- Spanish'
	print '2.- English'
	print '3.- Catalan'
	choice=int(raw_input('Option: '))
	if choice==1:
		print 'All the special characters have been removed'
		f=open("Dictionaries/spanish.txt","r")
		opcion=True
	elif choice==2:
		f=open("Dictionaries/english.txt","r")
		opcion=True
	elif choice==3:
		f=open("Dictionaries/catalan.txt","r")
		opcion=True
print "\nUse '#' to multiple matches in the same word"
print "\nUse '_' for any other character"
print "\nUse a letter to match it in that place"
print "\nExample: __##a# would return zurrar\n"
dato=raw_input("Write a word: ")
longitud=len(dato)

#Sacamos las posiciones de las letras claves
repetidos=[]
datos=[]
palabras=[]
for i in range(0,longitud):
	if(dato[i]=='#'):
		repetidos.append(i)
	elif(dato[i]!='_'):
		datos.append(i)

#Hacemos las comprobaciones
for palabra in f:
	if(len(palabra)==(longitud+1)):
		candidato=1
		if len(repetidos)!=0:
			pos=repetidos[0]
			for j in repetidos:
				if(palabra[j]!=palabra[pos]):
					candidato=0
					break
		if(candidato==1):
			for k in datos:
				if(palabra[k]!=dato[k]):
					candidato=0
					break
			if(candidato==1):
				print palabra
				palabras.append(palabra)

sub=raw_input('Do a subsearch? (Y/N): ')
while sub != 'Y' and sub != 'N':
	sub=raw_input('Do a subsearch? (Y/N): ')
while sub=='Y':
	dato=raw_input("Write a word: ")
	longitud=len(dato)
	repetidos=[]
	datos=[]
	temp=[]
	for i in range(0,longitud):
	        if(dato[i]=='#'):
	                repetidos.append(i)
	        elif(dato[i]!='_'):
	                datos.append(i)

	#Hacemos las comprobaciones
	for palabra in palabras:
		#El +1 es por el '\n'
	        if(len(palabra)==(longitud+1)):
	                candidato=1
	                if len(repetidos)!=0:
	                        pos=repetidos[0]
	                        for j in repetidos:
	                                if(palabra[j]!=palabra[pos]):
	                                        candidato=0
	                                        break   
	                if(candidato==1):
	                        for k in datos:
	                                if(palabra[k]!=dato[k]):
	                                        candidato=0
	                                        break
	                        if(candidato==1):
	                                print palabra
	                                temp.append(palabra)
	palabras=temp
	sub=raw_input('Do a subsearch? (Y/N): ')
	while sub != 'Y' and sub != 'N':
        	sub=raw_input('Do a subsearch? (Y/N): ')

f.close()
