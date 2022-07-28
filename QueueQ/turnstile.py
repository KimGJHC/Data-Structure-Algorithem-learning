"""
https://leetcode.com/discuss/interview-question/699973/

"""

from collections import deque
def getTimes(time, direction):
    """
    :param time:
    :param direction:
    :return: int[n] where i-value is the time when i-th person passed turnstiles
    """

    n = len(time)
    current_second = 0
    enter_queue, leave_queue = deque(), deque() # the queue will store (idx) of a person
    person_idx = 0
    previous_turnstile_statue = "unused" # it will be unused, enter, leave
    pass_time = [-1] * n

    while person_idx < n or enter_queue or leave_queue:
        # now we are at current_second, people need to enter the queue
        while person_idx < n:
            if time[person_idx] == current_second:
                if direction[person_idx] == 0:
                    enter_queue.append(person_idx)
                else:
                    leave_queue.append(person_idx)
            else:
                break
            person_idx += 1

        if not enter_queue and not leave_queue:
            if person_idx == n:
                break
            current_second = time[person_idx]
            previous_turnstile_statue = "unused"
            # we set the current_second to be the earliest time that people can join, let people enter the queue again
            while person_idx < n:
                if time[person_idx] == current_second:
                    if direction[person_idx] == 0:
                        enter_queue.append(person_idx)
                    else:
                        leave_queue.append(person_idx)
                else:
                    break
                person_idx += 1

        if previous_turnstile_statue in ("unused", "leave"):
            if leave_queue:
                pass_time[leave_queue.popleft()] = current_second
                previous_turnstile_statue = "leave"
            else:
                pass_time[enter_queue.popleft()] = current_second
                previous_turnstile_statue = "enter"
        else:
            if enter_queue:
                pass_time[enter_queue.popleft()] = current_second
                previous_turnstile_statue = "enter"
            else:
                pass_time[leave_queue.popleft()] = current_second
                previous_turnstile_statue = "leave"
        current_second += 1

    return pass_time

# time: O(n)
# space: O(n)

def test():
    print(getTimes([0, 0, 1, 5], [0, 1, 1, 0])) #[2, 0, 1, 5]
    print(getTimes([0, 0, 1, 1000000000, 1000000000], [0, 1, 1, 0, 0])) #[2,0,1,1000000000,1000000001]
    print(getTimes([1,1],[1,1]))  # [1,2]
    print(getTimes([1, 1, 3, 3, 4, 5, 6, 7, 7],[1, 1, 0, 0, 0, 1, 1, 1, 1])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(getTimes([0,0,0,0,1,1,4,5,5,5,5,7],[0,1,0,1,1,0,0,1,1,1,1,0]))  # [3, 0, 4, 1, 2, 5, 6, 8, 9, 10, 11, 7]
    print(getTimes([1,2,4],[0,1,1]))  # [1,2,4]