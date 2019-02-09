def phone_format(s)
    groups = s.gsub(/\D/, '').split('').each_slice(3).map{|g| g.join()}.join('-')
    groups = groups.gsub(/(\d)-(\d)$/, '-\1\2')
    #groups.gsub(-(\d)$/, 'blah')
    p groups
    #puts "array: #{digits_array}"
    #digits_array.each_slice(3) { |g| p g }
end

phone_format("555 123 1234")
phone_format("(+1) 888 33x19")
phone_format('1')
phone_format('12')
phone_format('123')
phone_format('1234')
phone_format('12345')
phone_format('123456')
phone_format('1234567')
phone_format('12345678')
phone_format('123456789')
phone_format('12345678910')
phone_format('1234567891011')
phone_format('123456789101112')
