#-*- coding: utf-8 -*-

# script.module.python3.koding.aio
# Python Koding AIO (c) by TOTALREVOLUTION LTD (support@trmc.freshdesk.com)

# Python Koding AIO is licensed under a
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.

# You should have received a copy of the license along with this
# work. If not, see http://creativecommons.org/licenses/by-nc-nd/4.0.

# Please make sure you've read and understood the license, this code can NOT be used commercially
# and it can NOT be modified and redistributed. If you're found to be in breach of this license
# then any affected add-ons will be blacklisted and will not be able to work on the same system
# as any other add-ons which use this code. Thank you for your cooperation.'''

import datetime
import os
import sys
import shutil
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from . import filetools

ADDONS      = 'special://home/addons'
XBMC_PATH   = xbmcvfs.translatePath('special://xbmc')
kodi_ver    = int(float(xbmc.getInfoLabel("System.BuildVersion")[:2]))
dialog      = xbmcgui.Dialog()

#----------------------------------------------------------------
# TUTORIAL #
def Addon_Genre(genre='adult',custom_url=''):
    """
Return a dictionary of add-ons which match a specific genre.

CODE: Addon_Genre([genre, custom_url])

AVAILABLE PARAMS:
    
    genre  -  By default this is set to 'adult' which will return a dictionary of all known
    adult add-ons. We recommend using the genre labels listed below as they are already in use
    by some add-on developers, however you can of course create your very own genre keys in
    your custom genre file if you wish.

    custom_url  -  If you have your own custom url which returns a dictionary
    of genres and add-ons you can enter it here. The page must adhere to the format shown below.

    Recommended Genre Keys:
    adult, anime, audiobooks, comedy, comics, documentary, food, gaming, health, howto, kids,
    livetv, movies, music, news, podcasts, radio, religion, space, sports, subscription,
    tech, trailers, tvshows, world

    Correct Genre Dictionary Structure:
    The dictionary must be a dictionary of genres with each genre dictionary containing keys for
    each add-on ID and the value being the name you want displayed. See below for an example:
    { "movies":{"plugin.video.mymovie":"My movie add-on","plugin.video.trailers":"My Trailer add-on"}, "sports":{"plugin.video.sports":"Sport Clips"} }

EXAMPLE CODE:
dialog.ok('ADD-ON GENRES','We will now list all known comedy based add-ons. If you have add-ons installed which you feel should be categorised as supplying comedy but they aren\'t then you can help tag them up correctly via the Add-on Portal at NaN.')
comedy_addons = koding.Addon_Genre(genre='comedy')
if comedy_addons:
    my_return = 'LIST OF AVAILABLE COMEDY BASED ADD-ONS:\n\n'

# Convert the dictionary into a list:
    comedy_addons = comedy_addons.items()
    for item in comedy_addons:
        my_return += '[COLOR=gold]Name:[/COLOR] %s   |   [COLOR=dodgerblue]ID:[/COLOR] %s\n' % (item[0],item[1])
    koding.Text_Box('[COLOR gold]COMEDY ADD-ONS[/COLOR]',my_return)
~"""
    import binascii
    from .__init__       import converthex
    from .filetools      import Text_File
    from .systemtools    import Timestamp
    from .vartools       import Merge_Dicts
    from .web            import Open_URL
    
    download_new = True
    local_path   = binascii.hexlify(b'genre_list')
    cookie_path  = "special://profile/addon_data/script.module.python3.koding.aio/cookies/"
    custom_genres= "special://profile/addon_data/script.module.python3.koding.aio/genres.txt"
    final_path   = os.path.join(cookie_path,str(local_path))
    if not xbmcvfs.exists(cookie_path):
        xbmcvfs.mkdirs(cookie_path)

    if xbmcvfs.exists(final_path):
        modified = xbmcvfs.Stat(final_path).st_mtime()
        old = int(modified)
        now = int(Timestamp('epoch'))
# Add a 24hr wait so we don't kill server
        if now < (modified+86400):
            download_new = False

# Create new file
    if download_new and custom_url != '':
        addon_list = Open_URL(custom_url)
        Text_File(final_path, "w", addon_list)

# Grab details of the relevant genre
    if xbmcvfs.exists(final_path):
        try:
            addon_list = eval( Text_File(final_path, 'r') )
            addon_list = addon_list[genre]
        except:
            xbmcvfs.delete(final_path)
            addon_list = {}

    if xbmcvfs.exists(custom_genres):
        try:
            custom_list = eval( Text_File(custom_genres, 'r') )
            custom_list = custom_list[genre]
            addon_list = Merge_Dicts(addon_list,custom_list)
        except:
            pass
    return addon_list
