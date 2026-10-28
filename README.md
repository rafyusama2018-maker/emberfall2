# Emberfall – Android build

Files: main.py (entry), emberfall.py (your game, unmodified), buildozer.spec

## Easiest: GitHub (no local setup)
1. Create a new GitHub repo and upload everything in this folder (keep .github/).
2. Open the Actions tab -> "Build APK" -> Run workflow.
3. After ~20-40 min, download the "emberfall-apk" artifact (contains the .apk).
4. Copy to your phone, allow "install unknown apps", and install.

## Or locally (Linux / WSL2 / macOS)
    pip install buildozer cython
    buildozer android debug
APK appears in ./bin/
