import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
deleter = uploader.deleter()

deleter.delete_model("stock.warehouse.orderpoint", 1, 1000)
deleter.delete_model("stock.move", 1, 10000)
deleter.delete_model("stock.picking", 1, 10000)
deleter.delete_model("product.template", 0, 1000, [])