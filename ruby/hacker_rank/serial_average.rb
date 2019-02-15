def serial_average(string)
    average = ((Float(string[4..8]) + Float(string[10..14])) / 2).round(2)
    return "#{string[0..2]}-#{average}"
end

p serial_average('001-12.43-56.78')
p serial_average('002-10.00-20.00')
