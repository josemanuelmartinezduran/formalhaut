import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
deleter = uploader.deleter()

deleter.set_field("sale.order", {'state': 'draft'}, 0, 1000)
deleter.delete_model("sale.order",0, 1000)
deleter.set_field("purchase.order", {'state': 'cancel'}, 0, 1000)
deleter.set_field("account.move", {'state': 'cancel'}, 0, 1000)
deleter.delete_model("account.move", 0, 1000)
deleter.delete_model("crm.lead", 0, 1000)
deleter.delete_model("purchase.order", 0 ,1000)
deleter.delete_model("res.partner", 0, 1000)

