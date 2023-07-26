import uploader, format

format_list = []
format_list.append(format.format("name", "string", 3, "", "", ""))
format_list.append(format.format("department_id", "many2one", 0, "NoCreate", "hr.department", "name"))
u = uploader.uploader()
u.upload("hr.job", format_list, 2, 10000, "departamentos.csv")