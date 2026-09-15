.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/no-os-functions

.. _ad-fmcomms2-ebz software no-os-functions:

AD9361 No-OS Software
=====================

Introduction
------------

This document describes the No-OS software used to control the AD9361 part.

AD9361 No-OS API
~~~~~~~~~~~~~~~~

An API is available to be used on systems without OS to interact with the AD9361
and provides all the necessary functions to control it.

Below is presented a short description of all the functions provided in the API:

.. list-table::
   :header-rows: 1

   * - Device Global Settings
     - Description
   * - See code below
     - See function descriptions in the code section

.. code:: c

   struct ad9361_rf_phy *ad9361_init
   (AD9361_InitParam *init_param)

.. list-table::

   * - Initializes the FMCOMMS2 board. Receives as parameter a structure that
       contains the AD9361 initial parameters. Returns a structure that contains
       the AD9361 current state in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_en_state_machine_mode
   (struct ad9361_rf_phy *phy, uint32_t mode)

.. list-table::

   * - Sets the Enable State Machine (ENSM) mode. Receives as parameters a
       structure that contains the AD9361 current state and the ENSM mode
       (SLEEP, ALERT, FDD, PINCTRL). Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_en_state_machine_mode
   (struct ad9361_rf_phy *phy, uint32_t*mode)

.. list-table::

   * - Gets the Enable State Machine (ENSM) mode. Receives as parameters a
       structure that contains the AD9361 current state and a variable to store
       the selected ENSM mode. Returns 0 in case of success, negative error code
       otherwise.
   * - Receive Chain Settings

\|

.. code:: c

   int32_t ad9361_set_rx_rf_gain
   (struct ad9361_rf_phy *phy, uint8_t ch, int32_t gain_db)

.. list-table::

   * - Sets the receive RF gain for the selected channel. Receives as parameters
       a structure that contains the AD9361 current state, the desired channel
       number (0, 1) and the RF gain. Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_rf_gain
   (struct ad9361_rf_phy *phy, uint8_t ch, int32_t*gain_db)

.. list-table::

   * - Gets current receive RF gain for the selected channel. Receives as
       parameters a structure that contains the AD9361 current state, the
       desired channel (0, 1) and a variable to store the RF gain. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_rf_bandwidth
   (struct ad9361_rf_phy *phy, uint32_t bandwidth_hz)

.. list-table::

   * - Sets the RF bandwidth. Receives as parameters a structure that contains
       the AD9361 current state and the desired bandwidth in Hz. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_rf_bandwidth
   (struct ad9361_rf_phy *phy, uint32_t*bandwidth_hz)

.. list-table::

   * - Gets current RF bandwidth. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the bandwidth
       value in Hz. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_sampling_freq
   (struct ad9361_rf_phy *phy, uint32_t sampling_freq_hz)

.. list-table::

   * - Sets the sampling frequency. Receives as parameters a structure that
       contains the AD9361 current state and the desired sampling frequency in
       Hz. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_sampling_freq
   (struct ad9361_rf_phy *phy, uint32_t*sampling_freq_hz)

.. list-table::

   * - Gets current sampling frequency. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the sampling
       frequency value in Hz. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_lo_freq
   (struct ad9361_rf_phy *phy, uint64_t lo_freq_hz)

.. list-table::

   * - Sets the LO frequency. Receives as parameters a structure that contains
       the AD9361 current state and the desired LO frequency in Hz. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_lo_freq
   (struct ad9361_rf_phy *phy, uint64_t*lo_freq_hz)

.. list-table::

   * - Gets current LO frequency. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the LO
       frequency value in Hz. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_lo_int_ext
   (struct ad9361_rf_phy *phy, uint8_t int_ext)

.. list-table::

   * - \* Switches between internal and external LO. Receives as parameters a
       structure that contains the AD9361 current state and the desired LO
       source (INT_LO or EXT_LO). Returns 0 in case of success, negative error
       code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_rssi
   (struct ad9361_rf_phy *phy, uint8_t ch, struct rf_rssi*rssi)

.. list-table::

   * - Gets the RSSI for the selected channel. Receives as parameters a
       structure that contains the AD9361 current state, the desired channel (0,
       1) and a variable to store the RSSI. Returns 0 in case of success,
       negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_gain_control_mode
   (struct ad9361_rf_phy *phy, uint8_t ch, uint8_t gc_mode)

.. list-table::

   * - Sets the gain control mode for the selected channel. Receives as
       parameters a structure that contains the AD9361 current state, the
       desired channel (0, 1) and the gain control mode (GAIN_MGC,
       GAIN_FASTATTACK_AGC, GAIN_SLOWATTACK_AGC, GAIN_HYBRID_AGC). Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_gain_control_mode
   (struct ad9361_rf_phy *phy, uint8_t ch, uint8_t*gc_mode)

.. list-table::

   * - Gets the gain control mode for the selected channel. Receives as
       parameters a structure that contains the AD9361 current state, the
       desired channel (0, 1) and a variable to store the gain control mode.
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_fir_config
   (struct ad9361_rf_phy *phy, AD9361_RXFIRConfig fir_cfg)

