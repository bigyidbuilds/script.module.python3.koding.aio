WHAT IS KODING.PY?
=================
This is a universal module which has an variety of functions to make life much easier for developers whilst giving them the opportunity to keep their code secure.


IMPORTING KODING.PY
===================

addon.xml - just import as you would any other module, the following code would work:
    
    <import addon="script.module.python3.koding.aio" version="0.0.1"/>

default.py (or whatever your initial opening py document is called) - all you need is to import koding.

------------------------------------------------------------------------------------------

## A D D O N   B A S E D   F U N C T I O N S

------------------------------------------------------------------------------------------

###### ADDON GENRE DICTIONARY:
Return a dictionary of add-ons which match a specific genre.

	CODE: Addon_Genre([genre, custom_url])

	AVAILABLE PARAMS:
	    
	    genre  -  By default this is set to 'adult' which will return
	    a dictionary of all known adult add-ons. The genre details are pulled from the
	    Add-on Portal at noobsandnerds.com so you can use any of the supported genre tags
	    listed on this page: http://noobsandnerds.com/latest/?p=3762

	    custom_url  -  If you have your own custom url which returns a dictionary
	    of genres you can enter it here and use that rather than rely on NaN categorisation.

	EXAMPLE CODE:
	-------------
	dialog.ok('ADD-ON GENRES','We will now list all known comedy based add-ons. If you have add-ons installed which you feel should be categorised as supplying comedy but they aren\'t then you can help tag them up correctly via the Add-on Portal at NaN.')
	comedy_addons = koding.Addon_Genre(genre='comedy')
	if comedy_addons:
	    my_return = 'LIST OF AVAILABLE COMEDY BASED ADD-ONS:\n\n'

	# Convert the dictionary into a list:
	    comedy_addons = comedy_addons.items()
	    for item in comedy_addons:
	        my_return += '[COLOR=gold]Name:[/COLOR] %s   |   [COLOR=dodgerblue]ID:[/COLOR] %s\n' % (item[0],item[1])
	    koding.Text_Box('[COLOR gold]COMEDY ADD-ONS[/COLOR]',my_return)

------------------------------------------------------------------------------------------

###### ADD-ON ID FROM PATH:
If you know the folder name of an add-on but want to find out the
addon id (it may not necessarily be the same as folder name) then
you can use this function. Even if the add-on isn't enabled on the
system this will regex out the add-on id.

	CODE:  Get_Addon_ID(folder)

	AVAILABLE PARAMS:
	    
	    folder  -  This is folder name of the add-on. Just the name not the path.

	EXAMPLE CODE:
	-------------
	dialog.ok('ABOUT','This function allows us to pass through a folder name found in the addons folder and it will return the real id. The vast majority of add-ons use the same folder name as id but there are exceptions. Let\'s check Python Koding...')
	my_id = koding.Get_Addon_ID(folder='script.module.python.koding.aio.alt')
	dialog.ok('PYTHON KODING ID','The add-on id found for this folder folder is:','[COLOR=dodgerblue]%s[/COLOR]'%my_id)

------------------------------------------------------------------------------------------

###### ADD-ON INFO:
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
	-------------
	dialog.ok('ADD-ON INFO','We will now try and pull name and version details for our current running add-on.')
	version = koding.Addon_Info(id='version')
	name = koding.Addon_Info(id='name')
	dialog.ok('NAME AND VERSION','[COLOR=dodgerblue]Add-on Name:[/COLOR] %s' % name,'[COLOR=dodgerblue]Version:[/COLOR] %s' % version)

------------------------------------------------------------------------------------------

###### ADDON LISTS:
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
	-------------
	enabled_list = Addon_List(enabled=True)
	disabled_list = Addon_List(enabled=False)
	my_return = ''

	for item in enabled_list:
	    my_return += '[COLOR=lime]ENABLED:[/COLOR] %s\n' % item
	for item in disabled_list:
	    my_return += '[COLOR=red]DISABLED:[/COLOR] %s\n' % item
	koding.Text_Box('ADDON STATUS',my_return)

------------------------------------------------------------------------------------------

###### ADDON SERVICE
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
	-------------
	dialog.ok('CHECKING FOR SERVICES','We will now check for all add-ons installed which contain services')
	service_addons = Addon_Service(mode='list')
	my_text = 'List of add-ons running as a service:\n\n'
	for item in service_addons:
	    my_text += item+'\n'
	koding.Text_Box('[COLOR gold]SERVICE ADDONS[/COLOR]',my_text)

------------------------------------------------------------------------------------------

###### ADDON SETTINGS - RETRIEVE/SET VALUE:
Change or retrieve an add-on setting.

	CODE: Addon_Setting(setting, [value, addon_id])

	AVAILABLE PARAMS:
	            
	    (*) setting  -  This is the name of the setting you want to access, by
	    default this function will return the value but if you add the
	    value param shown below it will CHANGE the setting.

	    value  -  If set this will change the setting above to whatever value
	    is in here.

	    addon_id  -  By default this will use your current add-on id but you
	    can access any add-on you want by entering an id in here.
	    
	EXAMPLE CODE:
	-------------
	dialog.ok('ADDON SETTING','We will now try and pull the language settings for the YouTube add-on')
	if os.path.exists(xbmc.translatePath('special://home/addons/plugin.video.youtube')):
	    my_setting = koding.Addon_Setting(setting='youtube.language',addon_id='plugin.video.youtube')
	    dialog.ok('YOUTUBE SETTING','[COLOR=dodgerblue]Setting name:[/COLOR] youtube.language','[COLOR=dodgerblue]Value:[/COLOR] %s' % my_setting)
	else:
	    dialog.ok('YOUTUBE NOT INSTALLED','Sorry we cannot run this example as you don\'t have YouTube installed.')

------------------------------------------------------------------------------------------

###### ADDON SETTINGS - OPEN:
By default this will open the current add-on settings but if you pass through an addon_id it will open the settings for that add-on.

	CODE: Open_Settings([addon_id, focus, click, stop_script])

	AVAILABLE PARAMS:

	    addon_id    - This optional, it can be any any installed add-on id. If nothing is passed
	    through the current add-on settings will be opened.

	    focus  -  This is optional, if not set the settings will just open to the first item
	    in the list (normal behaviour). However if you want to open to a specific category and
	    setting then enter the number in here separated by a dot. So for example if we want to
	    focus on the 2nd category and 3rd setting in the list we'd send through focus='2.3'

	    click  -  If you want the focused item to automatically be clicked set this to True.

	    stop_script - By default this is set to True, as soon as the addon settings are opened
	    the current script will stop running. If you pass through as False then the script will
	    continue running in the background - opening settings does not pause a script, Kodi just
	    see's it as another window being opened.

	EXAMPLE CODE:
	-------------
	youtube_path = xbmc.translatePath('special://home/addons/plugin.video.youtube')
	if os.path.exists(youtube_path):
	    dialog.ok('YOUTUBE SETTINGS','We will now open the YouTube settings.','We will focus on category 2, setting 3 AND send a click.')
	    koding.Open_Settings(addon_id='plugin.video.youtube',focus='2.3',click=True,stop_script=True)
	else:
	    dialog.ok('YOUTUBE NOT INSTALLED','We cannot run this example as it uses the YouTube add-on which has not been found on your system.')

------------------------------------------------------------------------------------------

###### ADDON TOGGLE:
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
	-------------
	xbmc.executebuiltin('ActivateWindow(Videos, addons://sources/video/)')
	xbmc.sleep(2000)
	dialog.ok('DISABLE YOUTUBE','We will now disable YouTube (if installed)')
	koding.Toggle_Addons(addon='plugin.video.youtube', enable=False, safe_mode=True, exclude_list=[], new_only=False)
	koding.Refresh('container')
	xbmc.sleep(2000)
	dialog.ok('ENABLE YOUTUBE','When you click OK we will enable YouTube (if installed)')
	koding.Toggle_Addons(addon='plugin.video.youtube', enable=True, safe_mode=True, exclude_list=[], new_only=False)
	koding.Refresh('container')

------------------------------------------------------------------------------------------

###### ADULT TOGGLE:
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

------------------------------------------------------------------------------------------

###### CALLER(S) OF FUNCTION:
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
	-------------
	my_addon = koding.Caller(my_return='addon')
	my_addons = koding.Caller(my_return='addons')
	my_path = koding.Caller(my_return='path')
	my_paths = koding.Caller(my_return='paths')

	dialog.ok('ADD-ON ID', 'Addon id you called this function from:','[COLOR=dodgerblue]%s[/COLOR]' % my_addon)
	dialog.ok('SCRIPT PATH', 'Script which called this function:','[COLOR=dodgerblue]%s[/COLOR]' % my_path)

	addon_list = 'Below is a list of add-on id\'s which have been called to get to this final piece of code:\n\n'
	for item in my_addons:
	    addon_list += item+'\n'
	koding.Text_Box('ADD-ON LIST', addon_list)
	koding.Sleep_If_Window_Active(10147)
	path_list = 'Below is a list of scripts which have been called to get to this final piece of code:\n\n'
	for item in my_paths:
	    path_list += item+'\n'
	koding.Text_Box('ADD-ON LIST', path_list)

------------------------------------------------------------------------------------------

###### CHECK REPO AVAILABILITY STATUS:
This will check the status of repo and return True if the repo is online or False
if it contains paths that are no longer accessible online.

IMPORTANT: If you're running an old version of Kodi which uses the old Python 2.6
(OSX and Android lower than Kodi 17 or a linux install with old Python installed on system)
you will get a return of False on https links regardless of their real status. This is due
to the fact Python 2.6 cannot access secure links. Any still using standard http links
will return the correct results.

	CODE:  Check_Repo(repo, [show_busy, timeout])

	AVAILABLE PARAMS:

	    (*) repo  -  This is the name of the folder the repository resides in.
	    You can either use the full path or just the folder name which in 99.99%
	    of cases is the add-on id. If only using the folder name DOUBLE check first as
	    there are a handful which have used a different folder name to the actual add-on id!

	    show_busy - By default this is set to True and a busy dialog will show during the check

	    timeout - By default this is set to 10 (seconds) - this is the maximum each request
	    to the repo url will take before timing out and returning False.

	EXAMPLE CODE:
	-------------
	repo_status = Check_Repo('special://xbmc',show_busy=False,timeout=10)
	if repo_status:
	    dialog.ok('REPO STATUS','The repository modules4all is: [COLOR=lime]ONLINE[/COLOR]')
	else:
	    dialog.ok('REPO STATUS','The repository modules4all is: [COLOR=red]OFFLINE[/COLOR]')

------------------------------------------------------------------------------------------

###### DEFAULT SETTING:
This will return the DEFAULT value for a setting (as set in resources/settings.xml)
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
	-------------
	youtube_path = xbmc.translatePath('special://home/addons/plugin.video.youtube')
	if os.path.exists(youtube_path):
	    my_value = koding.Default_Setting(setting='youtube.region', addon_id='plugin.video.youtube', reset=False)
	    dialog.ok('YOUTUBE SETTING','Below is a default setting for plugin.video.youtube:','Setting: [COLOR=dodgerblue]youtube.region[/COLOR]','Value: [COLOR=dodgerblue]%s[/COLOR]' % my_value)
	else:
	    dialog.ok('YOUTUBE NOT INSTALLED','We cannot run this example as it uses the YouTube add-on which has not been found on your system.')

------------------------------------------------------------------------------------------

###### DELETE COOKIES:
This will delete your cookies file.

	CODE: Delete_Cookies([filename])

	AVAILABLE PARAMS:

	    filename - By default this is set to the filename 'cookiejar'.
	    This is the default cookie filename which is created by the Open_URL
	    function but you can use any name you want and this function will
	    return True or False on whether or not it's successfully been removed.

	EXAMPLE CODE:
	-------------
	Open_URL(url='http://google.com',cookiejar='google')
	dialog.ok('GOOGLE COOKIES CREATED','We have just opened a page to google.com, if you check your addon_data folder for your add-on you should see a cookies folder and in there should be a cookie called "google". When you press OK this will be removed.')

------------------------------------------------------------------------------------------

###### DEPENDENCY CHECK:
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
	-------------
	current_id = xbmcaddon.Addon().getAddonInfo('id')
	dependencies = koding.Dependency_Check(addon_id=current_id, recursive=True)
	clean_text = ''
	for item in dependencies:
	    clean_text += item+'\n'
	koding.Text_Box('Modules required for %s'%current_id,clean_text)

------------------------------------------------------------------------------------------

###### INSTALLED ADD-ON DETAILS:
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
	-------------
	my_video_plugins = koding.Installed_Addons(types='xbmc.python.pluginsource', content='video', properties='name')
	final_string = ''
	for item in my_video_plugins:
	    final_string += 'ID: %s | Name: %s\n'%(item["addonid"], item["name"])
	koding.Text_Box('LIST OF VIDEO PLUGINS',final_string)

------------------------------------------------------------------------------------------

###### SETTINGS - CREATE CUSTOM ADD-ON SETTINGS:
All credit goes to OptimusGREEN for this module.

This will create a new settings file for your add-on which you can read and write to. This is separate
to the standard settings.xml and you can call the file whatever you want, however you would presumably
call it something other than settings.xml as that is already used by Kodi add-ons.

	CODE:  XML(path)

	AVAILABLE CLASSES:

	ParseValue  -  This class will allow you to get the value of an item in these custom settings.

	SetValue  -  This class allows you to set a value to the custom settings. If the settings.xml doesn't exist it will be automatically created so long as the path given in XML is writeable.


	EXAMPLE CODE:
	-------------
	myXmlFile = "special://userdata/addon_data/script.module.python.koding.aio.alt/timefile.xml"
	timefile = koding.xml(myXmlFile)
	getSetting = timefile.ParseValue
	setSetting = timefile.SetValue
	dialog.ok('CHECK SETTINGS','If you take a look in the addon_data folder for python koding a new file called timefile.xml will be created when you click OK.')
	setSetting("autorun", "true")
	autoRun = getSetting("autorun")
	dialog.ok('AUTORUN VALUE','The value of autorun in these new settings is [COLOR dodgerblue]%s[/COLOR].[CR][CR]Press OK to delete this file.'%autoRun)
	os.remove(koding.Physical_Path(myXmlFile))

------------------------------------------------------------------------------------------

###### TOGGLE ADD-ONS:
Send through either a list of add-on ids or one single add-on id. The add-ons sent through will then be added
to the addons*.db and enabled or disabled (depending on state sent through).

WARNING: If safe_mode is set to False this directly edits the addons*.db rather than using JSON-RPC.
Although directly amending the db is a lot quicker there is no guarantee it won't cause severe problems in
later versions of Kodi (this was created for v17). DO NOT set safe_mode to False unless you 100% understand
the consequences!

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

	EXAMPLE CODE:
	-------------
		xbmc.executebuiltin('ActivateWindow(Videos, addons://sources/video/)')
		xbmc.sleep(2000)
		dialog.ok('DISABLE YOUTUBE','We will now disable YouTube (if installed)')
		koding.Toggle_Addons(addon='plugin.video.youtube', enable=False, safe_mode=True, exclude_list=[], new_only=False)
		koding.Refresh('container')
		xbmc.sleep(2000)
		dialog.ok('ENABLE YOUTUBE','When you click OK we will enable YouTube (if installed)')
		koding.Toggle_Addons(addon='plugin.video.youtube', enable=True, safe_mode=True, exclude_list=[], new_only=False)

------------------------------------------------------------------------------------------

## A N D R O I D   S P E C I F I C

------------------------------------------------------------------------------------------

###### ANDROID APP SETTINGS:
Open up the settings for an installed Android app.

	CODE: App_Settings(apk_id)

	AVAILABLE PARAMS:

	    (*) apk_id  -  The id of the app you want to open the settings for.

	EXAMPLE CODE:
	-------------
	my_apps = koding.My_Apps()
	choice = dialog.select('CHOOSE AN APK', my_apps)
	koding.App_Settings(apk_id=my_apps[choice])

------------------------------------------------------------------------------------------

###### INSTALLED APPS:
Return a list of apk id's installed on system

	CODE: My_Apps()

	EXAMPLE CODE:
	-------------
	my_apps = koding.My_Apps()
	choice = dialog.select('CHOOSE AN APK', my_apps)
	if choice >= 0:
	    koding.App_Settings(apk_id=my_apps[choice])

------------------------------------------------------------------------------------------

###### START ANDROID APP:
Open an Android application

	CODE: Start_App(apk_id)

	AVAILABLE PARAMS:

	    (*) apk_id  -  The id of the app you want to open.

	EXAMPLE CODE:
	-------------
	dialog.ok('OPEN FACEBOOK','Presuming you have Facebook installed and this is an Android system we will now open that apk')
	koding.Start_App(apk_id='com.facebook.katana')

------------------------------------------------------------------------------------------

###### UNINSTALL ANDROID APP
Uninstall and Android app

	CODE: Uninstall_APK(apk_id)

	EXAMPLE CODE:
	-------------
	if dialog.yesno('UNINSTALL FACEBOOK','Would you like to uninstall the Facebook app from your system?'):
	    koding.Uninstall_APK(apk_id='com.facebook.katana')

