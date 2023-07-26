import odoorpc
class connection:
    def getConnection(self):
        servidor="132.148.77.223"
        puerto="7073"
        base_de_datos="orman"
        usuario="admin@orman"
        password="Orman*2020!"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo