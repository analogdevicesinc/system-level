.. _pluto devs port_forwarding:

Connecting your PlutoSDR to the Internet
===========================================

.. warning::

   Do not do this, unless you have compiled custom firmware that does not use
   the default password.

Ports that are used on the PlutoSDR
-------------------------------------

- 22 (ssh)
- 80 (http)
- 30431 (iiod)

Port forwarding
-----------------

You should not make port 30431 available on the internet, there is no
security built into it, and anyone could change anything about your radio
without you knowing about it.

If you need to run iio over the internet, set up a ssh tunnel, similar to this
linux command:

.. code:: console

   rgetz@brain:~$ ssh -nNT -L \*:30431:localhost:30431 root@192.168.2.1

This uses the following options:

- ``-n``: Redirects ``stdin`` from ``/dev/null`` (actually, prevents reading
  from stdin). This must be used when ssh is run in the background.
- ``-N``: Do not execute a remote command. This is useful for just forwarding
  ports.
- ``-T``: Disable pseudo-terminal allocation.
- ``-L``: ``[bind_address:]port:host:hostport`` Local port forward to
  ``host:hostport``

This would allow anyone on your subnet to connect you your machine (use your
IP) to connect to your PlutoSDR.
