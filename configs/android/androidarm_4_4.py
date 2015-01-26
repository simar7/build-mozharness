import os

config = {
    "buildbot_json_path": "buildprops.json",
    "host_utils_url": "http://talos-remote.pvt.build.mozilla.org/tegra/tegra-host-utils.Linux.1109310.2.zip",
    "robocop_package_name": "org.mozilla.roboexample.test",
    "tooltool_manifest_path": "testing/config/tooltool-manifests/androidarm/releng.manifest",
    "tooltool_cache": "/builds/tooltool_cache",
    "tooltool_servers": ["http://tooltool.pvt.build.mozilla.org/build/"],
    ".avds_dir": "/home/cltbld/.android",
    "emulator_url": "http://people.mozilla.org/~gbrown/android-sdk_r24.0.2-linux.zip",
    "emulator_process_name": "emulator64-arm",
    "emulator_cpu": "cortex-a9",
    "device_manager": "adb",
    "exes": {
        'adb': '/tools/android-sdk18/platform-tools/adb',
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
        'tooltool.py': "/tools/tooltool.py",
    },
    "env": {
        "DISPLAY": ":0.0",
        "PATH": "%(PATH)s:%(abs_work_dir)s/emulator/android-sdk-linux/tools:/tools/android-sdk18/platform-tools",
        "MINIDUMP_SAVEPATH": "%(abs_work_dir)s/../minidumps"
    },
    "default_actions": [
        'clobber',
        'read-buildbot-config',
        'setup-avds',
        'start-emulators',
        'download-and-extract',
        'create-virtualenv',
        'install',
        'run-tests',
        'stop-emulators',
    ],
    "emulators": [
        {
            "name": "test-1",
            "device_id": "emulator-5554",
            "http_port": "8854", # starting http port to use for the mochitest server
            "ssl_port": "4454", # starting ssl port to use for the server
            "emulator_port": 5554,
        },
    ],
    "test_suite_definitions": {
        "jsreftest-1": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=1"],
        },
        "jsreftest-2": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=2"],
        },
        "jsreftest-3": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=3"],
        },
        "jsreftest-4": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=4"],
        },
        "jsreftest-5": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=5"],
        },
        "jsreftest-6": {
            "category": "jsreftest",
            "extra_args": ["--this-chunk=6"],
        },
        "mochitest-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=1", "--run-only-tests=android23.json"],
        },
        "mochitest-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=2", "--run-only-tests=android23.json"],
        },
        "mochitest-3": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=3", "--run-only-tests=android23.json"],
        },
        "mochitest-4": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=4", "--run-only-tests=android23.json"],
        },
        "mochitest-5": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=5", "--run-only-tests=android23.json"],
        },
        "mochitest-6": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=6", "--run-only-tests=android23.json"],
        },
        "mochitest-7": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=7", "--run-only-tests=android23.json"],
        },
        "mochitest-8": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=8", "--run-only-tests=android23.json"],
        },
        "mochitest-9": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=9", "--run-only-tests=android23.json"],
        },
        "mochitest-10": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=10", "--run-only-tests=android23.json"],
        },
        "mochitest-11": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=11", "--run-only-tests=android23.json"],
        },
        "mochitest-12": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=12", "--run-only-tests=android23.json"],
        },
        "mochitest-13": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=13", "--run-only-tests=android23.json"],
        },
        "mochitest-14": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=14", "--run-only-tests=android23.json"],
        },
        "mochitest-15": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=15", "--run-only-tests=android23.json"],
        },
        "mochitest-16": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=16", "--run-only-tests=android23.json"],
        },
        "mochitest-gl-1": {
            "category": "mochitest-gl",
            "extra_args": ["--this-chunk=1"],
        },
        "mochitest-gl-2": {
            "category": "mochitest-gl",
            "extra_args": ["--this-chunk=2"],
        },
        "reftest-1": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=1",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-2": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=2",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-3": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=3",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-4": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=4",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-5": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=5",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-6": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=6",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-7": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=7",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-8": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=8",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-9": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=9",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-10": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=10",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-11": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=11",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-12": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=12",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-13": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=13",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-14": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=14",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-15": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=15",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-16": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=16",
                "tests/layout/reftests/reftest.list"]
        },
        "crashtest-1": {
            "category": "crashtest",
            "extra_args": ["--this-chunk=1"],
        },
        "crashtest-2": {
            "category": "crashtest",
            "extra_args": ["--this-chunk=2"],
        },
        "xpcshell-1": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=1"],
        },
        "xpcshell-2": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=2"],
        },
        "xpcshell-3": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=3"],
        },
        "robocop-1": {
            "category": "robocop",
            "extra_args": ["--this-chunk=1"],
        },
        "robocop-2": {
            "category": "robocop",
            "extra_args": ["--this-chunk=2"],
        },
        "robocop-3": {
            "category": "robocop",
            "extra_args": ["--this-chunk=3"],
        },
        "robocop-4": {
            "category": "robocop",
            "extra_args": ["--this-chunk=4"],
        },
    }, # end of "test_definitions"
    # test harness options are located in the gecko tree
    "in_tree_config": "config/mozharness/android_arm_4_4_config.py",
    "download_minidump_stackwalk": True,
    "default_blob_upload_servers": [
         "https://blobupload.elasticbeanstalk.com",
    ],
    "blob_uploader_auth_file" : os.path.join(os.getcwd(), "oauth.txt"),
}
