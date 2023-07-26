import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
u = uploader.uploader()
inicio = 379
fin = 2000
archivo = "productos_patch.csv"

format_list.append(format.format("no_parte", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("name", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("marca", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("modelo", "string", util.col2num("E"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("F"), "Create", "product.category", "name"))
format_list.append(format.format("ubicacion", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("codigo_interno", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format("origen", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format("datos_origen", "string", util.col2num("J"), "", "", ""))
format_list.append(format.format("rosca", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format("diametro", "string", util.col2num("L"), "", "", ""))
format_list.append(format.format("largo", "string", util.col2num("M"), "", "", ""))
format_list.append(format.format("ltu", "string", util.col2num("N"), "", "", ""))
format_list.append(format.format("material", "string", util.col2num("O"), "", "", ""))
format_list.append(format.format("material_punta", "string", util.col2num("P"), "", "", ""))
format_list.append(format.format("standard_price", "number", util.col2num("Q"), "", "", ""))
format_list.append(format.format("list_price", "number", util.col2num("R"), "", "", ""))
format_list.append(format.format("moneda", "string", util.col2num("S"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("T"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("T"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("type", "static", 1, "product", 1, 1))
format_list.append(format.format("tracking", "static", 1, "lot", 1, 1))


u.upload("product.template", format_list, inicio, fin, archivo, [('not_null', 'name')])

format_list = []
format_list.append(format.format("warehouse_id", "static", 1, 1, "", ""))
format_list.append(format.format("location_id", "static", 1, 1, "", ""))
format_list.append(format.format("product_min_qty", "number", util.col2num("U"), "", "", ""))
format_list.append(format.format("product_max_qty", "number", util.col2num("V"), "", "", ""))
format_list.append(format.format("qty_multiple", "static", 1, 1,"", ""))
format_list.append(format.format("product_id", "many2one", util.col2num("C"), "NoCreate", "product.product", "name"))
u.upload("stock.warehouse.orderpoint", format_list,inicio, fin, archivo, [('product_min_qty', 'name')])