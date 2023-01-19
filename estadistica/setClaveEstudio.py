import odoorpc

inicial = 0
final = 10000
contador = 0
odoo = odoorpc.ODOO('158.69.165.19', port='8069')
odoo.login('estadistica', 'admin', '240599')
user_data = odoo.execute('res.users', 'read', [1])
print (user_data)
