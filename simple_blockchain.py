import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(0, "Genesis Block")

    def create_block(self, index, data):
        timestamp = time.time()
        previous_hash = self.chain[-1].hash if self.chain else "0"
        block = Block(index, timestamp, data, previous_hash)
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} | Hash: {block.hash} | Previous Hash: {block.previous_hash} | Data: {block.data}")

def main():
    blockchain = Blockchain()

    while True:
        data = input("Enter data for the block (or type 'exit' to quit): ")
        if data.lower() == 'exit':
            break
        last_block = blockchain.get_last_block()
        new_block = blockchain.create_block(last_block.index + 1, data)
        print(f"Block {new_block.index} added to the blockchain!")

    print("\nCurrent Blockchain:")
    blockchain.display_chain()

if __name__ == "__main__":
    main()