.. list-table::

   * - Sets the FIR filter configuration. Receives as parameters a structure
       that contains the AD9361 current state and the FIR filter configuration.
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_fir_config
   (struct ad9361_rf_phy *phy, uint8_t rx_ch, AD9361_RXFIRConfig*fir_cfg)

.. list-table::

   * - Gets the FIR filter configuration. Receives as parameters a structure
       that contains the AD9361 current state and a variable to store the FIR
       filter configuration. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_fir_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the FIR filter. Receives as parameters a structure that
       contains the AD9361 current state and the option (ENABLE, DISABLE).
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_fir_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the FIR filter. Receives as parameters a structure
       that contains the AD9361 current state and the enable/disable status
       buffer. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_rfdc_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the RX RFDC Tracking. Receives as parameters a structure
       that contains the AD9361 current state and the option (ENABLE, DISABLE).
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_rfdc_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the RX RFDC Tracking. Receives as parameters a
       structure that contains the AD9361 current state and the enable/disable
       status buffer. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_bbdc_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the RX BasebandDC Tracking. Receives as parameters a
       structure that contains the AD9361 current state and the option (ENABLE,
       DISABLE). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_bbdc_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the RX BasebandDC Tracking. Receives as parameters a
       structure that contains the AD9361 current state and the enable/disable
       status buffer. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_quad_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the RX Quadrature Tracking. Receives as parameters a
       structure that contains the AD9361 current state and the option (ENABLE,
       DISABLE). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_quad_track_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the RX Quadrature Tracking. Receives as parameters a
       structure that contains the AD9361 current state and the enable/disable
       status buffer. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_rx_rf_port_input
   (struct ad9361_rf_phy *phy, uint32_t mode)

.. list-table::

   * - Sets the RX RF input port. Receives as parameters a structure that
       contains the AD9361 current state and the desired RF input port
       (A_BALANCED, B_BALANCED, C_BALANCED, A_N, A_P, B_N, B_P, C_N, C_P,
       TX_MON1, TX_MON2 or TX_MON1_2). Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_rf_port_input
   (struct ad9361_rf_phy *phy, uint32_t*mode)

.. list-table::

   * - Gets the RX RF input port. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the RF input
       port. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_rx_fastlock_store
   (struct ad9361_rf_phy *phy, uint32_t profile)

.. list-table::

   * - Stores RX fastlock profile. To create a profile tune the synthesizer
       (ad9361_set_rx_lo_freq()) and then call this function specifying the
       target profile number. Receives as parameters a structure that contains
       the AD9361 current state and the profile number (0 - 7). Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_rx_fastlock_recall
   (struct ad9361_rf_phy *phy, uint32_t profile)

.. list-table::

   * - Recalls specified RX fastlock profile. When in fastlock pin select mode
       (init_param->rx_fastlock_pincontrol_enable), the function needs to be
       called before then the pin-control can be used. Receives as parameters a
       structure that contains the AD9361 current state and the profile number
       (0 - 7). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_rx_fastlock_load
   (struct ad9361_rf_phy *phy, uint32_t profile, uint8_t*values)

.. list-table::

   * - Loads RX fastlock profile. A previously saved profile can be loaded in
       any of the 8 available slots. Receives as parameters a structure that
       contains the AD9361 current state, the profile number (0 - 7) and the
       fastlock profile program data. Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_rx_fastlock_save
   (struct ad9361_rf_phy *phy, uint32_t profile, uint8_t*values)

.. list-table::

   * - Saves RX fastlock profile. In order to use more than 8 Profiles, an
       existing profile can be read back and stored by the user application.
       Receives as parameters a structure that contains the AD9361 current
       state, the profile number (0 - 7) and the fastlock profile program data.
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_rx_lo_powerdown
   (struct ad9361_rf_phy *phy, uint8_t option)

.. list-table::

   * - Powers down the RX Local Oscillator. Receives as parameters a structure
       that contains the AD9361 current state and the power down option (ON,
       OFF). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_rx_lo_power
   (struct ad9361_rf_phy *phy, uint8_t*option)

.. list-table::

   * - Gets the RX Local Oscillator power status. Receives as parameters a
       structure that contains the AD9361 current state and a variable to store
       the power status. Returns 0 in case of success, negative error code
       otherwise.
   * - Transmit Chain Settings

\|

.. code:: c

   int32_t ad9361_set_tx_attenuation
   (struct ad9361_rf_phy *phy,
    uint8_t ch,
    uint32_t attenuation_mdb)

.. list-table::

   * - Sets the transmit attenuation for the selected channel. Receives as
       parameters a structure that contains the AD9361 current state, the
       desired channel number (0, 1) and the attenuation in dB. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_attenuation
   (struct ad9361_rf_phy *phy,
    uint8_t ch,
    uint32_t *attenuation_mdb)

.. list-table::

   * - Gets current transmit attenuation for the selected channel. Receives as
       parameters a structure that contains the AD9361 current state, the
       desired channel (0, 1) and a variable to store the attenuation value in
       dB. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_rf_bandwidth
   (struct ad9361_rf_phy *phy, uint32_t  bandwidth_hz)

.. list-table::

   * - Sets the RF bandwidth. Receives as parameters a structure that contains
       the AD9361 current state and the desired bandwidth in Hz. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_rf_bandwidth
   (struct ad9361_rf_phy *phy, uint32_t*bandwidth_hz)

