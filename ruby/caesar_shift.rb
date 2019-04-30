require 'minitest/spec'
require 'minitest/autorun'

# classify_strings runs in O(n) (linear) time.
# A single iteration over each string computes a "hash"
# for each string, which is the distance of each letter
# from the first letter of the string, normalized for the 
# alphabet.
# i.e., for the string "zoom", the hash is computed as [15, 15, 13]
# this is because, using the first letter as are starting point:
# o - shifted 15 places from z
# o - ditto
# m - shifted 13 places from z
# Strings are placed in the appropriate hash (Ruby dictionary) array
# based upon their computed key.

def string_hash(input_string)
    hash = []
    input_string.chars[1..-1].each do |c|
        difference = c.ord - input_string[0].ord > 0 ?
                        c.ord - input_string[0].ord :
                        c.ord - input_string[0].ord + 26
        hash.push(difference)
    end

    return hash
end

def classify_strings(strings)
    strings_by_hash = Hash.new { |hash, key| hash[key] = [] }

    strings.each do |string|
        hash_value = string_hash(string)
        strings_by_hash[hash_value].push(string)
    end

    return strings_by_hash.values.to_a
end


class TestStringClassification < MiniTest::Test
    def test_string_sorting
        assert(classify_strings(['abc', 'bcd', 'acd', 'bde']).sort == [['abc', 'bcd'], ['acd', 'bde']].sort)
        assert(classify_strings(['zap', 'zam', 'jkz', 'efu', 'yzo']).sort == [['zap', 'jkz', 'efu', 'yzo'], ['zam']].sort)
        assert(classify_strings(['nick', 'cxrz', 'dysa', 'toiq']).sort == [['nick', 'cxrz', 'dysa', 'toiq']].sort)
    end
end
