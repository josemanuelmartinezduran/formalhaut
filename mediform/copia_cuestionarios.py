import odoorpc


odoo = odoorpc.ODOO('149.56.87.164', port='7005')
odoo.login('mediform', 'admin', 'admin')
user = odoo.env.user
print(user.name)

origin_class = odoo.env['survey.survey']
cuestionario_class = odoo.env['altair.encuesta']
pregunta_class = odoo.env['altair.pregunta']
opcion_class = odoo.env['altair.opcion']
for i in origin_class.search([]):
    survey = origin_class.browse(i)
    print(survey.title)
    idcuestionaro = cuestionario_class.create({
        "nombre": survey.title,
        "titulo": survey.title,
        "instrucciones": "",
        "modelo": "crm.lead",
        "campo": "entrevista_id",
        "umbral": 80,
        })
    print(idcuestionaro);
    for p in survey.page_ids:
        for q in p.question_ids:
            tipo = "Input"
            if q.type == "multiple_choice":
                tipo = "Multiple"
            elif q.type == "simple_choice":
                tipo = "Opciones"
            preg = pregunta_class.create({
                "texto": q.question,
                "encuesta_id": idcuestionaro,
                "tipo": tipo,
                "widget": "text"
                })
            print(preg)
            for op in q.labels_ids:
                opcion_class.create({
                    "pregunta_id": preg,
                    "nombre": op.value,
                    "valor": op.quizz_mark

                })