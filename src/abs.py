from abc import * 

import os, sys

class car(metaclass = ABCMeta):
	@abstractmethod
	def drive(self):
		pass
# done
#class bmw(car):
#	pass

# not dome
class bmw(car):
	def drive(self):
		print('bmw driving')

auto = bmw()
auto.drive()
