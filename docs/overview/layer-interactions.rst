System Control Across Layers
============================

The DataX technology stack is designed to support multi-modal data processing and control paradigms. This allows for splitting the processing pipeline across multiple layers as needed or to support different deployment strategies. This is primarily enabled through the libiio backend features which allow for hardware control and data transfer to and from remote devices. This is also meant to be transparent for developers, so that they can use the same code to control local and remote devices if they wish to enable debugging or transistion to an untethered systems.

.. tab-set::

   .. tab-item:: Linux IIO

      .. svg:: linux-stack.svg
         :align: center

   .. tab-item:: no-OS in Linux user space

      .. svg:: noos-linux-stack.svg
         :align: center

   .. tab-item:: no-OS bare-metal

      .. svg:: noos-stack.svg
         :align: center
