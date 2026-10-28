# Android entry point: keeps the save file in the app's private storage,
# then launches the game unchanged.
import os
priv = os.environ.get("ANDROID_PRIVATE") or os.environ.get("ANDROID_ARGUMENT")
if priv:
    os.environ["HOME"] = priv          # emberfall saves to ~/.emberfall_save.json
import emberfall
emberfall.main()
