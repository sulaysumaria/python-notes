from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('Starting the car.')

    def stop(self):
        print('Stopping the car.')

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print('Button start.')

    def drive(self):
        print('Three Series is being driven.')


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print('Five Series is being driven.')


threeSeries = ThreeSeries(True, 'BMW', '328i', '2018')

print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()
