__author__ = 'technodog'
# nim game automatic setup (initial values)
import random
import sys, os
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
heapNo = [3, 5, 7]
objectNo = [9, 11, 13]
randHeap = random.choice(heapNo)

heap = [] #number of heaps
for i in range(randHeap):
    heap.append(random.choice(objectNo))

print "Created", randHeap, "heaps of sizes", ' '.join(map(str, heap)) #to remove the [] from heaps

# players and their selection
players = ["human", "computer"]
player = random.choice(players)

print "Player", player, "goes first"

# valid moves for Computer & Human
while True:
    if player == "computer":
        X = random.choice(range(randHeap))
        while heap[X] == 0:
            X = random.choice(range(randHeap))
        Y = random.choice(range(heap[X])) + 1
        print "Player computer took", Y, "objects from heap", X+1
        heap[X] -= Y

    else:
        while True:
            print "Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X"
            try :
                Y, X = map(int, raw_input().split())
                if 0 < Y <= heap[X-1] and X > 0:
                    heap[X-1] -= Y
                    break

                else:
                    heap[X-1] <= 0
                    print "Player human that is an invalid move, try again"

            except :
                print "Player human that is an invalid move, try again"

# updated status
    print ' '.join(map(str, heap))

# check win or loose status
    win = True
    for i in heap:
        if i != 0:
            win = False
    if win:
        print "Player", player, "has won"
        break
# player switch
    elif player == "human":
        player = "computer"

    else:
        player = "human"