#----------------------------------------------------------------
# TUTORIAL #
def Addon_Info(id='',addon_id=''):
    """
Retrieve details about an add-on, lots of built-in values are available
such as path, version, name etc.

CODE: Addon_Setting(id, [addon_id])

AVAILABLE PARAMS:
            
    (*) id  -  This is the name of the id you want to retrieve.
    The list of built in id's you can use (current as of 15th April 2017)
    are: author, changelog, description, disclaimer, fanart, icon, id, name,
    path, profile, stars, summary, type, version

    addon_id  -  By default this will use your current add-on id but you
    can access any add-on you want by entering an id in here.
    
EXAMPLE CODE:
dialog.ok('ADD-ON INFO','We will now try and pull name and version details for our current running add-on.')
version = koding.Addon_Info(id='version')
name = koding.Addon_Info(id='name')
dialog.ok('NAME AND VERSION','[COLOR=dodgerblue]Add-on Name:[/COLOR] {}\n[COLOR=dodgerblue]Version:[/COLOR] {}'.format(name,version))
~"""
    import xbmcaddon
    if addon_id == '':
        addon_id = Caller()
    ADDON = xbmcaddon.Addon(id=addon_id)
    if id == '':
        dialog.ok('ENTER A VALID ID','You\'ve called the Addon_Info function but forgot to add an ID. Please correct your code and enter a valid id to pull info on (e.g. "version")')
    else:
        return ADDON.getAddonInfo(id=id)
#----------------------------------------------------------------
# TUTORIAL #
def Addon_List(enabled=True, inc_new=False):
    """
Return a list of enabled or disabled add-ons found in the database.

CODE: Addon_List([enabled, inc_new])

AVAILABLE PARAMS:
    
    enabled  -  By default this is set to True which means you'll
    get a list of all the enabled add-ons found in addons*.db but
    if you want a list of all the disabled ones just set this to
    False.

    inc_new  -  This will also add any new add-on folders found on
    your system that aren't yet in the database (ie ones that have
    been recently been manually extracted but not scanned in). By
    default this is set to False.
        
EXAMPLE CODE:
enabled_list = Addon_List(enabled=True)
disabled_list = Addon_List(enabled=False)
my_return = ''

for item in enabled_list:
    my_return += '[COLOR=lime]ENABLED:[/COLOR] %s\n' % item
for item in disabled_list:
    my_return += '[COLOR=red]DISABLED:[/COLOR] %s\n' % item
koding.Text_Box('ADDON STATUS',my_return)
~"""
    from .database   import DB_Query
    from .guitools   import Text_Box
    from .filetools  import DB_Path_Check, Get_Contents
    
    enabled_list  = []
    disabled_list = []
    addons_db     = DB_Path_Check('addons')
    on_system     = DB_Query(addons_db,'SELECT addonID, enabled from installed')

# Create a list of enabled and disabled add-ons already on system
    for item in on_system:
        if item["enabled"]:
            enabled_list.append(item["addonID"])
        else:
            disabled_list.append(item["addonID"])

    if inc_new:
        my_addons = Get_Contents(path=ADDONS, exclude_list=['packages','temp'])
        for item in my_addons:
            addon_id = Get_Addon_ID(item)
            if not addon_id in enabled_list and not addon_id in disabled_list:
                disabled_list.append(addon_id)

    if enabled:
        return enabled_list
    else:
        return disabled_list
#----------------------------------------------------------------
# TUTORIAL #
def Addon_Restart(start_addon=''):
    """
Stop a Addon running and either restart the addon or start another, uses a script to preform this function 

CODE: Addon_Restart([start_addon])

AVAILABLE PARAMS:

    start_addon  -  by default this is set to the caller addon of the function, but can be any addon on the system 

EXAMPLE CODE:
dialog.ok('RESTARTING ADDON','We will now attempt to close and restart your addon')
Addon_Restart()
~"""
    if start_addon == '':
        start_addon = Caller()
    scriptPath = os.path.join(xbmcvfs.translatePath(Addon_Info('path','script.module.python3.koding.aio')),'resources','scripts','addon_restart.py')
    xbmc.executebuiltin('RunScript({},{},{})'.format(scriptPath,Caller(),start_addon))

