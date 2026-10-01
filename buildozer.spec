[app]
title = Tra Cuu Ho So
package.name = tracuuhoso
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

# Cố định phiên bản Kivy ổn định
requirements = python3==3.10.12,kivy==2.2.1,sqlite3

version = 0.1
orientation = portrait
fullscreen = 0

# Cấu hình Android SDK/NDK chuẩn
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
