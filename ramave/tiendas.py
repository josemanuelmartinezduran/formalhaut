import odoorpc

inicial = 0
final = 10000
contador = 0
odoo = odoorpc.ODOO('iron', port='7050')
odoo.login('ramave', 'admin@ramave', 'ramave2019')
user = odoo.env.user
print(user.name)
origin_class = odoo.env['account.invoice']
for i in origin_class.search([("sucursal", "=", False)]):
    print("Iterando")
    rec = origin_class.browse(i)
    print("Record {}, {}".format(rec, rec.tienda.id))
    if(rec.tienda.id):
        origin_class.write([i], {
            'sucursal': rec.tienda.id
        })
        print("Setting record {}".format(rec))
    else:
        print("Skip")