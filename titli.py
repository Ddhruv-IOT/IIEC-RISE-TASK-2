#! /usr/bin/python3

import cgi 
import subprocess

print("context-type: text/html")
print()

print("""

<!DOCTYPE html>

	<html>
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>CMD</title>
			
		</head>

		<body>
			<div class = "form1">

			<form action = '/cgi-bin/titli.py'>

				<h2 style="color: WHITE">Enter your command here: </h2>
				<input type = 'text' name = 'z' id = 'num1' placeholder = "command"/>
				<input type = 'submit' id = "b2"/>
			</form>

			</div>

			<style type="text/css">
				body{ background-color: teal;
				      color: white;
 	     			      font-family:Open Sans;
				    }

				form1
    				    { 
				      text-align: center;
				      text-decoration-color:green;
				      margin: auto;
				      width: 50vw;
				      height: 50vh;
				      position: absolute;
				      top:1vh;
				      bottom: 1vh;
				      left: 1vw;
				      right: 1vw;
				      margin: auto;
				      padding: 10vh;
   				    }
			</style>
		</body>
	</html>

""")

data = cgi.FieldStorage()
u_l = data.getvalue("z")
cmmd = "sudo " + u_l

try:
	output = subprocess.getoutput(cmmd)

	if "command not found" in output or "Error" in output:
		print("\n Failed !")

	else:	
		print("\n")
		print("""<h2 style="color: white">Output is: {}</h2>""".format(output))
		
except:
	print("Error")
