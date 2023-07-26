import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

format_list.append(format.format("default_code", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("barcode", "string", util.col2num("T"), "", "", ""))
format_list.append(format.format("purchase_ok", "boolean", util.col2num("D"), "", "", ""))
format_list.append(format.format("sale_ok", "boolean", util.col2num("E"), "", "", ""))
format_list.append(format.format("es_regalo", "boolean", util.col2num("F"), "", "", ""))
format_list.append(format.format("condiciones", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("type", "selection", util.col2num("H"), [("Almacenable","product"), ("Consumible","consu"), ("Servicio","service"), ("default", "product")],"", ""))
#format_list.append(format.format("active", "selection", util.col2num("I"), [("Inactivo", False), ("default", True)],"", ""))
format_list.append(format.format("linea", "many2one", util.col2num("J"), "Create", "mediform.linea", "nombre"))
format_list.append(format.format("estilo", "many2one", util.col2num("K"), "Create", "mediform.estilo", "nombre"))
format_list.append(format.format("color", "string", util.col2num("N"), "", "", ""))
format_list.append(format.format("sexo", "string", util.col2num("O"), "", "", ""))
format_list.append(format.format("talla", "string", util.col2num("P"), "", "", ""))
format_list.append(format.format("tipo_tela", "selection", util.col2num("Q"), [("Liso","Lisa"), ("Contrastado","Contrastado"), ("default", "Contrastado")],"", ""))
format_list.append(format.format("weight", "number", util.col2num("S"), "", "", ""))
format_list.append(format.format("multiplo_produccion", "number", util.col2num("AD"), "", "", ""))
format_list.append(format.format("tiempo_produccion", "number", util.col2num("AE"), "", "", ""))
format_list.append(format.format("comportamiento_ventas", "string", util.col2num("AF"), "", "", ""))
format_list.append(format.format("standard_price", "number", util.col2num("AY"), "", "", ""))
format_list.append(format.format("tracking", "selection", util.col2num("BG"), [("lote","lot"), ("default", "none")],"", ""))
format_list.append(format.format("precio_mayoreo", "number", util.col2num(""), 1.0, "", ""))
format_list.append(format.format("precio_menudeo", "number", util.col2num(""), 1.0, "", ""))
format_list.append(format.format("precio_dos", "number", util.col2num(""), 1.0, "", ""))
format_list.append(format.format("precio_tres", "number", util.col2num(""), 1.0, "", ""))
format_list.append(format.format("precio_cuatro", "number", util.col2num(""), 1.0, "", ""))





u = uploader.uploader()
u.upload("product.template", format_list, 2, 10000, "product_template.csv", [])