#----------------------------------------------------------------
# TUTORIAL #
def Addon_Service(addons='all', mode='list', skip_service=[]):
    """
Send through an add-on id, list of id's or leave as the default which is "all". This
will loop through the list of add-ons and return the ones which are run as services.

This enable/disable feature will comment out the service lines, and does not stop a running
service or start a service. This is designed more for if you've manually extracted a new
add-on into your system and it isn't yet enabled. Occasionally if the add-ons have dependencies
which are run as services then trying to enable them can cause Kodi to freeze.

CODE: Addon_Service([addon,disable])

AVAILABLE PARAMS:
    
    addons  -  By default this is set to "all" but if there's a sepcific set of add-ons you
    want to disable the service for just send through the id's in the form of a list.

    mode  -  By default this is set to 'list' meaning you'll get a return of add-on folders
    which contain an instance of service in the add-on.xml. You can set this to "disable" to
    comment out the instances of service and similarly when you need to re-enable you can use
    "enable" and that will uncomment out the service item. Please note that by uncommenting
    the service will not automatically start - you'll need to reload the profile for that.

    skip_service  -  When running the enable or disable mode you can choose to add a list of
    add-ons you'd like to skip the process for. Of course you may be thinking why would I send
    through a list of addons I want the service enabled/disabled for but then I also add them
    to the skip_service list to say DON'T enable/disable - it makes no sense?! Well you'd be
    correct that doesn't make any sense as presumably you've already filtered out the add-ons
    you don't want affected, this command is designed more for those who don't send through a
    list of add-ons and instead use the default "all" value for the addons paramater. This
    then makes it very easy to just skip a handful of add-on services and enable all others.

EXAMPLE CODE:
dialog.ok('CHECKING FOR SERVICES','We will now check for all add-ons installed which contain services')
service_addons = Addon_Service(mode='list')
my_text = 'List of add-ons running as a service:\n\n'
for item in service_addons:
    my_text += item+'\n'
koding.Text_Box('[COLOR gold]SERVICE ADDONS[/COLOR]',my_text)
~"""
    from .filetools  import Get_Contents, Physical_Path, Text_File
    from .vartools   import Data_Type
    from .guitools   import Text_Box
    service_addons = []
    if addons=='all':
        addons = Get_Contents(path=ADDONS, exclude_list=['packages','temp'],full_path=False)
    else:
        if Data_Type(addons) == 'str':
            addons = [addons]

    if Data_Type(skip_service) == 'str':
        skip_service = [skip_service]

    service_line = '<extension point="xbmc.service"'
    
    for item in addons:
        addon_path = os.path.join(ADDONS,item,'addon.xml')
        content = Text_File(addon_path,'r')
        if service_line in content:
            if item not in service_addons:
                service_addons.append(item)
                if mode != 'list':
                    if not item in skip_service:
                        for line in content.splitlines():
                            if service_line in line:
                                if not (line.strip().startswith('<!--')) and (mode == 'disable'):
                                    replace_line = '<!--%s-->'%line
                                    Text_File(addon_path,'w',content.replace(line,replace_line))
                                    break
                                elif line.strip().startswith('<!--') and mode == 'enable':
                                    replace_line = line.replace(r'<!--','').replace(r'-->','')
                                    Text_File(addon_path,'w',content.replace(line,replace_line))
                                    break
    return service_addons
#----------------------------------------------------------------
# TUTORIAL #
def Addon_Setting(setting='',value='return_default',addon_id='',setting_type=''):
    """
Change or retrieve an add-on setting.

CODE: Addon_Setting(setting, [value, addon_id, setting_type])

AVAILABLE PARAMS:
            
    (*) setting  -  This is the name of the setting you want to access, by
    default this function will return the value but if you add the
    value param shown below it will CHANGE the setting.

    value  -  If set this will change the setting above to whatever value
    is in here.

    addon_id  -  By default this will use your current add-on id but you
    can access any add-on you want by entering an id in here.

    setting_type  -  is used to set the type of setting if the value is to be change,
    left as '' will use standard xbmc setSetting function
    available types 'string','boolean','integer','number' 
    integer is a int
    number is a float
    
EXAMPLE CODE:
dialog.ok('ADDON SETTING','We will now try and pull the language settings for the YouTube add-on')
if os.path.exists(xbmcvfs.translatePath('special://home/addons/plugin.video.youtube')):
    my_setting = koding.Addon_Setting(setting='youtube.language',addon_id='plugin.video.youtube')
    dialog.ok('YOUTUBE SETTING','[COLOR=dodgerblue]Setting name:[/COLOR] youtube.language\n[COLOR=dodgerblue]Value:[/COLOR] {}'.format(my_setting))
else:
    dialog.ok('YOUTUBE NOT INSTALLED','Sorry we cannot run this example as you don\'t have YouTube installed.')
~"""
    import xbmcaddon
    if addon_id == '':
        addon_id = Caller()
    ADDON = xbmcaddon.Addon(id=addon_id)
    if value == 'return_default':
        mysetting = ADDON.getSetting(setting)
        return mysetting
    else:
        if setting_type == 'string':
            ADDON.setSettingString(setting, value)
        elif setting_type == 'number':
            ADDON.setSettingNumber(setting,value)
        elif setting_type == 'integer':
            ADDON.setSettingInt(setting,value)
        elif setting_type == 'boolean':
            ADDON.setSettingBool(setting,value)
        else:
            ADDON.setSetting(setting,value)
