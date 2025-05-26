#calcular la edad de su mama cuando lo tuvo ingresando año de nacimiento nac madre e hijo

nac_hijo = int(input("Favor ingresar fecha de nacimiento del hijo :"))
nac_madre = int(input("Favor ingresar fecha de nacimiento de la madre :"))
resul = int(nac_hijo - nac_madre)
print ("La edad de la madre al tener a su hijo fue de : ",resul,"años")