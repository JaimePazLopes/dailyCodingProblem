# Problem #21 [Easy]
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def quantityOfClassroom(classes):
    # if there is no classes, you need 0 classrooms
    if len(classes) == 0:
        return 0
    if classes is None:
        return 0
    # if there are classes, at least 1 classroom is needed
    maxrooms = 1
    # for each class
    for startA, endA in classes:
        rooms = 0
        # see if another class
        for startB, endB in classes:
            # has the same time, i consider that if a class end in time X, another can start at X. endB+1 to avoid that
            if startA in range(startB, endB) or startA in range(startB, endB):
                # if there is, you need another room
                rooms += 1
        else:
            # if the number of necessary rooms for class A to happen is bigger than maxrooms
            if rooms > maxrooms:
                maxrooms = rooms

    return maxrooms


classesA = [(30, 75), (0, 50), (60, 150)]
print(quantityOfClassroom(classesA))

classesB = [(230, 275), (1, 50), (60, 150)]
print(quantityOfClassroom(classesB))

classesC = [(0, 50), (10, 60), (20, 70), (30, 80), (40, 90), (50, 100), (60, 110), (70, 120), (80, 130), (90, 140), (100, 150)]
print(quantityOfClassroom(classesC))

classesD = [(1, 10), (2, 11), (3, 12), (20, 30)]
print(quantityOfClassroom(classesD))

# i didnt like this solution O(n²) sounds too much for this problem, but i could found a better solution.
# looking online everyone use heapq, didnt remember about this structure
import heapq

def quantityOfClassroomHeap(classes):
    if classes is None:
        return 0
    # put all the classes in order by the start time
    sortedClasses = sorted(classes, key=lambda x: x[0])
    heap = []
    maxrooms = 0
    # for each sortedclass
    for start, end in sortedClasses:
        # heap[0] is the soonest end that can have time conflict
        # it this end is sooner than start, there is no conflict, keep checking for all heap
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        # add the actual end to the heap
        heapq.heappush(heap, end)
        # if the heap is bigger them max rooms
        if len(heap) > maxrooms:
            maxrooms = len(heap)
    return maxrooms

print(quantityOfClassroomHeap(classesA))
print(quantityOfClassroomHeap(classesB))
print(quantityOfClassroomHeap(classesC))
print(quantityOfClassroomHeap(classesD))

# this took me a lot of time, i really could see the answer at first, I start trying to do better than O(n²),
# but couldnt get there. then i went to the O(n²), but was getting something wrong for a long time, deleted everything
# and start from the beginning, all that took me more than 2 hours. +1 hour for googling the heap solution and
# understanding it