#----------------------------------------------------------------
# TUTORIAL #
def Adult_Toggle(adult_list=[], disable=True, update_status=0):
    """
Remove/Enable a list of add-ons, these are put into a containment area until enabled again.

CODE: Adult_Toggle(adult_list, [disable, update_status])

AVAILABLE PARAMS:
            
    (*) adult_list  -  A list containing all the add-ons you want to be disabled.

    disable  -  By default this is set to true so any add-ons in the list sent
    through will be disabled. Set to False if you want to enable the hidden add-ons.

    update_status  - When running this function it needs to disable the
    auto-update of add-ons by Kodi otherwise it risks crashing. This
    update_status paramater is the state you want Kodi to revert back to
    once the toggle of add-ons has completed. By default this is set to 0
    which is auto-update. You can also choose 1 (notify of updates) or 2
    (disable auto updates).

~"""
    from .filetools import End_Path, Move_Tree, Physical_Path

    adult_store  = Physical_Path("special://profile/addon_data/script.module.python3.koding.aio/adult_store")
    disable_list = []
    if not xbmcvfs.exists(adult_store):
        xbmcvfs.mkdirs(adult_store)
    my_addons = Installed_Addons()
    if disable:
        for item in my_addons:
            if item != None:
                item = item["addonid"]
                if item in adult_list:
                    disable_list.append(item)

        Toggle_Addons(addon=disable_list, enable=False, safe_mode=True, refresh=True, update_status=update_status)
        for item in disable_list:
            try:
                addon_path = xbmcaddon.Addon(id=item).getAddonInfo("path")
            except:
                addon_path = Physical_Path(os.path.join(ADDONS,item))
            path_id = End_Path(addon_path)
            if os.path.exists(addon_path):
                Move_Tree(addon_path,os.path.join(adult_store,path_id))
    else:
        KODI_VER    = int(float(xbmc.getInfoLabel("System.BuildVersion")[:2]))
        addon_vault = []
        if os.path.exists(adult_store):
            for item in os.listdir(adult_store):
                store_dir = os.path.join(adult_store,item)
                addon_dir = os.path.join(ADDONS, item)
                if os.path.exists(store_dir):
                    Move_Tree(store_dir,addon_dir)
                    addon_vault.append(item)

        if KODI_VER >= 16:
            Toggle_Addons(addon=addon_vault, safe_mode=True, refresh=True, update_status=update_status)
        else:
            Refresh(['addons','repos'])
#----------------------------------------------------------------
# TUTORIAL #
def Caller(my_return='addon'):
    """
Return the add-on id or path of the script which originally called
your function. If it's been called through a number of add-ons/scripts
you can grab a list of paths that have been called.

CODE: Caller(my_return)

AVAILABLE PARAMS:
    
    my_return  -  By default this is set to 'addon', view the options below:
        
        'addon' : Return the add-on id of the add-on to call this function.
        
        'addons': Return a list of all add-on id's called to get to this function.
        
        'path'  : Return the full path to the script which called this function.
        
        'paths' : Return a list of paths which have been called to get to this
        final function.
        
EXAMPLE CODE:
my_addon = koding.Caller(my_return='addon')
my_addons = koding.Caller(my_return='addons')
my_path = koding.Caller(my_return='path')
my_paths = koding.Caller(my_return='paths')

dialog.ok('ADD-ON ID', 'Addon id you called this function from:\n[COLOR=dodgerblue]{}[/COLOR]'.format(my_addon))
dialog.ok('SCRIPT PATH', 'Script which called this function:\n[COLOR=dodgerblue]{}[/COLOR]'.format(my_path))

addon_list = 'Below is a list of add-on id\'s which have been called to get to this final piece of code:\n\n'
for item in my_addons:
    addon_list += item+'\n'
koding.Text_Box('ADD-ON LIST', addon_list)
koding.Sleep_If_Window_Active(10147)
path_list = 'Below is a list of scripts which have been called to get to this final piece of code:\n\n'
for item in my_paths:
    path_list += item+'\n'
koding.Text_Box('ADD-ON LIST', path_list)
~"""
    import inspect
    stack       = inspect.stack()
    last_stack  = len(stack)-1
    stack_array = []
    addon_array = []
    for item in stack:
        last_stack = item[1].replace('<string>','')
        last_stack = last_stack.strip()
        stack_array.append(last_stack)
        try:
            scrap,addon_id = last_stack.split('addons%s'%os.sep)
            addon_id = addon_id.split(os.sep)[0]
            addon_id = Get_Addon_ID(addon_id)
            if addon_id not in addon_array:
                addon_array.append(addon_id)
        except:
            pass

    if my_return == 'addons':
        return addon_array
    if my_return == 'addon':
        return addon_array[len(addon_array)-1]
    if my_return == 'path':
        return stack_array[len(stack_array)-1]
    if my_return == 'paths':
        return stack_array
#----------------------------------------------------------------
def Check_Deps(addon_path, depfiles = []):
    import re
    from .filetools import Text_File
    from .__init__  import dolog
    exclude_list  = ['xbmc.gui', 'script.module.metahandler', 'metadata.common.allmusic.com',\
                    'kodi.resource','xbmc.core','xbmc.metadata','xbmc.addon','xbmc.json','xbmc.python']
    file_location = os.path.join(addon_path,'addon.xml')
    if xbmcvfs.exists(file_location):
        readxml = Text_File(file_location,'r')
        dmatch   = re.compile('import addon="(.+?)"').findall(readxml)
        for requires in dmatch:
            if not requires in exclude_list and not requires in depfiles:
                depfiles.append(requires)
    return depfiles
