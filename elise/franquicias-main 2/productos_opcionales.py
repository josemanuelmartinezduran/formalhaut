import odoorpc
import csv
import os, sys
import utilidades

#datos para cambiar
servidor="127.0.0.1"
puerto="7072"
base_de_datos="franquicias"
usuario="admin"
password="admin"
objeto_a_crear="product.template"

#Donde inicia a cargar datos (filas del archivo de excel)
inicial = 1
#Donde termina de cargar datos
final = 1000
contador = 0
#Ruta del servidor y puerto
odoo = odoorpc.ODOO(servidor, port=puerto)
#base de datos, usuario, contraseña
odoo.login(base_de_datos, usuario, password)
print("Sesion iniciada {}".format(odoo))
#A donde voy a subir mis datos
origin_class = odoo.env[objeto_a_crear]
u=utilidades.utilidades()

#Nombre del archivo csv
with open(os.path.join(sys.path[0], "existencias.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        priducto_id = u.dameelid_nocrear("Caja de almacenaje", "product.template", "name", odoo)
        opcional_id = u.dameelid_nocrear("Caja de almacenaje", "product.template", "name", odoo)
        if(priducto_id == "" or opcional_id == ""):
            continue
        linea = origin_class.write(priducto_id, {
            'optional_product_ids': [priducto_id]
        })
        print("Actualizado {}".format(linea))
