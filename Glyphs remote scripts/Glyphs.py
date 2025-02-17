#!/usr/bin/env python
# encoding: utf-8

import time, objc
from Foundation import NSObject

__all__ = ["Glyphs", "currentDocument", "GSMOVE", "GSLINE", "GSCURVE", "GSOFFCURVE", "GSSHARP", "GSSMOOTH", "GSGlyph", "GSLayer", "GSApplication", "RunScript"]

NSConnection = objc.lookUpClass("NSConnection")

def application(appName):
	port = "com.GeorgSeifert.Glyphs3"
	conn = None
	tries = 0
	
	while ((conn is None) and (tries < 10)):
		conn = NSConnection.connectionWithRegisteredName_host_(port, None)
		tries = tries + 1;
		
		if (not conn):
			time.sleep(1)
	
	if (not conn):
		print("Could not find a JSTalk connection to " + appName)
		return None
	
	return conn.rootProxy()

Glyphs = application("Glyphs");
GSApplication = Glyphs
if Glyphs and Glyphs.orderedDocuments():
	currentDocument = Glyphs.orderedDocuments()[0]
else:
	currentDocument = None

class GSStdOut(NSObject):
	def setWrite_(self, text):
		print(text)

def RunScript(code):
	StdOut = GSStdOut.new()
	scriptingHandler = Glyphs.scriptingHandler()
	scriptingHandler.runMacroString_stdOut_(code, StdOut)

GSMOVE = 17
GSLINE = 1
GSCURVE = 35
GSOFFCURVE = 65
GSSHARP = 0
GSSMOOTH = 4096

def GSGlyph(name=None):
	_Glyph = Glyphs.glyph()
	if name and isinstance(name, str):
		name = NSString.stringWithString_(name)
		_Glyph.setName_(name)
	return _Glyph

def GSLayer():
	return glyphs.layer()
	
def GSPath():
	return glyphs.path()

def GSNode(pt = None, type = None):
	_Node = glyphs.node()
	if pt:
		_Node.setPosition_(pt)
	if type:
		_Node.setType_(type)
	return _Node

def GSAnchor(pt = None, name = None):
	_Anchor = glyphs.anchor()
	if pt:
		_Anchor.setPosition_(pt)
	if name:
		_Anchor.setName_(name)
	return _Anchor

def GSComponent(glyph = None, pt = None, scale = None):
	_Component = glyphs.component()
	if pt:
		_Component.setPosition_(pt)
	if glyph:
		if isinstance(glyph, str):
			_Component.setComponentName_(glyph)
		elif isinstance(name, "GSGlyph"):
			_Component.setComponent_(glyph)
	return _Component