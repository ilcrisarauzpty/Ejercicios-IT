# Calculadora de descuento

precio = float(input("Ingresa el precio del producto: "))
descuento = 10
precio_final = precio -(precio * descuento) / 100
if precio >=100:
    print("Hemos aplicado un 10% de descuento. El nuevo precio es: ", precio_final)
else: 
    print("No hemos aplicado descuento. Su precio es: ", precio)