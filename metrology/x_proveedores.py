import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
u = uploader.uploader()
inicio = 2
fin = 1000
archivo = "proveedores.csv"

format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("comment", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("phone", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("vat", "string", util.col2num("E"), "", "", ""))
format_list.append(format.format("country_id", "many2one", util.col2num("F"), "NoCreate", "res.country", "name"))
format_list.append(format.format("city", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("street", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format("zip", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format("street2", "string", util.col2num("J"), "", "", ""))
format_list.append(format.format("ref", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format("supplier", "static", 1, True, 1, 1))
format_list.append(format.format("customer", "static", 1, False, 1, 1))
format_list.append(format.format("company_type", "static", 1, "company", 1, 1))
u.upload("res.partner", format_list, inicio, fin, archivo, [('unique', 'name')])

format_list = []
format_list.append(format.format("name", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("parent_id", "many2one", util.col2num("A"), "NoCreate", "res.partner", "name"))
format_list.append(format.format("supplier", "static", 1, True, 1, 1))
format_list.append(format.format("customer", "static", 1, False, 1, 1))
u.upload("res.partner", format_list, inicio, fin, archivo, [('not_null', 'name')])
