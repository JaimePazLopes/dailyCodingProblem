# Problem #92
#
# We're given a hashmap with a key courseId and value a list of courseIds, which represents that the prerequsite of
# courseId is courseIds. Return a sorted ordering of courses such that we can finish all courses.
#
# Return null if there is no such ordering.
#
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
# should return ['CSC100', 'CSC200', 'CSC300'].


def sort_courses(courses: dict):
    ordered = list()

    # to help with not being able to change the dict during iterations
    to_order = courses.copy()

    # while there is a course to order
    while len(courses) > 0:
        change = False
        # look into all courses
        for course in courses:
            # if there is no requirement
            if not courses[course]:
                change = True
                # order it
                ordered.append(course)
                # and remove from the courses dict
                if course in to_order.keys():
                    del to_order[course]

        # if no course was ordered, there is no way to order
        if not change:
            return None

        # update the requirements by removing the ordered courses
        for course in to_order:
            to_order[course] = list(set(to_order[course]) - set(ordered))

        courses = to_order.copy()

    return ordered


courses_info = {}
assert sort_courses(courses_info) == []

courses_info = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
assert sort_courses(courses_info) == ['CSC100', 'CSC200', 'CSC300']

courses_info = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100']}
assert sort_courses(courses_info) is None

courses_info = {'CSC300': ['CSC100'], 'CSC200': ['CSC100'], 'CSC100': []}
assert sort_courses(courses_info) == ['CSC100', 'CSC300', 'CSC200']

# at first looked very complex, but by doing it was easy to find a solution. took me around 30 minutes
