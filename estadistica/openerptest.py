import xmlrpc.client

class OpenConnect():
    host='158.69.165.19'
    port=8069
    url = "http://158.69.165.19:8069/xmlrpc"
    db = 'estadistica'
    username = 'admin'
    password = '240599'
    
    def createSO(self, ejecutivo, apoyo, cliente, clave, nombre_corto, tipo_levantamiento, objetivo, metodologia, muestra, tiempo, observaciones,res_agencia, res_proyecto, entregables):
        common = xmlrpc.client.ServerProxy(self.url +'/common')
        uid = common.login(self.db, self.username, self.password)
        models = xmlrpc.client.ServerProxy(self.url +'/object')
        cliente_id = models.execute_kw(self.db, uid, self.password, 'res.partner', 'search', [[['name', "=", cliente]]])[0]
        ejecutivo_id = models.execute_kw(self.db, uid, self.password, 'res.users', 'search', [[['login', "=", ejecutivo]]])[0]
        apoyo_id = models.execute_kw(self.db, uid, self.password, 'res.users', 'search', [[['login', "=", apoyo]]])[0]
        saleorder_id = models.execute_kw(self.db, uid, self.password, 'sale.order', 'create', [{
            'name': clave,
            'partner_id': cliente_id,
            'partner_invoice_id': cliente_id,
            'partner_shipping_id': cliente_id,
            "shop_id": 1,
            "nombre_corto": nombre_corto,
            "tipo_levantamiento": tipo_levantamiento,
            "user_id": ejecutivo_id,
            "user_id_dos": apoyo_id,
            "pricelist_id": 1,
            "objetivo": objetivo,
            "metodologia": metodologia,
            "tmuestra": muestra,
            "ttiempos": tiempo,
            "observaciones": observaciones,
            'resp': res_agencia,
            'rpoy': res_proyecto,
            'ent': entregables
          }])
        return saleorder_id
    
    def updateSO(self, saleorder_id, ejecutivo, apoyo, cliente, clave, nombre_corto, tipo_levantamiento, objetivo, metodologia, muestra, tiempo, observaciones,res_agencia, res_proyecto, entregables):
        common = xmlrpc.client.ServerProxy(self.url +'/common')
        uid = common.login(self.db, self.username, self.password)
        models = xmlrpc.client.ServerProxy(self.url +'/object')
        cliente_id = models.execute_kw(self.db, uid, self.password, 'res.partner', 'search', [[['name', "=", cliente]]])[0]
        ejecutivo_id = models.execute_kw(self.db, uid, self.password, 'res.users', 'search', [[['login', "=", ejecutivo]]])[0]
        apoyo_id = models.execute_kw(self.db, uid, self.password, 'res.users', 'search', [[['login', "=", apoyo]]])[0]
        saleorder_id = models.execute_kw(self.db, uid, self.password, 'sale.order', 'write', [[saleorder_id], {
            'name': clave,
            'partner_id': cliente_id,
            'partner_invoice_id': cliente_id,
            'partner_shipping_id': cliente_id,
            "shop_id": 1,
            "nombre_corto": nombre_corto,
            "tipo_levantamiento": tipo_levantamiento,
            "user_id": ejecutivo_id,
            "user_id_dos": apoyo_id,
            "pricelist_id": 1,
            "objetivo": objetivo,
            "metodologia": metodologia,
            "tmuestra": muestra,
            "ttiempos": tiempo,
            "observaciones": observaciones,
            'resp': res_agencia,
            'rpoy': res_proyecto,
            'ent': entregables
          }])
        return saleorder_id
    
    def createSOLine(self, so_id, producto, cantidad, precio):
        common = xmlrpc.client.ServerProxy(self.url +'/common')
        uid = common.login(self.db, self.username, self.password)
        models = xmlrpc.client.ServerProxy(self.url +'/object')
        product_id = models.execute_kw(self.db, uid, self.password, 'product.product', 'search', [[['name', "=", producto]]])[0]
        saleorderline = models.execute_kw(self.db, uid, self.password, 'sale.order.line', 'create', [{
            'name': "",
            'product_id': product_id,
            'product_uom_qty': cantidad,
            'price_unit': precio,
            "order_id": so_id,
          }])
        return saleorderline
    
    def createOT(self, clave, nombre_corto, so_id, ejecutivo, fecha_inicio):
        common = xmlrpc.client.ServerProxy(self.url +'/common')
        uid = common.login(self.db, self.username, self.password)
        models = xmlrpc.client.ServerProxy(self.url +'/object')
        ejecutivo_id = models.execute_kw(self.db, uid, self.password, 'res.users', 'search', [[['login', "=", ejecutivo]]])[0]
        saleorderline = models.execute_kw(self.db, uid, self.password, 'ea.project_wizard', 'create', [{
            'name': clave,
            'nombre_corto': nombre_corto,
            'executive_id': ejecutivo_id,
            'cotizacion_id': so_id,
            "date_start": fecha_inicio,
          }])
        return saleorderline
        
c = OpenConnect()
''' id = c.createSO("6385 RODRIGO ALAGON", "6385 RODRIGO ALAGON", "BIMBO", "XMLRPC-2022", "PRUEBARPC", "En Sitio","objetivo", "metod", "muestra", "tiempo", "observa", "res_agencia", "Proyecto", "te lo entrego")
print(id)
nid = c.updateSO(id, "6385 RODRIGO ALAGON", "6385 RODRIGO ALAGON", "BIMBO", "XMLRPC-2022-update", "PRUEBARPC", "En Sitio","objetivo", "metod", "muestra", "tiempo", "observa", "res_agencia", "Proyecto", "te lo entrego")
print(nid)
id_linea = c.createSOLine(id, "Entrevistas", 10, 250)
print(id_linea) '''