.. list-table::

   * - Gets current RF bandwidth. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the bandwidth
       value in Hz. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_sampling_freq
   (struct ad9361_rf_phy *phy, uint32_t sampling_freq_hz)

.. list-table::

   * - Sets the sampling frequency. Receives as parameters a structure that
       contains the AD9361 current state and the desired sampling frequency in
       Hz. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_sampling_freq
   (struct ad9361_rf_phy *phy, uint32_t*sampling_freq_hz)

.. list-table::

   * - Gets current sampling frequency. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the sampling
       frequency value in Hz. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_lo_freq
   (struct ad9361_rf_phy *phy, uint64_t lo_freq_hz)

.. list-table::

   * - Sets the LO frequency. Receives as parameters a structure that contains
       the AD9361 current state and the desired LO frequency in Hz. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_lo_freq
   (struct ad9361_rf_phy *phy, uint64_t*lo_freq_hz)

.. list-table::

   * - Gets current LO frequency. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the LO
       frequency value in Hz. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_lo_int_ext
   (struct ad9361_rf_phy *phy, uint8_t int_ext)

.. list-table::

   * - Switches between internal and external LO. Receives as parameters a
       structure that contains the AD9361 current state and the desired LO
       source (INT_LO or EXT_LO). Returns 0 in case of success, negative error
       code otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_fir_config
   (struct ad9361_rf_phy *phy, AD9361_TXFIRConfig fir_cfg)

.. list-table::

   * - Sets the FIR filter configuration. Receives as parameters a structure
       that contains the AD9361 current state and the FIR filter configuration.
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_fir_config(struct ad9361_rf_phy *phy, uint8_t tx_ch, AD9361_TXFIRConfig*fir_cfg)

.. list-table::

   * - Gets the FIR filter configuration. Receives as parameters a structure
       that contains the AD9361 current state and a variable to store the FIR
       filter configuration. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_fir_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the FIR filter. Receives as parameters a structure that
       contains the AD9361 current state and the option (ENABLE, DISABLE).
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_fir_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the FIR filter. Receives as parameters a structure
       that contains the AD9361 current state and the enable/disable status
       buffer. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_rssi
   (struct ad9361_rf_phy *phy, uint8_t ch, uint32_t*rssi_db_x_1000)

.. list-table::

   * - Gets the TX RSSI for the selected channel. Receives as parameters a
       structure that contains the AD9361 current state, the desired channel (0,
       1) and a variable to store the RSSI. Returns 0 in case of success,
       negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_rf_port_output
   (struct ad9361_rf_phy *phy, uint32_t mode)

.. list-table::

   * - Sets the TX RF output port. Receives as parameters a structure that
       contains the AD9361 current state and the desired RF output port (TXA or
       TXB). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_rf_port_output
   (struct ad9361_rf_phy *phy, uint32_t*mode)

.. list-table::

   * - Gets the TX RF output port. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the RF output
       port. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_tx_auto_cal_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the auto calibration. Receives as parameters a structure
       that contains the AD9361 current state and the option (ENABLE, DISABLE).
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_auto_cal_en_dis
   (struct ad9361_rf_phy *phy, uint8_t*en_dis)

.. list-table::

   * - Gets the status of the auto calibration flag. Receives as parameters a
       structure that contains the AD9361 current state and a variable to store
       the option. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_tx_fastlock_store
   (struct ad9361_rf_phy *phy, uint32_t profile)

.. list-table::

   * - Stores TX fastlock profile. To create a profile tune the synthesizer
       (ad9361_set_tx_lo_freq()) and then call this function specifying the
       target profile number. Receives as parameters a structure that contains
       the AD9361 current state and the profile number (0 - 7). Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_tx_fastlock_recall
   (struct ad9361_rf_phy *phy, uint32_t profile)

.. list-table::

   * - Recalls specified TX fastlock profile. When in fastlock pin select mode
       (init_param->tx_fastlock_pincontrol_enable), the function needs to be
       called before then the pin-control can be used. Receives as parameters a
       structure that contains the AD9361 current state and the profile number
       (0 - 7). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_tx_fastlock_load
   (struct ad9361_rf_phy *phy, uint32_t profile, uint8_t*values)

.. list-table::

   * - Loads TX fastlock profile. A previously saved profile can be loaded in
       any of the 8 available slots. Receives as parameters a structure that
       contains the AD9361 current state, the profile number (0 - 7) and the
       fastlock profile program data. Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_tx_fastlock_save
   (struct ad9361_rf_phy *phy, uint32_t profile, uint8_t*values)

.. list-table::

   * - Saves TX fastlock profile. In order to use more than 8 Profiles, an
       existing profile can be read back and stored by the user application.
       Receives as parameters a structure that contains the AD9361 current
       state, the profile number (0 - 7) and the fastlock profile program data.
       Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_tx_lo_powerdown
   (struct ad9361_rf_phy *phy, uint8_t option)

.. list-table::

   * - Powers down the TX Local Oscillator. Receives as parameters a structure
       that contains the AD9361 current state and the power down option (ON,
       OFF). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_tx_lo_power
   (struct ad9361_rf_phy *phy, uint8_t*option)

