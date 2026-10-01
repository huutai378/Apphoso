[app]
title = App Cung
package.name = appcung
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy

version = 0.1

android.minapi = 21
android.api = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
