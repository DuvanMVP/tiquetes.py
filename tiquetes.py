porc_creditoVIP = 0.05
porc_turista = 0.10
porc_economica = 0.15


print( 'Bienvenidos a la aerolinea ANT MAN')
print( 'IMPORTANTE rellenar los siguientes datos a continuacion')
nombreStr = input('Nombre de usuario -> ')
montoFlt = float(input( 'Monto -> '))
var_OpcionStr = int(input('<<<MENU DE OPCIOES>>>\n\n1. VIP\n2. Turista\n3. Economica\n4. SALIR\n ->'))

if var_OpcionStr == 1:
    descFlt = montoFlt * 0.05
    valor_tiqueteInt = montoFlt - descFlt
    
    if var_OpcionStr == 2:
       descFlt = montoFlt * 0.10
       valor_tiqueteInt = montoFlt - descFlt
       
    if var_OpcionStr == 3:
        descFlt = montoFlt * 0.15
        valor_compradoInt = montoFlt - descFlt
        
print ('Nombre del usuario:' ,nombreStr)
print ('Descuento aplicado:' ,descFlt)
print ('Valor total a pagar es de: ''$',valor_tiqueteInt)
    
