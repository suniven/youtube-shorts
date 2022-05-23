#coding=utf-8
require 'whois'
require 'ostruct'
require 'optparse'

options = OpenStruct.new
OptionParser.new do |opts|
    # 下面第一项是 Short option（没有可以直接在引号间留空），第二项是 Long option，第三项是对 Option 的描述
    opts.on('-d domain', '--domain domain', 'domain name') do |v|
        options[:domain] = v
    end
end.parse!

begin
    # Domain WHOIS
    whois = Whois::Client.new
    domain = options[:domain]
    puts whois.lookup(domain)
    # => #<Whois::Record>
rescue
    puts "ServerNotFound"
end