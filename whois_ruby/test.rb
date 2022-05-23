require 'ostruct'
require 'optparse'

options = OpenStruct.new
OptionParser.new do |opts|
  opts.on('-u', '--username username', 'username') { |v| options[:username] = v }
  opts.on('-a', '--age age', 'age') { |v| options[:age] = v }
end.parse!

puts "username is #{options[:username]}, age is #{options[:age]}"
