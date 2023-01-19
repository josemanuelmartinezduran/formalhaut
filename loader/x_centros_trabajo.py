import uploader, format
format_list = []
format_list.append(format.format("name", "String", 0, "", "", ""))
format_list.append(format.format("time_efficency", "Number", 3, "", "", ""))
format_list.append(format.format("capacity", "Number", 4, "", "", ""))
format_list.append(format.format("oee_target", "Number", 5, "", "", ""))
format_list.append(format.format("costs_hour", "Number", 6, "", "", ""))
format_list.append(format.format("time_start", "Number", 7, "", "", ""))
format_list.append(format.format("time_stop", "Number", 8, "", "", ""))

u = uploader.uploader()
u.upload("mrp.workcenter", format_list, 2, 10000, "CentrosTrabajo.csv")