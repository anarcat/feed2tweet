How to install Feed2tweet
=========================
From PyPI
^^^^^^^^^
    $ pip install retweet

From sources
^^^^^^^^^^^^
* You need at least Python 2.7.

* On some Linux Distribution **setuptools** package does not come with default python install, you need to install it.

* Install **PIP**::

    	$ wget https://bootstrap.pypa.io/get-pip.py -O - | sudo python
    
    
* Install **setuptools** module::    
  
    $ wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
  (Alternatively, Setuptools may be installed to a user-local path)::
	  
	       $ wget https://bootstrap.pypa.io/ez_setup.py -O - | python - --user

* Untar the tarball and go to the source directory with the following commands::

    $ tar zxvf feed2tweet-0.1.tar.gz
    $ cd retweet

* Next, to install Retweet on your computer, type the following command with the root user::

    $ python setup.py install
    $ # or
    $ python setup.py install --install-scripts=/usr/bin

