#
#      Copyright (C) 2014 Datho-Digital
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#


import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import os
import random


ADDONID  = 'plugin.totalsettings'
ADDON    = xbmcaddon.Addon(ADDONID)
HOME     = ADDON.getAddonInfo('path')
TITLE    = 'TotalXBMC Maintenance'
VERSION  = '1.0.0'
ICON     =  os.path.join(HOME, 'icon.png')
FANART   =  os.path.join(HOME, 'fanart.jpg')


_TOTALINSTALLER		= 100
_ANDROID   			= 200
_SKIN      			= 300
_SUPERFAVOURITES   	= 400
_LIVETV    			= 500
_VPNICITY  			= 600
_TOTALSETTINGS		= 700
_STATUS    			= 800
_ADVANCED  			= 900
_FORUM				= 1000
_TOTALGUIDES		= 1100

def OpenSettings(id):
    xbmc.executebuiltin('XBMC.Addon.OpenSettings(%s)' % str(id))

def RunAddon(id):
    xbmc.executebuiltin('XBMC.RunAddon(%s)' % str(id))
   
def ActivateWindow(id):
    xbmc.executebuiltin('ActivateWindow(%s)' % str(id))
	
def StartAndroidActivity(id):
    xbmc.executebuiltin('StartAndroidActivity(%s)' % str(id))

def Main():   
    addDir('Install Addons',          			_TOTALINSTALLER)
    addDir('Video Guides',          			_TOTALGUIDES)
    addDir('Forum Browser',	          			_FORUM)
    addDir('Android Settings',          		_ANDROID)
    addDir('Skin Settings',             		_SKIN)
    addDir('Super Favourites Settings', 		_SUPERFAVOURITES)
    addDir('Total Installer Settings', 			_TOTALSETTINGS)
    addDir('OnTapp.TV Settings',		    	_LIVETV)
    addDir('VPNicity Settings',		     		_VPNICITY)
    addDir('Connectivity Status',       		_STATUS)
    addDir('Upload Log',                		_ADVANCED)

def CheckConnection():
    sites = []
    sites.append('www.microsoft.com')
    sites.append('www.google.com')
    sites.append('www.yahoo.com')
    sites.append('www.ebay.com')
    sites.append('www.youtube.com')
    sites.append('www.amazon.com')

    import urllib2

    random.shuffle(sites)

    counter = 0
    for site in sites:
        counter += 1
        if counter > 10:
            return False
        try:
            url  = 'http://' + site
            req  = urllib2.Request(url)
            resp = urllib2.urlopen(req)

            return True

        except Exception, e:
            pass

    return False


def STATUS():
    if CheckConnection():
	xbmcgui.Dialog().ok(TITLE, '', '[COLOR FF00FF00]You are connected to the internet[/COLOR]')
    else:
        xbmcgui.Dialog().ok(TITLE, '', '[COLOR FFFF0000]You are not connected to the internet[/COLOR]')


def TOTALINSTALLER():
    RunAddon('plugin.program.totalinstaller')

def ANDROID():
    StartAndroidActivity('&quot;com.android.settings&quot;')

def SKIN():
    ActivateWindow('skinsettings')
    
def LIVETV():
    OpenSettings('script.tvguidedixie')
    

def SUPERFAVOURITES():
    OpenSettings('plugin.program.super.favourites')

def VPNICITY():
    OpenSettings('plugin.program.vpnicity')
  
def TOTALSETTINGS():
    OpenSettings('plugin.program.totalinstaller')

def ADVANCED():
    RunAddon('script.xbmc.debug.log')

def FORUM():
    RunAddon('script.forum.browser')

def TOTALGUIDES():
    RunAddon('plugin.video.whufclee')


def addDir(name, mode, isFolder=False):
    #thumbnail = ICON

    thumbnail = ''
    u         = sys.argv[0] + '?mode=' + str(mode)        
    liz       = xbmcgui.ListItem(name, iconImage=thumbnail, thumbnailImage=thumbnail)

    #liz.setProperty('Fanart_Image', FANART)

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

   
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
           params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param



params = get_params()
mode   = None


try:
    mode=int(params['mode'])
except:
    pass


if mode == _ANDROID:
    ANDROID()

elif mode == _SKIN:
    SKIN()    
    
elif mode == _STATUS:
    STATUS()

elif mode == _LIVETV:
    LIVETV()
    
elif mode == _SUPERFAVOURITES:
    SUPERFAVOURITES()

elif mode == _VPNICITY:
    VPNICITY()

elif mode == _ADVANCED:
    ADVANCED()

elif mode == _TOTALINSTALLER:
    TOTALINSTALLER()

elif mode == _TOTALSETTINGS:
    TOTALSETTINGS()

elif mode == _TOTALGUIDES:
    TOTALGUIDES()

elif mode == _FORUM:
    FORUM()

else:
    Main()

    
xbmcplugin.endOfDirectory(int(sys.argv[1]))