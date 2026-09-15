.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0511/software_update

.. _circuits-from-the-lab cn0511 software_update:

Installation of Latest Lib-IIO and Other Requirements Needed to Run the Example for CN0511
==========================================================================================

.. important::

   #. This set of instructions will soon go away when the next version of Kuiper Linux is released
   #. Line script to be copied are those found after the "$" symbol
   #. Enter the password ``analog`` whenever asked for it during the installation process

   ::

      [sudo] password for analog: analog

--------------

Step 1: Installation of the latest libad9166-iio from Github
------------------------------------------------------------

   After the reboot, open command prompt or terminal again to clone the libad9166-iio from Github

   ::

      analog@analog:~$ git clone :git-libad9166-iio

   Go to libad9166-iio directory

   ::

      analog@analog:~$ cd libad9166-iio

   Install the libad9166-iio

   ::

      analog@analog:~:`libad9166-iio+` $ cmake ./CMakeLists.txt

   ::

      analog@analog:~/libad9166-iio $ make

   ::

      analog@analog:~/libad9166-iio $ sudo make install

   Go to python directory

   ::

      analog@analog:~/libad9166-iio $ cd bindings/python

   Install the other requirements needed for CN0511 libad9166-iio

   ::

      analog@analog:~/python $ sudo pip install -r requirements_dev.txt

   ::

      analog@analog:~/python $ cmake ./CMakeLists.txt

   ::

      analog@analog:~/python $ sudo make

   ::

      analog@analog:~/python $ sudo make install

--------------

Step 2: Installation of the latest pyadi-iio from github
--------------------------------------------------------

   ::

      analog@analog:~ $ sudo python -m pip install git+https://github.com/analogdevicesinc/pyadi-iio/

   ::

      analog@analog:~$ git clone :git-pyadi-iio

   Lastly install the libatlas-base-dev

   ::

      analog@analog:~$ sudo apt-get install libatlas-base-dev linux packages

Then choose "Y" if were asked to continue

--------------

After all these requirements has been loaded in the Raspberry Pi, example found in ~:`home/analog/pyadi-iio/examples+` for CN0511 can now be run.
