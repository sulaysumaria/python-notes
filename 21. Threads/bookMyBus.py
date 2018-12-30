from threading import Thread, Lock, Semaphore


class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        # self.l = Lock()
        self.l = Semaphore()

    def buy(self, seatsRequested):
        self.l.acquire()
        print('Seats available: ', self.availableSeats)
        if (self.availableSeats >= seatsRequested):
            print('Confirming a seat.')
            print('Processing the payment.')
            print('Printing the ticket.')
            self.availableSeats -= seatsRequested
        else:
            print('Sorry, no seats available.')
        self.l.release()


b1 = BookMyBus(10)
t1 = Thread(target=b1.buy, args=(3,))
t2 = Thread(target=b1.buy, args=(4,))
t3 = Thread(target=b1.buy, args=(4,))

t1.start()
t2.start()
t3.start()
