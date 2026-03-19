if ur code is facing this error :-
"c:\Users\sohan\Downloads\online_banking_website_html_css_js_python_flask_mysql-master\online_banking_website_html_css_js_python_flask_mysql-master\main.py"
Traceback (most recent call last):
  File "c:\Users\sohan\Downloads\online_banking_website_html_css_js_python_flask_mysql-master\online_banking_website_html_css_js_python_flask_mysql-master\main.py", line 4, in <module>
    app = Flask(_name_)
  File "C:\Users\sohan\AppData\Roaming\Python\Python314\site-packages\flask\app.py", line 376, in _init_
    instance_path = self.auto_find_instance_path()
  File "C:\Users\sohan\AppData\Roaming\Python\Python314\site-packages\flask\app.py", line 630, in auto_find_instance_path
    prefix, package_path = find_package(self.import_name)
                           ~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\sohan\AppData\Roaming\Python\Python314\site-packages\flask\scaffold.py", line 898, in find_package
    package_path = _find_package_path(import_name)
  File "C:\Users\sohan\AppData\Roaming\Python\Python314\site-packages\flask\scaffold.py", line 859, in _find_package_path
    loader = pkgutil.get_loader(root_mod_name)
             ^^^^^^^^^^^^^^^^^^
AttributeError: module 'pkgutil' has no attribute 'get_loader'

then u just need to change the version of # python - 3.12 
                                          # flask - 2.3.0
                                          # Werkxeug - 2.3.0
