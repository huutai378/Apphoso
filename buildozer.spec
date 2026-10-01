[app]

# (str) Title of your application
title = App Tra Cuu Ho So

# (str) Package name
package.name = apphoso

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the base dir)
source.include_exts = py,png,jpg,kv,atlas,db

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Khóa rõ phiên bản python3==3.10.11 để tránh dính Python 3.14
requirements = python3==3.10.11,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
