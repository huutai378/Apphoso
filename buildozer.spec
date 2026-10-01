[app]
title = App Tra Cuu Ho So
package.name = apphoso
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Đưa về bộ SDK/NDK ổn định nhất của Kivy
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
