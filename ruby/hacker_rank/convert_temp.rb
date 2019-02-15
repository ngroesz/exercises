# In this challenge, your task is to write a method convert_temp that helps in temperature conversion. The method will receive a number as an input (temperature), a named parameter input_scale (scale for input temperature), and an optional parameter output_scale (output temperature scale, defaults to Celsius) and return the converted temperature. It should perform interconversion between Celsius, Fahrenheit and Kelvin scale.
#
# For example,
#
# > convert_temp(0, input_scale: 'celsius', output_scale: 'kelvin')
# => 273.15
# > convert_temp(0, input_scale: 'celsius', output_scale: 'fahrenheit')
# => 32.0
# Note that the input values are lowercase version of corresponding scales.

def convert_temp(temperature, input_scale:, output_scale: 'celsius')
    fahrenheit_to_celsius = lambda { |f| (f - 32.0) * 5.0/9.0 }
    celsius_to_fahrenheit = lambda { |c| (c * 9.0/5.0) + 32.0 }
    celsius_to_kelvin = lambda { |c| c + 273.15 }
    kelvin_to_celsius = lambda { |k| k - 273.15 }
    case input_scale.downcase
        when 'fahrenheit'
            case output_scale.downcase
                when 'fahrenheit'
                    return temperature.round(2)
                when 'celsius'
                    return fahrenheit_to_celsius.call(temperature).round(2)
                when 'kelvin'
                    return celsius_to_kelvin.call(fahrenheit_to_celsius.call(temperature)).round(2)
                else
                    puts "Unknown output_scale '#{output_scale}'"
            end
        when 'celsius'
            case output_scale.downcase
                when 'fahrenheit'
                    return celsius_to_fahrenheit.call(temperature).round(2)
                when 'celsius'
                    return temperature.round(2)
                when 'kelvin'
                    return celsius_to_kelvin.call(temperature).round(2)
                else
                    puts "Unknown output_scale '#{output_scale}'"
            end
        when 'kelvin'
            case output_scale.downcase
                when 'fahrenheit'
                    return celsius_to_fahrenheit.call(kelvin_to_celsius.call(temperature)).round(2)
                when 'celsius'
                    return kelvin_to_celsius.call(temperature).round(2)
                when 'kelvin'
                    return temperature.round(2)
                else
                    puts "Unknown output_scale '#{output_scale}'"
            end
        else
            puts "Unknown input_scale '#{input_scale}'"
    end
end

p convert_temp(0, input_scale: 'celsius', output_scale: 'kelvin')
p convert_temp(0, input_scale: 'celsius', output_scale: 'fahrenheit')
p convert_temp(0, input_scale: 'celsius')
p convert_temp(40, input_scale: 'celsius')
p convert_temp(40, input_scale: 'celsius', output_scale: 'fahrenheit')
p convert_temp(60, input_scale: 'fahrenheit')
p convert_temp(60, input_scale: 'fahrenheit', output_scale: 'kelvin')
p convert_temp(60, input_scale: 'celsius', output_scale: 'kelvin')
p convert_temp(60, input_scale: 'celsius', output_scale: 'fahrenheit')
p convert_temp(60, input_scale: 'kelvin', output_scale: 'fahrenheit')
p convert_temp(60, input_scale: 'kelvin', output_scale: 'celsius')
p convert_temp(60.0004, input_scale: 'kelvin', output_scale: 'kelvin')