#----------------------------------------------------------------
# TUTORIAL #
def Check_Repo(repo,show_busy=True,timeout=10):
    """
This will check the status of repo and return True if the repo is online or False
if it contains paths that are no longer accessible online.

CODE:  Check_Repo(repo, [show_busy, timeout])

AVAILABLE PARAMS:

    (*) repo  -  This is the name/id of the repo or folder the repository resides in. In 99.99%
    of cases is the add-on id. If only using the folder name DOUBLE check first as
    there are a handful which have used a different folder name to the actual add-on id,
    if the repo is not recognised it will search the addon folder

    show_busy - By default this is set to True and a busy dialog will show during the check

    timeout - By default this is set to 10 (seconds) - this is the maximum each request
    to the repo url will take before timing out and returning False.

EXAMPLE CODE:
repo_status = Check_Repo('repository.koding.aio',show_busy=False,timeout=10)
if repo_status:
    dialog.ok('REPO STATUS','The repository Koding AIO is: [COLOR=lime]ONLINE[/COLOR]')
else:
    dialog.ok('REPO STATUS','The repository Koding AIO is: [COLOR=red]OFFLINE[/COLOR]')
~"""
    import xml.etree.ElementTree as ET
    from .__init__  import dolog
    from .filetools import Physical_Path
    from .guitools  import Show_Busy
    from .web       import Validate_Link
    if show_busy:
        Show_Busy()
    pathList = list()
    xbmc.log('### CHECKING %s'%repo,2)
    status = True
    if xbmc.getCondVisibility('System.HasAddon({})'.format(repo)):
        if xbmc.getCondVisibility('System.AddonIsEnabled({})'.format(repo)):
            pathList.append(Physical_Path(Addon_Info('path',repo)))
        else:
            pathList.append(os.path.join(Physical_Path(),'addons',repo))
    else:
        for root, dirs, files in os.walk(Physical_Path()):
            for _dir in dirs:
                p=os.path.join(root,_dir)
                if p.endswith(repo):
                    pathList.append(p)
    if len(pathList)>=1:
        for repo_path in pathList:
            path = os.path.join(repo_path,'addon.xml')
            if xbmcvfs.exists(path):
                root = ET.parse(path)
                _addon = root.getroot()
                for _extension in _addon:
                    if _extension.get('point') == "xbmc.addon.repository":
                        checksum = _extension.find('checksum').text
                        if checksum:
                            link_status = Validate_Link(checksum,timeout)
                            dolog('STATUS: {}'.format(link_status))
                            if link_status < 200 or link_status >= 400:
                                status = False
                                break
                if show_busy:
                    Show_Busy(False)
                return status
            else:
                xbmc.log('### ADDON XML file not found {}'.format(repo),2)
    else:
        xbmc.log('### UNABLE to locate repo {}'.format(repo),2)
        if show_busy:
            Show_Busy(False)
        return False
#----------------------------------------------------------------
# TUTORIAL #
def Default_Setting(setting='',addon_id='',reset=False):
    """
This will return the DEFAULT value in a dictionary for a setting (as set in resources/settings.xml)
and optionally reset the current value back to this default. If you pass through
the setting as blank it will return a dictionary of all default settings.

CODE:  Default_Setting(setting, [addon_id, reset])

AVAILABLE PARAMS:

    setting  -  The setting you want to retreive the value for.
    Leave blank to return a dictionary of all settings

    addon_id  -  This is optional, if not set it will use the current id.

    reset  -  By default this is set to False but if set to true and it will
    reset the current value to the default.

EXAMPLE CODE:
youtube_path = xbmcvfs.translatePath('special://home/addons/plugin.video.youtube')
if os.path.exists(youtube_path):
    my_setting='youtube.region'
    my_value = koding.Default_Setting(setting=my_setting, addon_id='plugin.video.youtube', reset=False)
    dialog.ok('YOUTUBE SETTING','Below is a default setting for plugin.video.youtube:\nSetting: [COLOR=dodgerblue]{}[/COLOR]\nValue: [COLOR=dodgerblue]{}[/COLOR]'.format(my_setting,my_value))
else:
    dialog.ok('YOUTUBE NOT INSTALLED','We cannot run this example as it uses the YouTube add-on which has not been found on your system.')
~"""
    import xml.etree.ElementTree as ET

    if addon_id == '':
        addon_id = Caller()
    values = {}
    addon_path = Addon_Info(id='path',addon_id=addon_id)
    settings_path = os.path.join(addon_path,'resources','settings.xml')
    if xbmcvfs.exists(settings_path):
        tree = ET.parse(settings_path)
        _settings = tree.getroot()
        for _section in _settings:
            for _category in _section:
                for _group in _category:
                    for _setting in _group:
                        _settingtype = _setting.get('type')
                        if _settingtype != "action":
                            _default = _setting.find('default').text
                            _settingid = _setting.get('id')
                            if setting != '' and _settingid == setting:    
                                values.update({_settingid:{'default':_default,'settingtype':_settingtype}})
                                if not _default:
                                    xbmc.log('{} SETTING HAS NO DEFAULT'.format(setting),2)
                                break
                            elif setting == '':
                                if _default:
                                    values.update({_settingid:{'default':_default,'settingtype':_settingtype}})
        if reset:
            for k,v in values.items():
                settingtype = v.get('settingtype')
                default     = v.get('default')
                if settingtype == 'boolean':
                    if default == 'true':
                        default = True 
                    elif default == 'false':
                        default = False
                Addon_Setting(addon_id=addon_id,setting=k,value=default,settingtype=settingtype)
    return values
