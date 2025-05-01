#Requires AutoHotkey v2.0

; Path to your PBIX file
pbixFile := "C:\Users\vargh\Desktop\Projects\n8n powerBI project\PowerBI files\n8n powerbi dashboard.pbix"

; Launch the Power BI file
Run(pbixFile)

; Wait for Power BI to fully load
Sleep(15000)

; Match any part of the window title
SetTitleMatchMode(2)

; Activate Power BI window
WinActivate("n8n powerbi dashboard")
WinWaitActive("n8n powerbi dashboard", , 10)

; Refresh using Alt → H → R (sequentially)
Send("{Alt}")
Sleep(5000)
Send("h")
Sleep(500)
Send("r")
Sleep(1000)

; Wait for refresh to finish
Sleep(2000)

; Close Power BI (Alt + F4)
Send("!{F4}")

; WAIT for Save Changes popup
Sleep(2000)

; Press "Don't Save" (Alt + D)
Send("!d")  
