# wx-helper

> to manage messages and contacts in wechat
>

#### Features:

* Bulk add contacts in groups




#### Installation / Packaging:
1. Clone the repository

   > ```
   > git clone https://github.com/tritonzhu/wxHelper.git
   > cd wxHelper
   > ```

2. Install Python 3.6

3. (optional) Install virtualenv, create a virtual environment and activate it

   > ``` 
   > pip install virtualenv
   > pip install virtualenv
   > virtualenv venv
   > source venv/Scripts/activate
   > ```

4. Install requirements in requirements.txt

   > ```
   > pip install -r requirements.txt
   > ```

5. Install pyinstaller developer version since pyinstaller 3.2.1 doesn't install Python3.6 yet

   > ```
   > pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
   > ```

6. Packaging  with pyinstaller (only tested on Windows)

   > ```
   > venv/Scripts/pyinstaller.exe main.spec
   > ```

   The executable file would be in directory *dist*

