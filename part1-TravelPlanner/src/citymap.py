from collections import deque
import json
import os


def load_data(source_file):
    """Reading JSON from the file and deserializing it
    :param source_file: JSON map of tram stops (str)
    :return: obj (array)
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, '..', source_file)) as file:
        return json.load(file)


class State:

    def __init__(self, stop, previous=None):
        """ State lets you trace back the route from the last stop
        :attr stop: Code of the stop (str)
        :attr previous: Previous state of the route (State)
        """
        self.stop = stop
        self.previous = previous


    def __str__(self):
        """ Returns route as a string from the last stop to the beginning. 
        Format: 1030423 -> 1010420 -> 1010427 
        """
        result = self.stop
        state = self.previous
        while state is not None:
            result += " -> " + state.stop
            state = state.previous

        return result

    def get_stop(self):
        return self.stop

    def get_previous(self):
        return self.previous


class CityMap:
    """Storage of the tram network stops
    :attr data: (obj)
    :attr stops: dictionary {stop_code: stop}
    """
    def __init__(self, source_file):
        self.data = load_data(source_file)
        self.stops = {}
        for stop in self.data:
            self.stops[stop["code"]] = stop

    def get_neighbors(self, stop_code):
        """Returns dictionary containing all neighbor stops """
        return self.stops.get(stop_code)["neighbors"]

    def get_neighbors_codes(self, stop_code):
        """Returns codes of all neighbor stops """
        return list(self.stops.get(stop_code)["neighbors"].keys())

    def search(self, start, goal):
        """Thsi performs a simple breadth-first search and returns the path from the starting stop to the 
        ending stop as a linked list of States. In the list, the first node contains the goal stop code and each 
        node is linked to the previous node in the path. The last node in the list is the starting stop
        and its previous node is None.

        :param start: Code of the initial stop (str)
        :param goal: Code of the last stop (str)
        :returns (obj)
        """
        
        queue = deque()
        queue.append(State(start))
 
        visited=[start]
        
        while len(queue) != 0:
            cur_road=queue.popleft()
            neighbors = self.get_neighbors(cur_road.get_stop())
            for neighbor in neighbors:
                if neighbor not in visited:
                    state = State(neighbor,cur_road)
                    if neighbor == goal:
                        return state
                    queue.append(state)
                    visited.append(neighbor)
        return None
