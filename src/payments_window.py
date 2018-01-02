from min_max_heap import min_max_heap
from payment_graph import payment_graph
import datetime

class payments_window:
    def __init__(self,window=60):
        self.payment_heap = min_max_heap()
        self.payment_graph = payment_graph()
        self.window = 60

    def __add_payment(self,payment):
        self.payment_heap.insert(key=payment['created_time'],val=payment)
        self.payment_graph.insert_edge(payment)
        self.prune_heap()

    def add_payment(self,payment):
        if self.payment_heap.is_empty():
            self.__add_payment(payment)
        else:
            newest_payment_time = self.payment_heap.get_max()['created_time']
            #insert a payment that is within window seconds of the newest payment
            if newest_payment_time - payment['created_time'] <= datetime.timedelta(seconds=self.window):
                self.__add_payment(payment)

    #remove oldest payment until the difference between newest and oldest is within the window 
    def prune_heap(self):
        newest_payment_time = self.payment_heap.get_max()['created_time']
        oldest_payment_time = self.payment_heap.get_min()['created_time']
       
        while newest_payment_time - oldest_payment_time > datetime.timedelta(seconds=self.window) and not self.payment_heap.is_empty():
            payment = self.payment_heap.delete_min()
            self.payment_graph.remove_edge(payment)
            oldest_payment_time = self.payment_heap.get_min()['created_time']

    def get_median_degree(self):
        return self.payment_graph.get_median_degree()
