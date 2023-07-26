import odoorpc
class connection:
    def getConnection(self):
        servidor="antaresea.opentech-mx.com"
        puerto="7034"
        base_de_datos="estadistica"
        usuario="admin"
        password="admin"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo