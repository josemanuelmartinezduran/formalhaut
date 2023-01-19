import uploader, format
format_list = []
format_list.append(format.format("name", "Many2one", 2, "NoCreate", "res.partner", "name"))
format_list.append(format.format("min_qty", "static", 0, "1", "", ""))
format_list.append(format.format("product_tmpl_id", "Many2one", 1, "NoCreate", "product.template", "default_code"))
format_list.append(format.format("price", "Number", 3, "", "", ""))
u = uploader.uploader()
u.upload("product.supplierinfo", format_list, 2, 10000, "ListaInsumos.csv")
format_list = []
format_list.append(format.format("name", "Many2one", 4, "NoCreate", "res.partner", "name"))
format_list.append(format.format("min_qty", "static", 0, "1", "", ""))
format_list.append(format.format("product_tmpl_id", "Many2one", 1, "NoCreate", "product.template", "default_code"))
format_list.append(format.format("price", "Number", 5, "", "", ""))
u = uploader.uploader()
u.upload("product.supplierinfo", format_list, 2, 10000, "ListaInsumos.csv")