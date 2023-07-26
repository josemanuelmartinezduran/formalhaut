import odoorpc
class connection:
    def getConnection(self):
        servidor="sistema.contigoadondesea.net"
        puerto="7073"
        base_de_datos="mediform"
        usuario="admin@mediform"
        password="Med%es2022"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo
