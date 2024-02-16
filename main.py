class Queue():
    def __init__(self):
        self.cards = []
    def push(self, card):
        self.cards.append(card)
    def pop(self):
        if self.is_empty():
            print("Queue is empty. Cannot pop.")
            return None
        else:
            return self.cards.pop(0)
    def is_empty(self):
        return len(self.cards) == 0
        

if __name__ == '__main__':
     my_queue = Queue()