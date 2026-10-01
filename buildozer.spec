[app]
# (str) Title of your application
title = App Tra Cuu Ho So

# (str) Package name
package.name = apphoso

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (include db if needed)
source.include_exts = py,png,jpg,kv,atlas,db

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Nếu app dùng thêm thư viện như requests, sqlite3... hãy thêm vào sau kivy (ví dụ: python3,kivy,requests)
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required. 21 = Android 5.0
android.minapi = 21

# (bool) Accept SDK license automatically (RẤT QUAN TRỌNG)
android.accept_sdk_license = True

# (str) Android NDK architecture to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 =  disabled, 1 = enabled)
warn_on_root = 1
