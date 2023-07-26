import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("email", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("phone", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("mobile", "string", util.col2num("E"), "", "", ""))
format_list.append(format.format("supplier", "static", 1, False, 1, 1))
format_list.append(format.format("customer", "static", 1, True, 1, 1))
format_list.append(format.format("company_type", "static", 1, "person", 1, 1))
format_list.append(format.format("parent_id", "many2one", util.col2num("B"), "NoCreate", "res.partner", "name"))


u = uploader.uploader()
u.upload("res.partner", format_list, 2, 10000, "partner.csv", [])

