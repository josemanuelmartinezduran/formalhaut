import odoorpc


odoo = odoorpc.ODOO('149.56.87.164', port='7005')
odoo.login('mediform', 'admin', 'admin')
user = odoo.env.user
print(user.name)

origin_class = odoo.env['survey.user_input']
lead_class = odoo.env['crm.lead']
lead_class.create({
            "name": "Cuestionario no completado respuesta",
        })
for i in origin_class.search([['crm_creado', '=', False]]):
    encuesta = origin_class.browse(i)
    print(encuesta.id)
    print("Creando {}".format(encuesta.tipo))
    crm = lead_class.create({
            "name": "Cuestionario no completado respuesta",
            "encuesta_id": encuesta.id,
            "tipo": encuesta.tipo,
        })
    print("Seteando {}".format(encuesta))
    origin_class.write( encuesta.id, {
        "crm_creado": True
    })
for i in origin_class.search([['crm_finalizado', '=', False],['state', '=', 'done']]):
    user_input = origin_class.browse(i)
    for j in lead_class.search([['encuesta_id.id', '=', i]]):
        print("Llenando {}".format(j))
        my_crm = lead_class.browse(j)
        my_crm.llena()
        origin_class.write(i, {
            'crm_finalizado': True
        })
        print(my_crm)