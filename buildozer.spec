[app]

# (str) Title of your application
title = Tra Cuu Ho So

# (str) Package name
package.name = tracuuhoso

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,db

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,sqlite3

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be old enough to be compatible with your device.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip hosting check when installing the SDK
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a libdir and symlinks.
android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
