#!/usr/bin/env ruby

# the problem statement is:
# Compute the number of distinct y values within the range -10000 ≤ y ≤ 10000 such that there are distinct numbers a, b in the file where a + b = y

# the way this program works:
#   - it accepts a filename as the first argument
#   - it reads all the integers from that file (separated by newlines) and stores the set of unique integers from that file
#   - it iterates over each integer and treats that integer as the first summand (or term) and:
#       - recursively performs a binary search of the set to locate a second summand that will produce a sum within the range
#       - iterates over the set, to either side of the index of the second summand, to attempt to locate all possible second terms

LOWER_BOUND = -10_000
UPPER_BOUND = 10_000

# take a filename and return an array of the unique integers within the file
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


# perform a binary search between lower_range and upper_range using recursion
# the condition we are looking to satisfy is that $sorted_numbers[j] + $sorted_numbers[index] is
# between LOWER_BOUND and UPPER_BOUND
def find_a_starting_index_within_range(j, lower_range, upper_range)
    step = ((upper_range - lower_range) / 2).round

    index = lower_range + step
    sum = $sorted_numbers[j] + $sorted_numbers[index]

    # if we found an index that satisifies the conditions, we return it
    if sum.between?(LOWER_BOUND, UPPER_BOUND)
        return index
    end

    # otherwise, we recurse until we find it or we've exhausted the search space

    # return nil if we've exhausted all possiblities
    return nil if step == 0

    if sum < LOWER_BOUND
        # in this case, we are below the lower bound, so we constrain our binary search upwards
        return find_a_starting_index_within_range(j, lower_range + step, upper_range)
    elsif sum > UPPER_BOUND
        # in this case, we are above the upper bound, so we constrain our binary search downwards
        return find_a_starting_index_within_range(j, lower_range, upper_range - step)
    else
        # this should never happen
        raise 'logic error'
    end
end


filename = ARGV[0]
$sorted_numbers = read_and_sort_unique_numbers_from_file(filename)

# we store the results in $unique_sums
$unique_sums = Hash.new

# we just store off the length here, because we refer to it so much
cardinality = $sorted_numbers.length

# we iterate over element in $sorted_numbers; each represents a potential summand
0.upto(cardinality - 1) do |j|
    current_value = $sorted_numbers[j]
    sum = $sorted_numbers[j] * 2
    starting_index = nil

    # we are about to attempt to find an index starting_index, such that LOWER_BOUND < ($sorted_numbers[j] + $sorted_numbers[starting_index]) < UPPER_BOUND
    if sum.between?(LOWER_BOUND, UPPER_BOUND)
        # if the number j * 2 is within the boundaries, we can just start off using identical indexes
        starting_index = j
    elsif sum > UPPER_BOUND
        # if j * 2 is too large, we start our binary search between the 0-th index and the j index
        starting_index = find_a_starting_index_within_range(j, 0, j)
    else
        # if j * 2 is too small, we start our binary search between the j index and the last index in the array
        starting_index = find_a_starting_index_within_range(j, j, cardinality - 1)
    end

    # we only need to iterate over possibilities if there is a possiblity of finding a sum within bounds
    # if starting_index is nil, our binary search showed us that there are no possible summands that will result in a sum within bounds
    if starting_index
        # we examine all of $sorted_numbers[starting_index..length-1]
        # but if the sum is greater than the upper bound, we can skip to the next part
        starting_index.upto(cardinality - 1) do |k|
            # the rules state that the summands must be distinct
            next if k == j
            sum = $sorted_numbers[j] + $sorted_numbers[k]
            break if sum > UPPER_BOUND
            if sum.between?(LOWER_BOUND, UPPER_BOUND)
                # we found summands that satisified the conditions!
                # we record the result
                $unique_sums[sum] = 1
            end
        end

        # similarily to the previous block, we examine every element $sorted_numbers[k..0]
        # but if the sum is less than the lower bound, we can move on to the next number
        starting_index.downto(0) do |k|
            # the rules state that the summands must be distinct
            next if k == j
            sum = $sorted_numbers[j] + $sorted_numbers[k]
            break if sum < LOWER_BOUND
            if sum.between?(LOWER_BOUND, UPPER_BOUND)
                # we found summands that satisified the conditions!
                # we record the result
                $unique_sums[sum] = 1
            end
        end
    end
end

results = $unique_sums.keys.sort

puts results.count
