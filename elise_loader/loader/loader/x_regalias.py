import uploader, format
format_list = []
format_list.append(format.format("concepto", "string", 0, "", "", ""))
format_list.append(format.format("tipo", "string", 1, "", "", ""))
format_list.append(format.format("porcentaje", "number", 3, "", "", ""))
format_list.append(format.format("monto", "number", 2, "", "", ""))
format_list.append(format.format("frecuencia", "string", 4, "", "", ""))
format_list.append(format.format("dia_cobro", "string", 5, "", "", ""))
format_list.append(format.format("dias_bloqueo", "number", 6, "", "", ""))
u = uploader.uploader()
u.upload("franquicia.regalias", format_list, 2, 10000, "regalias.csv")