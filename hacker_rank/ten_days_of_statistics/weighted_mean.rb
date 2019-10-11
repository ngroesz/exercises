n = gets.chomp.to_i
integers = gets.split(' ').map { |s| s.to_i }
weights = gets.split(' ').map { |s| s.to_i }

raise ArgumentError, "Expected #{n} elements and weights" unless n == integers.length && n == weights.length

sum = 0
integers.zip(weights) { |n, w| sum += n * w }

weights_sum = 0
weights.each { |w| weights_sum += w }

puts "#{(sum / weights_sum.to_f).round(1)}"
