def phone_format(s)
    only_digits = s.gsub(/\D/, '')
    formatted_number = ''
    start = 0
    loop do
        # we want to avoid a single digit in the final grouping
        if only_digits.length - 4 == start
            group_length = 2
        else
            group_length = 3
        end
        formatted_number << only_digits.slice(start, group_length)
        start += group_length

        break if start >= only_digits.length

        formatted_number << '-'
    end

    return formatted_number
end
