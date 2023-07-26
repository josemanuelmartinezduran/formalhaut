import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()

for p in c.env['res.partner'].search([("id", "<", 715)]):
    try:
        print("BOrrando a {}".format(p))
        c.env['res.partner'].unlink([p])
    except:
        print("No borrado")