#----------------------------------------------------------------
# TUTORIAL #
def Dependency_Check(addon_id = 'all', recursive = False):
    """
This will return a list of all dependencies required by an add-on.
This information is grabbed directly from the currently installed addon.xml,
an individual add-on id or a list of add-on id's.

CODE:  Dependency_Check([addon_id, recursive])

AVAILABLE PARAMS:

    addon_id  -  This is optional, if not set it will return a list of every
    dependency required from all installed add-ons. If you only want to
    return results of one particular add-on then send through the id.

    recursive  -  By default this is set to False but if set to true and you
    also send through an individual addon_id it will return all dependencies
    required for that addon id AND the dependencies of the dependencies.

EXAMPLE CODE:
current_id = xbmcaddon.Addon().getAddonInfo('id')
dependencies = koding.Dependency_Check(addon_id=current_id, recursive=True)
clean_text = ''
for item in dependencies:
    clean_text += item+'\n'
koding.Text_Box('Modules required for %s'%current_id,clean_text)
~"""
    import xbmcaddon
    import re
    from .filetools  import Text_File
    from .vartools   import Data_Type 
    
    processed    = []
    depfiles     = []    
    
    if addon_id == 'all':
        addon_id = xbmcvfs.listdir(ADDONS)
    elif Data_Type(addon_id) == 'str':
        addon_id = [addon_id]

    for name in addon_id:
        try:
            addon_path = xbmcaddon.Addon(id=name).getAddonInfo('path')
        except:
            addon_path = os.path.join(ADDONS, name)
        if not name in processed:
            processed.append(name)

    # Get list of master dependencies
        depfiles = Check_Deps(addon_path,[name])
        
    # Recursively check all other dependencies
        depchecks = depfiles
        if recursive:
            while len(depchecks):
                for depfile in depfiles:
                    if depfile not in processed:
                        try:
                            dep_path = xbmcaddon.Addon(id=depfile).getAddonInfo('path')
                        except:
                            dep_path = os.path.join(ADDONS,depfile)
                        newdepfiles = Check_Deps(dep_path, depfiles)
                    # Pass through the path of sub-dependency and add items to master list and list to check
                        for newdep in newdepfiles:
                            if not (newdep in depchecks) and not (newdep in processed):
                                depchecks.append(newdep)
                            if not newdep in depfiles:
                                depfiles.append(newdep)
                    processed.append(depfile)
                    depchecks.remove(depfile)
                if name in depchecks:
                    depchecks.remove(name)
    return processed[1:]
#----------------------------------------------------------------
# TUTORIAL #
def Get_Addon_ID(folder):
    """
If you know the folder name of an add-on but want to find out the
addon id (it may not necessarily be the same as folder name) then
you can use this function. Even if the add-on isn't enabled on the
system this will regex out the add-on id.

CODE:  Get_Addon_ID(folder)

AVAILABLE PARAMS:
    
    folder  -  This is folder name of the add-on. Just the name not the path.

EXAMPLE CODE:
dialog.ok('ABOUT','This function allows us to pass through a folder name found in the addons folder and it will return the real id. The vast majority of add-ons use the same folder name as id but there are exceptions. Let\'s check Python Koding...')
my_id = koding.Get_Addon_ID(folder='script.module.python3.koding.aio')
dialog.ok('PYTHON KODING ID','The add-on id found for this folder folder is:\n\n[COLOR=dodgerblue]{}[/COLOR]'.format(my_id))
~"""
    from .filetools import Text_File
    import re
    xmlpath = os.path.join(ADDONS, folder, 'addon.xml')
    if xbmcvfs.exists(xmlpath):
        contents = Text_File(xmlpath,'r')
        addon_id = re.compile('id="(.+?)"').findall(contents)
        addon_id = addon_id[0] if (len(addon_id) > 0) else ''
        return addon_id
    else:
        return folder
#----------------------------------------------------------------
# TUTORIAL #
def Installed_Addons(types='unknown', content ='unknown', properties = ''):
    """
This will send back a list of currently installed add-ons on the system.
All the three paramaters you can send through to this function are optional,
by default (without any params) this function will return a dictionary of all
installed add-ons. The dictionary will contain "addonid" and "type" e.g. 'xbmc.python.pluginsource'.

CODE: Installed_Addons([types, content, properties]):

AVAILABLE PARAMS:

    types       -  If you only want to retrieve details for specific types of add-ons
    then use this filter. Unfortunately only one type can be filtered at a time,
    it is not yet possible to filter multiple types all in one go. Please check
    the official wiki for the add-on types avaialble but here is an example if
    you only wanted to show installed repositories: koding.Installed_Addons(types='xbmc.addon.repository')

    content     -  Just as above unfortunately only one content type can be filtered
    at a time, you can filter by video,audio,image and executable. If you want to
    only return installed add-ons which appear in the video add-ons section you
    would use this: koding.Installed_Addons(content='video')

    properties  -  By default a dictionary containing "addonid" and "type" will be
    returned for all found add-ons meeting your criteria. However you can add any
    properties in here available in the add-on xml (check official Wiki for properties
    available). Unlike the above two options you can choose to add multiple properties
    to your dictionary, see example below:
    koding.Installed_Addons(properties='name,thumbnail,description')


EXAMPLE CODE:
my_video_plugins = koding.Installed_Addons(types='xbmc.python.pluginsource', content='video', properties='name')
final_string = ''
for item in my_video_plugins:
    final_string += 'ID: %s | Name: %s\n'%(item["addonid"], item["name"])
koding.Text_Box('LIST OF VIDEO PLUGINS',final_string)
~"""
    try:    import simplejson as json
    except: import json

    addon_dict = []
    if properties != '':
        properties = properties.replace(' ','')
        properties = '"%s"' % properties
        properties = properties.replace(',','","')
    
    query = '{"jsonrpc":"2.0", "method":"Addons.GetAddons","params":{"properties":[%s],"enabled":"all","type":"%s","content":"%s"}, "id":1}' % (properties,types,content)
    response = xbmc.executeJSONRPC(query)
    data = json.loads(response)
    if "result" in data:
        try:
            addon_dict = data["result"]["addons"]
        except:
            pass
    return addon_dict