------------------------------------------------------------------------------------------

## D A T A B A S E S

------------------------------------------------------------------------------------------

###### A GENERIC QUERY:
Open a database and either return an array of results with the SELECT SQL command or perform an action such as INSERT, UPDATE, CREATE.

	CODE:  DB_Query(db_path, query, [values])

	AVAILABLE PARAMS:

	    (*) db_path -  the full path to the database file you want to access.
	    
	    (*) query   -  this is the actual db query you want to process, use question marks for values

	    values  -  a list of values, even if there's only one value it must be sent through as a list item.

	IMPORTANT: Directly accessing databases which are outside of your add-ons domain is very much frowned
	upon. If you need to access a built-in kodi database (as shown in example below) you should always use
	the JSON-RPC commands where possible. 

	EXAMPLE CODE:
	-------------
	dbpath = filetools.DB_Path_Check('addons')
	db_table = 'addon'
	kodi_version = int(float(xbmc.getInfoLabel("System.BuildVersion")[:2]))
	if kodi_version >= 17:
	    db_table = 'addons'
	db_query = koding.DB_Query(db_path=dbpath, query='SELECT * FROM %s WHERE addonID LIKE ? AND addonID NOT LIKE ?'%db_table, values=['%youtube%','%script.module%'])
	koding.Text_Box('DB SEARCH RESULTS',str(db_query))
------------------------------------------------------------------------------------------

