from datetime import datetime
import webbrowser

f = open('NicoMarquez.html','w')

now = datetime.now()

ahora = now.strftime("%d/%m/%Y %H:%M:%S")

html1 = """<html>
<head></head>
<body><p>HOLA SOY NICO Y ES MI PRIMERA PAGINA WEB BASICA CREADA CON PYTHON """
html2="""</p></body>
</html>"""
html1=html1+ahora+html2

f.write(html1)
f.close()

webbrowser.open_new_tab('NicoMarquez.html')