#----------------------------------------------------------------
# TUTORIAL #
def Open_Settings(addon_id='',restart=True,restart_addon=''):
    """
By default this will open the current add-on settings but if you pass through an addon_id it will open the settings for that add-on.

CODE: Open_Settings([addon_id,restart,restart_addon])

AVAILABLE PARAMS:

    addon_id    - This optional, it can be any any installed add-on id. If nothing is passed
    through the current add-on settings will be opened.

    restart - By default this is set to True, as soon as the addon settings are closed
    the current script will stop running and restart

    restart_addon  -  This is used in combination with restart arg if restart is True by default this is set to the caller addon but by passing another addon id it will attempt to open that   

EXAMPLE CODE:
youtube_path = xbmcvfs.translatePath('special://home/addons/plugin.video.youtube')
if os.path.exists(youtube_path):
    dialog.ok('YOUTUBE SETTINGS','We will now open the YouTube settings.\nUpon closung the addons settings your addon will close and open the youtube addon')
    koding.Open_Settings(addon_id='plugin.video.youtube',restart=True,restart_addon='plugin.video.youtube')
else:
    dialog.ok('YOUTUBE NOT INSTALLED','We cannot run this example as it uses the YouTube add-on which has not been found on your system.')
~"""
    import xbmcaddon
    if addon_id == '':
        addon_id = Caller()
    if restart_addon == '':
        restart_addon = Caller()
    xbmc.log('ADDON ID: {}'.format(addon_id),2)
    xbmc.executebuiltin('Addon.OpenSettings({})'.format(addon_id))
    xbmc.sleep(500)
    while xbmc.getCondVisibility('Window.IsVisible(10140)'):
        xbmc.sleep(500)
    else:
        if restart:
            Addon_Restart(restart_addon)
    
#----------------------------------------------------------------
# TUTORIAL #
def Toggle_Addons(addon='all', enable=True, safe_mode=True, exclude_list=[], new_only=True, refresh=True, update_status=0):
    """
Send through either a list of add-on ids or one single add-on id.
The add-ons sent through will then be added to the addons*.db
and enabled or disabled (depending on state sent through).

WARNING: If safe_mode is set to False this directly edits the
addons*.db rather than using JSON-RPC. Although directly amending
the db is a lot quicker there is no guarantee it won't cause
severe problems in later versions of Kodi (this was created for v17).
DO NOT set safe_mode to False unless you 100% understand the consequences!

CODE:  Toggle_Addons([addon, enable, safe_mode, exclude_list, new_only, refresh])

AVAILABLE PARAMS:
    (*) addon  -  This can be a list of addon ids, one single id or
    'all' to enable/disable all. If enabling all you can still use
    the exclude_list for any you want excluded from this function.
    enable  -  By default this is set to True, if you want to disable
    the add-on(s) then set this to False.
    
    safe_mode  -  By default this is set to True which means the add-ons
    are enabled/disabled via JSON-RPC which is the method recommended by
    the XBMC foundation. Setting this to False will result in a much
    quicker function BUT there is no guarantee this will work on future
    versions of Kodi and it may even cause corruption in future versions.
    Setting to False is NOT recommended and you should ONLY use this if
    you 100% understand the risks that you could break multiple setups.
    
    exclude_list  -  Send through a list of any add-on id's you do not
    want to be included in this command.
    
    new_only  -  By default this is set to True so only newly extracted
    add-on folders will be enabled/disabled. This means that any existing
    add-ons which have deliberately been disabled by the end user are
    not affected.
    
    refresh  - By default this is set to True, it will refresh the
    current container and also force a local update on your add-ons db.

    update_status  - When running this function it needs to disable the
    auto-update of add-ons by Kodi otherwise it risks crashing. This
    update_status paramater is the state you want Kodi to revert back to
    once the toggle of add-ons has completed. By default this is set to 0
    which is auto-update. You can also choose 1 (notify of updates) or 2
    (disable auto updates).

EXAMPLE CODE:
from .systemtools import Refresh
xbmc.executebuiltin('ActivateWindow(Videos, addons://sources/video/)')
xbmc.sleep(2000)
dialog.ok('DISABLE YOUTUBE','We will now disable YouTube (if installed)')
koding.Toggle_Addons(addon='plugin.video.youtube', enable=False, safe_mode=True, exclude_list=[], new_only=False)
koding.Refresh('container')
xbmc.sleep(2000)
dialog.ok('ENABLE YOUTUBE','When you click OK we will enable YouTube (if installed)')
koding.Toggle_Addons(addon='plugin.video.youtube', enable=True, safe_mode=True, exclude_list=[], new_only=False)
koding.Refresh('container')
~"""
    from .__init__       import dolog
    from .filetools      import DB_Path_Check, Get_Contents
    from .database       import DB_Query
    from .systemtools    import Last_Error, Refresh, Set_Setting, Sleep_If_Function_Active, Timestamp
    from .vartools       import Data_Type

    Set_Setting('general.addonupdates', 'kodi_setting', '2')
    dolog('disabled auto updates for add-ons')
    kodi_ver        = int(float(xbmc.getInfoLabel("System.BuildVersion")[:2]))
    addons_db       = DB_Path_Check('addons')
    data_type       = Data_Type(addon)
    state           = int(bool(enable))
    enabled_list    = []
    disabled_list   = []
    if kodi_ver >= 17:
        on_system   = DB_Query(addons_db,'SELECT addonID, enabled from installed')
