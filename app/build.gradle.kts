plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.akyildizer16.sigdeck"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.akyildizer16.sigdeck"
        minSdk = 26
        targetSdk = 34
        versionCode = 10
