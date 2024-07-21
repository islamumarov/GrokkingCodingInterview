from typing import List


class TimeNeededBuyTickets:
    def timeRquiredToBuy(self, tickets: List[int], k: int) -> int:
        needs = 0
        i = 0
        while tickets[k] > 0:
            needs += 1
            tickets[i] -= 1
            if tickets[i] == 0:
                tickets.pop(i)
                i -= 1
                k = i
            i += 1
            if i == len(tickets):
                i = 0
        return needs

if __name__ == '__main__':
    sol = TimeNeededBuyTickets

    print(sol.timeRquiredToBuy(sol, [2,3,2], 2))
    print(sol.timeRquiredToBuy(sol, [5,1,1,1], 0))