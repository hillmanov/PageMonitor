You must create a hash of the content that you want to monitor. 

To do this, use the following method in a Python shell: 

	import hashlib
	hashlib.sha224(<YOUR_CONTENT>).hexdigest()
	
Replace the BASE_HASH value in main.py with the return value.

You Google Account credentials needs to be entered into the config.cfg file. I created this file so that you can enter your credentials in a separate file, and not have to worry about someone looking over your shoulder while you work on main.py. If you don't like this approach (I wouldn't blame you) then you can just use "raw_input" to gather that information on script startup. 
	