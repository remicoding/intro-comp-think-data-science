"""
Remi Coding
Problem Set 1 from Introduction to Computational Thinking and Data Science
MITOPENCOURSEWARE
"""

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # initialize dictionary that maps cow's names:weights pairs
    cows_dict = {}
    with open(filename) as file_name:
        # read in file content
        for line in file_name:
            # clean file content
            line = line.strip('\n')
            line = line.split(',')
            # enter cow name and weight pairs in dictionary
            cows_dict[line[0]] = int(line[1])
    return cows_dict


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # copy and sort dictionary content
    cows_copy_list = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    # initialize list of all trips
    trips_list = []
    # loop throup list of cows as long as not empty
    while cows_copy_list:
        # initialize lists of each trip and indexes of cows picked
        # initialize total weight picked for trip and number of cows picked
        trip_list, index_list, total_weight, cows_num = [], [], 0.0, 0
        for index, (cow_name, cow_weight) in enumerate(cows_copy_list):
            # check if cow can be added to trip
            if (total_weight + cow_weight) <= limit:
                # add cow's name to trip list
                trip_list.append(cow_name)
                # add cow's weight to total weight
                total_weight += cow_weight
                # add cow's index to index list removing the number of cows picked
                # to account for dynamically modifying list length
                index_list.append(index - cows_num)
                # increase number of cows picked
                cows_num += 1
        # add trip to list of trips
        if trip_list:
            trips_list.append(trip_list)
        # remove cows picked from list of cows
        for index in index_list:
            del cows_copy_list[index]

    return trips_list


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # copy dictionary's content
    cows_copy_list = [(cow_name, cow_weight)
                      for (cow_name, cow_weight) in cows.items()]
    # initialize the minimum number of trips and the cows taken on that trip
    min_num_trip, cows_taken = len(cows_copy_list), None
    # iterate over all possible partitions of cows in the list
    for cow_partitions in get_partitions(cows_copy_list):
        # initialize number of trips
        num_trip, weight_trip_list = 0, []
        # iterate over cows in partition
        for cows in cow_partitions:
            # increment number of trips
            num_trip += 1
            # add the weight of the trip to the list of weight for each trip
            weight_trip_list.append(sum([cow_weight
                                         for _, cow_weight in cows]))
        # check if maximum weight is less than limit and if number of trip is less than minimum number of trip
        if max(weight_trip_list) <= limit and num_trip < min_num_trip:
            # update minimum number of trip and cows taken
            min_num_trip = num_trip
            cows_taken = [[cow[0] for cow in cows_trip]
                          for cows_trip in cow_partitions]
    return cows_taken


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # running and measuring time for brute_force_cow_transport
    result, time = timing_algorithm(brute_force_cow_transport)
    print_algorithm_result("brute force", result, time)

    # running and measuring time for greedy_cow_transport
    result, time = timing_algorithm(greedy_cow_transport)
    print_algorithm_result("greedy", result, time)


def timing_algorithm(algorithm):
    """Run provided algorithm as a function on selected dataset.
       Returns result of run of algorithm and running time."""
    start = time.time()
    result = algorithm(load_cows('datasets/ps1_cow_data.txt'))
    end = time.time()
    return result, end - start


def print_algorithm_result(name, result, time):
    """Formats and prints name, result and time."""
    print(f"\nResults for {name} algorithm:")
    print(f"  - Number of trips: {len(result)}")
    print(f"  - Time: {time:.5f} seconds")


def main():
    """Runs different parts of this module with comments and results."""
    # Problem 4
    compare_cow_transport_algorithms()


if __name__ == '__main__':
    main()