.. list-table::

   * - Gets the TX Local Oscillator power status. Receives as parameters a
       structure that contains the AD9361 current state and a variable to store
       the power status. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_trx_path_clks
   (struct ad9361_rf_phy *phy,
    uint32_t *rx_path_clks,
    uint32_t *tx_path_clks)

.. list-table::

   * - Sets the RX and TX path rates. Receives as parameters a structure that
       contains the AD9361 current state, the RX and the TX clocks. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_trx_path_clks
   (struct ad9361_rf_phy *phy,
    uint32_t *rx_path_clks,
    uint32_t *tx_path_clks)

.. list-table::

   * - Gets the RX and TX path rates. Receives as parameters a structure that
       contains the AD9361 current state, the RX and the TX buffers to store the
       clock frequencies. Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_set_no_ch_mode
   (struct ad9361_rf_phy *phy, uint8_t no_ch_mode)

.. list-table::

   * - Set the number of channels mode. Receives as parameters a structure that
       contains the AD9361 current state and the number of channels mode (1 -
       1x1; 2 - 2x2). Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_do_mcs
   (struct ad9361_rf_phy *phy_master, struct ad9361_rf_phy*phy_slave)

.. list-table::

   * - Does multi chip synchronization. Receives as parameters a structure that
       contains the Master AD9361 current state and a structure that contains
       the Slave AD9361 current state. Returns 0 in case of success, negative
       error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_trx_fir_en_dis
   (struct ad9361_rf_phy *phy, uint8_t en_dis)

.. list-table::

   * - Enables/disables the TRX FIR filters. Receives as parameters a structure
       that contains the AD9361 current state and the option (ENABLE or
       DISABLE). Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_set_trx_rate_gov
   (struct ad9361_rf_phy *phy, uint32_t rate_gov)

.. list-table::

   * - Sets the OSR rate governor. Receives as parameters a structure that
       contains the AD9361 current state and the OSR rate governor (HIGHEST_OSR
       or NOMINAL_OSR). Returns 0 in case of success, negative error code
       otherwise.

\|

.. code:: c

   int32_t ad9361_get_trx_rate_gov
   (struct ad9361_rf_phy *phy, uint32_t*rate_gov)

.. list-table::

   * - Gets the OSR rate governor. Receives as parameters a structure that
       contains the AD9361 current state and a variable to store the OSR rate
       governor. Returns 0 in case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_do_calib
   (struct ad9361_rf_phy *phy, uint32_t cal, int32_t arg)

.. list-table::

   * - Performs the selected calibration. Receives as parameters a structure
       that contains the AD9361 current state, the desired calibration
       (TX_QUAD_CAL, RFDC_CAL) and for TX_QUAD_CAL - the optional RX phase value
       overwrite (set to zero). Returns 0 in case of success, negative error
       code otherwise.

\|

.. code:: c

   int32_t ad9361_trx_load_enable_fir
   (struct ad9361_rf_phy *phy, AD9361_RXFIRConfig rx_fir_cfg, AD9361_TXFIRConfig tx_fir_cfg)

.. list-table::

   * - Loads and enables TRX FIR filters configurations. Receives as parameters
       a structure that contains the AD9361 current state, the RX FIR filter
       configuration and the TX FIR filter configuration. Returns 0 in case of
       success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_do_dcxo_tune_coarse
   (struct ad9361_rf_phy *phy, uint32_t coarse)

.. list-table::

   * - Does DCXO coarse tuning. Receives as parameters a structure that contains
       the AD9361 current state and the DCXO coarse tuning value. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_do_dcxo_tune_fine
   (struct ad9361_rf_phy *phy, uint32_t fine)

.. list-table::

   * - Does DCXO fine tuning. Receives as parameters a structure that contains
       the AD9361 current state and the DCXO fine tuning value. Returns 0 in
       case of success, negative error code otherwise.

\|

.. code:: c

   int32_t ad9361_get_temperature
   (struct ad9361_rf_phy *phy, int32_t*temp)

.. list-table::

   * - Gets the temperature. Receives as parameters a structure that contains
       the AD9361 current state and a variable to store the temperature (degrees
       C \* 1000). Returns 0 in case of success, negative error code otherwise.

**Notes:** 1. Below is defined the AD9361_ParamInit structure used by the
ad9361_init() function:

For more details on each of the struct members please see here:
:dokuwiki:`AD9361 Device Driver Customization </resources/tools-software/linux-drivers/iio-transceiver/ad9361-customization>`

