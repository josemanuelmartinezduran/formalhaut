import odoorpc

inicial = 0
final = 10000
contador = 0
odoo = odoorpc.ODOO('', port='')
odoo.login('', '', '')
nuevo = odoorpc.ODOO('', port='')
nuevo.login('', '', '')
user = odoo.env.user
print(user.name)
user = nuevo.env.user
print(user.name)
origin_class = odoo.env['']
dest_class = nuevo.env['']
for i in origin_class.search([]):
    if contador < inicial:
        contador += 1
        continue
elif contador > final:
    break
contador += 1
print(str(contador))
origin_object = origin_class.browse(i)
print(origin_object['name'])
name = origin_object['name'] if origin_object['name'] else ''
dest_class.create({
    'name': name,
})
print('Creado {}'.format(name))