class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(card)

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        if self.is_empty():
            print("Queue is empty. Cannot pop.")
            return None
        else:
            return self.cards.pop(0)
        

if __name__ == '__main__':
     my_queue = Queue()
     my_queue.push("Card1")
     my_queue.push("Card2")
     my_queue.push("Card3")
     popped_card = my_queue.pop()
     if popped_card is not None:
        print(f"Popped card: {popped_card}")
     popped_card = my_queue.pop()
     if popped_card is not None:
        print(f"Popped card: {popped_card}")
     my_queue.push("Card4")
     my_queue.push("Card5")
     popped_card = my_queue.pop()
     if popped_card is not None:
        print(f"Popped card: {popped_card}")

     popped_card = my_queue.pop()
     if popped_card is not None:
        print(f"Popped card: {popped_card}")
     popped_card = my_queue.pop()
     if popped_card is not None:
        print(f"Popped card: {popped_card}")