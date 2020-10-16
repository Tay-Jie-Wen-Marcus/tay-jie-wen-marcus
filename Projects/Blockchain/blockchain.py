from datetime import datetime
from hashlib import sha256
from json import dumps
from time import time

class Transaction:
    """
    Transaction information to be stored inside a block of the blockchain
    """
    def __init__(self, sender, receiver, tx_datetime, content):
        self.sender = sender
        self.receiver = receiver
        self.tx_datetime = tx_datetime
        self.content = content

    # TODO: RSA to verify who created this transaction

class Block:
    """
    A single block of the blockchain that contains
        1. timestamp: datetime of when the block is created
        2. transaction: Transaction object
        3. previous_hash: hash value of the previous block in the chain
        4. nonce: number that changes so that the hashed value of the
                    block can conform to the requirements of Proof-of-Work
        5. hash: hash value of this block
    """
    def __init__(self, transaction, previous_hash=""):
        self.timestamp = str(datetime.now()).split('.')[0]
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0

    @property
    def hash(self):
        """
        Hash property of a block class
        """
        return sha256((self.timestamp \
                    + dumps(self.transaction.__dict__) \
                    + self.previous_hash \
                    + str(self.nonce) \
                ).encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        """
        Calculate the block hash according to the difficulty set in the chain
        """
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1

        print('Success mine: ', self.hash)

class Blockchain:
    """
    The full blockchain. User can choose the following attributes:
        1. genesis_block: the first block in the chain (instance of Transaction to be used)
        2. pow_min_time: Proof_of_Work minimum time set
        3. mining_reward: Reward to give to miners to incentivise mining. (Not implemented yet)
    """
    __instance__ = None
    difficulty = 2

    def __init__(self, genesis_block, pow_min_time=20, mining_reward=0):
        self.chain = [genesis_block]
        self.mining_reward = mining_reward
        self.pow_min_time = pow_min_time
        self.pending_transaction = []

        if Blockchain.__instance__ is None:
            Blockchain.__instance__ = self
        else:
            raise Exception("Only need one instance of the Blockchain")

    @staticmethod
    def get_instance():
        """
        Throws exception when class have not been initialised before
        Otherwise, returns blockchain instance
        """
        if not Blockchain.__instance__:
            raise Exception("Create your instance of blockchain with the respective properties")
        return Blockchain.__instance__

    @classmethod
    def get_difficulty(cls):
        """
        Returns difficulty level.
        """
        return cls.difficulty

    def get_latest_block(self):
        """
        return latest block in chain
        """
        return self.chain[-1]
    
    def add_new_pending_data(self, transaction):
        """
        Adds transactions into the waiting list to be mined
        """
        self.pending_transaction.append(transaction)

    def mine_pending_data(self, miner_pk):
        """
        Mining the transaction in pending list. Increases difficulty if successful
        mine in time shorter than set POW. 

        Miners reward (not implemented yet)
        
        Implementation depends on individual.
        For demo convenience, loops through all pending transaction in one call
        """
        while len(self.pending_transaction) != 0:
            transaction = self.pending_transaction[0]
            mine_block = Block(transaction, self.get_latest_block().hash)

            start_time = time()
            mine_block.mine_block(self.__class__.difficulty)
            end_time = time()
            
            if end_time - start_time < self.pow_min_time:
                self.__class__.difficulty += 1

            try:
                self.pending_transaction.remove(transaction)
                self.chain.append(mine_block)
                print("Mine time taken: ", end_time - start_time, " | By miner: ", miner_pk)
                # TODO: Implement some form of miner reward scheme
            except:
                pass

    def verify_blockchain(self):
        """
        Verify if blockchain is valid
        Returns true if valid and false otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_blockchain(self):
        """
        Helper function to print entire blockchain for demo
        """
        print()
        print("-------------")
        print("Blockchain")
        print("-------------")
        for block in self.chain:
            print("-------------")
            print('Timestamp: ', block.timestamp)
            print('Transaction: ', block.transaction.__dict__)
            print('Previous Hash: ', block.previous_hash)
            print('Hash: ', block.hash)
            print("-------------")
