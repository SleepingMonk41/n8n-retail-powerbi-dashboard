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
Sleep(500)
Send("h")
Sleep(500)
Send("r")

; Wait for refresh to finish
Sleep(10000)

; Save the file (Ctrl + S)
Send("^s")
Sleep(3000)

; Close Power BI (Alt + F4)
Send("!{F4}")
