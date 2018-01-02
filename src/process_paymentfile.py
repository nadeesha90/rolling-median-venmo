import json
from datetime import datetime
import pdb
import sys

from payments_window import payments_window
#class to process payment file
class process_paymentfile:
    def __init__(self,fname):
        self.fname = fname

    #yeilds dictionary encapsulating the payment
    def payment_gen(self):
        with open(self.fname,'r') as f:
            for line in f:
                payment = json.loads(line.strip()) 
                payment['created_time'] = datetime.strptime(payment['created_time'],'%Y-%m-%dT%H:%M:%SZ')
                yield payment

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    proc_paymentfile = process_paymentfile(input_file)
    payments_window = payments_window(window=60)
    payment_gen = proc_paymentfile.payment_gen()
    
    with open(output_file,'w') as fout:
        for payment in payment_gen:
            payments_window.add_payment(payment)
            fout.write('{:0.2f}'.format(payments_window.get_median_degree()) + '\n')

