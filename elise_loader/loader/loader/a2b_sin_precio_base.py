import uploader
import format
import connection
import utilities
id_warehouse = 1
id_ubicacion = 8
id_company = 1
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_listas_precios = []

# Modificar por consultor
nombre_archivo = "5.2.franqui.csv"
fila_inicial = 2
fila_final = 10
cargar_seguimiento = False
cargar_fechas_caducidad = False
es_franquicia = True
es_multisucursal = False
cargar_minimos = False
cargar_almacen_inicial = False
listas_precios = ["Precio amigable", "Menudeo", "consumidor", "mayoreo"]
columnas_listas_precios = ["AB", "AC", "AD", "AE"]


id_fabricar = util.getIdNoCreate("Fabricar", "stock.location.route", "name", c)
id_comprar = util.getIdNoCreate("Comprar", "stock.location.route", "name", c)

format_list = []
format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format(
    "default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("categ_id", "many2one",
                   util.col2num("D"), "Create", "product.category", "name"))
format_list.append(format.format(
    "list_price", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format("uom_id", "many2one",
                   util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one",
                   util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean",
                   util.col2num("G"), "options", "model", "compare"))
format_list.append(format.format(
    "barcode", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format("description_sale",
                   "string", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "weight", "number", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "volume", "number", util.col2num("L"), "", "", ""))
format_list.append(format.format("sale_delay", "number",
                   util.col2num("M"), "options", "model", "compare"))
format_list.append(format.format("route_ids", "many2many_selection", util.col2num("N"), [("lo fabricamos", [
                   id_fabricar]), ("lo compramos", [id_comprar]), ("ambos", [id_fabricar, id_comprar])], "model", "compare"))
format_list.append(format.format("sale_ok", "static", 1, 1, "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "", "", ""))
format_list.append(format.format(
    "standard_price", "number", util.col2num("O"), "", "", ""))
if (cargar_seguimiento):
    format_list.append(format.format("tracking", "selection", util.col2num("Q"), [
                       ("Serie", "serial"), ("Lote", "lot"), ("Sin seguimiento", "none")], "", ""))
if (cargar_fechas_caducidad):
    format_list.append(format.format("use_expiration_date", "boolean",
                       util.col2num("R"), "options", "model", "compare"))
    format_list.append(format.format("expiration_time", "number",
                       util.col2num("S"), "options", "model", "compare"))
    format_list.append(format.format("use_time", "number",
                       util.col2num("T"), "options", "model", "compare"))
    format_list.append(format.format("removal_time", "number",
                       util.col2num("U"), "options", "model", "compare"))
format_list.append(format.format("type", "selection", util.col2num("V"), [(
    "Servicio", "service"), ("Almacenable", "product"), ("Consumible", "consu")], "", ""))
format_list.append(format.format(
    "clave_sat", "string", util.col2num("Z"), "", "", ""))
format_list.append(format.format("unidad_sat", "string",
                   util.col2num("AA"), "", "", ""))

if (es_franquicia):
    format_list.append(format.format("garantia", "number",
                       util.col2num("AF"), "options", "model", "compare"))
    format_list.append(format.format("comision", "number",
                       util.col2num("AG"), "options", "model", "compare"))
    format_list.append(format.format("comision_especial", "number",
                       util.col2num("AH"), "options", "model", "compare"))

if (es_multisucursal):
    format_list.append(format.format(
        "company_id", "many2many_comas", util.col2num("AF"), "name", "res.company", ""))

format_list2 = []
format_list2.append(format.format(
    "warehouse_id", "static", id_warehouse, 1, "", ""))
format_list2.append(format.format(
    "location_id", "static", id_ubicacion, 1, "", ""))
format_list2.append(format.format("product_min_qty",
                    "number", util.col2num("X"), "", "", ""))
format_list2.append(format.format("product_max_qty",
                    "number", util.col2num("W"), "", "", ""))
format_list2.append(format.format(
    "qty_multiple", "number", util.col2num("Y"), 1, "", ""))
format_list2.append(format.format("product_id", "many2one",
                    util.col2num("B"), "NoCreate", "product.product", "name"))

format_list3 = []
if (es_multisucursal):
    format_list3.append(format.format(
        "company_id", "static", id_company, id_company, 1, 1))
format_list3.append(format.format(
    "location_in_id", "static", id_ubicacion, id_ubicacion, 1, 1))
format_list3.append(format.format("location_out_id", "many2one", util.col2num(
    "AI"), "NoCreate", "stock.location", "name"))
format_list3.append(format.format("product_id", "many2one", util.col2num(
    "B"), "NoCreate", "product.product", "default_code"))


u = uploader.uploader()
u.upload("product.template", format_list, fila_inicial,
         fila_final, nombre_archivo, [("unique", "default_code")])
if (cargar_minimos):
    u.upload("stock.warehouse.orderpoint", format_list2,
             fila_inicial, fila_final, nombre_archivo)
if (cargar_almacen_inicial):
     u.upload("stock.putaway.rule", format_list3,
             fila_inicial, fila_final, nombre_archivo)

# Creando la lista
# Modificar por cada lista
format_list = []
for i, n in enumerate(listas_precios):
    id_lista = c.env["product.pricelist"].create({"name": n})
    id_listas_precios.append(id_lista)
    print("Lista creada {}".format(id_lista))
    format_list.append(format.format(
        "applied_on", "static", 1, "1_product", 1, 1))
    format_list.append(format.format("min_quantity", "static", 1, 0, 1, 1))
    format_list.append(format.format(
        "compute_price", "static", 1, "fixed", 1, 1))
    format_list.append(format.format("product_tmpl_id", "many2one", util.col2num(
        "C"), "NoCreate", "product.template", "default_code"))
    format_list.append(format.format("fixed_price", "number",
                       util.col2num(columnas_listas_precios[i]), "", "", ""))
    format_list.append(format.format(
        "pricelist_id", "static", 1, id_lista, 1, 1))
    u.upload("product.pricelist.item", format_list,
         fila_inicial, fila_final, nombre_archivo)