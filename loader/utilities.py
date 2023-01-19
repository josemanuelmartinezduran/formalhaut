import string

class utilities():
    def cleanNumber(self, texto):
        nuevoTexto = texto.strip()
        nuevoTexto= nuevoTexto.replace("-", "")
        nuevoTexto= nuevoTexto.replace(",", "")
        nuevoTexto= nuevoTexto.replace("/", "")
        nuevoTexto= nuevoTexto.replace("&", "")
        nuevoTexto= nuevoTexto.replace("'", "")
        nuevoTexto= nuevoTexto.replace("\"", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("$", "")
        nuevoTexto= nuevoTexto.replace("N/A", "")
        nuevoTexto = nuevoTexto.strip()
        return nuevoTexto
    
    def cleanString(self, texto):
        nuevoTexto = texto.strip()
        nuevoTexto = texto.strip()
        return nuevoTexto
        

    def getIdCreate(self, nombre, model, odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([('name', 'ilike', nombre)]):
            model_id = cat
        if(model_id == ""):    
             model_id = category_class.create({
                'name':  nombre,
            })
        return model_id
    
    def getIdCreate(self, nombre, model, campo, odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([(campo,'ilike',nombre)]):
            model_id = cat
        if(model_id==""):    
             model_id = category_class.create({
            'name': nombre,
        })
        return model_id
    
    def existsInModel(self, model, field, value, odoo):
        found = False
        check_class =  odoo.env[model]
        for check in check_class.search([(field, '=', value)]):
            found = True
        return found

    def getIdNoCreate(self,nombre, model,odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([('name','ilike',nombre)]):
            model_id = cat
        return model_id
    
    def getIdNoCreate(self,nombre,model,campo,odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([(campo,'ilike',nombre)]):
            model_id = cat
        return model_id
    
    def getIdNoCreateCompany(self, nombre, model, campo, company, odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([(campo,'ilike',nombre),("company_id", "=", company)]):
            model_id = cat
        return model_id
    
    def getObject(self, field, needle, model, odoo):
        category_class = odoo.env[model]
        object = None
        for cat in category_class.search([(field,'ilike', needle)]):
            object = category_class.browse(cat)
        return object


    def deleteAll(self, model, odoo):
        delete_class = odoo.env[model]
        for i in  delete_class.search([]):
            delete_class.unlink( [i])


    def replaceString(self, texto, encuentra, reemplaza):
        contador = 0
        for i in encuentra:
            if texto == i:
                return reemplaza[contador]
            contador += 1

    def strToBoolean(self, texto):
        if texto.upper() in ["SI", "VERDADERO", "TRUE", "OK", "YES"]:
            return True
        else:
            return False

    
    def selectionToString(self, texto, tupleList):
        retorno = ""
        for elemento in tupleList:
            if texto.upper() == elemento[0].upper():
                retorno = elemento[1]
        return retorno


    def writeError(self, error):
        with open('errores.txt', 'a') as f:
            f.write("{} \n".format(error))

    def col2num(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num += num * 26 + (ord(c.upper()) - ord('A')) +  1
        return (num - len(col))