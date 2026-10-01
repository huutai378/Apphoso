[app]

# (str) Title of your application
title = App Của Tôi

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# KHÓA CỨNG PYTHON 3.11 VÀ KIVY 2.3.0 ĐỂ TRÁNH BỊ KÉO PYTHON 3.14 LỖI
requirements = python3==3.11.5,kivy==2.3.0

# (str) Custom source folders for requirements
# version of your application
version = 0.1

# (int) Minimum API required
android.minapi = 21

# (int) Target Android API
android.api = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for
# CHỈ BUILD 1 KIẾN TRÚC ARM64 ĐỂ RÚT NGẮN 50% THỜI GIAN VÀ TRÁNH LỖI XUNG ĐỘT
android.archs = arm64-v8a

# (bool) Enable Android auto backup
android.allow_backup = True

# (str) python-for-android git branch to use
# CỐ ĐỊNH NHÁNH P4A CỰC KỲ ỔN ĐỊNH
p4a.branch = release-2023.05.21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
