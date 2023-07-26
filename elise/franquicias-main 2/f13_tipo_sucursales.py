import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

nombre_archivo = "tipo_sucursales.csv"
fila_inicial = 2
fila_final = 3

format_list.append(format.format("tipo_sucursal", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("zona", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("tamano", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("es_fabrica", "boolean", util.col2num("D"), "", "", ""))
format_list.append(format.format("lista_precio_base", "many2one", util.col2num("E"), "NoCreate", "product.pricelist", "name"))
format_list.append(format.format("listas_precio_habilitadas", "many2many_comas", util.col2num("F"), "name", "product.pricelist", ""))

u = uploader.uploader()
u.upload("franquicia.tipo", format_list, fila_inicial, fila_final, nombre_archivo)