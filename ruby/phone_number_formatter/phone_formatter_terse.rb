def phone_format(s)
    return s.gsub(/\D/, '').gsub(/(\d{2}(?=\d{2}$)|\d{3}(?=\d))/, '\1-')
end

puts phone_format("555 123 1234")
puts phone_format("(+1) 888 33x19")
puts phone_format('1')
puts phone_format('12')
puts phone_format('123')
puts phone_format('1234')
puts phone_format('12345')
puts phone_format('123456')
puts phone_format('1234567')
puts phone_format('12345678')
puts phone_format('123456789')
puts phone_format('12345678910')
puts phone_format('1234567891011')
puts phone_format('123456789101112')
