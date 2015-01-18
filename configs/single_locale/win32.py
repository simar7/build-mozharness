import sys

config = {
    "platform": "win32",
    "update_platform": "WINNT_x86-msvc",
    "mozconfig": "%(branch)s/browser/config/mozconfigs/win32/l10n-mozconfig",
    "bootstrap_env": {
        "MOZ_OBJDIR": "obj-l10n",
        "EN_US_BINARY_URL": "%(en_us_binary_url)s",
        "LOCALE_MERGEDIR": "%(abs_merge_dir)s/",
        "MOZ_UPDATE_CHANNEL": "%(update_channel)s",
        "DIST": "%(abs_objdir)s",
        "LOCALE_MERGEDIR": "%(abs_merge_dir)s/",
        "L10NBASEDIR": "../../l10n",
        "MAKE_COMPLETE_MAR": "1",
        #"MOZ_AUTOMATION_UPDATE_PACKAGING": "0",
    },
    "log_name": "single_locale",
    "objdir": "obj-l10n",
    "js_src_dir": "js/src",
    "make_dirs": ['config'],
    "vcs_share_base": "c:/builds/hg-shared",

    # tooltool
    'tooltool_url': 'http://tooltool.pvt.build.mozilla.org/build/',
    'tooltool_script': [sys.executable,
                        'C:/mozilla-build/tooltool.py'],
    'tooltool_bootstrap': "setup.sh",
    'tooltool_manifest_src': 'browser/config/tooltool-manifests/win32/releng.manifest',
    # balrog credential file:
    'balrog_credentials_file': 'oauth.txt',

    # l10n
    "ignore_locales": ["en-US"],
    "l10n_dir": "l10n",
    "locales_file": "%(branch)s/browser/locales/all-locales",
    "locales_dir": "browser/locales",
    "hg_l10n_base": "https://hg.mozilla.org/l10n-central",
    "hg_l10n_tag": "default",
    "merge_locales": True,

    # MAR
    "previous_mar_dir": "dist\\previous",
    "current_mar_dir": "dist\\current",
    "update_mar_dir": "dist\\update",  # sure?
    "previous_mar_filename": "previous.mar",
    "current_work_mar_dir": "current.work",
    "package_base_dir": "dist\\l10n-stage",
    "application_ini": "application.ini",
    "buildid_section": 'App',
    "buildid_option": "BuildID",
    "unpack_script": "tools\\update-packaging\\unwrap_full_update.pl",
    "incremental_update_script": "tools\\update-packaging\\make_incremental_update.sh",
    "balrog_release_pusher_script": "scripts\\updates\\balrog-release-pusher.py",
    "update_packaging_dir": "tools\\update-packaging",
    "local_mar_tool_dir": "dist\\host\\bin",
    "mar": "mar.exe",
    "mbsdiff": "mbsdiff.exe",
    "current_mar_filename": "firefox-%(version)s.%(locale)s.win32.complete.mar",
    "complete_mar": "firefox-%(version)s.en-US.win32.complete.mar",
    "localized_mar": "firefox-%(version)s.%(locale)s.win32.complete.mar",
    "partial_mar": "firefox-%(version)s.%(locale)s.partial.%(from_buildid)s-%(to_buildid)s.mar",
    'installer_file': "firefox-%(version)s.en-US.win32.installer.exe",

    # use pymake instead of make?
    "enable_pymake": True,
    'exes': {
        'python2.7': sys.executable,
    }
}
