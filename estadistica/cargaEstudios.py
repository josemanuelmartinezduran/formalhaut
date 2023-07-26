import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
fila_inicial = 2
fila_final = 3
nombre_archivo = "estudios.csv"
u = uploader.uploader()

format_list.append(format.format("nombre_corto", "string", util.col2num("A"), "", "", ""))

u.upload("estadistica.cotizacion", format_list, fila_inicial, fila_final, nombre_archivo)