# Create a list of enabled and disabled add-ons already on system
        enabled_list  = Addon_List(enabled=True)
        disabled_list = Addon_List(enabled=False)

# If addon has been sent through as a string we add into a list
    if data_type == 'unicode':
        addon = addon.encode('utf8')
        data_type = Data_Type(addon)

    if data_type == 'str' and addon!= 'all':
        addon = [addon]

# Grab all the add-on ids from addons folder
    if addon == 'all':
        addon     = []
        ADDONS    = xbmcvfs.translatePath('special://home/addons')
        my_addons = Get_Contents(path=ADDONS, exclude_list=['packages','temp'])
        for item in my_addons:
            addon_id = Get_Addon_ID(item)
            addon.append(addon_id)

# Find out what is and isn't enabled in the addons*.db
    temp_list = []
    for addon_id in addon:
        if not addon_id in exclude_list and addon_id != '':
            if addon_id in disabled_list and not new_only and enable:
                temp_list.append(addon_id)
            elif addon_id not in disabled_list and addon_id not in enabled_list:
                temp_list.append(addon_id)
            elif addon_id in enabled_list and not enable:
                temp_list.append(addon_id)
            elif addon_id in disabled_list and enable:
                temp_list.append(addon_id)
    addon = temp_list

# If you want to bypass the JSON-RPC mode and directly modify the db (READ WARNING ABOVE!!!)
    if not safe_mode and kodi_ver >= 17:
        installedtime   = Timestamp('date_time')
        insert_query    = 'INSERT or IGNORE into installed (addonID , enabled, installDate) VALUES (?,?,?)'
        update_query    = 'UPDATE installed SET enabled = ? WHERE addonID = ? '
        insert_values   = [addon, state, installedtime]
        try:
            for item in addon:
                DB_Query(addons_db, insert_query, [item, state, installedtime])
                DB_Query(addons_db, update_query, [state, item])
        except:
            dolog(Last_Error())
        if refresh:
            Refresh()

# Using the safe_mode (JSON-RPC)
    else:
        mydeps        = []
        final_enabled = []
        if state:
            my_value      = 'true'
            log_value     = 'ENABLED'
            final_addons  = []
        else:
            my_value      = 'false'
            log_value     = 'DISABLED'
            final_addons  = addon

        for my_addon in addon:

        # If enabling the add-on then we also check for dependencies and enable them first
            if state:
                dependencies = Dependency_Check(addon_id=my_addon, recursive=True)
                mydeps.append(dependencies)

    # if enable selected we traverse through the dependencies enabling addons with lowest amount of deps to highest
        if state:
            mydeps = sorted(mydeps, key=len)
            for dep in mydeps:
                counter = 0
                for item in dep:
                    enable_dep = True
                    if counter == 0:
                        final_addons.append(item)
                        enable_dep = False
                    elif item in final_enabled:
                        enable_dep = False
                    else:
                        enable_dep = True
                    if enable_dep:
                        if not item in exclude_list and not item in final_enabled and not item in enabled_list:
                            if Set_Setting(setting_type='addon_enable', setting=item, value = 'true'):
                                final_enabled.append(item)
                    counter += 1

    # Now the dependencies are enabled we need to enable the actual main add-ons
        for my_addon in final_addons:
            if not my_addon in final_enabled:
                if Set_Setting(setting_type='addon_enable', setting=my_addon, value = my_value):
                    final_enabled.append(addon)
    if refresh:
        Refresh(['addons','container'])
    Set_Setting('general.addonupdates', 'kodi_setting', '%s'%update_status)
#----------------------------------------------------------------