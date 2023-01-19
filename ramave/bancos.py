import odoorpc

inicial = 0
final = 10000
contador = 0
odoo = odoorpc.ODOO('iron', port='7050')
odoo.login('ramave', 'admin@ramave', 'ramave2019')
user = odoo.env.user
print(user.name)
origin_class = odoo.env['account.invoice']
for i in origin_class.search([("banco_id", "=", False)]):
    print("Iterando")
    rec = origin_class.browse(i)
    print("Record {}, {}".format(rec, rec.cuenta_bancaria.id))
    if(rec.cuenta_bancaria.id):
        origin_class.write([i], {
            'banco_id': rec.cuenta_bancaria.id
        })
        print("Setting record {}".format(rec))
    else:
        print("Skip")