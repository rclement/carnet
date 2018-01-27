carnet
======

|Build Status| |Coverage Status|

Static website generator framework.

Getting started
---------------

After creating a virtual environment for your website (using ``pipenv``
is highly recommended), start using ``carnet`` using the following
instructions.

Installation
~~~~~~~~~~~~

Using ``pipenv`` (recommended):

::

    $ pipenv install carnet

Using ``pip``:

::

    $ pip install carnet

Starting the local webserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the local development webserver using:

::

    $ carnet -d runserver

Head over to `localhost:5000 <http://localhost:5000>`__ and start
creating your website using the quick-start page!

By default, four new folders will be created:

-  ``pages``: where are stored the website pages
-  ``posts``: where are stored the website posts/articles (blog-like)
-  ``output``: output destination for the generated frozen website
-  ``instance``: store specific config file for local development server
   (DO NOT COMMIT)

Adding content
~~~~~~~~~~~~~~

Write Markdown files for pages and posts in their respective folders.

Example page/post:

::

        title: My new post
        author: My Name
        published: 2018-01-01 09:10:58
        categories: [category-1, category-2]
        tags: [tag-1, tag-2, tag-3, tag-4]
        header-image: img/my-new-post-header.png
        
        ## Section
        
        Lorem ipsum dolor sit amet
        
        ### Sub-section
        
        Lorem ipsum dolor sit amet

Subfolders can be organized as desired. E.g. sorting posts by year:

::

        my-websize
        |__ posts
            |__ 2016
            |   |__ my-first-post.md
            |__ 2017
            |   |__ my-second-post.md
            |   |__ my-third-post.md
            |__ 2018
                |__ my-fourth-post.md

Freezing your website
~~~~~~~~~~~~~~~~~~~~~

The website can be generated using:

::

    $ carnet freeze

The result will be stored in the specified output folder.

Dependencies
------------

``carnet`` makes use of the following open-source projects:

-  ``blinker``
-  ``flask``
-  ``flask-flatpages``
-  ``flask-moment``
-  ``flask-script``
-  ``flask-themes``
-  ``flask-wtf``
-  ``frozen-flask``
-  ``pygments``

License
-------

The MIT License (MIT)

Copyright (c) 2018 Romain Clement

.. |Build Status| image:: https://travis-ci.org/rclement/carnet.svg?branch=develop
   :target: https://travis-ci.org/rclement/carnet
.. |Coverage Status| image:: https://coveralls.io/repos/github/rclement/carnet/badge.svg?branch=develop
   :target: https://coveralls.io/github/rclement/carnet?branch=develop
