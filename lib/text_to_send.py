# Help Commands
class help_command(object):
	def __init__(self):
		s = self
		end = '\r\n'

		s.help_msg = " FrankerZ What would you like help with? !socialCmds, !miscCmds, !infoCmds FrankerZ " + end

class help_command_social(object):
	def __init__(self):
		s = self
		end = '\r\n'

		s.help_social = "Commands are: !Instagram, !Facebook, !Twitter, !Youtube" + end

class help_command_misc(object):
	def __init__(self):
		s = self
		end = '\r\n'

		s.help_misc = "Commands are: ThunBeast !pbw, !" + end

class help_command_info(object):
	def __init__(self):
		s = self
		end = '\r\n'

		s.help_info = "Commands are: NOTHIN HERE YET" + end
