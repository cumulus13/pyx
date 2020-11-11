require 'requests'
require 'io/console'
require 'ruby-progressbar'
require 'optparse'

class Kodi

	@@KODI_SERVER = '192.168.43.2'
	@@KODI_PORT = 8080

	def self.Initialize
		@URL = ''
	end

	def self.UpdateLibrary(type, server:nil, port:nil)
		# data = {}
		if not server
			server = @@KODI_SERVER
		end
		
		if not port
			port = @@KODI_PORT
		end

		if type == 'video'
			@id = 'libMovies'
			@method = 'VideoLibrary.Scan'
		elsif type == 'audio'
			@id = 'libMusics'
			@method = 'MusicLibrary.Scan'
		end

		# puts "data = %s" % (data)
		@URL = 'http://%s:%s/jsonrpc?request={"jsonrpc": "2.0", "method": "%s", "id":"%s"}' % [server,port.to_s, @method, @id]
		print "URL = ", @URL, "\n"
		r = Requests.request('GET', @URL)
		response = r.body
		print "response.class = ",response.class, "\n"
		print "r.body = ", r.body
		if response.is_a?(String)
			JSON.parse(response)
		# else
		# 	r.body
		# 	print "Type Response: ".r.body.type
		end

	end

	def self.usage_test
		ARGV.each do |argv| 
			if argv == '-v' || argv == '--update-video'
				print "updating video library ...."
			elsif argv == '-a' || argv == '--update-audio'
				print "updating audio library ...."
			end
		end
	end

	def self.usage_test1
		options = {}
		optparse = OptionParser.new do |opts|
		  	opts.banner = "Usage: [options] -v -a"

		  	opts.on('-v', '--update-video', 'Update Video Library') do |arg|
		  		options[:v] = puts "RO"
		  	end
	  		opts.on('-a', '--update-audio', 'Update Audio Library') do |arg|
		    	options[:a] = puts "RE"
		  	end
		end
		optparse.parse!
	end

	def self.usage
		options = {}
		OptionParser.new do |opts|
		  	opts.banner = "Usage: kodicli.rb [options]"
		  	opts.on('-a', '--update-audio', 'Update Video Library') { |v| options[:update_video] = v }
		  	opts.on('-v', '--update-video', 'Update Audio Library') { |v| options[:update_audio] = v }
		  	opts.on('-s', '--server host', 'Kodi Host Address/IP') { |v| options[:kodi_host] = v }
		  	opts.on('-p', '--port port', 'Kodi Port number') { |v| options[:kodi_port] = v }
		end.parse!

		puts options

		if options.length == 0
			puts "\n"
			puts "Usage: kodicli.rb [options]"
		end
		if options[:update_audio]
		 	puts "Update Audio Library ..."
		 	UpdateLibrary(options[:update_audio], options[:kodi_host], options[:kodi_port])
		end
		if options[:update_video]
			puts "Update Video Library ..."
			UpdateLibrary(options[:update_video], options[:kodi_host], options[:kodi_port])
		end
	end
end

# Kodi.UpdateLibrary('video')
Kodi.usage
