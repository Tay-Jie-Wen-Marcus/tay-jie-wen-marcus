from datetime import datetime
from blockchain import Blockchain, Block, Transaction

def main():
    '''
    Standard blockchain created with 1 genesis block and mined through all transactions
    '''
    bc = Blockchain(Block(Transaction("Genesis Block", "Genesis Block", \
                    str(datetime.now()).split('.')[0], "Genesis Block"), "0"), \
                    2, 10)
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:00:00', '1x iPhone 11'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia RTX 3090'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia RTX 3080'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia RTX 3070'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia RTX 2080'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia RTX 2060'))
    bc.add_new_pending_data(Transaction('ABC Company', 'CBA Company', '2020-09-04 22:10:00', '1x Nvidia 1080ti'))
    print("Mining information: ")
    bc.mine_pending_data('123')
    bc.print_blockchain()
    print("Blockchain valid: ", bc.verify_blockchain())

if __name__ == "__main__":
    main()
