require 'requests'
require 'io/console'
require 'ruby-progressbar'
require 'optparse'

class Offcloud
	@@MASTER_URL = 'https://offcloud.com'
	@@API_KEY = 'uka0dUxAaUiuEvYR0pUW7ky5mw2BSkbc'

	def self.login(api_key=nil,username=nil,password=nil)
		if not api_key
			if not username
				print "USERNAME [email]: "
				username = gets.chomp
			end
			if not password
				print "PASSWORD        : "
				password = STDIN.noecho(&:gets).chomp
			end
			print "\n"
			url = 'https://offcloud.com/api/login/classic?username=%s&password=%s' % [username, password]
			data = {
				:username => username,
				:password => password
			}
			print "URL 0: ", url, "\n\n"
			req = Requests.request('POST', url, data: data)
		else
			url = "https://offcloud.com/api/login/classic?apikey=%s" % [api_key]
			print "URL 1: ", url, "\n\n"
			req = Requests.request('POST', url)
		end

		print "LENGTH: ", req.body.length, "\n"
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.cloud_download(url_download, api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		puts "cloud download ..."
		url = "https://offcloud.com/api/cloud/download?apikey=%s" % [api_key]
		print "URL: ", url, "\n"
		data = {:url => url_download}
		req = Requests.request('POST', url, data: data)
		print "LENGTH: ", req.body.length, "\n"
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
		
	end
	
	def self.instant_download(url_download, api_key=nil, proxyId=nil)
		if not api_key
			api_key = @@API_KEY
		end
		puts "instant download ..."
		url = "https://offcloud.com/api/instant/download?apikey=%s" % [api_key]
		# data = {'url' => 'http://www.mediafire.com/file/zbjpsoi6wlfyorm/MOTOROLA_EPLUS_NMA26.42-75_ROW.7z'}
		data = {:url => url_download}
		if proxyId
			data[:proxyId => proxyId]
		end
		print "URL: ", url, "\n"
		req = Requests.request('POST', url, data: data)
		print "LENGTH: ", req.body.length, "\n"
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	
	def self.remote_download(url_download, api_key=nil, remoteOptionId=nil, folderId=nil)
		if not api_key
			api_key = @@API_KEY
		end
		puts "instant download ..."
		url = "https://offcloud.com/api/instant/download?apikey=%s" % [api_key]
		data = {:url => url_download, :remoteOptionId => remoteOptionId, :folderId => folderId}
		print "URL: ", url, "\n"
		req = Requests.request('POST', url, data: data)
		print "LENGTH: ", req.body.length, "\n"
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.download_cloud_status(api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/cloud/status?apikey=%s" % [api_key]
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.download_remote_status(api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/remote/status?apikey=%s" % [api_key]
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.proxy_list(api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/proxy/list?apikey=%s" % [api_key]
		print "URL: ", url, "\n"
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.cloud_explore(request_id)
		url = "https://offcloud.com/api/cloud/explore/%s" % [request_id]
		print "URL: ", url, "\n"
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.remote_account_list(api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/remote-account/list?apikey=%s" % [api_key]
		print "URL: ", url, "\n"
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "RESPONSE: ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
			print "PAGE NOT FOUND", "\n"
		end
	end

	def self.check_login(api_key=nil)		
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/login/check?apikey=%s" % [api_key]
		print "URL: ", url, "\n"
		req = Requests.request('POST', url)
		if not req.body.length > 1000
			print  "body    = ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
		end
	end

	def self.get_account(api_key=nil)
		if not api_key
			api_key = @@API_KEY
		end
		url = "https://offcloud.com/api/account/get?apikey=%s" % [api_key]
		print "URL: ", url, "\n"
		req = Requests.request('GET', url)
		if not req.body.length > 1000
			print  "body    = ", req.body, "\n"
		else
			print "STATUS: ", req.status, "\n"		
		end
	end

	def self.usage()
		options = {}
		print "LINE   : ", "#{__FILE__}:#{__LINE__}:#{options}\n"
		print "METHOD : ", __method__, "\n"
		print "CLASS  : ", name, "\n"
		OptionParser.new do |opts|
			opts.banner = "USAGE: " + File.basename(__FILE__) + " " + "[options]"
			opts.on('-a', '--api-key') { |v| options[:api_key] = v }
			opts.on('-c', '--download-cloud URL') { |v| options[:download_cloud] = v }
			opts.on('-i', '--download-instant URL') { |v| options[:download_instant] = v }
			opts.on('-r', '--download-remote URL') { |v| options[:download_remote] = v }
			opts.on('-s', '--download-cloud-status URL') { |v| options[:download_cloud_status] = v }
			opts.on('-S', '--download-remote-status URL') { |v| options[:download_remote_status] = v }
			opts.on('-l', '--login') { |v| options[:login] = v }
			opts.on('-u', '--username USERNAME') { |v| options[:username] = v }
			opts.on('-p', '--password PASSWORD') { |v| options[:password] = v }
			opts.on('-P', '--proxy-list') { |v| options[:proxy_list] = v }
			opts.on('-x', '--cloud-explore REQUEST_ID') { |v| options[:cloud_explore] = v }
			opts.on('-C', '--check-login') { |v| options[:check_login] = v }
			opts.on('-g', '--get-account') { |v| options[:get_account] = v }
		end.parse!
		
		print "OPTIONS : ", options, "\n"
		if options[:download_cloud]
			cloud_download(options[:download_cloud], options[:api_key])
		elsif options[:download_instant]
			instant_download(options[:download_instant], options[:api_key])
		elsif options[:download_remote]
			remote_download(options[:download_remote], options[:api_key])
		elsif options[:download_cloud_status]
			download_cloud_status(options[:api_key])
		elsif options[:download_remote_status]
			download_remote_status(options[:api_key])
		elsif options[:login]
			login(options[:api_key], options[:username], options[:password])
		elsif options[:proxy_list]
			proxy_list(options[:api_key])
		elsif options[:check_login]
			check_login(options[:api_key])
		elsif options[:get_account]
			get_account(options[:api_key])
		elsif options[:cloud_explore]
			cloud_explore(options[:cloud_explore])
		else
			print "USAGE " + File.basename(__FILE__) + " " + "[options]", "\n"
		end
	end
end

api_key = 'uka0dUxAaUiuEvYR0pUW7ky5mw2BSkbc'
url ='http://www.mediafire.com/file/zbjpsoi6wlfyorm/MOTOROLA_EPLUS_NMA26.42-75_ROW.7z'
Offcloud.usage