.. code:: C

   typedef struct
   {
       /*Identification number*/
       uint8_t     id_no;
       /*Reference Clock*/
       uint32_t    reference_clk_rate;
       /*Base Configuration*/
       uint8_t     two_rx_two_tx_mode_enable;  /*adi,2rx-2tx-mode-enable*/
       uint8_t     frequency_division_duplex_mode_enable;  /*adi,frequency-division-duplex-mode-enable*/
       uint8_t     tdd_use_dual_synth_mode_enable; /*adi,tdd-use-dual-synth-mode-enable*/
       uint8_t     tdd_skip_vco_cal_enable;        /*adi,tdd-skip-vco-cal-enable*/
       uint32_t    tx_fastlock_delay_ns;   /*adi,tx-fastlock-delay-ns*/
       uint32_t    rx_fastlock_delay_ns;   /*adi,rx-fastlock-delay-ns*/
       uint8_t     rx_fastlock_pincontrol_enable;  /*adi,rx-fastlock-pincontrol-enable*/
       uint8_t     tx_fastlock_pincontrol_enable;  /*adi,tx-fastlock-pincontrol-enable*/
       uint8_t     external_rx_lo_enable;  /*adi,external-rx-lo-enable*/
       uint8_t     external_tx_lo_enable;  /*adi,external-tx-lo-enable*/
       uint8_t     dc_offset_tracking_update_event_mask;   /*adi,dc-offset-tracking-update-event-mask*/
       uint8_t     dc_offset_attenuation_high_range;   /*adi,dc-offset-attenuation-high-range*/
       uint8_t     dc_offset_attenuation_low_range;    /*adi,dc-offset-attenuation-low-range*/
       uint8_t     dc_offset_count_high_range;         /*adi,dc-offset-count-high-range*/
       uint8_t     dc_offset_count_low_range;          /*adi,dc-offset-count-low-range*/
       uint8_t     tdd_use_fdd_vco_tables_enable;  /*adi,tdd-use-fdd-vco-tables-enable*/
       uint8_t     split_gain_table_mode_enable;   /*adi,split-gain-table-mode-enable*/
       uint32_t    trx_synthesizer_target_fref_overwrite_hz;   /*adi,trx-synthesizer-target-fref-overwrite-hz*/
       uint8_t     qec_tracking_slow_mode_enable;  /*adi,qec-tracking-slow-mode-enable*/
       /*ENSM Control*/
       uint8_t     ensm_enable_pin_pulse_mode_enable;  /*adi,ensm-enable-pin-pulse-mode-enable*/
       uint8_t     ensm_enable_txnrx_control_enable;   /*adi,ensm-enable-txnrx-control-enable*/
       /*LO Control*/
       uint64_t    rx_synthesizer_frequency_hz;    /*adi,rx-synthesizer-frequency-hz*/
       uint64_t    tx_synthesizer_frequency_hz;    /*adi,tx-synthesizer-frequency-hz*/
       /*Rate & BW Control*/
       uint32_t    rx_path_clock_frequencies[6];   /*adi,rx-path-clock-frequencies*/
       uint32_t    tx_path_clock_frequencies[6];   /*adi,tx-path-clock-frequencies*/
       uint32_t    rf_rx_bandwidth_hz; /*adi,rf-rx-bandwidth-hz*/
       uint32_t    rf_tx_bandwidth_hz; /*adi,rf-tx-bandwidth-hz*/
       /*RF Port Control*/
       uint32_t    rx_rf_port_input_select;    /*adi,rx-rf-port-input-select*/
       uint32_t    tx_rf_port_input_select;    /*adi,tx-rf-port-input-select*/
       /*TX Attenuation Control*/
       int32_t     tx_attenuation_mdB; /*adi,tx-attenuation-mdB*/
       uint8_t     update_tx_gain_in_alert_enable; /*adi,update-tx-gain-in-alert-enable*/
       /*Reference Clock Control*/
       uint8_t     xo_disable_use_ext_refclk_enable;   /*adi,xo-disable-use-ext-refclk-enable*/
       uint32_t    dcxo_coarse_and_fine_tune[2];   /*adi,dcxo-coarse-and-fine-tune*/
       uint32_t    clk_output_mode_select;     /*adi,clk-output-mode-select*/
       /*Gain Control*/
       uint8_t     gc_rx1_mode;    /*adi,gc-rx1-mode*/
       uint8_t     gc_rx2_mode;    /*adi,gc-rx2-mode*/
       uint8_t     gc_adc_large_overload_thresh;   /*adi,gc-adc-large-overload-thresh*/
       uint8_t     gc_adc_ovr_sample_size; /*adi,gc-adc-ovr-sample-size*/
       uint8_t     gc_adc_small_overload_thresh;   /*adi,gc-adc-small-overload-thresh*/
       uint16_t    gc_dec_pow_measurement_duration;    /*adi,gc-dec-pow-measurement-duration*/
       uint8_t     gc_dig_gain_enable; /*adi,gc-dig-gain-enable*/
       uint16_t    gc_lmt_overload_high_thresh;    /*adi,gc-lmt-overload-high-thresh*/
       uint16_t    gc_lmt_overload_low_thresh; /*adi,gc-lmt-overload-low-thresh*/
       uint8_t     gc_low_power_thresh;    /*adi,gc-low-power-thresh*/
       uint8_t     gc_max_dig_gain;    /*adi,gc-max-dig-gain*/
       /*Gain MGC Control*/
       uint8_t     mgc_dec_gain_step;  /*adi,mgc-dec-gain-step*/
       uint8_t     mgc_inc_gain_step;  /*adi,mgc-inc-gain-step*/
       uint8_t     mgc_rx1_ctrl_inp_enable;    /*adi,mgc-rx1-ctrl-inp-enable*/
       uint8_t     mgc_rx2_ctrl_inp_enable;    /*adi,mgc-rx2-ctrl-inp-enable*/
       uint8_t     mgc_split_table_ctrl_inp_gain_mode; /*adi,mgc-split-table-ctrl-inp-gain-mode*/
       /*Gain AGC Control*/
       uint8_t     agc_adc_large_overload_exceed_counter;  /*adi,agc-adc-large-overload-exceed-counter*/
       uint8_t     agc_adc_large_overload_inc_steps;   /*adi,agc-adc-large-overload-inc-steps*/
       uint8_t     agc_adc_lmt_small_overload_prevent_gain_inc_enable; /*adi,agc-adc-lmt-small-overload-prevent-gain-inc-enable*/
       uint8_t     agc_adc_small_overload_exceed_counter;  /*adi,agc-adc-small-overload-exceed-counter*/
       uint8_t     agc_dig_gain_step_size; /*adi,agc-dig-gain-step-size*/
       uint8_t     agc_dig_saturation_exceed_counter;  /*adi,agc-dig-saturation-exceed-counter*/
       uint32_t    agc_gain_update_interval_us; /*adi,agc-gain-update-interval-us*/
       uint8_t     agc_immed_gain_change_if_large_adc_overload_enable; /*adi,agc-immed-gain-change-if-large-adc-overload-enable*/
       uint8_t     agc_immed_gain_change_if_large_lmt_overload_enable; /*adi,agc-immed-gain-change-if-large-lmt-overload-enable*/
       uint8_t     agc_inner_thresh_high;  /*adi,agc-inner-thresh-high*/
       uint8_t     agc_inner_thresh_high_dec_steps;    /*adi,agc-inner-thresh-high-dec-steps*/
       uint8_t     agc_inner_thresh_low;   /*adi,agc-inner-thresh-low*/
       uint8_t     agc_inner_thresh_low_inc_steps; /*adi,agc-inner-thresh-low-inc-steps*/
       uint8_t     agc_lmt_overload_large_exceed_counter;  /*adi,agc-lmt-overload-large-exceed-counter*/
       uint8_t     agc_lmt_overload_large_inc_steps;   /*adi,agc-lmt-overload-large-inc-steps*/
       uint8_t     agc_lmt_overload_small_exceed_counter;  /*adi,agc-lmt-overload-small-exceed-counter*/
       uint8_t     agc_outer_thresh_high;  /*adi,agc-outer-thresh-high*/
       uint8_t     agc_outer_thresh_high_dec_steps;    /*adi,agc-outer-thresh-high-dec-steps*/
       uint8_t     agc_outer_thresh_low;   /*adi,agc-outer-thresh-low*/
       uint8_t     agc_outer_thresh_low_inc_steps; /*adi,agc-outer-thresh-low-inc-steps*/
       uint32_t    agc_attack_delay_extra_margin_us;   /*adi,agc-attack-delay-extra-margin-us*/
       uint8_t     agc_sync_for_gain_counter_enable;   /*adi,agc-sync-for-gain-counter-enable*/
       /*Fast AGC*/
       uint32_t    fagc_dec_pow_measuremnt_duration;   /*adi,fagc-dec-pow-measurement-duration*/
       uint32_t    fagc_state_wait_time_ns;    /*adi,fagc-state-wait-time-ns*/
           /*Fast AGC - Low Power*/
       uint8_t     fagc_allow_agc_gain_increase;   /*adi,fagc-allow-agc-gain-increase-enable*/
       uint32_t    fagc_lp_thresh_increment_time;  /*adi,fagc-lp-thresh-increment-time*/
       uint32_t    fagc_lp_thresh_increment_steps; /*adi,fagc-lp-thresh-increment-steps*/
           /*Fast AGC - Lock Level*/
       uint32_t    fagc_lock_level;    /*adi,fagc-lock-level*/
       uint8_t     fagc_lock_level_lmt_gain_increase_en;   /*adi,fagc-lock-level-lmt-gain-increase-enable*/
       uint32_t    fagc_lock_level_gain_increase_upper_limit;  /*adi,fagc-lock-level-gain-increase-upper-limit*/
           /*Fast AGC - Peak Detectors and Final Settling*/
       uint32_t    fagc_lpf_final_settling_steps;  /*adi,fagc-lpf-final-settling-steps*/
       uint32_t    fagc_lmt_final_settling_steps;  /*adi,fagc-lmt-final-settling-steps*/
       uint32_t    fagc_final_overrange_count; /*adi,fagc-final-overrange-count*/
           /*Fast AGC - Final Power Test*/
       uint8_t     fagc_gain_increase_after_gain_lock_en;  /*adi,fagc-gain-increase-after-gain-lock-enable*/
           /*Fast AGC - Unlocking the Gain*/
       uint32_t    fagc_gain_index_type_after_exit_rx_mode;    /*adi,fagc-gain-index-type-after-exit-rx-mode*/
       uint8_t     fagc_use_last_lock_level_for_set_gain_en;   /*adi,fagc-use-last-lock-level-for-set-gain-enable*/
       uint8_t     fagc_rst_gla_stronger_sig_thresh_exceeded_en;   /*adi,fagc-rst-gla-stronger-sig-thresh-exceeded-enable*/
       uint32_t    fagc_optimized_gain_offset; /*adi,fagc-optimized-gain-offset*/
       uint32_t    fagc_rst_gla_stronger_sig_thresh_above_ll;  /*adi,fagc-rst-gla-stronger-sig-thresh-above-ll*/
       uint8_t     fagc_rst_gla_engergy_lost_sig_thresh_exceeded_en;   /*adi,fagc-rst-gla-engergy-lost-sig-thresh-exceeded-enable*/
       uint8_t     fagc_rst_gla_engergy_lost_goto_optim_gain_en;   /*adi,fagc-rst-gla-engergy-lost-goto-optim-gain-enable*/
       uint32_t    fagc_rst_gla_engergy_lost_sig_thresh_below_ll;  /*adi,fagc-rst-gla-engergy-lost-sig-thresh-below-ll*/
       uint32_t    fagc_energy_lost_stronger_sig_gain_lock_exit_cnt;   /*adi,fagc-energy-lost-stronger-sig-gain-lock-exit-cnt*/
       uint8_t     fagc_rst_gla_large_adc_overload_en; /*adi,fagc-rst-gla-large-adc-overload-enable*/
       uint8_t     fagc_rst_gla_large_lmt_overload_en; /*adi,fagc-rst-gla-large-lmt-overload-enable*/
       uint8_t     fagc_rst_gla_en_agc_pulled_high_en; /*adi,fagc-rst-gla-en-agc-pulled-high-enable*/
       uint32_t    fagc_rst_gla_if_en_agc_pulled_high_mode;    /*adi,fagc-rst-gla-if-en-agc-pulled-high-mode*/
       uint32_t    fagc_power_measurement_duration_in_state5;  /*adi,fagc-power-measurement-duration-in-state5*/
       /*RSSI Control*/
       uint32_t    rssi_delay; /*adi,rssi-delay*/
       uint32_t    rssi_duration;  /*adi,rssi-duration*/
       uint8_t     rssi_restart_mode;  /*adi,rssi-restart-mode*/
       uint8_t     rssi_unit_is_rx_samples_enable; /*adi,rssi-unit-is-rx-samples-enable*/
       uint32_t    rssi_wait;  /*adi,rssi-wait*/
       /*Aux ADC Control*/
       uint32_t    aux_adc_decimation; /*adi,aux-adc-decimation*/
       uint32_t    aux_adc_rate;   /*adi,aux-adc-rate*/
       /*AuxDAC Control*/
       uint8_t     aux_dac_manual_mode_enable; /*adi,aux-dac-manual-mode-enable*/
       uint32_t    aux_dac1_default_value_mV;  /*adi,aux-dac1-default-value-mV*/
       uint8_t     aux_dac1_active_in_rx_enable;   /*adi,aux-dac1-active-in-rx-enable*/
       uint8_t     aux_dac1_active_in_tx_enable;   /*adi,aux-dac1-active-in-tx-enable*/
       uint8_t     aux_dac1_active_in_alert_enable;    /*adi,aux-dac1-active-in-alert-enable*/
       uint32_t    aux_dac1_rx_delay_us;   /*adi,aux-dac1-rx-delay-us*/
       uint32_t    aux_dac1_tx_delay_us;   /*adi,aux-dac1-tx-delay-us*/
       uint32_t    aux_dac2_default_value_mV;  /*adi,aux-dac2-default-value-mV*/
       uint8_t     aux_dac2_active_in_rx_enable;   /*adi,aux-dac2-active-in-rx-enable*/
       uint8_t     aux_dac2_active_in_tx_enable;   /*adi,aux-dac2-active-in-tx-enable*/
       uint8_t     aux_dac2_active_in_alert_enable;    /*adi,aux-dac2-active-in-alert-enable*/
       uint32_t    aux_dac2_rx_delay_us;   /*adi,aux-dac2-rx-delay-us*/
       uint32_t    aux_dac2_tx_delay_us;   /*adi,aux-dac2-tx-delay-us*/
       /*Temperature Sensor Control*/
       uint32_t    temp_sense_decimation;  /*adi,temp-sense-decimation*/
       uint16_t    temp_sense_measurement_interval_ms; /*adi,temp-sense-measurement-interval-ms*/
       int8_t      temp_sense_offset_signed;   /*adi,temp-sense-offset-signed*/
       uint8_t     temp_sense_periodic_measurement_enable; /*adi,temp-sense-periodic-measurement-enable*/
       /*Control Out Setup*/
       uint8_t     ctrl_outs_enable_mask;  /*adi,ctrl-outs-enable-mask*/
       uint8_t     ctrl_outs_index;    /*adi,ctrl-outs-index*/
       /*External LNA Control*/
       uint32_t    elna_settling_delay_ns; /*adi,elna-settling-delay-ns*/
       uint32_t    elna_gain_mdB;  /*adi,elna-gain-mdB*/
       uint32_t    elna_bypass_loss_mdB;   /*adi,elna-bypass-loss-mdB*/
       uint8_t     elna_rx1_gpo0_control_enable;   /*adi,elna-rx1-gpo0-control-enable*/
       uint8_t     elna_rx2_gpo1_control_enable;   /*adi,elna-rx2-gpo1-control-enable*/
       /*Digital Interface Control*/
       uint8_t     pp_tx_swap_enable;  /*adi,pp-tx-swap-enable*/
       uint8_t     pp_rx_swap_enable;  /*adi,pp-rx-swap-enable*/
       uint8_t     tx_channel_swap_enable; /*adi,tx-channel-swap-enable*/
       uint8_t     rx_channel_swap_enable; /*adi,rx-channel-swap-enable*/
       uint8_t     rx_frame_pulse_mode_enable; /*adi,rx-frame-pulse-mode-enable*/
       uint8_t     two_t_two_r_timing_enable;  /*adi,2t2r-timing-enable*/
       uint8_t     invert_data_bus_enable; /*adi,invert-data-bus-enable*/
       uint8_t     invert_data_clk_enable; /*adi,invert-data-clk-enable*/
       uint8_t     fdd_alt_word_order_enable;  /*adi,fdd-alt-word-order-enable*/
       uint8_t     invert_rx_frame_enable; /*adi,invert-rx-frame-enable*/
       uint8_t     fdd_rx_rate_2tx_enable; /*adi,fdd-rx-rate-2tx-enable*/
       uint8_t     swap_ports_enable;  /*adi,swap-ports-enable*/
       uint8_t     single_data_rate_enable;    /*adi,single-data-rate-enable*/
       uint8_t     lvds_mode_enable;   /*adi,lvds-mode-enable*/
       uint8_t     half_duplex_mode_enable;    /*adi,half-duplex-mode-enable*/
       uint8_t     single_port_mode_enable;    /*adi,single-port-mode-enable*/
       uint8_t     full_port_enable;   /*adi,full-port-enable*/
       uint8_t     full_duplex_swap_bits_enable;   /*adi,full-duplex-swap-bits-enable*/
       uint32_t    delay_rx_data;  /*adi,delay-rx-data*/
       uint32_t    rx_data_clock_delay;    /*adi,rx-data-clock-delay*/
       uint32_t    rx_data_delay;  /*adi,rx-data-delay*/
       uint32_t    tx_fb_clock_delay;  /*adi,tx-fb-clock-delay*/
       uint32_t    tx_data_delay;  /*adi,tx-data-delay*/
       uint32_t    lvds_bias_mV;   /*adi,lvds-bias-mV*/
       uint8_t     lvds_rx_onchip_termination_enable;  /*adi,lvds-rx-onchip-termination-enable*/
       uint8_t     rx1rx2_phase_inversion_en;  /*adi,rx1-rx2-phase-inversion-enable*/
       /*Tx Monitor Control*/
       uint32_t    low_high_gain_threshold_mdB;    /*adi,txmon-low-high-thresh*/
       uint32_t    low_gain_dB;    /*adi,txmon-low-gain*/
       uint32_t    high_gain_dB;   /*adi,txmon-high-gain*/
       uint8_t     tx_mon_track_en;    /*adi,txmon-dc-tracking-enable*/
       uint8_t     one_shot_mode_en;   /*adi,txmon-one-shot-mode-enable*/
       uint32_t    tx_mon_delay;   /*adi,txmon-delay*/
       uint32_t    tx_mon_duration;    /*adi,txmon-duration*/
       uint32_t    tx1_mon_front_end_gain; /*adi,txmon-1-front-end-gain*/
       uint32_t    tx2_mon_front_end_gain; /*adi,txmon-2-front-end-gain*/
       uint32_t    tx1_mon_lo_cm;  /*adi,txmon-1-lo-cm*/
       uint32_t    tx2_mon_lo_cm;  /*adi,txmon-2-lo-cm*/
       /*GPIO definitions*/
       int32_t     gpio_resetb;    /*reset-gpios*/
       /*MCS Sync*/
       int32_t     gpio_sync;      /*sync-gpios*/
       int32_t     gpio_cal_sw1;   /*cal-sw1-gpios*/
       int32_t     gpio_cal_sw2;   /*cal-sw2-gpios*/
   }AD9361_InitParam;

