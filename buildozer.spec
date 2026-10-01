[app]
title = App Tra Cuu Ho So
package.name = apphoso
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 0.1

# Khai báo các thư viện chuẩn
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Cấu hình SDK chuẩn
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
