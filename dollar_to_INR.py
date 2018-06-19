class Account(object):

    def __init__(self,rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        return self.__amt

    @property
    def rate_value(self):
        return self.rate

    @property
    def inr(self):
        return (self.__amt * self.rate)

if __name__== '__main__':
    obj = Account(rate=66.75)
    obj.amount = 20
    print ("Amount:" ,obj.amount )
    print ("Rate:" , obj.rate_value)
    print ("Calculated:" , obj.inr)