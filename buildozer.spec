[app]
title = App Tra Cuu Ho So
package.name = apphoso
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 0.1

# Khai báo các thư viện Python
requirements = python3,kivy,sqlite3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Cấu hình Android SDK/NDK
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

# Chỉ build 1 kiến trúc chip arm64-v8a để tối ưu thời gian & bộ nhớ
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
