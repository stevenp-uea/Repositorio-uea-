def calcular_descuento (monto_total, porcentaje_descuento =25):

#establecemos un descuento por defecto que sera 25%
    descuento= monto_total * (porcentaje_descuento/100)

    return descuento
#Establecemos la operacion a realizar

#Descuento con el pocentaje por defecto que es 25
monto1 = 200
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Monto total: ${monto1:.2f}")
print(f"Descuento aplicado (25% por defecto): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# Opcion 2 con un descuento especifico
monto2 = 300
descuento2 = calcular_descuento(monto2, 15)
monto_final2 = monto2 - descuento2
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado (15% personalizado): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
