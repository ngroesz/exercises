def skip_animals(animals, skip)
    result = []
    animals.each_with_index { |animal, index| result.push("#{index}:#{animal}") if index >= skip }
    return result
  # Your code here
end

p skip_animals(['leopard', 'bear', 'fox', 'wolf'], 2)
