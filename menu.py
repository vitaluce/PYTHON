#importar modulos y funciones necesarias
from ABM_productos import (
    agregar_producto,
    mostrar_productos,
    buscar_por_id,
    actualizar_producto,
    eliminar_producto,
    reporte_stock
)

#importar colorama para colores en consola
from colorama import Fore, Style, init
init(autoreset=True)

#menu principal
def mostrar_menu():
    while True:
        #impresion en consola del menú principal
        print(Fore.LIGHTWHITE_EX + "\n|==== MENÚ PRINCIPAL ====|")
        print(Fore.GREEN + "1. Registrar producto" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Ver inventario" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Buscar producto por ID" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Actualizar producto" + Style.RESET_ALL)
        print(Fore.RED + "5. Eliminar producto" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Reporte stock" + Style.RESET_ALL)
        print(Fore.YELLOW  + "7. Salir" + Style.RESET_ALL)

        opcion = input(Fore.WHITE+ "\nSeleccione una opción: " + Style.RESET_ALL)
        
 #procesar la opción seleccionada
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_stock()
        elif opcion == "7":
            print(Fore.LIGHTYELLOW_EX + "Saliendo...")
            break
        else:
            print(Fore.LIGHTRED_EX + "Opción inválida.")
