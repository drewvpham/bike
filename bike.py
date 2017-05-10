class Bike(object):

    def __init__(self, price, max_speed, miles=0):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles

    def displayInfo(self):
        print 'I costed ${}'.format(self.price)
        print 'I have a top speed of {}'.format(self.max_speed)
        print 'I have been riden for {} miles'.format(self.miles)

    def ride(self, num):
        print 'Riding this bike'
        for x in range(0,num):
            self.miles+=10
        return self

    def reverse(self, num):
        print 'Reversing this bike'
        for x in range(0,num):
            self.miles-=5
        if self.miles<0:
            self.miles=0
        return self

bike1=Bike(200, "25mph")
bike2=Bike(300, "1mph")
bike3=Bike(5000000, "2mph")

bike1.ride(3).reverse(1).displayInfo()
bike2.ride(2).reverse(2).displayInfo()