2. Below is defined the rf_rssi structure used by the ad9361_get_rx_rssi()
   function:

.. code:: C

   struct rf_rssi {
       u32 ant;    // Antenna number for which RSSI is reported
       u32 symbol; // Runtime RSSI
       u32 preamble;   // Initial RSSI
       s32 multiplier; // Multiplier to convert reported RSSI
       u8 duration;    // Duration to be considered for measuring
   };

3. Below is defined the AD9361_RXFIRConfig structure used by the
   ad9361_set_rx_fir_config() function:

.. code:: C

   typedef struct
   {
       uint32_t rx;        // 1, 2, 3(both)
       int32_t rx_gain;    // -12, -6, 0, 6
       uint32_t rx_dec;    // 1, 2, 4
       int16_t rx_coef[64];
   }AD9361_RXFIRConfig;

4. Below is defined the AD9361_TXFIRConfig structure used by the
   ad9361_set_tx_fir_config() function:

.. code:: C

   typedef struct
   {
       uint32_t tx;        // 1, 2, 3(both)
       int32_t tx_gain;    // -6, 0
       uint32_t tx_int;    // 1, 2, 4
       int16_t tx_coef[64];
   }AD9361_TXFIRConfig;

AD9361 Doxygen Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://analogdevicesinc.github.io/no-OS/
