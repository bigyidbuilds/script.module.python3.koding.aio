#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcaddon

class AddonRestart():


	def __init__(self):
		self.__addon__     = xbmcaddon.Addon(sys.argv[1])
		self.__addonid__   = self.__addon__.getAddonInfo('id')
		self.__addonname__ = self.__addon__.getAddonInfo('name')
		self.start_addon = xbmcaddon.Addon(sys.argv[2]).getAddonInfo('id')
		self.InitScript()

	def Stop(self):
		self.Log('Stopping {} via addon_restart script'.format(self.__addonname__))
		xbmc.executebuiltin("ActivateWindow(Home)")

	def Start(self):
		self.Log('restarting {} via addon_restart script'.format(self.start_addon))
		xbmc.executebuiltin("RunAddon({})".format(self.start_addon))


	def InitScript(self):
		self.Stop()
		xbmc.sleep(1000)
		if  xbmc.getCondVisibility('System.AddonIsEnabled({})'.format(self.start_addon)):  
			self.Start()
		else:
			self.Log('{} is not enabled on the system'.format(self.start_addon))

	def Log(self,msg):
		xbmc.log('{}'.format(msg),2)

if __name__ == '__main__':
	AddonRestart()
