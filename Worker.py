

class ImproperInput(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "Improper Input given: {}".format(self.value)


class Worker():
    def __init__(self,level=2):
        self.level = level
        pass

    def output(self,*msg):
        print(*msg)

    def input(self,promt):
        data = input(promt)
        data = self.validateInput(data)
        return data

    def validateInput(self,data):
        data =str(data)
        data = data.strip(' ')
        data = data.strip('\n')
        if len(data) > 1:
            raise ImproperInput('Improper Input')
        else:
            return data
    def removeEmptyStringFromList(self,data):
        xdata = []
        for row in data:
            if row != '':
                xdata.append(row)
        return xdata


    def processItem(self,item):
        item =item.strip(' ')
        item = item.upper()
        return item
    
    def getList(self,filename):
        with open(filename,'r') as file:
            data = file.read()
            data = data.split('\n')
            data = self.removeEmptyStringFromList(data)
            data = [ self.processItem(item) for item in data]
        return data
    
    def debug(self,msg):
        if self.level >= 0: #Replace with Logging
            with open('hangman.log','a') as file:
                file.write('Debug: {}\n'.format(msg))

