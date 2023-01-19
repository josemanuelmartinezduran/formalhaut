import odoorpc
class connection:
    def getConnection(self):
        servidor="72.167.55.23"
        puerto="7073"
        base_de_datos="Bodegas"
        usuario="noreply@"
        password="RFESystems$O"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo