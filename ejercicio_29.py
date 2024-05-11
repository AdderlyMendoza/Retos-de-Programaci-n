# Maquina expendedora

monedas = []
DesProducto = ["Oreo","Inca cola","Kr","Wafer","Doritos"]
PreProducto = [50,100,75,125,200]

# PEDIR MONEDAS
cantidadMonedas = int(input("Cantidad de monedas:"))
while( len(monedas) < cantidadMonedas ):
    moneda = int(input("Inserte moneda: "))
    if moneda in [5,10,50,100,200]:
        monedas.append(moneda)
    else:
        print("moneda ", moneda, " incorrecta, vuelva a insertar una moneda valida (5,10,50,100,200).")
print("Monedas insertadas: ", monedas)

# PEDIR PRODUCTO
print("-----------------------------")
print("PRODUCTOS")
for i in range(len(DesProducto)):
    print(DesProducto[i],PreProducto[i])
print("-----------------------------")
    
producto = int(input("Seleccione producto: "))
print("Producto seleccionado:",DesProducto[producto-1],",",PreProducto[producto-1],"soles")

# DEVOLVER CAMBIO
precioProductoSelec = PreProducto[producto]
cobro = sorted(monedas, reverse=True)
print(cobro)
vuelto = cobro
j = 0
for i in cobro:
    print("i:",i)
    if precioProductoSelec-i >= 0:
        precioProductoSelec = precioProductoSelec - i
        vuelto.pop(j)
    print("precioProductoSelec:",precioProductoSelec)
    j = j + 1
print(vuelto)
        
     



