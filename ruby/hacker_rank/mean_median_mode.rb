def mean(numbers)
    sum = 0
    numbers.each { |n| sum+=n }
    return sum / numbers.length.to_f
end

def median(numbers)
    sorted_numbers = numbers.sort
    middle_index = sorted_numbers.length / 2
    if sorted_numbers.length % 2 == 0
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2.to_f
    else
        return sorted_numbers[middle_index]
    end
end

def mode(numbers)
    counts = Hash[numbers.collect { |n| [n, 0] }]
    numbers.each { |n|
        counts[n] += 1
    }

    highest_frequency = counts.values.max
    numbers_with_highest_frequency = []
    counts.each { |n, frequency|
        if frequency == highest_frequency
            numbers_with_highest_frequency.push(n)
        end
    }

    numbers_with_highest_frequency = numbers_with_highest_frequency.sort
    return numbers_with_highest_frequency.sort[0]
end


n = gets.chomp.to_i
numbers = gets.split(' ').map { |s| s.to_i }

puts "#{mean(numbers).round(1)}"
puts "#{median(numbers).round(1)}"
puts "#{mode(numbers)}"


