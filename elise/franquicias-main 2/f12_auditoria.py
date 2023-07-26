import uploader, utilities, connection, format
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

nombre_archivo = "auditoria_sucursales.csv"
fila_inicial = 2
fila_final = 3

format_list.append(format.format("relation", "many2one", util.col2num("A"), "Create", "auditoria.checklist", "name"))
format_list.append(format.format("seccion", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("pregunta", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("puesto", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("tipo_respuesta", "selection", util.col2num("E"), [("Si/no","sino"), ("Numérica", "num"), ("Texto abierto", "abierta"), ("default", "sino")],"", ""))
format_list.append(format.format("valor_referencia", "number", util.col2num("F"), "", "", ""))
format_list.append(format.format("calificaion", "number", util.col2num("G"), "", "", ""))

u = uploader.uploader()
u.upload("auditoria.checklist_preguntas", format_list, fila_inicial, fila_final, nombre_archivo, constraints=[("notnull", "relation")])