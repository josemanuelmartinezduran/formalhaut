import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

filename = 'ordenes.csv'
start=2
end= 10

format_list.append(format.format("producto", "many2one", util.col2num("H"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("folio", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("estilo", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("color", "string", util.col2num("E"), "", "", ""))
format_list.append(format.format("talla", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("cantidad", "number", util.col2num("J"), 0, "", ""))

u = uploader.uploader()
u.upload("mediform.manufactura", format_list, start, end, filename, [('unique', 'folio'), ('not_null', 'folio')])

format_list = []
format_list.append(format.format("manufactura_id", "many2one", util.col2num("A"), "NoCreate", "mediform.manufactura", "folio"))
format_list.append(format.format("piezas", "number", util.col2num("J"), 0, "", ""))
format_list.append(format.format("estatus", "static", 1, "Nuevo", 1, 1))
format_list.append(format.format("numero", "static", 1, "1", 1, 1))
u.upload("mediform.caja", format_list, start, end, filename, [])
