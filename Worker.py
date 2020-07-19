

class ImproperInput(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "Improper Input given: {}".format(self.value)


class Worker():
    def __init__(self):
        pass

    def output(self,*msg):
        print(msg)

    def input(self):
        data = input()
        data = self.validateInput(data)
        return data

    def validateInput(self,data):
        data =str(data)
        data = data.strip(' ')
        data = data.strip('\n')
        if len(data) >= 1:
            raise ImproperInput('Improper Input')
        else:
            return data