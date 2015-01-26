config = {
    "log_name": "central_to_aurora",

    "branding_dirs": [
        "mobile/android/config/mozconfigs/android/",
        "mobile/android/config/mozconfigs/android-api-11/",
        "mobile/android/config/mozconfigs/android-api-9-10-constrained/",
        "mobile/android/config/mozconfigs/android-armv6/",
        "mobile/android/config/mozconfigs/android-x86/",
    ],
    "branding_files": ["debug", "l10n-nightly", "nightly"],

    "profiling_files": [
        "mobile/android/config/mozconfigs/android/nightly",
        "browser/config/mozconfigs/linux32/nightly",
        "browser/config/mozconfigs/linux64/nightly",
        "browser/config/mozconfigs/macosx-universal/nightly",
        "browser/config/mozconfigs/win32/nightly",
        "browser/config/mozconfigs/win64/nightly"
    ],
    "elf_hack_files": [
        # Not necessary since bug 788974 landed.
    ],
    "locale_files": [
        "browser/locales/shipped-locales",
        "browser/locales/all-locales",
        "mobile/android/locales/maemo-locales",
        "mobile/android/locales/all-locales"
    ],

    # Disallow sharing, since we want pristine .hg directories.
    # "vcs_share_base": None,
    # "hg_share_base": None,
    "tools_repo_url": "https://hg.mozilla.org/build/tools",
    "tools_repo_revision": "default",
    "from_repo_url": "ssh://hg.mozilla.org/mozilla-central",
    "to_repo_url": "ssh://hg.mozilla.org/releases/mozilla-aurora",

    "base_tag": "FIREFOX_AURORA_%(major_version)s_BASE",
    "end_tag": "FIREFOX_AURORA_%(major_version)s_END",

    "migration_behavior": "central_to_aurora",

    "balrog_rules_to_lock": [
        8, # Fennec aurora channel
        10, # Firefox aurora channel
        18, # MetroFirefox aurora channel
    ],
    "balrog_credentials_file": "oauth.txt",

    "virtualenv_modules": [
        "requests==2.2.1",
    ],

    "post_merge_builders": [
        "mozilla-aurora hg bundle",
        "mozilla-central hg bundle",
    ],
    "post_merge_nightly_branches": [
        "mozilla-central",
        "mozilla-aurora",
    ],
}
