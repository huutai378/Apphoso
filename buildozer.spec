[app]
title = Tra Cuu Ho So
package.name = tracuuhoso
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 1.0
requirements = python3,kivy,sqlite3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
