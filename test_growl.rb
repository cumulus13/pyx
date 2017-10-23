#require 'karl-growl'
require 'Growl'

def self.is_windows?
  processor, platform, *rest = RUBY_PLATFORM.split("-")
  platform == 'mswin32'
end

def self.exec *args
  bin = PACKAGED_BIN
  bin += '.com' if is_windows?

  Kernel.system bin, *args
end

def run
  raise Error, 'message required' unless message
  self.class.switches.each do |name, win_name|
    if send(:"#{name}?")
      value = send(name).to_s if send(name) && !(TrueClass === send(name))
      if is_windows?
        next if win_name.nil?

        switch = (win_name == :EMPTY) ? "" : "/#{win_name}:"
        args << switch + value
      else
        args << "--#{name}"
        args << value
      end
    end
  end
  Growl.exec *args
end

#Growl.notify {
#    self.message = 'Hello World'
#    self.image = File.join 'path', 'to', 'image.png'
#}

Growl.notify 'Foo', :icon => :jpeg, :title => 'Growl'

