 
import setuptools 
  
with open("README.md", "r") as fh: 
    description = fh.read() 
  
setuptools.setup( 
    name="trading_web_app", 
    version="0.0.1", 
    author="Hanna Zwolinska, Michal Nowakowski", 
    author_email="zwolinskahania2416@gmail.com", 
    packages=["app"], 
    description="Small package to track patterns in stock market", 
    long_description=description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/hahahania/trading_web_app", 
    license='', 
    python_requires='>=3.10', 
    install_requires=[] 
) 
