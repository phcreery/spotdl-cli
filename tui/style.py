class styleSet:
	def __init__(self, styleType = "modern"):
		if styleType == "modern" or styleType == "default":
			self.tl = u'\u2554'
			self.t  = u'\u2550'
			self.tr = u'\u2557'
			self.r  = u'\u2551'
			self.br = u'\u255D'
			self.b  = u'\u2550'
			self.bl = u'\u255A'
			self.l  = u'\u2551'
			self.c  = u'\u2588'
		elif styleType == "block":
			self.tl = u'\u2588'
			self.t  = u'\u2588'
			self.tr = u'\u2588'
			self.r  = u'\u2588'
			self.br = u'\u2588'
			self.b  = u'\u2588'
			self.bl = u'\u2588'
			self.l  = u'\u2588'
			self.c  = u'\u2588'
		else:
			self.tl = "+"
			self.t  = "-"
			self.tr = "+"
			self.r  = "|"
			self.br = "+"
			self.b  = "-"
			self.bl = "+"
			self.l  = "|"
			self.c  = "_"

