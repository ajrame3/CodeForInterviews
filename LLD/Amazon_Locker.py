'''
Interviewer: An Amazon pickup location has various lockers for packages to be dropped off and picked up. 
We have both packages and lockers of varying sizes. Model the lockers, packages, and pickup location 
and implement an algorithm to find the best possible empty locker for a given package efficiently.

Start with Clarifying Questions
A sample communication between a candidate and an interview can look like:

What are the sizes for packages and lockers?
Small, Medium, Large
Can I assume that a package should go to the corresponding locker size?
Yes
What if there is no small locker left and a small package arrives?
Good question, if there is no locker with matching size of the package, the package should go to the 
next locker size available (e.g. Small package goes inside of a medium locker)
Nice, how many lockers from each size exist in the pickup location?
It changes per pickup location. Your model should be able to handle that.
Understood, what if a package arrives and there is no valid locker available?
Your pickup location should not accept the package.
What do you mean by finding an empty locker efficiently?
Well, customers drop and pick up packages constantly. The lockers becomes full and empty constantly 
as well. Your code should be able to find an available locker very quickly.
And the list of questions can go on (consider the interview time as well when asking questions) 
but you got the idea.

Propose Your Solution
Before you try to write any code, communicate with the interviewer about your approach 
(absolutely important). The interviewer might be able to help you right away if your solution 
cannot handle the requirements properly.

Note that there is no best solution for a problem. It’s a matter of proposing a good enough 
solution while being able to justify it. At first, you start with mentioning your classes, 
like separate classes for PickupLocation, Locker, and Package. For the logic, 
one possible solution is to use queues to track empty lockers for each size and a hash map to 
keep track of used lockers. Once you get a green light from the interviewer on your general approach,
 start coding your solution.

One possible implementation looks like the below (remember that there is no best answer and 
your code can be much different from this):

'''

from enum import Enum
from collections import deque
import uuid

class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

    def get_num_val(self):
        return self.value

class PickupLocation:
    def __init__(self, locker_sizes):
        self.available_lockers = {}
        self.package_loc = {}
        # Initialize lockers
        for size, count in locker_sizes.items():
            locker_q = deque()
            for _ in range(count):
                locker_q.append(Locker(size))
            self.available_lockers[size] = locker_q

    def assign_package(self, package):
        for size in Size:
            # Don't try to assign package to a smaller size
            if size.get_num_val() < package.get_size().get_num_val():
                continue
            assigned_locker = self.assign_locker(package, size)
            # There is a locker found for the package
            if assigned_locker:
                return assigned_locker
            # Continue with one size larger
        return None

    def get_package(self, package_id):
        if package_id not in self.package_loc:
            return None
        locker = self.package_loc[package_id]
        p = locker.empty_locker()
        # Put the locker back in the available queue
        self.available_lockers[locker.get_size()].append(locker)
        return p

    def assign_locker(self, package, size):
        if len(self.available_lockers[size]) == 0:
            return None
        # Remove locker from the available queue
        locker_to_assign = self.available_lockers[size].popleft()
        locker_to_assign.assign_package(package)
        self.package_loc[package.get_id()] = locker_to_assign
        return locker_to_assign

class Locker:
    def __init__(self, size):
        self.locker_size = size
        self.locker_id = uuid.uuid4().hex
        self.package_inside_locker = None

    def get_size(self):
        return self.locker_size

    def get_id(self):
        return self.locker_id

    def assign_package(self, package):
        self.package_inside_locker = package

    def empty_locker(self):
        p = self.package_inside_locker
        self.package_inside_locker = None
        return p

class Package:
    def __init__(self, size):
        self.package_size = size
        self.package_id = uuid.uuid4().hex

    def get_size(self):
        return self.package_size

    def get_id(self):
        return self.package_id
