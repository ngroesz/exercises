#!/usr/bin/env ruby

# the problem statement is:
# Compute the number of distinct y values within the range -10000 ≤ y ≤ 10000 such that there are distinct numbers a, b in the file where a + b = y

# the way this program works:
#   - it accepts a filename as the first argument
#   - it reads all the integers from that file (separated by newlines) and stores the set of unique integers from that file
#   - it iterates over evey integer in the set, and:
#       - iterate over every integer in the set, ignoring identical integers and tests if the two integers meet the conditions specified above

# This has an O(n^2) runtime
# Each possible combination of integers is compared twice (which is pretty bad, even for a naive implementation)

LOWER_BOUND = -10_000
UPPER_BOUND = 10_000

def read_and_sort_unique_numbers_from_file(filename)
    fh = File.new(filename, 'r')

    numbers = Hash.new

    while line = fh.gets
        number = line.to_i
        numbers[number] = 1
    end
    fh.close

    return numbers.keys.sort
end

filename = ARGV[0]
sorted_numbers = read_and_sort_unique_numbers_from_file(filename)

unique_sums = Hash.new

for index_j in 0..sorted_numbers.size - 1
    j = sorted_numbers[index_j]
    for index_k in index_j..sorted_numbers.size - 1
        k = sorted_numbers[index_k]
        next if j == k
        if(j + k >= LOWER_BOUND && j + k <= UPPER_BOUND) then
            unique_sums[j + k] = 1
        end 
    end
end

results = unique_sums.keys.sort

puts results.count
