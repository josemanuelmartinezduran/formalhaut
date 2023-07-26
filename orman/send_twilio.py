import uploader, format, utilities, connection, twilio_lib
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
sender = twilio_lib.sender()

caso_clase = c.env["or.caso"]
#
for c in caso_clase.search([("user_id", "=", 637), ("state", "not in", ["Cancelado", "Cobrado", "Cobranza Extrajudicial"])]):
    caso = caso_clase.browse(c)
    print(caso.paterno, "  ", caso.materno, "  ", caso.nombres, "Celular: " + caso.celular )
    mensaje:str = "APRECIABLE {} {} {} EL ASESOR MARCOS FRANCO ALVARADO YA NO LABORA EN LA EMPRESA ORMAN SOLUCIONES PREVISIONALES DEBIDO A MALAS PRACTICAS LABORALES. SI USTED DESEA RETOMAR EL TRAMITE CON NOSOTROS CON LA EMPRESA P O DESEA RECOGER SU PAPELERIA PUEDE PASAR A LA OFICINA DE ORMAN SOLUCIONES PREVISIONALES.".format(caso.nombres, caso.paterno, caso.materno)
    print(mensaje)
    print("Estado {}".format(caso.state))
    sender.send(caso.celular, mensaje)
    