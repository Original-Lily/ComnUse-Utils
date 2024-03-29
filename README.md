<h2>HTB-CommonTools</h2>

<h3>Description</h3>
Repository for use automating common tasks (in my experience) on HackTheBox Expand where necessary, suggestions welcome! </br>

<h2>DiskSan - Disk Sanitization</h2>

<h3>Description</h3>
The project encompasses a straightforward PowerShell script guiding users through the process of securely erasing (wiping) connected drives on the system. The utility allows you to select the target disk and choose the number of passes that are performed. The PowerShell script dynamically generates a diskpart script file according to user preferences, initiating Diskpart for the execution of the disk sanitization process </br>

<h2>FiM - File Integrity Monitor</h2>

<h3>Description</h3>
This PowerShell script provides a versatile solution for monitoring files within a specified directory and managing a baseline of their hash values. The script offers two main functionalities:</br>

<b>Collect New Baseline (Option A):</b>

Calculates the SHA512 hash for each file in the "Files" directory.
Creates or overwrites a baseline file ("baseline.txt") with file paths and corresponding hash values.

<b>Begin Monitoring Files with Saved Baseline (Option B):</b>

Loads a saved baseline from "baseline.txt" into memory.
Continuously monitors files in the "Files" directory for changes or additions.
Notifies the user when a new file is created, a file is changed, or a baseline file is deleted.

<h2>Sentinel Log exporter</h2>

<h3>Description</h3>
This PowerShell script is designed to run continuously, monitoring Windows Event Viewer logs for failed RDP (Remote Desktop Protocol) login attempts. Note: The script relies on an external IP geolocation API (https://ipgeolocation.io/) to fetch additional information about the source IP address. The API key needs to be obtained from that service and inserted into the script for it to work correctly. </br>

<h2>GoScan: Web Technology Scanning Utility</h2>

<h3>Description</h3>
GoScan is a command-line tool developed in Go (Golang) that allows users to analyze  the web technologies used by websites. With GoScan, you can gain much quicker knowledge reguarding the technologies & frameworks behind websites.

<h2>Overall Languages and Utilities Used</h2>

- <b>PowerShell</b>
- <b>Python</b>
- <b>Diskpart</b>
- <b>Microsoft Azure</b>
- <b>Golang</b>
