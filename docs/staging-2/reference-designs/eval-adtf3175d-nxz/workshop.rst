.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175d-nxz/workshop

.. _eval-adtf3175d-nxz workshop:

NO TITLE
========

- Download the following applications :

  - Installer :
    https://swdownloads.analog.com/cse/aditof/aware3d/TOF_Evaluation_BM_Workshop-Rel9.9.9.9_ALPHA.exe
  - WinSCP : https://winscp.net/eng/download.php
  - Putty : https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

- Make image R/W

  - Link to R/W page :
    :dokuwiki:`eval-adtf3175x-access </resources/eval/user-guides/eval-adtf3175x-access>`

- Powercycle Camera

- WINSCP into camera

  - IP : 10.42.0.1
  - username : analog \| password : analog
  - Copy ToF repo from installer location to nxp

- Putty into NXP (SSH)

  - IP : 10.42.0.1
  - username : analog \| password : analog

- Change date to current time

  - sudo date -s ``HH:MM:SS 5 DEC 2022``

- Build sdk on NXP platform :

  - ``cd Workspace/ToF/``
  - ``mkdir build``
  - ``cd build``
  - ``cmake -DWITH_PYTHON=on -DUSE_DEPTH_COMPUTE_STUBS=on
    -DCMAKE_POSITION_INDEPENDENT_CODE=1 -DNXP=1 -DWITH_NETWORK=1
    -DCMAKE_PREFIX_PATH=``/opt/glog;/opt/protobuf;/opt/websockets``
    -DWITH_EXAMPLES=on ..``
  - ``make -j4``
  - ``sudo systemctl stop network-gadget``
  - ``sudo cp apps/server/aditof-server /usr/share/systemd/aditof-server``
  - ``sudo reboot``

- Run GUI

  - ini files

- Run data_collect pipeline

  - :dokuwiki:`datacollect_cli </resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`
  - :dokuwiki:`depthcompute_cli </resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`

- Run python example

  - python first_frame_network_stream.py

- Capture data with v4l2 driver

  - Putty into camera
  - cd Workspace/adsd3500_getframe
  - ./get_frame_mp_ab.sh

- Exercise

  - Visualize frame with depth compute
