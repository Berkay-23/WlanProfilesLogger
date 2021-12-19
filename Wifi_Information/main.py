import subprocess
import os

pathUser = os.path.expanduser('~')
file = open(fr'{pathUser}\Desktop\Wlan Profiles.txt', 'w+')

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:

    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            # print("{:<30}|  {:<}".format(profile, results[0]))
            file.write("{:<30}|  {:<}\n".format(profile, results[0]))

        except IndexError:
            # print("{:<30}|  {:<}".format(profile, ""))
            file.write("{:<30}|  {:<}\n".format(profile, ""))

    except subprocess.CalledProcessError:
        # print("{:<30}|  {:<}".format(profile, "ENCODING ERROR"))
        file.write("{:<30}|  {:<}\n".format(profile, "ENCODING ERROR"))

file.close()