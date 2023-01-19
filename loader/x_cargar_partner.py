import uploader, format, utilities, connection
format_list = []
format_list.append(format.format("name", "string", 1, "", "", ""))
format_list.append(format.format("city", "string", 5, "", "", ""))
format_list.append(format.format("property_account_income_id", "static", 32, 32, "", ""))
format_list.append(format.format("property_account_expense_id", "static", 34, 34, "", ""))
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_mx = util.getIdNoCreate("México", "res.country", "name", c)
format_list.append(format.format("country_ud", "static", 0, id_mx, "", ""))

u = uploader.uploader()
u.upload("product.template",format_list,3,10000,"products.csv")