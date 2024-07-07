def determinar_rango_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "Vlan del rango normal"
    elif 1006 <= vlan <= 4094:
        return "Vlan del rango extendido"
    else:
        return "Número de Vlan fuera de rango"

try:
    vlan = int(input("Introduce el número de Vlan: "))
    print(determinar_rango_vlan(vlan))
except ValueError:
    print("Numero invalido, introduce un número valido de Vlan.")

