import odoorpc
class connection:
    def getConnection(self):
        servidor="208.113.166.49"
        puerto="7073"
        base_de_datos="metrology"
        usuario="admin@metrology"
        password="m3tr0l0gy23"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo
