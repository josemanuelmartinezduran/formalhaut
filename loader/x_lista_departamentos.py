import uploader, format
format_list = []
format_list.append(format.format("name", "string", 0, "", "", ""))
u = uploader.uploader()
u.upload("hr.department", format_list, 2, 10000, "departamentos.csv")

