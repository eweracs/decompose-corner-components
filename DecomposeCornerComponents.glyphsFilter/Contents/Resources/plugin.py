# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class DecomposeCornerComponents(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			"en": "Decompose Corner Components",
			"de": "Corner-Komponenten in Pfade umwandeln",
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		layer.decomposeCorners()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
