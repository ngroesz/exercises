import re

class LoadTestData():
    def __init__(self, filename):
        self.filename = filename
        self.problems = []
        self.read_test_data()

    def read_test_data(self):
        with open(self.filename, 'r') as test_data:
            current_problem = {'graph': [], 'solution': None}
            for line in test_data:
                line = line.strip()

                if not line:
                    self.problems.append(current_problem)
                    current_problem = {'graph': [], 'solution': None}
                    continue

                single_digit_match = re.match('^(\d+)$', line)
                if single_digit_match:
                    current_problem['solution'] = int(single_digit_match.group(1))
                    continue

                r = line.split()
                row = list(map(lambda x: int(x), line.split()))
                current_problem['graph'].append(row)
            self.problems.append(current_problem)
