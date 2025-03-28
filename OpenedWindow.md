# Scrape from already opened chrome window
This  is how you can run selenium from a tab thats already opened. 
### Add the following option arguments to your selenium code
```py
options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9014')
driver = webdriver.Chrome(options=options)
```
### Run the following command in command prompt
```sh
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="C:\test\Chrome_Test_Profile"
```
↑ edit the above path to your installed chrome.exe.  
