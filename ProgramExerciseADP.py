class Food:
    def __init__(self,food,amount):
        self.__foodName = food
        self.__foodAmt = amount
        self.__foodPrice = None
        self.__calcPrice = None

    def getFoodName(self):
        return self.__foodName
    
    def getFoodAmount(self):
        return self.__foodAmt
    
    def getPriceList(self):
        return self.__foodPrice
    
    def priceCalculator(self):
        return self.__calcPrice
    
    def priceList(self):
        if self.__foodName == 'Dry Cured Iberian Ham':
            self.__foodPrice = 177.80
        elif self.__foodName == 'Wagyu Steaks':
            self.__foodPrice = 450.00
        elif self.__foodName == 'Matsutake Mushrooms':
            self.__foodPrice = 272.00
        elif self.__foodName == 'Kopi Luwak Coffee':
            self.__foodPrice = 306.40
        elif self.__foodName == 'Moose Cheese':
            self.__foodPrice = 487.20
        elif self.__foodName == 'White Truffles':
            self.__foodPrice = 3600.00
        elif self.__foodName == 'Blue Fin Tuna':
            self.__foodPrice = 3603.00
        elif self.__foodName == 'Le Bonnotte Potatoes':
            self.__foodPrice = 270.81
        else:
            print(f'bad')

    def costCalculation(self):
        if self.__foodName in self.__foodPrice:
            self.__calcPrice = self.__foodAmt * self.__foodPrice(self.__foodName)
        return self.__calcPrice
    
    def __str__(self):
        return f'Name: {self.__foodName} Amount: {self.__foodAmt}'\
               f'Standard Price per Pound: {self.__foodPrice}'
    
    def _str_(self):
        return f"Food: {self.__foodName}, Amount: {self.__foodAmt} pounds, " \
               f"Standard Price per Pound: {self.__foodPrice}, " \
               f"Calculated Price: {self.__calcPrice}"  
