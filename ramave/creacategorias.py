import odoorpc

inicial = 0
final = 10000
contador = 0
odoo = odoorpc.ODOO('iron', port='7050')
odoo.login('ramave', 'admin@ramave', 'ramave2019')
user = odoo.env.user
print(user.name)
origin_class = odoo.env['ramave.categoriagasto']
for i in range(20):
    origin_class.create({
        'id': i,
        "name": str(i)
    })