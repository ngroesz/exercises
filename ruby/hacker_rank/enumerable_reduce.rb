def sum_terms(n)
    return (1..n).inject { |sum, i| sum + (i**2 + 1) }
end

p sum_terms(25)