###### ADD TO TABLE:
Add a row to the table in /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Add_To_Table(table, spec)

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	    (*) spec   -  Sent through as a dictionary this is the colums and constraints.

	    abort_on_error  -  Default is set to False but set to True if you want to abort
	    the process when it hits an error.
	    
	EXAMPLE CODE:
	-------------
	create_specs = {"columns":{"name":"TEXT", "id":"TEXT"}}
	koding.Create_Table("test_table", create_specs)
	add_specs1 = {"name":"YouTube", "id":"plugin.video.youtube"}
	add_specs2 = {"name":"vimeo","id":"plugin.video.vimeo"}
	koding.Add_To_Table("test_table", add_specs1)
	koding.Add_To_Table("test_table", add_specs2)
	results = koding.Get_All_From_Table("test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB RESULTS', final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### ADD MULTIPLE ROWS TO TABLE:
This will allow you to add multiple rows to a table in one big (fast) bulk command
The db file is: /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Add_To_Table(table, spec)

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	    (*) keys   -  Send through a list of keys you want to add to

	    (*) values -  A list of values you want to add, this needs to be
	    a list of lists (see example below)

	EXAMPLE CODE:
	-------------
	create_specs = {"columns":{"name":"TEXT", "id":"TEXT"}}
	koding.Create_Table("test_table", create_specs)
	dialog.ok('ADD TO TABLE','Lets add the details of 3 add-ons to "test_table" in our database.')
	mykeys = ["name","id"]
	myvalues = [("YouTube","plugin.video.youtube"), ("vimeo","plugin.video.vimeo"), ("test2","plugin.video.test2")]
	koding.Add_Multiple_To_Table(table="test_table", keys=mykeys, values=myvalues)
	results = koding.Get_All_From_Table("test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB RESULTS', 'Below are details of the items pulled from our db:\n\n%s'%final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### CREATE A NEW TABLE:
Create a new table in the database at /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Create_Table(table, spec)

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	    (*) spec   -  Sent through as a dictionary this is the colums and constraints.

	EXAMPLE CODE:
	-------------
	create_specs = { "columns":{"name":"TEXT", "id":"TEXT"}, "constraints":{"unique":"id"} }
	koding.Create_Table("test_table", create_specs)
	dialog.ok('TABLE CREATED','A new table has been created in your database and the id column has been set as UNIQUE.')
	my_specs = {"name":"YouTube", "id":"plugin.video.youtube"}
	try:
	    koding.Add_To_Table("test_table", my_specs)
	    koding.Add_To_Table("test_table", my_specs)
	except:
	    dialog.ok('FAILED TO ADD','Could not add duplicate items because the the column "id" is set to be UNIQUE')
	results = koding.Get_All_From_Table("test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB RESULTS', final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### GET ALL RESULTS FROM A TABLE:
Return a list of all entries from a specific table in /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Get_All_From_Table(table)

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	EXAMPLE CODE:
	-------------
	create_specs = {"columns":{"name":"TEXT", "id":"TEXT"}}
	koding.Create_Table("test_table", create_specs)
	add_specs1 = {"name":"YouTube", "id":"plugin.video.youtube"}
	add_specs2 = {"name":"vimeo","id":"plugin.video.vimeo"}
	koding.Add_To_Table("test_table", add_specs1)
	koding.Add_To_Table("test_table", add_specs2)
	results = koding.Get_All_From_Table("test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB RESULTS', final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### GET SPECIFIC RESULTS FROM A TABLE:
Return a list of all entries matching a specific criteria from the
database stored at: /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Get_From_Table(table, spec, compare_operator)

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	    spec  -  This is the query value, sent through as a dictionary.

	    default_compare_operator  -  By default this is set to '=' but could be any
	    other SQL query string such as 'LIKE', 'NOT LIKE', '!=' etc.

	EXAMPLE CODE:
	-------------
	create_specs = {"columns":{"name":"TEXT", "id":"TEXT"}}
	koding.Create_Table("test_table", create_specs)
	add_specs1 = {"name":"YouTube", "id":"plugin.video.youtube"}
	add_specs2 = {"name":"vimeo","id":"plugin.video.vimeo"}
	koding.Add_To_Table("test_table", add_specs1)
	koding.Add_To_Table("test_table", add_specs2)
	results = koding.Get_From_Table(table="test_table", spec={"name":"%vim%"}, default_compare_operator="LIKE")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB CONTENTS', final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### REMOVE ROW FROM TABLE:
Remove entries in the db table at /userdata/addon_data/<your_addon_id>/database.db

	CODE:  Remove_From_Table(table, spec, [compare_operator])

	AVAILABLE PARAMS:

	    (*) table  -  The table name you want to query

	    spec  -  This is the query value, sent through as a dictionary.

	    default_compare_operator  -  By default this is set to '=' but could be any
	    other SQL query string such as 'LIKE', 'NOT LIKE', '!=' etc.

	EXAMPLE CODE:
	-------------
	create_specs = {"columns":{"name":"TEXT", "id":"TEXT"}}
	koding.Create_Table(table="test_table", spec=create_specs)
	add_specs1 = {"name":"YouTube", "id":"plugin.video.youtube"}
	add_specs2 = {"name":"vimeo","id":"plugin.video.vimeo"}
	koding.Add_To_Table(table="test_table", spec=add_specs1)
	koding.Add_To_Table(table="test_table", spec=add_specs2)
	results = koding.Get_All_From_Table(table="test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('DB CONTENTS', final_results)
	dialog.ok('REMOVE ITEM','We will now remove vimeo from the table, lets see if it worked...')
	koding.Remove_From_Table(table="test_table", spec={"name":"vimeo"})
	results = koding.Get_All_From_Table(table="test_table")
	final_results = ''
	for item in results:
	    final_results += 'ID: %s | Name: %s\n'%(item["id"], item["name"])
	koding.Text_Box('NEW DB CONTENTS', final_results)
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

###### REMOVE TABLE:
Use with caution, this will completely remove a database table and
all of it's contents. The only database you can access with this command
is your add-ons own db file called database.db

	CODE:  Remove_Table(table)

	AVAILABLE PARAMS:

	    (*) table  -  This is the name of the table you want to permanently delete.

	EXAMPLE CODE:
	-------------
	dialog.ok('REMOVE TABLE','It\'s a bit pointless doing this as you can\'t physically see what\'s happening so you\'ll just have to take our word it works!')
	koding.Remove_Table('test_table')

------------------------------------------------------------------------------------------

## D I A L O G S

------------------------------------------------------------------------------------------

###### BROWSE TO A FILE AND RETURN PATH:
This will allow the user to browse to a specific file and return the path.

IMPORTANT: Do not confuse this with the Browse_To_Folder function

	CODE: koding.Browse_To_File([header, path, extension, browse_in_archives])

	AVAILABLE PARAMS:

	    header    -  As the name suggests this is a string to be used for the header/title
	    of the window. The default is "Select the file you want to use".

	    path      -  Optionally you can add a default path for the browse start folder.
	    The default start position is the Kodi HOME folder.

	    extension -  Optionally set extensions to filter by, let's say you only wanted
	    zip and txt files to show you would send through '.zip|.txt'

	    browse_in_archives -  Set to true if you want to be able to browse inside zips and
	    other archive files. By default this is set to False.

	EXAMPLE CODE:
	-------------
	dialog.ok('[COLOR gold]BROWSE TO FILE 1[/COLOR]','We will now browse to your addons folder with browse_in_archives set to [COLOR dodgerblue]False[/COLOR]. Try clicking on a zip file if you can find one (check packages folder).')
	folder = koding.Browse_To_File(header='Choose a file you want to use', path='special://home/addons')
	dialog.ok('FOLDER DETAILS','File path: [COLOR=dodgerblue]%s[/COLOR]'%folder)
	dialog.ok('[COLOR gold]BROWSE TO FILE 2[/COLOR]','We will now browse to your addons folder with browse_in_archives set to [COLOR dodgerblue]True[/COLOR]. Try clicking on a zip file if you can find one (check packages folder).')
	folder = koding.Browse_To_File(header='Choose a file you want to use', path='special://home/addons', browse_in_archives=True)
	dialog.ok('FOLDER DETAILS','File path: [COLOR=dodgerblue]%s[/COLOR]'%folder)

------------------------------------------------------------------------------------------

###### BROWSE TO A FOLDER AND RETURN PATH:
As the title suggests this will bring up a dialog that allows the user to browse to a folder
and the path is then returned.

IMPORTANT: Do not confuse this with the Browse_To_File function

	CODE: Browse_To_Folder(header, path)

	AVAILABLE PARAMS:
	    header  -  As the name suggests this is a string to be used for the header/title
	    of the window. The default is "Select the folder you want to use".

	    path    -  Optionally you can add a default path for the browse start folder.
	    The default start position is the Kodi HOME folder.

	
	EXAMPLE CODE:
	-------------
	folder = koding.Browse_To_Folder(header='Choose a folder you want to use', path='special://home/userdata')
	dialog.ok('FOLDER DETAILS','Folder path: [COLOR=dodgerblue]%s[/COLOR]'%folder)

------------------------------------------------------------------------------------------

###### COUNTDOWN TIMER:
Bring up a countdown timer and return true if waited or false if cancelled.

	CODE: Countdown(title, message, update_msg, wait_time, allow_cancel, cancel_msg):

	AVAILABLE PARAMS:

	    title  -  The header string in the dialog window, the default is:
	    'COUNTDOWN STARTED'

	    message   -  A short line of info which will show on the first line
	    of the dialog window just below the title. Default is:
	    'A quick simple countdown example.'

	    update_msg  - The message you want to update during the countdown.
	    This must contain a %s which will be replaced by the current amount
	    of seconds that have passed. The default is:
	    'Please wait, %s seconds remaining.'

	    wait_time  -  This is the amount of seconds you want the countdown to
	    run for. The default is 10.

	    allow_cancel  -  By default this is set to true and the user can cancel
	    which will result in False being returned. If this is set to True
	    they will be unable to cancel.

	    cancel_msg  -  If allow_cancel is set to False you can add a custom
	    message when the user tries to cancel. The default string is:
	    '[COLOR=gold]Sorry, this process cannot be cancelled[/COLOR]'

	EXAMPLE CODE:
	-------------
	dialog.ok('COUNTDOWN EXAMPLE', 'Press OK to bring up a countdown timer', '', 'Try cancelling the process.')
	my_return = koding.Countdown(title='COUNTDOWN EXAMPLE', message='Quick simple countdown message (cancel enabled).', update_msg='%s seconds remaining', wait_time=5)
	if my_return:
	    dialog.ok('SUCCESS!','Congratulations you actually waited through the countdown timer without cancelling!')
	else:
	    dialog.ok('BORED MUCH?','What happened, did you get bored waiting?', '', '[COLOR=dodgerblue]Let\'s set off another countdown you CANNOT cancel...[/COLOR]')
	    koding.Countdown(title='COUNTDOWN EXAMPLE', message='Quick simple countdown message (cancel disabled).', update_msg='%s seconds remaining', wait_time=5, allow_cancel=False, cancel_msg='[COLOR=gold]Sorry, this process cannot be cancelled[/COLOR]')

------------------------------------------------------------------------------------------

###### CUSTOM DIALOG:
A fully customisable dialog where you can have as many buttons as you want.
Similar behaviour to the standard Kodi yesno dialog but this allows as many buttons
as you want, as much text as you want (with a slider) as well as fully configurable
sizing and positioning.

	CODE: Custom_Dialog([pos, dialog, size, button_width, header, main_content, buttons,\
	    header_color, text_color, background, transparency, highlight_color, button_color_focused,\
	    button_trans_focused, button_color_nonfocused, button_trans_nonfocused])

	AVAILABLE PARAMS:

	    pos  -  This is the co-ordinates of where on the screen you want the
	    dialog to appear. This needs to be sent through as a string so for
	    example if you want the dialog top left corner to be 20px in and
	    10px down you would use pos='20x10'. By default this is set to 'center'
	    which will center the dialog on the screen.

	    dialog   -  By default this is set to 'Text'. Currently that is the
	    only custom dialog available but there are plans to improve upon this
	    and allow for image and even video dialogs.

	    size  - Sent through as a string this is the dimensions you want the
	    dialog to be, by default it's set to '700x500' but you can set to any
	    size you want using that same format. Setting to 'fullscreen' will
	    use 1280x720 (fullscreen).

	    button_width  -  This is sent through as an integer and is the width you
	    want your buttons to be. By default this is set to 200 which is quite large
	    but looks quite nice if using only 2 or 3 buttons.

	    header  -  Sent through as a string this is the header shown in the dialog.
	    The default is 'Disclaimer'.

	    header_color  -  Set the text colour, by default it's 'gold'

	    text_color  -  Set the text colour, by default it's 'white'

	    main_content  -  This is sent through as a string and is the main message text
	    you want to show in your dialog. When the ability to add videos, images etc.
	    is added there may well be new options added to this param but it will remain
	    backwards compatible.

	    buttons  -  Sent through as a list (tuple) this is a list of all your buttons.
	    Make sure you do not duplicate any names otherwise it will throw off the
	    formatting of the dialog and you'll get false positives with the results.

	    background  -  Optionally set the background colour (hex colour codes required).
	    The default is '000000' (black).

	    transparency  -  Set the percentage of transparency as an integer. By default
	    it's set to 100 which is a solid colour.

	    highlight_color  -  Set the highlighted text colour, by default it's 'gold'

	    button_color_focused - Using the same format as background you can set the
	    colour to use for a button when it's focused.

	    button_trans_focused - Using the same format as transparency you can set the
	    transparency amount to use on the button when in focus.

	    button_color_nonfocused - Using the same format as background you can set the
	    colour to use for buttons when they are not in focus.

	    button_trans_nonfocused - Using the same format as transparency you can set the
	    transparency amount to use on the buttons when not in focus.

	EXAMPLE CODE:
	-------------
	main_text = 'This is my main text.\n\nYou can add anything you want in here and the slider will allow you to see all the contents.\n\nThis example shows using a blue background colour and a transparency of 90%.\n\nWe have also changed the highlighted_color to yellow.'
	my_buttons = ['button 1', 'button 2', 'button 3']
	my_choice = koding.Custom_Dialog(main_content=main_text,pos='center',buttons=my_buttons,background='213749',transparency=90,highlight_color='yellow')
	dialog.ok('CUSTOM DIALOG 1','You selected option %s'%my_choice,'The value of this is: [COLOR=dodgerblue]%s[/COLOR]'%my_buttons[my_choice])

	main_text = 'This is example 2 with no fancy colours, just a fullscreen and a working scrollbar.\n\nYou\'ll notice there are also a few more buttons on this one.\n\nline 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10\nline 11\nline 12\nline 13\nline 14\nline 15\nline 16\nline 17\nline 18\nline 19\nline 20\n\nYou get the idea we\'ll stop there!'
	my_buttons = ['button 1', 'button 2', 'button 3','button 4', 'button 5', 'button 6','button 7', 'button 8', 'button 9','button 10', 'button 11', 'button 12', 'button 13','button 14', 'button 15', 'button 16','button 17', 'button 18', 'button 19','button 20']
	my_choice = koding.Custom_Dialog(main_content=main_text,pos='center',size='fullscreen',buttons=my_buttons)
	dialog.ok('CUSTOM DIALOG 2','You selected option %s'%my_choice,'The value of this is: [COLOR=dodgerblue]%s[/COLOR]'%my_buttons[my_choice])

------------------------------------------------------------------------------------------

###### ENABLE/DISABLE THE BUSY (WORKING) SYMBOL:
This will show/hide a "working" symbol.

	CODE: Show_Busy([status, sleep])

	AVAILABLE PARAMS:

	    status - This optional, by default it's True which means the "working"
	    symbol appears. False will disable.

	    sleep  -  If set the busy symbol will appear for <sleep> amount of
	    milliseconds and then disappear.

	EXAMPLE CODE:
	-------------
	dialog.ok('BUSY SYMBOL','Press OK to show a busy dialog which restricts any user interaction. We have added a sleep of 5 seconds at which point it will disable.')
	koding.Show_Busy(sleep=5000)
	dialog.ok('BUSY SYMBOL','We will now do the same but with slightly different code')
	koding.Show_Busy(status=True)
	xbmc.sleep(5000)
	koding.Show_Busy(status=False)

------------------------------------------------------------------------------------------

###### KEYBOARD:
Show an on-screen keyboard and return the string

	CODE: koding.Keyboard([default, heading, hidden, return_false, autoclose, kb_type])

	AVAILABLE PARAMS:

	    heading  -  Optionally enter a heading for the text box.

	    default  -  This is optional, if set this will act as the default text shown in the text box

	    hidden   -  Boolean, if set to True the text will appear as hidden (starred out)

	    return_false - By default this is set to False and when escaping out of the keyboard
	    the default text is returned (or an empty string if not set). If set to True then
	    you'll receive a return of False.

	    autoclose - By default this is set to False but if you want the keyboard to auto-close
	    after a period of time you can send through an integer. The value sent through needs to
	    be milliseconds, so for example if you want it to close after 3 seconds you'd send through
	    3000. The autoclose function only works with standard alphanumeric keyboard types.

	    kb_type  -  This is the type of keyboard you want to show, by default it's set to alphanum.
	    A list of available values are listed below:

	        'alphanum'  - A standard on-screen keyboard containing alphanumeric characters.
	        'numeric'   - An on-screen numerical pad.
	        'date'      - An on-screen numerical pad formatted only for a date.
	        'time'      - An on-screen numerical pad formatted only for a time.
	        'ipaddress' - An on-screen numerical pad formatted only for an IP Address.
	        'password'  - A standard keyboard but returns value as md5 hash. When typing
	        the text is starred out, once you've entered the password you'll get another
	        keyboard pop up asking you to verify. If the 2 match then your md5 has is returned.


	EXAMPLE CODE:
	-------------
	mytext = koding.Keyboard(heading='Type in the text you want returned',default='test text')
	dialog.ok('TEXT RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	dialog.ok('AUTOCLOSE ENABLED','This following example we\'ve set the autoclose to 3000. That\'s milliseconds which converts to 3 seconds.')
	mytext = koding.Keyboard(heading='Type in the text you want returned',default='this will close in 3s',autoclose=3000)
	dialog.ok('TEXT RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	mytext = koding.Keyboard(heading='Enter a number',kb_type='numeric')
	dialog.ok('NUMBER RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	dialog.ok('RETURN FALSE ENABLED','All of the following examples have "return_false" enabled. This means if you escape out of the keyboard the return will be False.')
	mytext = koding.Keyboard(heading='Enter a date',return_false=True,kb_type='date')
	dialog.ok('DATE RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	mytext = koding.Keyboard(heading='Enter a time',return_false=True,kb_type='time')
	dialog.ok('TIME RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	mytext = koding.Keyboard(heading='IP Address',return_false=True,kb_type='ipaddress',autoclose=5)
	dialog.ok('IP RETURNED','You typed in:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)
	mytext = koding.Keyboard(heading='Password',kb_type='password')
	dialog.ok('MD5 RETURN','The md5 for this password is:', '', '[COLOR=dodgerblue]%s[/COLOR]'%mytext)

------------------------------------------------------------------------------------------

###### NOTIFICATION POPUP:
Show a short notification for x amount of seconds

	CODE: koding.Notify(title, message, [duration, icon])

	AVAILABLE PARAMS:

	    (*) title    -  A short title to show on top line of notification

	    (*) message  -  A short message to show on the bottom line of notification

	    duration  -  An integer in milliseconds, the default to show the notification for is 2000

	    icon      -  The icon to show in notification bar, default is the update icon from this module. 

	EXAMPLE CODE:
	-------------
	koding.Notify(title='TEST NOTIFICATION', message='This is a quick 5 second test', duration=5000)

------------------------------------------------------------------------------------------

###### OK DIALOG:
This will bring up a short text message in a dialog.ok window.

	CODE: OK_Dialog(title,message)

	AVAILABLE PARAMS:

	    (*) title  -  This is title which appears in the header of the window.

	    (*) message  -  This is the main text you want to appear.

	EXAMPLE CODE:
	-------------
	koding.OK_Dialog(title='TEST DIALOG',message='This is a test dialog ok box. Click OK to quit.')

------------------------------------------------------------------------------------------

###### PERCENTAGE RESET (CUSTOM DIALOGS):
If using the Update_Progress function for setting percentages in skinning then this
will allow you to reset all the percent properties (1-100)

	CODE: Reset_Percent([property,window_id])

	AVAILABLE PARAMS:

	    property  -  the property name you want reset, this will reset all properties starting
	    with this string from 1-100. For example if you use the default 'update_percent_' this
	    will loop through and reset update_percent_1, update_percent_2 etc. all the way through
	    to update_percent_100.

	    window_id -  By default this is set to 10000 but you can send any id through you want.

	    kwargs  -  Send through any other params and the respective property will be set.colours etc.')

------------------------------------------------------------------------------------------

###### SELECTION DIALOG
This will bring up a selection of options to choose from. The options are
sent through as a list and only one can be selected - this is not a multi-select dialog.

	CODE: Select_Dialog(title,options,[key])

	AVAILABLE PARAMS:

	    (*) title  -  This is title which appears in the header of the window.

	    (*) options  -  This is a list of the options you want the user to be able to choose from.

	    key  -  By default this is set to True so you'll get a return of the item number. For example
	    if the user picks "option 2" and that is the second item in the list you'll receive a return of
	    1 (0 would be the first item in list and 1 is the second). If set to False you'll recieve a return
	    of the actual string associated with that key, in this example the return would be "option 2".

	EXAMPLE CODE:
	-------------
	my_options = ['Option 1','Option 2','Option 3','Option 4','Option 5']
	mychoice = koding.Select_Dialog(title='TEST DIALOG',options=my_options,key=False)
	koding.OK_Dialog(title='SELECTED ITEM',message='You selected: [COLOR=dodgerblue]%s[/COLOR]\nNow let\'s try again - this time we will return a key...'%mychoice)
	mychoice = koding.Select_Dialog(title='TEST DIALOG',options=my_options,key=True)
	koding.OK_Dialog(title='SELECTED ITEM',message='The item you selected was position number [COLOR=dodgerblue]%s[/COLOR] in the list'%mychoice)

------------------------------------------------------------------------------------------

###### TEXT BOX (LARGE WINDOW OF TEXT):
This will allow you to open a blank window and fill it with some text.

	CODE: koding.Text_Box(header, message)

	AVAILABLE PARAMS:

	    (*) header  -  As the name suggests this is a string to be used for the header/title of the window

	    (*) message -  Yes you've probably already gussed it, this is the main message text


	EXAMPLE CODE:
	-------------
	koding.Text_Box('TEST HEADER','Just some random text... Use kodi tags for new lines, colours etc.')

------------------------------------------------------------------------------------------

###### UPDATE PROGRESS:
This function is designed for skinners but can be used for general Python too. It will
work out the current percentage of items that have been processed and update the
"update_percent" property accordingly (1-100). You can also send through any properties
you want updated and it will loop through updating them with the relevant values.

To send through properties just send through the property name as the param and assign to a value.
Example: Update_Progress( total_items=100,current_item=56, {"myproperty1":"test1","myproperty2":"test2"} )


	CODE: Update_Progress(total_items,current_item,[kwargs])

	AVAILABLE PARAMS:

	    (*) total_items  -  Total amount of items in your list you're processing

	    (*) current_item -  Current item number that's been processed.

	    kwargs  -  Send through any other params and the respective property will be set.colours etc.

------------------------------------------------------------------------------------------

###### UPDATE SCREEN:
This will create a full screen overlay showing progress of updates. You'll need to
use this in conjunction with the Update_Progress function.

	CODE: Update_Screen([disable_quit, auto_close))

	AVAILABLE PARAMS:

	    disable_quit  -  By default this is set to False and pressing the parent directory
	    button (generally esc) will allow you to close the window. Setting this to True
	    will mean it's not possible to close the window manually.

	    auto_close  -  By default this is set to true and when the percentage hits 100
	    the window will close. If you intend on then sending through some more commands
	    you might want to consider leaving this window open in which case you'd set this
	    to false. Bare in mind if you go this route the window will stay active until
	    you send through the kill command which is: xbmc.executebuiltin('Action(firstpage)')

	EXAMPLE CODE:
	-------------
	mykwargs = {
	    "update_header"    : "Downloading latest updates",\
	    "update_main_text" : "Your device is now downloading all the latest updates.\nThis shouldn\'t take too long, "\
	                         "depending on your internet speed this could take anything from 2 to 10 minutes.\n\n"\
	                         "Once downloaded the system will start to install the updates.",\
	    "update_bar_color" : "4e91cf",\
	    "update_icon"      : "special://home/addons/script.module.python.koding.aio.alt/resources/skins/Default/media/update.png",\
	    "update_spinner"   : "true"}
	Update_Screen()
	counter = 1
	while counter <= 60:
	    xbmc.sleep(300)
	    Update_Progress(total_items=60,current_item=counter,**mykwargs)
	    if counter == 30:
	        mykwargs = {
	            "update_header"        : "Halfway there!",\
	            "update_main_text"     : "We just updated the properties to show how you can change things on the fly "\
	                                     "simply by sending through some different properties. Both the icon and the "\
	                                     "background images you see here are being pulled from online.",\
	            "update_header_color"  : "4e91cf",\
	            "update_percent_color" : "4e91cf",\
	            "update_bar_color"     : "4e91cf",\
	            "update_background"    : "http://www.planwallpaper.com/static/images/518164-backgrounds.jpg",\
	            "update_icon"          : "http://totalrevolution.tv/img/tr_small_black_bg.jpg",\
	            "update_spinner"       : "false"}
	    counter += 1

------------------------------------------------------------------------------------------

###### YES/NO DIALOG:
This will bring up a short text message in a dialog.yesno window. This will
return True or False

	CODE: YesNo_Dialog(title,message,[yeslabel,nolabel])

	AVAILABLE PARAMS:

	    (*) title  -  This is title which appears in the header of the window.

	    (*) message  -  This is the main text you want to appear.

	    yes  -  Optionally change the default "YES" to a custom string

	    no  -  Optionally change the default "NO" to a custom string

	EXAMPLE CODE:
	-------------
	mychoice = koding.YesNo_Dialog(title='TEST DIALOG',message='This is a yes/no dialog with custom labels.\nDo you want to see an example of a standard yes/no.',yes='Go on then',no='Nooooo!')
	if mychoice:
	    koding.YesNo_Dialog(title='STANDARD DIALOG',message='This is an example of a standard one without sending custom yes/no params through.')

------------------------------------------------------------------------------------------

## D I R E C T O R Y   F U N C T I O N S

------------------------------------------------------------------------------------------

###### ADD DIRECTORY ITEM:
This allows you to create a list item/folder inside your add-on.
Please take a look at your addon default.py comments for more information
(presuming you created one at http://totalrevolution.tv)

TOP TIP: If you want to send multiple variables through to a function just
send through as a dictionary encapsulated in quotation marks. In the function
you can then use the following code to access them:

params = eval(url)
^ That will then give you a dictionary where you can just pull each variable and value from.

	CODE: Add_Dir(name, url, mode, [folder, icon, fanart, description, info_labels, content_type, context_items, context_override, playable])

	AVAILABLE PARAMS:

	    (*) name  -  This is the name you want to show for the list item

	    url   -  If the route (mode) you're calling requires extra paramaters
	    to be sent through then this is where you add them. If the function is
	    only expecting one item then you can send through as a simple string.
	    Unlike many other Add_Dir functions Python Koding does allow for multiple
	    params to be sent through in the form of a dictionary so let's say your
	    function is expecting the 2 params my_time & my_date. You would send this info
	    through as a dictionary like this:
	    url={'my_time':'10:00', 'my_date':'01.01.1970'}
	    
	    If you send through a url starting with plugin:// the item will open up into
	    that plugin path so for example:
	    url='plugin://plugin.video.youtube/play/?video_id=FTI16i7APhU'

	    mode  -  The mode you want to open when this item is clicked, this is set
	    in your master_modes dictionary (see template add-on linked above)

	    folder       -  This is an optional boolean, by default it's set to False.
	    True will open into a folder rather than an executable command

	    icon         -  The path to the thumbnail you want to use for this list item

	    fanart       -  The path to the fanart you want to use for this list item

	    description  - A description of your list item, it's skin dependant but this
	    usually appears below the thumbnail

	    info_labels  - You can send through any number of info_labels via this option.
	    For full details on the infolabels available please check the pydocs here:
	    http://mirrors.kodi.tv/docs/python-docs/16.x-jarvis/xbmcgui.html#ListItem-setInfo

	    When passing through infolabels you need to use a dictionary in this format:
	    {"genre":"comedy", "title":"test video"}
	    
	    set_art  -  Using the same format as info_labels you can set your artwork via
	    a dictionary here. Full details can be found here:
	    http://mirrors.kodi.tv/docs/python-docs/16.x-jarvis/xbmcgui.html#ListItem-setArt

	    set_property  -  Using the same format as info_labels you can set your artwork via
	    a dictionary here. Full details can be found here:
	    http://kodi.wiki/view/InfoLabels#ListItem

	    content_type - By default this will set the content_type for kodi to a blank string
	    which is what Kodi expects for generic category listings. There are plenty of different
	    types though and when set Kodi will perform different actions (such as access the
	    database looking for season/episode information for the list item).

	    WARNING: Setting the wrong content type for your listing can cause the system to
	    log thousands of error reports in your log, cause the system to lag and make
	    thousands of unnecessary db calls - sometimes resulting in a crash. You can find
	    details on the content_types available here: http://forum.kodi.tv/showthread.php?tid=299107

	    context_items - Add context items to your directory. The params you need to send through
	    need to be in a list format of [(label, action,),] look at the example code below for
	    more details.

	    context_override - By default your context items will be added to the global context
	    menu items but you can override this by setting this to True and then only your
	    context menu items will show.

	    playable  -  By default this is set to False but if set to True kodi will just try
	    and play this item natively with no extra fancy functions.

	EXAMPLE:
	--------
	my_context = [('Music','xbmc.executebuiltin("ActivateWindow(music)")'),('Programs','xbmc.executebuiltin("ActivateWindow(programs)")')]
	# ^ This is our two basic context menu items (music and programs)

	Add_Dir(name='TEST DIRECTORY', url='', mode='test_directory', folder=True, context_items=my_context, context_override=True)
	# ^ This will add a folder AND a context menu item for when bring up the menu (when focused on this directory).
	# ^^ The context_override is set to True which means it will override the default Kodi context menu items.

	Add_Dir(name='TEST ITEM', url='', mode='test_item', folder=False, context_items=my_context, context_override=False)
	# ^ This will add an item to the list AND a context menu item for when bring up the menu (when focused on this item).
	# ^^ The context_override is set to False which means the new items will appear alongside the default Kodi context menu items.

------------------------------------------------------------------------------------------

###### ROUTE:
Use this to set a function in your master_modes dictionary.
This is to be used for Add_Dir() items, see the example below.

	CODE: route(mode, [args])

	AVAILABLE PARAMS:
	            
	    (*) mode  -  This must be set, it needs to be a custom string.
	    This is the string you'd use in your Add_Dir command to call
	    the function.

	    args  -  This is optional but if the function you're calling
	    requires extra paramaters you can add them in here. Just add them
	    as a list of strings. Example: args=['name','artwork','description']

	BELOW IS AN EXAMPLE OF HOW TO CALL THE CODE IN YOUR MAIN ADDON PY FILE:
	-----------------------------------------------------------------------
	@route(mode="test", args=["name","description"])
	def Test_Function(name,description):
	    dialog.ok('This is a test function', name, description')

	koding.Add_Dir(name='Test Dialog', url={"name":"My Test Function", "description" : "Its ALIVE!!!"}, mode='test')
	koding.run()

------------------------------------------------------------------------------------------

###### RUN:
This needs to be called at the bottom of your code in the main default.py

This checks the modes called in Add_Dir and does all the clever stuff
in the background which assigns those modes to functions and sends
through the various params.

Just after this command you need to make
sure you set the endOfDirectory (as shown below).


	CODE: run([default])
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

	AVAILABLE PARAMS:
	    
	    default  -  This is the default mode you want the add-on to open
	    into, it's set as "main" by default. If you have a different mode
	    name you want to open into just edit accordingly.

------------------------------------------------------------------------------------------

## F I L E   T O O L S

------------------------------------------------------------------------------------------

###### CLEAN CACHED IMAGES:
This will check for any cached artwork and wipe if it's not been accessed more than 10 times in the past x amount of days.

	CODE: Cleanup_Textures([frequency, use_count])

	AVAILABLE PARAMS:
	    
	    frequency  -  This is an optional integer, be default it checks for any
	    images not accessed in 14 days but you can use any amount of days here.

	    use_count   -  This is an optional integer, be default it checks for any
	    images not accessed more than 10 times. If you want to be more ruthless
	    and remove all images not accessed in the past x amount of days then set this very high.

	EXAMPLE CODE:
	-------------
	dialog.ok('Clean Textures','We are going to clear any old cached images not accessed at least 10 times in the past 5 days')
	koding.Cleanup_Textures(frequency=5)

------------------------------------------------------------------------------------------

###### COMPRESS FILES:
Compress files in either zip or tar format. This will most likely be replacing
Archive_Tree longer term as this has better functionality but it's currently
missing the custom message and exclude files options.

IMPORTANT: There was a known bug where some certain compressed tar.gz files can cause the system to hang
and a bad zipfile will continue to be made until it runs out of space on your storage device. In the unlikely
event you encounter this issue just add the problematic file(s) to your exclude list. I think this has since
been fixed since a complete re-code to this function, or at least I've been unable to recreate it. If you
find this problem is still occuring please let me know on the forum at http://totalrevolution.tv/forum
(user: trevdev), thankyou.

	CODE: Compress(src,dst,[compression,parent])

	AVAILABLE PARAMS:

	    (*) src  -  This is the source folder you want to compress

	    (*) dst  -  This is the destination file you want to create

	    compression  -  By default this is set to 'zip' but you can also use 'tar'

	    parent  -  By default this is set to False which means it will compress
	    everything inside the path given. If set to True it will do the same but
	    it will include the parent folder name - ideal if you want to zip up
	    an add-on folder and be able to install via Kodi Settings.

	    exclude_dirs   - This is optional, if you have folder names you want to exclude just
	    add them here as a list item. By default the folder 'temp' is added to this list so
	    if you need to include folders called temp make sure you send through a list, even
	    if it's an empty one. The reason for leaving temp out is that's where Kodi logfiles
	    and crashlogs are stored on a lot of devices and these are generally not needed in
	    backup zips.

	    exclude_files  - This is optional, if you have specific file names you want to
	    exclude just add them here as a list item. By default the list consists of:
	    'kodi.log','kodi.old.log','xbmc.log','xbmc.old.log','spmc.log','spmc.old.log'

	EXAMPLE CODE:
	-------------
	koding_path = koding.Physical_Path('special://home/addons/script.module.python.koding.aio.alt')
	zip_dest = koding.Physical_Path('special://home/test_addon.zip')
	zip_dest2 = koding.Physical_Path('special://home/test_addon2.zip')
	tar_dest = koding.Physical_Path('special://home/test_addon.tar')
	tar_dest2 = koding.Physical_Path('special://home/test_addon2.tar')
	koding.Compress(src=koding_path,dst=zip_dest,compression='zip',parent=True)
	koding.Compress(src=koding_path,dst=zip_dest2,compression='zip',parent=False)
	koding.Compress(src=koding_path,dst=tar_dest,compression='tar',parent=True)
	koding.Compress(src=koding_path,dst=tar_dest2,compression='tar',parent=False)
	koding.Text_Box('CHECK HOME FOLDER','If you check your Kodi home folder you should now have 4 different compressed versions of the Python Koding add-on.\n\ntest_addon.zip: This has been zipped up with parent set to True\n\ntest_addon2.zip: This has been zipped up with parent set to False.\n\ntest_addon.tar: This has been compressed using tar format and parent set to True\n\ntest_addon2.tar: This has been compressed using tar format and parent set to False.\n\nFeel free to manually delete these.')

------------------------------------------------------------------------------------------

###### CONVERT PHYSICAL PATHS TO SPECIAL:
	Convert physcial paths stored in text files to their special:// equivalent or
	replace instances of physical paths to special in a string sent through.

	CODE: Convert_Special([filepath, string])

	AVAILABLE PARAMS:

	    filepath  -  This is the path you want to scan, by default it's set to the Kodi HOME directory.
	    
	    string  -  By default this is set to False which means it will convert all instances found of
	    the physical paths to their special equivalent. The scan will convert all instances in all filenames
	    ending in ini, xml, hash, properties. If you set this value to True you will get a return of your
	    'filepath' string and no files will be altered.

	    quoted  -  By default this is set to true, this means the return you get will be converted
	    with urllib.quote_plus(). This is ideal if you need to get a string you can send
	    through as a path for routing.

	EXAMPLE CODE:
	-------------
	path = koding.Physical_Path('special://profile')
	dialog.ok('ORIGINAL PATH','Let\'s convert this path to it\'s special equivalent:\n[COLOR dodgerblue]%s[/COLOR]'%path)
	path = Convert_Special(filepath=path,string=True,quoted=False)
	dialog.ok('CONVERTED PATH','This is the converted path:\n[COLOR dodgerblue]%s[/COLOR]'%path)
	if dialog.yesno('CONVERT PHYSICAL PATHS','We will now run through your Kodi folder converting all physical paths to their special:// equivalent in xml/hash/properties/ini files.\nDo you want to continue?'):
	    koding.Convert_Special()
	    dialog.ok('SUCCESS','Congratulations, all references to your physical paths have been converted to special:// paths.')

------------------------------------------------------------------------------------------

###### CREATE A DUMMY FILE:
Create a dummy file in whatever location you want and with the size you want.
Use very carefully, this is designed for testing purposes only. Accidental
useage can result in the devices storage becoming completely full in just a
few seconds. If using a cheap poor quality device (like many android units)
then you could even end up killing the device as some of them are made
with very poor components which are liable to irreversable corruption.

	CODE: koding.Dummy_File(dest, [size, size_format])

	AVAILABLE PARAMS:

	    dst          - This is the destination folder. This needs to be a FULL path including
	    the file extension. By default this is set to special://home/dummy.txt

	    size         -  This is an optional integer, by default a file of 10 MB will be created.

	    size_format  -  By default this is set to 'mb' (megabytes) but you can change this to
	    'b' (bytes), 'kb' (kilobytes), 'gb' (gigabytes)

	EXAMPLE CODE:
	-------------
	dummy = 'special://home/test_dummy.txt'
	koding.Dummy_File(dst=dummy, size=100, size_format='b')
	dialog.ok('DUMMY FILE CREATED','Check your Kodi home folder and you should see a 100 byte test_dummy.txt file.','[COLOR=gold]Press OK to delete this file.[/COLOR]')
	xbmcvfs.delete(dummy)

------------------------------------------------------------------------------------------

###### CREATE PATHS:
Send through a path to a file, if the directories required do not exist this will create them.

	CODE: Create_Paths(path)

	AVAILABLE PARAMS:

	    (*) path  -  This is the full path including the filename. The path
	    sent through will be split up at every instance of '/'

	EXAMPLE CODE:
	-------------
	my_path = xbmc.translatePath('special://home/test/testing/readme.txt')
	koding.Create_Paths(path=my_path)
	dialog.ok('PATH CREATED','Check in your Kodi home folder and you should now have sub-folders of /test/testing/.','[COLOR=gold]Press ok to remove these folders.[/COLOR]')
	shutil.rmtree(xbmc.translatePath('special://home/test'))

------------------------------------------------------------------------------------------

###### DELETE CRASHLOGS
Delete all kodi crashlogs. This function will retun the amount of successfully removed crashlogs.

	CODE: Delete_Crashlogs([extra_paths])

	AVAILABLE PARAMS:
	    extra_paths  -  By default this will search for crashlogs for xbmc,
	    kodi and spmc. If you want to add compatibility for other forks of
	    Kodi please send through a list of the files you want deleted. The
	    format to use needs to be like example shown below.

	EXAMPLE CODE:
	-------------
	# Lets setup some extra crashlog types for tvmc and ftmc kodi forks
	log_path =  xbmc.translatePath('special://logpath/')
	tvmc_path = os.path.join(log_path,'tvmc_crashlog*.*')
	ftmc_path = os.path.join(log_path,'ftmc_crashlog*.*')


	deleted_files = koding.Delete_Crashlogs(extra_paths=[tvmc_path, ftmc_path])
	if deleted_files > 0:
	    dialog.ok('CRASHLOGS DELETED','Congratulations, a total of %s crashlogs have been deleted.')
	else:
	    dialog.ok('NO CRASHLOGS','No crashlogs could be found on the system.')

------------------------------------------------------------------------------------------

###### DELETE FILES IN PATH:
Delete all specific filetypes in a path (including sub-directories)

	CODE: Delete_Files([filepath, filetype, subdirectories])

	AVAILABLE PARAMS:
	    
	    (*) filepath  -  By default this points to the Kodi HOME folder (special://home).
	    The path you send through must be a physical path and not special://

	    (*) filetype  -  The type of files you want to delete, by default it's set to *.txt

	    subdirectories  -  By default it will only search the folder given, if set to True
	    all filetypes listed above will be deleted in the sub-directories too.

	WARNING: This is an extremely powerful and dangerous tool! If you wipe your whole system
	by putting in the wrong path then it's your own stupid fault!

	EXAMPLE CODE:
	-------------
	delete_path = 'special://profile/addon_data/test'
	xbmcvfs.mkdirs(delete_path)
	test1 = os.path.join(delete_path,'test1.txt')
	test2 = os.path.join(delete_path,'test2.txt')
	koding.Text_File(test1,'w','testing1')
	koding.Text_File(test2,'w','testing2')
	dialog.ok('DELETE FILES','All *.txt files will be deleted from:', '', '/userdata/addon_data/test/')
	koding.Delete_Files(filepath=delete_path, filetype='.txt', subdirectories=True)

------------------------------------------------------------------------------------------

###### DELETE A FOLDER PATH:
Completely delete a folder and all it's sub-folders. With the ability to add
an ignore list for any folders/files you don't want removed.

	CODE: Delete_Folders(filepath, [ignore])

	AVAILABLE PARAMS:
	    
	    (*) filepath  -  Use the physical path you want to remove, this must be converted
	    to the physical path and will not work with special://

	    ignore  -  A list of paths you want to ignore. These need to be sent
	    through as physical paths so just use koding.Physical_Path() when creating
	    your list and these can be folder paths or filepaths.

	WARNING: This is an extremely powerful and dangerous tool! If you wipe important
	system files from your system by putting in the wrong path then I'm afraid that's
	your own stupid fault! A check has been put in place so you can't accidentally
	wipe the whole root.

	EXAMPLE CODE:
	-------------
	delete_path = koding.Physical_Path('special://profile/py_koding_test')

	# Create new test directory to remove
	if not os.path.exists(delete_path):
	    os.makedirs(delete_path)

	# Fill it with some dummy files
	file1 = os.path.join(delete_path,'file1.txt')
	file2 = os.path.join(delete_path,'file2.txt')
	file3 = os.path.join(delete_path,'file3.txt')
	koding.Dummy_File(dst=file1, size=10, size_format='kb')
	koding.Dummy_File(dst=file2, size=10, size_format='kb')
	koding.Dummy_File(dst=file3, size=10, size_format='kb')

	dialog.ok('TEST FILE CREATED','If you look in your userdata folder you should now see a new test folder containing 3 dummy files. The folder name is \'py_koding_test\'.')
	if dialog.yesno('[COLOR gold]DELETE FOLDER[/COLOR]','Everything except file1.txt will now be removed from:', '/userdata/py_koding_test/','Do you want to continue?'):
	    koding.Delete_Folders(filepath=delete_path, ignore=[file1])
	    dialog.ok('DELETE LEFTOVERS','When you press OK we will delete the whole temporary folder we created including it\'s contents')
	    koding.Delete_Folders(filepath=delete_path)

------------------------------------------------------------------------------------------

###### EXTRACT:
This function will extract a zip or tar file and return true or false so unlike the
builtin xbmc function "Extract" this one will pause code until it's completed the action.

	CODE: koding.Extract(src,dst,[dp])
	dp is optional, by default it is set to false

	AVAILABLE PARAMS:

	    (*) src    - This is the source file, the actual zip/tar. Make sure this is a full path to
	    your zip file and also make sure you're not using "special://". This extract function
	    is only compatible with .zip/.tar/.tar.gz files

	    (*) dst    - This is the destination folder, make sure it's a physical path and not
	    "special://...". This needs to be a FULL path, if you want it to extract to the same
	    location as where the zip is located you still have to enter the full path.

	    dp - This is optional, if you pass through the dp function as a DialogProgress()
	    then you'll get to see the status of the extraction process. If you choose not to add
	    this paramater then you'll just get a busy spinning circle icon until it's completed.
	    See the example below for a dp example.

	    show_error - By default this is set to False, if set to True an error dialog 
	    will appear showing details of the file which failed to extract.

	EXAMPLE CODE:
	-------------
	koding_path = koding.Physical_Path('special://home/addons/script.module.python.koding.aio.alt')
	zip_dest = koding.Physical_Path('special://home/test_addon.zip')
	extract_dest = koding.Physical_Path('special://home/TEST')
	koding.Compress(src=koding_path,dst=zip_dest,compression='zip',parent=True)
	dp = xbmcgui.DialogProgress()
	dp.create('Extracting Zip','Please Wait')
	if koding.Extract(_in=zip_dest,_out=extract_dest,dp=dp,show_error=True):
	    dialog.ok('YAY IT WORKED!','We just zipped up your python koding add-on then extracted it to a new folder in your Kodi root directory called TEST. Press OK to delete these files.')
	    xbmcvfs.delete(zip_dest)
	    shutil.rmtree(extract_dest)
	else:
	    dialog.ok('BAD NEWS!','UH OH SOMETHING WENT HORRIBLY WRONG')

------------------------------------------------------------------------------------------

###### FREE SPACE:
Show the amount of available free space in a path, this can be returned in a number of different formats.

	CODE: Free_Space([dirname, filesize])

	AVAILABLE PARAMS:

	    dirname  - This optional, by default it will tell you how much space is available in your special://home
	    folder. If you require information for another path (such as a different partition or storage device)
	    then enter the physical path. This currently only works for local paths and not networked drives.

	    filesize - By default you'll get a return of total bytes, however you can get the value as bytes,
	    kilobytes, megabytes, gigabytes and terabytes..

	        VALUES:
	        'b'  = bytes (integer)
	        'kb' = kilobytes (float to 1 decimal place)
	        'mb' = kilobytes (float to 2 decimal places)
	        'gb' = kilobytes (float to 3 decimal places)
	        'tb' = terabytes (float to 4 decimal places)

	EXAMPLE CODE:
	-------------
	HOME = koding.Physical_Path('special://home')
	my_space = koding.Free_Space(HOME, 'gb')
	dialog.ok('Free Space','Available space in HOME: %s GB' % my_space)

------------------------------------------------------------------------------------------

###### FOLDER SIZE:
Return the size of a folder path including sub-directories,
this can be returned in a number of different formats.

	CODE: koding.Folder_Size([dirname, filesize])

	AVAILABLE PARAMS:

	    dirname  - This optional, by default it will tell you how much space is available in your
	    special://home folder. If you require information for another path (such as a different
	    partition or storage device) then enter the physical path. This currently only works for
	    local paths and not networked drives.

	    filesize - By default you'll get a return of total bytes, however you can get the value as
	    bytes, kilobytes, megabytes, gigabytes and terabytes..

	        VALUES:
	        'b'  = bytes (integer)
	        'kb' = kilobytes (float to 1 decimal place)
	        'mb' = kilobytes (float to 2 decimal places)
	        'gb' = kilobytes (float to 3 decimal places)
	        'tb' = terabytes (float to 4 decimal places)

	EXAMPLE CODE:
	-------------
	HOME = Physical_Path('special://home')
	home_size = Folder_Size(HOME, 'mb')
	dialog.ok('Folder Size','KODI HOME: %s MB' % home_size)

------------------------------------------------------------------------------------------

###### FRESH INSTALL:
Attempt to completely wipe your install. You can send through a list
of addons or paths you want to ignore (leave in the setup) or you can
leave blank. If left blank and the platform is OpenELEC or LibreELEC
it will perform a hard reset command followed by a reboot.

	CODE:  Fresh_Install([keep_addons, ignore, keepdb)

	AVAILABLE PARAMS:

	    keep_addons  -  This is optional, if you have specific add-ons you want to omit
	    from the wipe (leave intact) then just enter a list of add-on id's here. The code
	    will determine from the addon.xml file which dependencies and sub-dependencies are
	    required for that add-on so there's no need to create a huge list, you only need to
	    list the master add-on id's. For example if you want to keep the current skin and
	    your add-on you would use: keep_addons=['plugin.program.myaddon',System('currentskin')]
	    and all addons/dependencies associated with those two add-ons will be added to the ignore
	    list.

	    ignore  -  This is optional, you can send through a list of paths you want to omit from
	    the wipe. You can use folder paths to skip the whole folder or you can use individual
	    file paths. Please make sure you use the physical path and not special://
	    So before creating your list make sure you use xbmc.translatePath()

	    keepdb  -  By default this is set to True which means the code will keep all the Kodi databases
	    intact and perform a profile reload once wipe is complete. This will mean addons, video, music,
	    epg, ADSP and viewtypes databases will remain completely untouched and Kodi should be fine to use
	    without the need for a restart. If you set keepdb to False nothing will happen once the wipe has
	    completed and it's up to you to choose what to do in your main code. I would highly recommend an
	    ok dialog followed by xbmc.executebuiltin('Quit'). This will force Kodi to recreate all the relevant
	    databases when they re-open. If you try and continue using Kodi without restarting the databases
	    will not be recreated and you risk corruption.

	EXAMPLE CODE:
	-------------
	if dialog.yesno('[COLOR gold]TOTAL WIPEOUT![/COLOR]','This will attempt give you a totally fresh install of Kodi.','Are you sure you want to continue?'):
	    if dialog.yesno('[COLOR gold]FINAL CHANCE!!![/COLOR]','If you click Yes this WILL attempt to wipe your install', '[COLOR=dodgerblue]ARE YOU 100% CERTAIN YOU WANT TO WIPE?[/COLOR]'):
	        clean_state = koding.Fresh_Install()
------------------------------------------------------------------------------------------

###### GET CONTENTS OF A PATH (INC. SUB-DIRECTORIES)
Return a list of either files or folders in a given path.

	CODE:  Get_Contents(path, [folders, subfolders, exclude_list, full_path, filter])

	AVAILABLE PARAMS:
	    
	    (*) path  -  This is the path you want to search, no sub-directories are scanned.
	    
	    folders  -  By default this is set to True and the returned list will only
	    show folders. If set to False the returned list will show files only.

	    exclude_list  -  Optionally you can add a list of items you don't want returned

	    full_path  -  By default the entries in the returned list will contain the full
	    path to the folder/file. If you only want the file/folder name set this to False.

	    subfolders  -  By default this is set to False but if set to true it will check
	    all sub-directories and not just the directory sent through.

	    filter  -  If you want to only return files ending in a specific string you
	    can add details here. For example to only show '.xml' files you would send
	    through filter='.xml'.

	EXAMPLE CODE:
	-------------
	ADDONS = Physical_Path('special://home/addons')
	addon_folders = koding.Get_Contents(path=ADDONS, folders=True, exclude_list=['packages','temp'], full_path=False)
	results = ''
	for item in addon_folders:
	    results += 'FOLDER: [COLOR=dodgerblue]%s[/COLOR]\n'%item
	koding.Text_Box('ADDON FOLDERS','Below is a list of folders found in the addons folder (excluding packages and temp):\n\n%s'%results)

------------------------------------------------------------------------------------------

###### HIGHEST VERSION:
Send through a list of strings which all have a common naming structure,
the one with the highest version number will be returned.

	CODE: Highest_Version(content,[start_point,end_point])

	AVAILABLE PARAMS:

	    (*) content  -  This is the list of filenames you want to check.

	    start_point  -  If your filenames have a common character/string immediately
	    before the version number enter that here. For example if you're looking at
	    online repository/add-on files you would use '-' as the start_point. The version
	    numbers always appear after the final '-' with add-ons residing on repo's.

	    end_point  -  If your version number is followed by a common string (e.g. '.zip')
	    then enter it in here.

	EXAMPLE CODE:
	-------------
	mylist = ['plugin.test-1.0.zip','plugin.test-0.7.zip','plugin.test-1.1.zip','plugin.test-0.9.zip']
	dialog.ok('OUR LIST OF FILES', '[COLOR=dodgerblue]%s[/COLOR]\n[COLOR=powderblue]%s[/COLOR]\n[COLOR=dodgerblue]%s[/COLOR]\n[COLOR=powderblue]%s[/COLOR]'%(mylist[0],mylist[1],mylist[2],mylist[3]))

	highest = Highest_Version(content=mylist,start_point='-',end_point='.zip')
	dialog.ok('HIGHEST VERSION', 'The highest version number of your files is:','[COLOR=dodgerblue]%s[/COLOR]'%highest)

------------------------------------------------------------------------------------------

###### MOVE A DIRECTORY:
Move a directory including all sub-directories to a new location.
This will automatically create the new location if it doesn't already
exist and it wierwrite any existing entries if they exist.

	CODE: koding.Move_Tree(src, dst)

	AVAILABLE PARAMS:

	    (*) src  -  This is source directory that you want to copy

	    (*) dst  -  This is the destination location you want to copy a directory to.

	    dp - This is optional, if you pass through the dp function as a DialogProgress()
	    then you'll get to see the status of the move process. See the example below for a dp example.

	EXAMPLE CODE:
	-------------
	dp = xbmcgui.DialogProgress()
	source = koding.Physical_Path('special://profile/move_test')

	# Lets create a 500MB dummy file so we can move and see dialog progress
	dummy = os.path.join(source,'dummy')
	if not os.path.exists(source):
	    os.makedirs(source)
	koding.Dummy_File(dst=dummy+'1.txt', size=10, size_format='mb')
	koding.Dummy_File(dst=dummy+'2.txt', size=10, size_format='mb')
	koding.Dummy_File(dst=dummy+'3.txt', size=10, size_format='mb')
	koding.Dummy_File(dst=dummy+'4.txt', size=10, size_format='mb')
	koding.Dummy_File(dst=dummy+'5.txt', size=10, size_format='mb')
	koding.Dummy_File(dst=dummy+'6.txt', size=10, size_format='mb')
	dialog.ok('DUMMY FILE CREATED','If you want to check in your userdata folder you should have a new folder called "move_test" which has 6x 10MB dummy files.')

	# This is optional but if you want to see a dialog progress then you'll need this
	dp.create('MOVING FILES','Please Wait')

	destination = koding.Physical_Path('special://home/My MOVED Dummy File')
	koding.Move_Tree(source, destination, dp)
	dialog.ok('CHECK YOUR KODI HOME FOLDER','Please check your Kodi home folder, the dummy file should now have moved in there. When you press OK it will be removed')
	shutil.rmtree(destination)

------------------------------------------------------------------------------------------

###### PATH TO CURRENT "LIVE" DATABASE:
If you need to find out the current "real" database in use then this is the function for you.
It will scan for a specific database type (e.g. addons) and return the path to the one which was last updated.
This is particularly useful if the system has previously updated to a newer version rather than a fresh install
or if they've installed a "build" which contained old databases.

	CODE: DB_Path_Check(db_path)

	AVAILABLE VALUES:

	    (*) db_path  -  This is the string the database starts with.
	    If you want to find the path for the addons*.db you would use "addons"
	    as the value, if you wanted to find the path of the MyVideos*.db you would use
	    "myvideos" etc. - it is not case sensitive.

	EXAMPLE CODE:
	-------------
	dbpath = koding.DB_Path_Check(db_path='addons')
	dialog.ok('ADDONS DB','The path to the current addons database is:',dbpath)

------------------------------------------------------------------------------------------

###### PHYSICAL PATHS:
Send through a special:// path and get the real physical path returned.
This has been written due to the problem where if you're running the Windows Store
version of Kodi the built-in xbmc.translatePath() function is returning bogus results
making it impossible to access databases.

	CODE: koding.Physical_Path([path])

	AVAILABLE PARAMS:
	    
	    path  -  This is the path to the folder/file you want returned. This is optional,
	    if you leave this out it will just return the path to the root directory (special://home)

	EXAMPLE CODE:
	-------------
	location = 'special://home/addons/script.module.python.koding.aio.alt'
	real_location = koding.Physical_Path(location)
	xbmc.log(real_location,2)
	dialog.ok('PHYSICAL PATH','The real path of special://home/addons/script.module.python.koding.aio.alt is:','[COLOR=dodgerblue]%s[/COLOR]'%real_location)

------------------------------------------------------------------------------------------

###### READ/WRITE TEXT FILES:
Open/create a text file and read/write to it.

	CODE: koding.Text_File(path, mode, [text])

	AVAILABLE PARAMS:
	    
	    (*) path  -  This is the path to the text file

	    (*) mode  -  This can be 'r' (for reading) or 'w' (for writing)

	    text  -  This is only required if you're writing to a file, this
	    is the text you want to enter. This will completely overwrite any
	    text already in the file.

	EXAMPLE CODE:
	-------------
	HOME = koding.Physical_Path('special://home')
	koding_test = os.path.join(HOME, 'koding_test.txt')
	koding.Text_File(path=koding_test, mode='w', text='Well done, you\'ve created a text file containing this text!')
	dialog.ok('CREATE TEXT FILE','If you check your home Kodi folder and you should now have a new koding_test.txt file in there.','[COLOR=gold]DO NOT DELETE IT YET![/COLOR]')
	mytext = koding.Text_File(path=koding_test, mode='r')
	dialog.ok('TEXT FILE CONTENTS','The text in the file created is:','[COLOR=dodgerblue]%s[/COLOR]'%mytext,'[COLOR=gold]CLICK OK TO DELETE THE FILE[/COLOR]')
	try:
	    os.remove(koding_test)
	except:
	    dialog.ok('FAILED TO REMOVE','Could not remove the file, looks like you might have it open in a text editor. Please manually remove yourself')

------------------------------------------------------------------------------------------

###### RETURN END OF A PATH:
Split the path at every '/' and return the final file/folder name.
If your path uses backslashes rather than forward slashes it will use
that as the separator.

	CODE:  End_Path(path)

	AVAILABLE PARAMS:

	    path  -  This is the path where you want to grab the end item name.

	EXAMPLE CODE:
	-------------
	addons_path = 'special://home/addons'
	file_name = koding.End_Path(path=addons_path)
	dialog.ok('ADDONS FOLDER','Path checked:',addons_path,'Folder Name: [COLOR=dodgerblue]%s[/COLOR]'%file_name)
	file_path = 'special://home/addons/script.module.python.koding.aio.alt/addon.xml'
	file_name = koding.End_Path(path=file_path)
	dialog.ok('FILE NAME','Path checked:',file_path,'File Name: [COLOR=dodgerblue]%s[/COLOR]'%file_name)

------------------------------------------------------------------------------------------

## S Y S T E M   B A S E D   F U N C T I O N S

------------------------------------------------------------------------------------------

###### CURRENT PROFILE:
This will return the current running profile, it's only one line of code but this is for my benefit as much as
anyone else's. I use this function quite a lot and keep forgetting the code so figured it would be easier to
just write a simple function for it :)

	CODE:  Current_Profile()

	EXAMPLE CODE:
	-------------
	profile = koding.Current_Profile()
	dialog.ok('CURRENT PROFILE','Your current running profile is:','[COLOR=dodgerblue]%s[/COLOR]' % profile)

------------------------------------------------------------------------------------------

###### CURRENT TIMESTAMP:
This will return the timestamp in various formats. By default it returns as "integer" mode but other options are listed below:

	CODE: Timestamp(mode)
	mode is optional, by default it's set as integer

	AVAILABLE VALUES:

	    'integer' -  An integer which is nice and easy to work with in Python (especially for
	    finding out human readable diffs). The format returned is [year][month][day][hour][minutes][seconds]. 
	    
	    'epoch'   -  Unix Epoch format (calculated in seconds passed since 12:00 1st Jan 1970).

	    'clean'   -  A clean user friendly time format: Tue Jan 13 10:17:09 2009

	    'date_time' -  A clean interger style date with time at end: 2017-04-07 10:17:09

	EXAMPLE CODE:
	-------------
	integer_time = koding.Timestamp('integer')
	epoch_time = koding.Timestamp('epoch')
	clean_time = koding.Timestamp('clean')
	date_time = koding.Timestamp('date_time')
	import datetime
	installedtime = str(datetime.datetime.now())[:-7]
	dialog.ok('CURRENT TIME','Integer: %s' % integer_time, 'Epoch: %s' % epoch_time, 'Clean: %s' % clean_time)

------------------------------------------------------------------------------------------

###### ENABLE/DISABLE/SET VARIOUS KODI SETTINGS:
Use this to set built-in kodi settings via JSON or set skin settings.

	CODE: Set_Setting(setting, [setting_type, value])

	AVAILABLE PARAMS:
	    
	    setting_type - The type of setting type you want to change. By default
	    it's set to 'kodi_setting', see below for more info.

	    AVAILALE VALUES:

	        'string' : sets a skin string, requires a value.

	        'bool_true' :  sets a skin boolean to true, no value required.

	        'bool_false' sets a skin boolean to false, no value required.
	        
	        'kodi_setting' : sets values found in guisettings.xml. Requires
	        a string of 'true' or 'false' for the value paramater.
	        
	        'addon_enable' : enables/disables an addon. Requires a string of
	        'true' (enable) or 'false' (disable) as the value. You will get a
	        return of True/False on whether successul. Depending on your requirements
	        you may prefer to use the Toggle_Addons function.

	        'json' : WIP - setitng = method, value = params, see documentation on
	        JSON-RPC API here: http://kodi.wiki/view/JSON-RPC_API)

	    setting - This is the name of the setting you want to change, it could be a
	    setting from the kodi settings or a skin based setting. If you're wanting
	    to enable/disable an add-on this is set as the add-on id.

	    value: This is the value you want to change the setting to. By default this
	    is set to 'true'.


	EXAMPLE CODE:
	-------------
	if dialog.yesno('RSS FEEDS','Would you like to enable or disable your RSS feeds?',yeslabel='ENABLE',nolabel='DISABLE'):
	    koding.Set_Setting(setting_type='kodi_setting', setting='lookandfeel.enablerssfeeds', value='true')
	else:
	    koding.Set_Setting(setting_type='kodi_setting', setting='lookandfeel.enablerssfeeds', value='false')

------------------------------------------------------------------------------------------

###### FORCE CLOSE:
Force close Kodi, should only be used in extreme circumstances.

	CODE: Force_Close()

	EXAMPLE CODE:
	-------------
	if dialog.yesno('FORCE CLOSE','Are you sure you want to forcably close Kodi? This could potentially cause corruption if system tasks are taking place in background.'):
	    koding.Force_Close()

------------------------------------------------------------------------------------------

###### GET USER ID & GROUP ID:
A simple function to set user id and group id to the current running App
for system commands. For example if you're using the subprocess command
you could send through the preexec_fn paramater as koding.Get_ID(setid=True).
This function will also return the uid and gid in form of a dictionary.

	CODE: Get_ID([setid])

	AVAILABLE PARAMS:
	    
	    (*) setid  -  By default this is set to False but if set to True it
	    will set the ids (to be used for subprocess commands)

	EXAMPLE CODE:
	-------------
	ids = Get_ID(setid=False)
	if ids:
	    uid = ids['uid']
	    gid = ids['gid']
	    dialog.ok('USER & GROUP ID','User ID: %s'%uid, 'Group ID: %s'%gid)
	else:
	    dialog.ok('USER & GROUP ID','This function is not applicable to your system. We\'ve been sent back a return of False to indicate this function does not exist on your os.')

------------------------------------------------------------------------------------------

###### GRAB LOG:
This will grab the log file contents, works on all systems even forked kodi.

	CODE:  Grab_Log([log_type, formatting, sort_order])

	AVAILABLE PARAMS:
	    
	    log_type    -  This is optional, if not set you will get the current log.
	    If you would prefer the old log set this to 'old'

	    formatting  -  By default you'll just get a default log but you can set
	    this to 'warnings', 'notices', 'errors' to filter by only those error types.
	    Notices will return in blue, warnings in gold and errors in red.
	    You can use as many of the formatting values as you want, just separate by an
	    underscore such as 'warnings_errors'. If using anything other than the
	    default in here your log will returned in order of newest log activity first
	    (reversed order). You can also use 'clean' as an option and that will just
	    return the full log but with clean text formatting and in reverse order.

	    sort_order   -  This will only work if you've sent through an argument other
	    than 'original' for the formatting. By default the log will be shown in
	    'reverse' order but you can set this to 'original' if you prefer ascending
	    timestamp ordering like a normal log.

	EXAMPLE CODE:
	-------------
	my_log = koding.Grab_Log()
	dialog.ok('KODI LOG LOOP','Press OK to see various logging options, every 5 seconds it will show a new log style.')
	koding.Text_Box('CURRENT LOG FILE (ORIGINAL)',my_log)
	xbmc.sleep(5000)
	my_log = koding.Grab_Log(formatting='clean', sort_order='reverse')
	koding.Text_Box('CURRENT LOG FILE (clean in reverse order)',my_log)
	xbmc.sleep(5000)
	my_log = koding.Grab_Log(formatting='errors_warnings', sort_order='reverse')
	koding.Text_Box('CURRENT LOG FILE (erros & warnings only - reversed)',my_log)
	xbmc.sleep(5000)
	old_log = koding.Grab_Log(log_type='old')
	koding.Text_Box('OLD LOG FILE',old_log)

------------------------------------------------------------------------------------------

###### LAST ERROR:
Return details of the last error produced, perfect for try/except statements

	CODE: Last_Error()

	EXAMPLE CODE:
	-------------
	try:
	    xbmc.log(this_should_error)
	except:
	    koding.Text_Box('ERROR MESSAGE',Last_Error())

------------------------------------------------------------------------------------------

NETWORK SETTINGS:
Attempt to open the WiFi/network settings for the current running operating system.

I have no access to any iOS based systems so if anybody wants to add support for
that and you know the working code please contact me at info@totalrevolution.tv
The Linux one is also currently untested and of course there are many different
distros so if you know of any improved code please do pass on. Thank you.

	CODE: Network_Settings()

	EXAMPLE CODE:
	-------------
	koding.Network_Settings()

------------------------------------------------------------------------------------------

###### PRINT TO LOG - DEBUG MODE:
Print to the Kodi log but only if debugging is enabled in settings.xml

	CODE: koding.dolog(string, [my_debug])

	AVAILABLE PARAMS:

	    (*) string  -  This is your text you want printed to log.

	    my_debug  -  This is optional, if you set this to True you will print
	    to the log regardless of what the debug setting is set at in add-on settings.

	    line_info - By default this is set to True and will show the line number where
	    the dolog command was called from along with the filepath it was called from.

	EXAMPLE CODE:
	-------------
	koding.dolog(string='Quick test to see if this gets printed to the log', my_debug=True, line_info=True)
	dialog.ok('[COLOR gold]CHECK LOGFILE 1[/COLOR]','If you check your log file you should be able to see a new test line we printed \
	and immediately below that should be details of where it was called from.')
	koding.dolog(string='This one should print without the line and file info', my_debug=True, line_info=False)
	dialog.ok('[COLOR gold]CHECK LOGFILE 2[/COLOR]','If you check your log file again you should now be able to see a new line printed \
	but without the file/line details.')

------------------------------------------------------------------------------------------

###### PYTHON VERSION:
Return the current version of Python as a string. Very useful if you need
to find out whether or not to return https links (Python 2.6 is not SSL friendly).

CODE: Python_Version()

	EXAMPLE CODE:
	-------------
	py_version = koding.Python_Version()
	dialog.ok('PYTHON VERSION','You are currently running:','Python v.%s'%py_version)

------------------------------------------------------------------------------------------

###### REFRESH/RELOAD VARIOUS SECTIONS:
Refresh a number of items in kodi, choose the order they are
executed in by putting first in your r_mode. For example if you
want to refresh addons then repo and then the profile you would
send through a list in the order you want them to be executed.

	CODE: Refresh(r_mode, [profile])

	AVAILABLE PARAMS:

	    r_mode  -  This is the types of "refresh you want to perform",
	    you can send through just one item or a list of items from the
	    list below. If you want a sleep between each action just put a
	    '~' followed by amount of milliseconds after the r_mode. For example
	    r_mode=['addons~3000', 'repos~2000', 'profile']. This would refresh
	    the addons, wait 2 seconds then refresh the repos, wait 3 seconds then
	    reload the profile. The default is set to do a force refresh on
	    addons and repositories - ['addons', 'repos'].
	      
	       'addons': This will perform the 'UpdateLocalAddons' command.

	       'container': This will refresh the contents of the page.

	       'profile': This will refresh the current profile or if
	       the profile_name param is set it will load that.

	       'repos': This will perform the 'UpdateAddonRepos' command.

	       'skin': This will perform the 'ReloadSkin' command.

	    profile_name -  If you're sending through the option to refresh
	    a profile it will reload the current running profile by default
	    but you can pass through a profile name here.

	EXAMPLE CODE:
	-------------
	dialog.ok('RELOAD SKIN','We will now attempt to update the addons, pause 3s, update repos and pause 2s then reload the skin. Press OK to continue.')
	koding.Refresh(r_mode=['addons~3000', 'repos~2000', 'skin'])
	xbmc.sleep(2000)
	dialog.ok('COMPLETE','Ok that wasn\'t the best test to perform as you can\'t physically see any visible changes other than the skin refreshing so you\'ll just have to trust us that it worked!')

------------------------------------------------------------------------------------------

###### REQUIREMENTS:
Return the min and max versions of built-in kodi dependencies required by
the running version of Kodi (xbmc.gui, xbmc.python etc.), The return will
be a dictionary with the keys 'min' and 'max'.

	CODE: Requirements(dependency)

	AVAILABLE PARAMS:

	    (*) dependency  -  This is the dependency you want to check.
	    You can check any built-in dependency which has backwards-compatibility
	    but the most commonly used are xbmc.gui and xbmc.python.

	EXAMPLE CODE:
	-------------
	xbmc_gui = Requirements('xbmc.gui')
	xbmc_python = Requirements('xbmc.python')
	dialog.ok('DEPENDENCIES','[COLOR=dodgerblue]xbmc.gui[/COLOR]  Min: %s  Max: %s'%(xbmc_gui['min'],xbmc_gui['max']),'[COLOR=dodgerblue]xbmc.python[/COLOR]  Min: %s  Max: %s'%(xbmc_python['min'],xbmc_python['max']))

------------------------------------------------------------------------------------------

###### RUNNING APP:
Return the Kodi app name you're running, useful for fork compatibility

	CODE: Running_App()

	EXAMPLE CODE:
	-------------
	my_kodi = koding.Running_App()
	kodi_ver = xbmc.getInfoLabel("System.BuildVersion")
	dialog.ok('KODI VERSION','You are running:','[COLOR=dodgerblue]%s[/COLOR] - v.%s' % (my_kodi, kodi_ver))

------------------------------------------------------------------------------------------

###### SLEEP IF FUNCTION ACTIVE:
This will allow you to pause code while a specific function is
running in the background.

	CODE: Sleep_If_Function_Active(function, args, kill_time, show_busy)

	AVAILABLE PARAMS:

	    function  -  This is the function you want to run. This does
	    not require brackets, you only need the function name.

	    args  -  These are the arguments you want to send through to
	    the function, these need to be sent through as a list.

	    kill_time - By default this is set to 30. This is the maximum
	    time in seconds you want to wait for a response. If the max.
	    time is reached before the function completes you will get
	    a response of False.

	    show_busy - By default this is set to True so you'll get a busy
	    working dialog appear while the function is running. Set to
	    false if you'd rather not have this.

	EXAMPLE CODE:
	-------------
	def Open_Test_URL(url):
	    koding.Open_URL(url)

	dialog.ok('SLEEP IF FUNCTION ACTIVE','We will now attempt to read a 20MB zip and then give up after 10 seconds.','Press OK to continue.')
	koding.Sleep_If_Function_Active(function=Open_Test_URL, args=['http://download.thinkbroadband.com/20MB.zip'], kill_time=10, show_busy=True)
	dialog.ok('FUNCTION COMPLETE','Of course we cannot read that file in just 10 seconds so we\'ve given up!')

------------------------------------------------------------------------------------------

###### SLEEP IF WINDOW/DIALOG IS ACTIVE:
This will allow you to pause code while a specific window is open.

	CODE: Sleep_If_Window_Active(window_type)

	AVAILABLE PARAMS:

	    window_type  -  This is the window xml name you want to check for, if it's
	    active then the code will sleep until it becomes inactive. By default this
	    is set to the custom text box (10147). You can find a list of window ID's
	    here: http://kodi.wiki/view/Window_IDs

	EXAMPLE CODE:
	-------------
	koding.Text_Box('EXAMPLE TEXT','This is just an example, normally a text box would not pause code and the next command would automatically run immediately over the top of this.')
	koding.Sleep_If_Window_Active(10147) # This is the window id for the text box
	dialog.ok('WINDOW CLOSED','The window has now been closed so this dialog code has now been initiated')

------------------------------------------------------------------------------------------

###### SYSTEM COMMANDS:
This is just a simplified method of grabbing certain Kodi infolabels, paths
and booleans as well as performing some basic built in kodi functions.
We have a number of regularly used functions added to a dictionary which can
quickly be called via this function or you can use this function to easily
run a command not currently in the dictionary. Just use one of the
many infolabels, builtin commands or conditional visibilities available:

info: http://kodi.wiki/view/InfoLabels
bool: http://kodi.wiki/view/List_of_boolean_conditions

	CODE: System(command, [function])

	AVAILABLE PARAMS:
	    
	    (*) command  -  This is the command you want to perform, below is a list
	    of all the default commands you can choose from, however you can of course
	    send through your own custom command if using the function option (details
	    at bottom of page)

	    AVAILABLE VALUES:

	        'addonid'       : Returns the FOLDER id of the current add-on. Please note could differ from real add-on id.
	        'addonname'     : Returns the current name of the add-on
	        'builddate'     : Return the build date for the current running version of Kodi
	        'cpu'           : Returns the CPU usage as a percentage
	        'cputemp'       : Returns the CPU temperature in farenheit or celcius depending on system settings
	        'currentlabel'  : Returns the current label of the item in focus
	        'currenticon'   : Returns the name of the current icon
	        'currentpos'    : Returns the current list position of focused item
	        'currentpath'   : Returns the url called by Kodi for the focused item
	        'currentrepo'   : Returns the repo of the current focused item
	        'currentskin'   : Returns the FOLDER id of the skin. Please note could differ from actual add-on id
	        'date'          : Returns the date (Tuesday, April 11, 2017)
	        'debug'         : Toggles debug mode on/off
	        'freeram'       : Returns the amount of free memory available (in MB)
	        'freespace'     : Returns amount of free space on storage in this format: 10848 MB Free
	        'hibernate'     : Hibernate system, please note not all systems are capable of waking from hibernation
	        'internetstate' : Returns True or False on whether device is connected to internet
	        'ip'            : Return the current LOCAL IP address (not your public IP)
	        'kernel'        : Return details of the system kernel
	        'language'      : Return the language currently in use
	        'mac'           : Return the mac address, will only return the mac currently in use (Wi-Fi OR ethernet, not both)
	        'numitems'      : Return the total amount of list items curently in focus
	        'profile'       : Return the currently running profile name
	        'quit'          : Quit Kodi
	        'reboot'        : Reboot the system
	        'restart'       : Restart Kodi (Windows/Linux only)
	        'shutdown'      : Shutdown the system
	        'sortmethod'    : Return the current list sort method
	        'sortorder'     : Return the current list sort order
	        'systemname'    : Return a clean friendly name for the system
	        'time'          : Return the current time in this format: 2:05 PM
	        'usedspace'     : Return the amount of used space on the storage in this format: 74982 MB Used
	        'version'       : Return the current version of Kodi, this may need cleaning up as it contains full file details
	        'viewmode'      : Return the current list viewmode
	        'weatheraddon'  : Return the current plugin being used for weather


	    function  -  This is optional and default is set to a blank string which will
	    allow you to use the commands listed above but if set you can use your own
	    custom commands by setting this to one of the values below.

	    AVAILABLE VALUES:

	        'bool' : This will allow you to send through a xbmc.getCondVisibility() command
	        'info' : This will allow you to send through a xbmc.getInfoLabel() command
	        'exec' : This will allow you to send through a xbmc.executebuiltin() command

	EXAMPLE CODE:
	-------------
	current_time = koding.System(command='time')
	current_label = koding.System(command='currentlabel')
	is_folder = koding.System(command='ListItem.IsFolder', function='bool')
	dialog.ok('PULLED DETAILS','The current time is %s' % current_time, 'Folder status of list item [COLOR=dodgerblue]%s[/COLOR]: %s' % (current_label, is_folder),'^ A zero means False, as in it\'s not a folder.')

------------------------------------------------------------------------------------------

## V A R I A B L E    /   S T R I N G    B A S E D   F U N C T I O N S

------------------------------------------------------------------------------------------

###### ASCII CHECK:
Return a list of files found containing non ASCII characters in the filename.

	CODE: ASCII_Check([sourcefile, dp])

	AVAILABLE PARAMS:
	    
	    sourcefile  -  The folder you want to scan, by default it's set to the
	    Kodi home folder.
	        
	    dp  -  Optional DialogProgress, by default this is False. If you want
	    to show a dp make sure you initiate an instance of xbmcgui.DialogProgress()
	    and send through as the param.
	        
	EXAMPLE CODE:
	-------------
	home = koding.Physical_Path('special://home')
	progress = xbmcgui.DialogProgress()
	progress.create('ASCII CHECK')
	my_return = ASCII_Check(sourcefile=home, dp=progress)
	if len(my_return) > 0:
	    dialog.select('NON ASCII FILES', my_return)
	else:
	    dialog.ok('ASCII CHECK CLEAN','Congratulations!','There weren\'t any non-ASCII files found on this system.')

------------------------------------------------------------------------------------------

###### CLEANUP A STRING:
Clean a string, removes whitespaces and common buggy formatting when pulling from websites

	CODE: Cleanup_String(my_string)

	AVAILABLE PARAMS:
	    
	    (*) my_string   -  This is the main text you want cleaned up.
	        
	EXAMPLE CODE:
	-------------
	current_text = '" This is a string of text which should be cleaned up   /'
	dialog.ok('ORIGINAL STRING', '[COLOR dodgerblue]%s[/COLOR]\n\nPress OK to view the cleaned up version.'%current_text)
	clean_text = koding.Cleanup_String(current_text)
	dialog.ok('CLEAN STRING', '[COLOR dodgerblue]%s[/COLOR]'%clean_text)

------------------------------------------------------------------------------------------

###### DATA TYPE:
This will return whether the item received is a dictionary, list, string, integer etc.

	CODE:  Data_Type(data)

	AVAILABLE PARAMS:
	    
	    (*) data  -  This is the variable you want to check.

	RETURN VALUES:
	    list, dict, str, int, float, bool

	EXAMPLE CODE:
	-------------
	test1 = ['this','is','a','list']
	test2 = {"a" : "1", "b" : "2", "c" : 3}
	test3 = 'this is a test string'
	test4 = 12
	test5 = 4.3
	test6 = True

	my_return = '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test1, koding.Data_Type(test1))
	my_return += '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test2, koding.Data_Type(test2))
	my_return += '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test3, koding.Data_Type(test3))
	my_return += '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test4, koding.Data_Type(test4))
	my_return += '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test5, koding.Data_Type(test5))
	my_return += '[COLOR dodgerblue]%s[/COLOR] : %s\n' % (test6, koding.Data_Type(test6))

	koding.Text_Box('TEST RESULTS', my_return)

------------------------------------------------------------------------------------------

###### DECODE STRING TO CLEAN TEXT:
This will allow you to send a string which contains a variety of special characters (including
non ascii, unicode etc.) and it will convert into a nice clean string which plays nicely
with Python and Kodi.

	CODE: Decode_String(string)

	AVAILABLE PARAMS:
	    
	    (*) string - This is the string you want to convert

	EXAMPLE CODE:
	-------------
	my_string = 'symbols like [COLOR dodgerblue]¥¨˚∆ƒπø“¬∂≈óõřĖė[/COLOR] can cause errors \nnormal chars like [COLOR dodgerblue]asfasdf[/COLOR] are fine'
	dialog.ok('ORIGINAL TEXT',my_string)
	my_string = koding.Decode_String(my_string)
	dialog.ok('DECODED/STRIPPED',my_string)
		
------------------------------------------------------------------------------------------

###### FANCY TEXT:
Capitalize a string and make the first colour of each string blue and the rest of text white
That's the default colours but you can change to whatever colours you want.

	CODE: Colour_Text(text, [color1, color2])

	AVAILABLE PARAMS:
	    
	    (*) text   -  This is the main text you want to change

	    colour1 -  This is optional and is set as dodgerblue by default.
	    This is the first letter of each word in the string

	    colour2 -  This is optional and is set as white by default. 
	    This is the colour of the text

	IMPORTANT: I use the Queens English so please note the word "colour" has a 'u' in it!

	EXAMPLE CODE:
	-------------
	current_text = 'This is a string of text which should be changed to dodgerblue and white with every first letter capitalised'
	mytext = koding.Colour_Text(text=current_text, colour1='dodgerblue', colour2='white')
	xbmc.log(current_text)
	xbmc.log(mytext)
	dialog.ok('CURRENT TEXT', current_text)
	dialog.ok('NEW TEXT', mytext)

------------------------------------------------------------------------------------------

###### FIND IN TEXT:
Regex through some text and return a list of matches.
Please note this will return a LIST so even if only one item is found
you will still need to access it as a list, see example below.

	CODE: Find_In_Text(content, start, end, [show_errors])

	AVAILABLE PARAMS:
	    
	    (*) content  -  This is the string to search

	    (*) start    -  The start search string

	    (*) end      -  The end search string

	    show_errors  -  Default is False, if set to True the code will show help
	    dialogs for bad code.

	EXAMPLE CODE:
	-------------
	textsearch = 'This is some text so lets have a look and see if we can find the words "lets have a look"'
	dialog.ok('ORIGINAL TEXT','Below is the text we\'re going to use for our search:','[COLOR dodgerblue]%s[/COLOR]'%textsearch)
	search_result = koding.Find_In_Text(textsearch, 'text so ', ' and see')
	dialog.ok('SEARCH RESULT','You searched for the start string of "text so " and the end string of " and see".','','Your result is: [COLOR dodgerblue]%s[/COLOR]' % search_result[0])

	# Please note: we know for a fact there is only one result which is why we're only accessing list item zero.
	# If we were expecting more than one return we would probably do something more useful and loop through in a for loop.

------------------------------------------------------------------------------------------

######  FUZZY MATCH:
Send through a list of items and try to match against the search string.
This will match where the search_string exists in the list or an item in
the list exists in the search_string.

	CODE: Fuzzy_Search(search_string, search_list, [strip])

	AVAILABLE PARAMS:
	    
	    (*) search_string  -  This is the string to search for

	    (*) search_list    -  The list of items to search through

	    replace_strings  -  Optionally send through a list of strings you want to
	    replace. For example you may want to search for "West Ham United" but in
	    the list you've sent through they've abbreviated it to "West Ham Utd FC". In
	    this case we might want to send through a replace_strings list of:

	    (["united","utd"], ["fc",""])

	    This will remove any instances of "FC" from the search and it will replace
	    instances of "united" to "utd". The code will convert everythig to lowercase
	    so it doesn't matter what case you use in these searches.

	EXAMPLE CODE:
	-------------
	my_search = 'west ham utd'
	my_list = ['west ham united', 'west ham utd', 'rangers fc', 'Man City', 'West Ham United FC', 'Fulham FC', 'West Ham f.c']
	my_replace = (["united","utd"], ["fc",""], ["f.c",""])
	dialog.ok('FUZZY SEARCH','Let\'s search for matches similar to "west ham utd" in the list:\n\n%s'%my_list)
	search_result = koding.Fuzzy_Search(my_search, my_list, my_replace)
	good = ', '.join(search_result)
	bad = ''
	for item in my_list:
	    if item not in search_result:
	        bad += item+', '
	dialog.ok('RESULTS FOUND','[COLOR=dodgerblue]SEARCH:[/COLOR] %s\n[COLOR=lime]GOOD:[/COLOR] %s\n[COLOR=cyan]BAD:[/COLOR] %s'%(my_search,good,bad))

------------------------------------------------------------------------------------------

###### GENERATE RANDOM PASSWORD:
This will generate a random string made up of uppercase & lowercase ASCII
characters and digits - it does not contain special characters.

	CODE:  ID_Generator([size])
	size is an optional paramater.

	AVAILABLE PARAMS:

	    size - just send through an integer, this is the length of the string you'll get returned.
	    So if you want a password generated that's 20 characters long just use ID_Generator(20). The default is 15.

	EXAMPLE CODE:
	-------------
	my_password = koding.ID_Generator(20)
	dialog.ok('ID GENERATOR','Password generated:', '', '[COLOR=dodgerblue]%s[/COLOR]' % my_password)

------------------------------------------------------------------------------------------

###### LANGUAGE STRINGS:
This will return the relevant language skin as set in the
resources/language folder for your add-on. By default you'll get
the language string returned from your current running add-on
but if you send through another add-on id you can grab from
any add-on or even the built-in kodi language strings.

	CODE: String(code, [source])

	AVAILABLE PARAMS:

	    (*) code  -  This is the language string code set in your strings.po file.

	    source  -  By default this is set to a blank string and will
	    use your current add-on id. However if you want to pull the string
	    from another add-on just enter the add-on id in here. If you'd prefer
	    to pull from the built-in kodi resources files just set as 'system'.

	EXAMPLE CODE:
	-------------
	kodi_string = koding.String(code=10140, source='system')
	koding_string = koding.String(code=30825, source='script.module.python.koding.aio.alt')
	dialog.ok('SYSTEM STRING','The string [COLOR=dodgerblue]10140[/COLOR] pulled from the default system language resources is:','[COLOR=gold]%s[/COLOR]' % kodi_string)
	dialog.ok('PYTHON KODING STRING','The string [COLOR=dodgerblue]30825[/COLOR] pulled from the Python Koding language resources is:','[COLOR=gold]%s[/COLOR]' % koding_string)
		
------------------------------------------------------------------------------------------

###### LIST FROM DICTIONARY:
Send through a dictionary and return a list of either the keys or values.
Please note: The returned list will be sorted in alphabetical order.

	CODE: List_From_Dict(mydict,[use_key])

	AVAILABLE PARAMS:

	    (*) mydict  -  This is the dictionary (original data) you want to traverse through.

	    use_key  -  By default this is set to True and a list of all your dictionary keys
	    will be returned. Set to False if you'd prefer to have a list of the values returned.

	EXAMPLE CODE:
	-------------
		raw_data = {'test1':'one','test2':'two','test3':'three','test4':'four','test5':'five'}
		mylist1 = koding.List_From_Dict(mydict=raw_data)
		mylist2 = koding.List_From_Dict(mydict=raw_data,use_key=False)
		koding.Text_Box('LIST_FROM_DICT','Original dictionary: [COLOR dodgerblue]%s[/COLOR][CR][CR]Returned List (use_key=True): [COLOR dodgerblue]%s[/COLOR][CR]Returned List (use_key=False): [COLOR dodgerblue]%s[/COLOR]'%(raw_data,mylist1,mylist2))

------------------------------------------------------------------------------------------

###### MERGE DICTIONARIES:
Send through any number of dictionaries and get a return of one merged dictionary.
Please note: If you have duplicate keys the value will be overwritten by the final
dictionary to be checked. So if you send through dicts a-f and the same key exists
in dicts a,e,f the final value for that key would be whatever is set in 'f'.

	CODE: Merge_Dicts(*dict_args)

	AVAILABLE PARAMS:

	    (*) *dict_args  -  Enter as many dictionaries as you want, these will be merged
	    into one final dictionary. Please send each dictionary through as a new paramater.

	EXAMPLE CODE:
	-------------
		dict1 = {'1':'one','2':'two'}
		dict2 = {'3':'three','4':'four','5':'five'}
		dict3 = {'6':'six','7':'seven'}
		dict4 = {'1':'three','8':'eight'}

		mytext = 'Original Dicts:\ndict1 = %s\ndict2 = %s\ndict3 = %s\ndict4 = %s\n\n'%(repr(dict1),repr(dict2),repr(dict3),repr(dict4))
		mytext += 'Merged dictionaries (1-3): %s\n\n'%repr(koding.Merge_Dicts(dict1,dict2,dict3))
		mytext += 'Merged dictionaries (1-4): %s\n\n'%repr(koding.Merge_Dicts(dict1,dict2,dict3,dict4))
		mytext += "[COLOR = gold]IMPORTANT:[/COLOR]\nNotice how on the last run the key '1'now has a value of three.\nThis is because dict4 also contains that same key."
		Text_Box('Merge_Dicts',mytext)

------------------------------------------------------------------------------------------

###### MD5 CHECK:
Return the md5 value of string/file/directory, this will return just one unique value.

	CODE: md5_check(src,[string])

	AVAILABLE PARAMS:

	    (*) src  -  This is the source you want the md5 value of.
	    This can be a string, path of a file or path to a folder.

	    string  -  By default this is set to False but if you want to send
	    through a string rather than a path set this to True.

	EXAMPLE CODE:
	-------------
	home = koding.Physical_Path('special://home')
	home_md5 = koding.md5_check(home)
	dialog.ok('md5 Check', 'The md5 of your home folder is:', '[COLOR=dodgerblue]%s[/COLOR]'%home_md5)

	guisettings = xbmc.translatePath('special://profile/guisettings.xml')
	guisettings_md5 = koding.md5_check(guisettings)
	dialog.ok('md5 Check', 'The md5 of your guisettings.xml:', '[COLOR=dodgerblue]%s[/COLOR]'%guisettings_md5)

	mystring = 'This is just a random text string we\'ll get the md5 value of'
	myvalue = koding.md5_check(src=mystring,string=True)
	dialog.ok('md5 String Check', 'String to get md5 value of:', '[COLOR=dodgerblue]%s[/COLOR]'%mystring)
	dialog.ok('md5 String Check', 'The md5 value of your string:', '[COLOR=dodgerblue]%s[/COLOR]'%myvalue)

------------------------------------------------------------------------------------------

###### PARSE XML:
Send through the contents of an XML file and pull out a list of matching
items in the form of dictionaries. When checking your results you should
allow for lists to be returned, by default each tag found in the xml will
be returned as a string but if multiple entries of the same tag exists your
dictionary item will be a list. Although this can be used for many uses this
was predominantly added for support of XML's which contain multiple links to video
files using things like <sublink>. When checking to see if a string or list has been
returned you can use the Data_Type function from Koding which will return 'str' or 'list'.

	CODE: Parse_XML(source, block, tags)

	AVAILABLE PARAMS:

	    source  -  This is the original source file, this must already be read into
	    memory as a string so made sure you've either used Open_URL or Text_File to
	    read the contents before sending through.

	    block -  This is the master tag you want to use for creating a dictionary of items.
	    For example if you have an xml which contains multiple tags called <item> and you wanted
	    to create a dictionary of sub items found in each of these you would just use 'item'.

	    tags - This is a list of tags you want to return in your dictionary, so lets say each <item>
	    section contains <link>, <title> and <thumb> tags you can return a dictionary of all those
	    items by sending through ['link','title','thumb']

	EXAMPLE CODE:
	-------------
	dialog.ok('DICTIONARY OF ITEMS','We will now attempt to return a list of the source details pulled from the official Kodi repository addon.xml')
	xml_file = koding.Physical_Path('special://xbmc/addons/repository.xbmc.org/addon.xml')
	xml_file = koding.Text_File(xml_file,'r')
	xbmc.log(xml_file,2)
	repo_details = koding.Parse_XML(source=xml_file, block='extension', tags=['info','checksum','datadir'])
	counter = 0
	for item in repo_details:
	    dialog.ok( 'REPO %s'%(counter+1),'info path: [COLOR dodgerblue]%s[/COLOR]\nchecksum path: [COLOR dodgerblue]%s[/COLOR]\ndatadir: [COLOR dodgerblue]%s[/COLOR]' % (repo_details[counter]['info'],repo_details[counter]['checksum'],repo_details[counter]['datadir']) )
	    counter += 1

------------------------------------------------------------------------------------------

###### REMOVE FORMATTING FROM TEXT:
This will cleanup a Kodi string, it can remove color, bold and italic tags as well as
preceding spaces, dots and dashes. Particularly useful if you want to show the names of
add-ons in alphabetical order where add-on names have deliberately had certain formatting
added to them to get them to always show at the top of lists.

	CODE: Remove_Formatting(string, [color, bold, italic, spaces, dots, dashes])

	AVAILABLE PARAMS:

	    (*) string  -  This is string you want to remove formatting from.

	    color  -  By default this is set to true and all references to the color tag
	    will be removed, set this to false if you don't want color formatting removed.

	    bold  -  By default this is set to true and all references to the bold tag
	    will be removed, set this to false if you don't want bold formatting removed.

	    italic  -  By default this is set to true and all references to the italic tag
	    will be removed, set this to false if you don't want italic formatting removed.

	    spaces  -  By default this is set to true and any spaces at the start of the text
	    will be removed, set this to false if you don't want the spaces removed.

	    dots  -  By default this is set to true and any dots (.) at the start of the text
	    will be removed, set this to false if you don't want the dots removed.

	    dashes  -  By default this is set to true and any dashes (-) at the start of the text
	    will be removed, set this to false if you don't want the dashes removed.

	EXAMPLE CODE:
	-------------
	mystring = '...-- [I]This[/I]  is the [COLOR dodgerblue]ORIGINAL[/COLOR] [B][COLOR cyan]TEXT[/COLOR][/B]'
	dialog.ok('ORIGINAL TEXT','Below is the original text we\'re going to try and clean up:[CR]%s'%mystring)
	dialog.ok('DOTS REMOVED','[COLOR gold]Original:[/COLOR][CR]%s[CR][COLOR gold]This is with only dots set to True:[/COLOR][CR]%s'%(mystring,koding.Remove_Formatting(mystring, color=False, bold=False, italic=False, spaces=False, dots=True, dashes=False)))
	dialog.ok('DOTS & DASHES REMOVED','[COLOR gold]Original:[/COLOR][CR]%s[CR][COLOR gold]This is with dots & dashes set to True:[/COLOR][CR]%s'%(mystring,koding.Remove_Formatting(mystring, color=False, bold=False, italic=False, spaces=False, dots=True, dashes=True)))
	dialog.ok('DOTS, DASHES & SPACES REMOVED','[COLOR gold]Original:[/COLOR][CR]%s[CR][COLOR gold]This is with dots, dashes & spaces set to True:[/COLOR][CR]%s'%(mystring,koding.Remove_Formatting(mystring, color=False, bold=False, italic=False, spaces=True, dots=True, dashes=True)))
	dialog.ok('ALL FORMATTING REMOVED','[COLOR gold]Original:[/COLOR][CR]%s[CR][COLOR gold]This is with all options set to True:[/COLOR][CR]%s'%(mystring,koding.Remove_Formatting(mystring)))

------------------------------------------------------------------------------------------

###### SPLIT LIST:
Send through a list and split it up into multiple lists. You can choose to create
lists of every x amount of items or you can split at every nth item and only include
specific items in your new list.

	CODE: Split_List(source, split_point, include)

	AVAILABLE PARAMS:

	    source  -  This is the original list you want split

	    split_point -  This is the postition you want to split your list at. For example:
	    original list: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	    Lets say we want to split it at every 5 items the split point would be 5

	    include - You have 3 options here:

	        'all' - This will add all items to your lists, so in the example above you will
	        get a return of ([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15])

	        [] - Send through a list of positions you want to include, based on the example
	        above and using include=[0,1,3] you will get a return of ([1,2,4],[6,7,9],[11,12,14])

	        int - Send through an integer and it will return everything up to that position,
	        based on the example above and using include=3 you will get a return of
	        ([1,2,3],[6,7,8],[11,12,13])


	EXAMPLE CODE:
	-------------
	my_list = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen']
	dialog.ok('SPLIT LIST 1','We will now attempt to split the following list into blocks of 5:\n%s'%my_list)
	newlist = koding.Split_List(source=my_list, split_point=5)
	dialog.ok('RESULTS','Our returned var:\n%s'%newlist)
	dialog.ok('SPLIT LIST 2','We will now attempt to split the same list at every 5th item position and only show items [0,1,3]')
	newlist = koding.Split_List(source=my_list, split_point=5, include=[0,1,3])
	dialog.ok('RESULTS','Our returned var:\n%s'%newlist)
	dialog.ok('SPLIT LIST 3','We will now attempt to split the same list at every 5th item position and only show the first 3 items.')
	newlist = koding.Split_List(source=my_list, split_point=5, include=3)
	dialog.ok('RESULTS','Our returned var:\n%s'%newlist)

------------------------------------------------------------------------------------------

###### SPLIT STRING INTO LINES OF X AMOUNT OF CHARACTERS:
Splits up a piece of text into a list of lines x amount of chars in length.

	CODE: koding.Split_Lines(raw_string, size)

	AVAILABLE PARAMS:

	    (*) raw_string  -  This is the text you want split up into lines

	    (*) size        -  This is the maximum size you want the line length to be (in characters)

	EXAMPLE CODE:
	-------------
	raw_string = 'This is some test code, let\'s take a look and see what happens if we split this up into lines of 20 chars per line'
	dialog.ok('ORIGINAL TEXT',raw_string)
	my_list = koding.Split_Lines(raw_string,20)
	koding.Text_Box('List of lines',str(my_list))

------------------------------------------------------------------------------------------

###### TABLE CONVERT:
Open a web page which a table and pull out the contents of that table
into a list of dictionaries with your own custom keys.

	CODE:   Table_Convert(url, contents, table)

	AVAILABLE PARAMS:

	    url  -  The url you want to open and pull data from

	    contents  -  Send through a dictionary of the keys you want to assign to
	    each of the cells. The format would be: {my_key : position}
	    You can pull out as many cells as you want, so if your table has 10 columns
	    but you only wanted to pull data for cells 2,4,5,6,8 then you could do so
	    by setting contents to the following params:
	    contents = {"name 1":2, "name 2":4, "name 3":5, "name 4":6, "name 5":8}

	    table  -  By default this is set to zero, this is to be used if there's
	    multiple tables on the page you're accessing. Remeber to start at zero,
	    so if you want to access the 2nd table on the page it will be table=1.

	EXAMPLE CODE:
	-------------
	dialog.ok('TABLE DATA','Let\'s pull some details from the proxy list table found at:\nhttps://free-proxy-list.net.')
	proxies = koding.Table_Convert(url='https://free-proxy-list.net', contents={"ip":0,"port":1}, table=0)
	mytext = '[COLOR dodgerblue]Here are some proxies:[/COLOR]\n'
	for item in proxies:
	    mytext += '\nIP: %s\nPort: %s\n[COLOR steelblue]----------------[/COLOR]'%(item['ip'],item['port'])
	Text_Box('MASTER PROXY LIST',mytext)

------------------------------------------------------------------------------------------

## V I D E O   T O O L S

------------------------------------------------------------------------------------------

###### CHECK IF VIDEO PLAYBACK IS SUCCESSFUL:
This function will return true or false based on video playback. Simply start a stream
(whether via an add-on, direct link to URL or local storage doesn't matter), the code will
then work out if playback is successful. This uses a number of checks and should take into
account all potential glitches which can occur during playback. The return should happen
within a second or two of playback being successful (or not).

	CODE: Check_Playback()

	AVAILABLE PARAMS:

	    ignore_dp  -  By default this is set to True but if set to False
	    this will ignore the DialogProgress window. If you use a DP while
	    waiting for the stream to start then you'll want to set this True.
	    Please bare in mind the reason this check is in place and enabled
	    by default is because some streams do bring up a DialogProgress
	    when initiated (such as f4m proxy links) and disabling this check
	    in those circumstances can cause false positives.

	    timeout  -  This is the amount of time you want to allow for playback
	    to start before sending back a response of False. Please note if
	    ignore_dp is set to True then it will also add a potential 10s extra
	    to this amount if a DialogProgress window is open. The default setting
	    for this is 10s.

	EXAMPLE CODE:
	-------------
	xbmc.Player().play('http://totalrevolution.tv/videos/python_koding/Browse_To_Folder.mov')
	isplaying = koding.Check_Playback()
	if isplaying:
	    dialog.ok('PLAYBACK SUCCESSFUL','Congratulations, playback was successful')
	    xbmc.Player().stop()
	else:
	    dialog.ok('PLAYBACK FAILED','Sorry, playback failed :(')

------------------------------------------------------------------------------------------

###### LAST PLAYED (OR CURRENTLY PLAYING) FILE:
Return the link of the last played (or currently playing) video.
This differs to the built in getPlayingFile command as that only shows details
of the current playing file, these details can differ to the url which was
originally sent through to initiate the stream. This Last_Played function
directly accesses the database to get the REAL link which was initiated and
will even return the plugin path if it's been played through an external add-on.

	CODE: Last_Played()

	EXAMPLE CODE:
	-------------
	if koding.Play_Video('http://totalrevolution.tv/videos/python_koding/Browse_To_Folder.mov'):
	    xbmc.sleep(3000)
	    xbmc.Player().stop()
	    last_vid = Last_Played()
	    dialog.ok('VIDEO LINK','The link we just played is:\n\n%s'%last_vid)
	else:
	    dialog.ok('PLAYBACK FAILED','Sorry this video is no longer available, please try using a different video link.')

------------------------------------------------------------------------------------------

###### M3U / M3U8 PLAYLIST SELECTOR:
Send through an m3u/m3u8 playlist and have the contents displayed via a dialog select.
The return will be a dictionary of 'name' and 'url'. You can send through either
a locally stored filepath or an online URL.

This function will try it's best to pull out the relevant playlist details even if the
web page isn't a correctly formatted m3u playlist (e.g. an m3u playlist embedded into
a blog page).

	CODE: M3U_Selector(url, [post_type, header])

	AVAILABLE PARAMS:
	    (*) url  -  The location of your m3u file, this can be local or online

	    post_type  -  If you need to use POST rather than a standard query string
	    in your url set this to 'post', by default it's set to 'get'.

	    header  -  This is the header you want to appear at the top of your dialog
	    selection window, by default it's set to "Stream Selection"

	EXAMPLE CODE:
	-------------
	dialog.ok('M3U SELECTOR','We will now call this function using the following url:','','[COLOR dodgerblue]http://totalrevolution.tv/videos/playlists/youtube.m3u[/COLOR]')

	# This example uses YouTube plugin paths but any playable paths will work
	vid = koding.M3U_Selector(url='http://totalrevolution.tv/videos/playlists/youtube.m3u')


	# Make sure there is a valid link returned
	if vid:
	    playback = koding.Play_Video(video=vid['url'], showbusy=False)
	    if playback:
	        dialog.ok('SUCCESS!','Congratulations the playback was successful!')
	        xbmc.Player().stop()
	    else:
	        dialog.ok('OOPS!','Looks like something went wrong there, the playback failed. Check the links are still valid.')

------------------------------------------------------------------------------------------

###### PLAY VIDEO:
This will attempt to play a video and return True or False on
whether or not playback was successful. This function is similar
to Check_Playback but this actually tries a number of methods to
play the video whereas Check_Playback does not actually try to
play a video - it will just return True/False on whether or not
a video is currently playing.

If you have m3u or m3u8 playlist links please use the M3U_Selector
function to get the final resolved url.

	CODE: Play_Video(video, [showbusy, content, ignore_dp, timeout, item])

	AVAILABLE PARAMS:

	    (*) video  -  This is the path to the video, this can be a local
	    path, online path or a channel number from the PVR.

	    showbusy  -  By default this is set to True which means while the
	    function is attempting to playback the video the user will see the
	    busy dialog. Set to False if you prefer this not to appear but do
	    bare in mind a user may navigate to another section and try playing
	    something else if they think this isn't doing anything.

	    content  -  By default this is set to 'video', however if you're
	    passing through audio you may want to set this to 'music' so the
	    system can correctly set the tags for artist, song etc.

	    ignore_dp  -  By default this is set to True but if set to False
	    this will ignore the DialogProgress window. If you use a DP while
	    waiting for the stream to start then you'll want to set this True.
	    Please bare in mind the reason this check is in place and enabled
	    by default is because some streams do bring up a DialogProgress
	    when initiated (such as f4m proxy links) and disabling this check
	    in those circumstances can cause false positives.

	    timeout  -  This is the amount of time you want to allow for playback
	    to start before sending back a response of False. Please note if
	    ignore_dp is set to True then it will also add a potential 10s extra
	    to this amount if a DialogProgress window is open. The default setting
	    for this is 10s.

	    item  -  By default this is set to None and in this case the metadata
	    will be auto-populated from the previous Add_Dir so you'll just get the
	    basics like title, thumb and description. If you want to send through your
	    own metadata in the form of a dictionary you can do so and it will override
	    the auto-generation. If anything else sent through no metadata will be set,
	    you would use this option if you've already set metadata in a previous function.

	    player  -  By default this is set to xbmc.Player() but you can send through
	    a different class/function if required.

	    resolver  -  By default this is set to resolveurl but if you prefer to use
	    your own custom resolver then just send through that class when calling this
	    function and the link sent through will be resolved by your custom resolver.
    
	EXAMPLE CODE:
	-------------
	isplaying = koding.Play_Video('http://totalrevolution.tv/videos/python_koding/Browse_To_Folder.mov')
	if isplaying:
	    dialog.ok('PLAYBACK SUCCESSFUL','Congratulations, playback was successful')
	    xbmc.Player().stop()
	else:
	    dialog.ok('PLAYBACK FAILED','Sorry, playback failed :(')
------------------------------------------------------------------------------------------

###### SLEEP IF PLAYBACK IS ACTIVE:
This will allow you to pause code while kodi is playing audio or video

	CODE: Sleep_If_Playback_Active()

	EXAMPLE CODE:
	-------------
	dialog.ok('PLAY A VIDEO','We will now attempt to play a video, once you stop this video you should see a dialog.ok message.')
	xbmc.Player().play('http://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_stereo.avi')
	xbmc.sleep(3000) # Give kodi enough time to load up the video
	koding.Sleep_If_Playback_Active()
	dialog.ok('PLAYBACK FINISHED','The playback has now been finished so this dialog code has now been initiated')

------------------------------------------------------------------------------------------

###### TEST LINKS:
Send through a link and test whether or not it's playable on other devices.
Many links include items in the query string which lock the content down to your
IP only so what may open fine for you may not open for anyone else!

This function will attempt to load the page using a proxy. If when trying to access
the link via a proxy the header size and content-type match then we assume the
link will play on any device. This is not fool proof and could potentially return
false positives depending on the security used on the website being accessed.

The return you'll get is a dictionary of the following items:

    'plugin_path' - This will have the path for a plugin, it means the stream was
    originally passed through an add-on to get the final link. If this is not set
    to None then it "should" work on any device so long as that add-on is installed
    (e.g. YouTube).

    'url' - This is the final resolved url which Kodi was playing, you need to check
    the status though to find out whether or not that link is locked to your IP only.

    'status' - This will return one of the following status codes:
        good - The link should work on all IPs.

        bad_link - The link was not valid, won't even play on your current Kodi setup.

        proxy_fail - None of the proxies sent through worked.

        locked - The url only works on this device, if this is the case consider using
        the plugin_path which should generally work on all devices (although this does
        depend on how the developer of that add-on coded up their add-on).

	CODE: Link_Tester([proxy_list, url, ip_col, port_col, table])

	AVAILABLE PARAMS:

	    video  -  This is the url of the video you want to check

	    local_check - By default this is set to True and this function will first of
	    all attempt to play the video locally with no proxy just to make sure the
	    link is valid in the first place. If you want to skip this step then set
	    this to False.

	    proxy_list  -  If you already have a list of proxies you want to test with
	    send them through in the form of a list of dictionaries. Use the following
	    format: [{"ip":"0.0.0.0","port":"80"},{"ip":"127.0.0.1","port":"8080"}]

	    proxy_url  -  If you want to scrape for online proxies and loop through until a
	    working one has been found you can set the url here. If using this then
	    proxy_list can be left as the default (None). If you open this Link_Tester
	    function with no params the defaults are setup to grab from:
	    free-proxy-list.net but there is no guarantee this will always
	    work, the website may well change it's layout/security over time.

	    ip_col  -  If you've sent through a proxy_url then you'll need to set a column number
	    for where in the table the IP address is stored. The default is 0

	    port_col  -  If you've sent through a proxy_url then you'll need to set a column number
	    for where in the table the port details are stored. The default is 1

	    table  -  If you've sent through a proxy_url then you'll need to set a table number.
	    The default is 0 - this presumes we need to use the first html table found on the
	    page, if you require a different table then alter accordingly - remember zero is the
	    first instance so if you want the 3rd table on the page you would set to 2.

	EXAMPLE CODE:
	-------------
	vid_test = Link_Tester(video='http://totalrevolution.tv/videos/python_koding/Browse_To_Folder.mov')
	if vid_test['status'] == 'bad_link':
	    dialog.ok('BAD LINK','The link you sent through cannot even be played on this device let alone another one!')
	elif vid_test['status'] == 'proxy_fail':
	    dialog.ok('PROXIES EXHAUSTED','It was not possible to get any working proxies as a result it\'s not possible to fully test whether this link will work on other devices.')
	elif vid_test['status'] == 'locked':
	    dialog.ok('NOT PLAYABLE','Although you can play this link locally the tester was unable to play it when using a proxy so this is no good.')
	    if vid_test['plugin_path']:
	        dialog.ok('THERE IS SOME GOOD NEWS!','Although the direct link for this video won\'t work on other IPs it "should" be possible to open this using the following path:\n[COLOR dodgerblue]%s[/COLOR]'%vid_test['plugin_path'])
	else:
	    dialog.ok('WORKING!!!','Congratulations this link can be resolved and added to your playlist.')

------------------------------------------------------------------------------------------

## W E B   T O O L S

------------------------------------------------------------------------------------------

###### CLEANUO URL:
Clean a url, removes whitespaces and common buggy formatting when pulling from websites

	CODE: Cleanup_URL(url)

	AVAILABLE PARAMS:
	        
	    (*) url   -  This is the main url you want cleaned up.

	EXAMPLE CODE:
	-------------
	raw_url = '" http://test.com/video/"/'
	clean_url = koding.Cleanup_URL(raw_url)
	dialog.ok('CLEANUP URL', 'Orig: %s'%raw_url,'Clean: %s'%clean_url)

------------------------------------------------------------------------------------------

######   DOWNLOAD:
This will download a file, currently this has to be a standard download link which doesn't require cookies/login.

	CODE: Download(src,dst,[dp])
	dp is optional, by default it is set to false

	AVAILABLE PARAMS:

	    (*) src  - This is the source file, the URL to your download. If you attempted to download an item but it's not behaving the way you think it should (e.g. a zip file not unzipping) then change the extension of the downloaded file to .txt and open up in a text editor. You'll most likely find it's just a piece of text that was returned from the URL you gave and it should have details explaining why it failed. Could be that's the wrong URL, it requires some kind of login, it only accepts certain user-agents etc.

	    (*) dst  - This is the destination file, make sure it's a physical path and not "special://...". Also remember you need to add the actual filename to the end of the path, so if we were downloading something to the "downloads" folder and we wanted the file to be called "test.txt" we would use this path: dst = "downloads/test.txt". Of course the downloads folder would actually need to exist otherwise it would fail and based on this poor example the downloads folder would be at root level of your device as we've not specified a path prior to that so it just uses the first level that's accessible.

	    dp - This is optional, if you pass through the dp function as a DialogProgress() then you'll get to see the progress of the download. If you choose not to add this paramater then you'll just get a busy spinning circle icon until it's completed. See the example below for a dp example.

	    timeout - By default this is set to 5. This is the max. amount of time you want to allow for checking whether or
	    not the url is a valid link and can be accessed via the system.

	EXAMPLE CODE:
	-------------
	src = 'http://noobsandnerds.com/portal/Bits%20and%20bobs/Documents/user%20guide%20of%20the%20gyro%20remote.pdf'
	dst = 'special://home/remote.pdf'
	dp = xbmcgui.DialogProgress()
	dp.create('Downloading File','Please Wait')
	koding.Download(src,dst,dp)
	dialog.ok('DOWNLOAD COMPLETE','Your download is complete, please check your home Kodi folder. There should be a new file called remote.pdf.')
	dialog.ok('DELETE FILE','Click OK to delete the downloaded file.')
	xbmcvfs.delete(dst)

------------------------------------------------------------------------------------------

###### GRAB THE EXTENSION OF A URL:
Return the extension of a url

	CODE:   Get_Extension(url)

	AVAILABLE PARAMS:

	    (*) url  -  This is the url you want to grab the extension from

	EXAMPLE CODE:
	-------------
	dialog.ok('ONLINE FILE','We will now try and get the extension of the file found at this URL:','','[COLOR=dodgerblue]http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4[/COLOR]')
	url_extension = koding.Get_Extension('http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4')
	dialog.ok('FILE EXTENSION','The file extension of this Big Buck Bunny sample is:','','[COLOR=dodgerblue]%s[/COLOR]'%url_extension)

------------------------------------------------------------------------------------------

###### OPEN URL:
If you need to pull the contents of a webpage it's very simple to do so by using this function.
This uses the Python Requests module, for more detailed info on how the params work
please look at the following link: http://docs.python-requests.org/en/master/user/advanced/

IMPORTANT: This function will attempt to convert a url with a query string into the
correct params for a post or get command but I highly recommend sending through your
query string as a dictionary using the payload params. It's much cleaner and is a
safer way of doing things, if you send through your url with a query string attached
then I take no responsibility if it doesn't work!

	CODE:   Open_URL(url,[post_type,payload,headers,cookies,auth,timeout,cookiejar])

	AVAILABLE PARAMS:

	    url  -  This is the main url you want to send through. Send it through
	    as a query string format even if it's a post.

	    post_type  -  By default this is set to 'get' but this can be set to 'post',
	    if set to post the query string will be split up into a post format automatically.
	    
	    payload - By default this is not used but if you just want a standard
	    basic Open_URL function you can add a dictionary of params here. If you
	    don't enter anything in here the function will just split up your url
	    accordingly. Make sure you read the important information at the top
	    of this tutorial text.

	    headers -  Optionally send through headers in form of a dictionary.

	    cookies  -  If set to true your request will send through and store cookies.

	    auth  -  User/pass details

	    timeout  -  Optionally set a timeout for the request.

	    cookiejar  -  An name for the location to store cookies. By default it's
	    set to addon_data/<addon_id>/cookies/cookiejar but if you have multiple
	    websites you access then you may want to use a separate filename for each site.

	    proxies - Use a proxy for accessing the link, see requests documentation for full
	    information but essentially you would send through a dictionary like this:
	    proxies = {"http":"http://10.10.1.10:3128","htts":"https://10.10.1.10:3128"}

	EXAMPLE CODE:
	-------------
	dialog.ok('OPEN FORUM PAGE','We will attempt to open the noobsandnerds forum page and return the contents. You will now be asked for your forum credentials.')
	myurl = 'http://noobsandnerds.com/support/index.php'
	username = koding.Keyboard('ENTER USERNAME')
	password = koding.Keyboard('ENTER PASSWORD')
	params = {"username":username,"password":password}
	xbmc.log(repr(params),2)
	url_contents = koding.Open_URL(url=myurl, payload=params, post_type='get')
	koding.Text_Box('CONTENTS OF WEB PAGE',url_contents)

------------------------------------------------------------------------------------------

###### VALIDATE LINK:
Returns the code for a particular link, so for example 200 is a good link and 404 is a URL not found

	CODE:   Validate_Link(url,[timeout])

	AVAILABLE PARAMS:

	    (*) url  -  This is url you want to check the header code for

	    timeout  -  An optional timeout integer for checking url (default is 30 seconds)

	EXAMPLE CODE:
	-------------
	url_code = koding.Validate_Link('http://totalrevolution.tv')
	if url_code == 200:
	    dialog.ok('WEBSITE STATUS','The website [COLOR=dodgerblue]totalrevolution.tv[/COLOR] is [COLOR=lime]ONLINE[/COLOR]')
	else:
	    dialog.ok('WEBSITE STATUS','The website [COLOR=dodgerblue]totalrevolution.tv[/COLOR] is [COLOR=red]OFFLINE[/COLOR]')

------------------------------------------------------------------------------------------