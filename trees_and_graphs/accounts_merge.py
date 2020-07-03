from typing import List, Set
from pprint import pprint
from dataclasses import dataclass

DEBUG = False

def log(o, label=None, *args, **kwargs):
    if DEBUG:
        if label is not None:
            print(label)
            pprint(o)
            print()
        else:
            print(*args, **kwargs)

@dataclass
class Account:
    id: int
    name: str
    emails: Set[str]

class Solution:
    def process_email(self, email, id, accounts, e2a, id2a, processed_emails):
        if email in processed_emails:
            return
        processed_emails.add(email)

        for acc in e2a[email]:
            if id in id2a:
                id2a[id].emails |= acc.emails
            else:
                id2a[id] = Account(acc.id, acc.name, set(acc.emails))

            for e in acc.emails:
                self.process_email(e, id, accounts, e2a, id2a, processed_emails)


    def accountsMerge(self, accs: List[List[str]]) -> List[List[str]]:
        accounts = []

        for acc in accs:
            accounts.append(Account(None, acc[0], set(acc[1:])))

        e2a = dict()
        for acc in accounts:
            for email in acc.emails:
                if email in e2a:
                    e2a[email].append(acc)
                else:
                    e2a[email] = [acc]

        log(accounts, label='ACCOUNTS')
        log(e2a, label='E2A')

        processed_emails = set()
        id2a = dict()
        id = 0
        for email in e2a:
            self.process_email(email, id, accounts, e2a, id2a, processed_emails)
            id += 1

        ret = []
        for acc in id2a.values():
            ret.append([acc.name] + sorted(list(acc.emails)))

        return ret

DEBUG = False

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().accountsMerge(input))

    def test_1(self):
        self.compare([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]], [])

if __name__ == '__main__':
    unittest.main()
