<h1>DiskSan - Disk Sanitization</h1>

<h2>Languages and Utilities Used</h2>

- <b>PowerShell</b> 
- <b>Diskpart</b>

<h2>Description</h2>
The project encompasses a straightforward PowerShell script guiding users through the process of securely erasing (wiping) connected drives on the system. The utility allows you to select the target disk and choose the number of passes that are performed. The PowerShell script dynamically generates a diskpart script file according to user preferences, initiating Diskpart for the execution of the disk sanitization process </br>

<h1>DiskSan - Disk Sanitization</h1>

<h2>Description</h2>
This PowerShell script provides a versatile solution for monitoring files within a specified directory and managing a baseline of their hash values. The script offers two main functionalities:</br>

<b>Collect New Baseline (Option A):</b>

Calculates the SHA512 hash for each file in the "Files" directory.
Creates or overwrites a baseline file ("baseline.txt") with file paths and corresponding hash values.

<b>Begin Monitoring Files with Saved Baseline (Option B):</b>

Loads a saved baseline from "baseline.txt" into memory.
Continuously monitors files in the "Files" directory for changes or additions.
Notifies the user when a new file is created, a file is changed, or a baseline file is deleted.
