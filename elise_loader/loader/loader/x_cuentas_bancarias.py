import uploader, format
format_list = []
format_list.append(format.format("name", "string", 0, "", "", ""))
format_list.append(format.format("type", "static", 0, "bank", "", ""))
format_list.append(format.format("company_id", "many2one", 1, "NoCreate", "res.company", "name"))
format_list.append(format.format("code", "string", 2, "", "", ""))

u = uploader.uploader()
u.upload("account.journal", format_list, 2, 10000, "cuentas_bancarias.csv")
