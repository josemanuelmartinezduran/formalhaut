import uploader, format
format_list = []
format_list.append(format.format("name", "string", 0, "", "", ""))
format_list.append(format.format("default_code", "string", 1, "", "", ""))
format_list.append(format.format("categ_id", "many2one", 2, "NoCreate", "product.category", "name"))
format_list.append(format.format("list_price", "number", 3, "", "", ""))
format_list.append(format.format("uom_id", "many2one", 5, "NoCreate", "uom.uom", "name"))
format_list.append(format.format("company_id", "static", 3, 5, "", ""))
format_list.append(format.format("property_account_income_id", "static", 0, 408, "", ""))
format_list.append(format.format("property_account_expense_id", "static", 0, 410, "", ""))
format_list.append(format.format("type", "static", 0, "product", "", ""))

format_list2 = []
format_list2.append(format.format("product_min_qty", "number", 18, "", "", ""))
format_list2.append(format.format("product_max_qty", "number", 17, "", "", ""))
format_list2.append(format.format("qty_multiple", "static", 0, 1, "", ""))
format_list2.append(format.format("company_id", "static", 3, 5, "", ""))
format_list2.append(format.format("product_id", "many2onecompany", 1, "NoCreate", "product.product", "default_code"))



u = uploader.uploader()
u.doubleupload("product.template", format_list, "stock.warehouse.orderpoint", format_list2, 3, 4, "V-VERA.csv")