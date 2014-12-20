# This config file can be appended to any other mozharness job
# running under tbpl. The purpose of this config is to override
# values that are specific to Release Engineering machines
# that can reach specific hosts within their network.
# In other words, this config allows you to run any job
# outside of the Release Engineering network
#
# Using this config file should be accompanied with using
# --test-url and --installer-url where appropiate
import os

config = {
    "developer_mode": True,
    "exes": {},
    "find_links": ["http://pypi.pub.build.mozilla.org/pub"],
    "tooltool_servers": ["https://secure.pub.build.mozilla.org/tooltool/pvt/build"],
    "replace_urls": [
        ("http://pvtbuilds.pvt.build", "https://pvtbuilds"),
        ("http://tooltool.pvt.build.mozilla.org/build", "https://secure.pub.build.mozilla.org/tooltool/pvt/build")
    ],
    "python_webserver": True,
    "webroot": '%s/build/talos-data' % os.getcwd(),
    "virtualenv_path": '%s/build/venv' % os.getcwd(),
}
