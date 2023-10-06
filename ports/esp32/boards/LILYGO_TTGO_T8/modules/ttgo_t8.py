"""LILYGO TTGO T8 MicroPython Helper Library."""

import machine
import os
import sdcard
import sys

from micropython import const


class TTGO_T8:
    """Device Support for LILYGO TTGO T8."""

    def __init__(self):
        self.SD_CS = const(13)
        self.SD_MOSI = const(15)
        self.SD_MISO = const(2)
        self.SD_SCLK = const(14)
        self.__sd = None
        self.__sd_lib = False

    def sdcard(self, baudrate=20_000_000):
        cs = machine.Pin(self.SD_CS, machine.Pin.OUT)
        spi = machine.SPI(
            1,
            baudrate=baudrate,
            polarity=0,
            phase=0,
            bits=8,
            firstbit=machine.SPI.MSB,
            sck=machine.Pin(self.SD_SCLK),
            mosi=machine.Pin(self.SD_MOSI),
            miso=machine.Pin(self.SD_MISO)
        )
        self.__sd = sdcard.SDCard(spi, cs)
        return self.__sd

    def sdcard_mount(self, mountpoint='/sd'):
        if self.__sd is None:
            self.sdcard()

        try:
            os.mount(self.__sd, mountpoint)
        except Exception as e:
            raise e

        if 'lib' in os.listdir(mountpoint):
            sys.path.append(f'{mountpoint}/lib')
            self.__sd_lib = True

    def sdcard_umount(self, mountpoint='/sd'):
        try:
            os.umount(mountpoint)
        except Exception as e:
            raise e
        else:
            self.__sd.spi.deinit()

        if self.__sd_lib:
            sys.path.pop(sys.path.index(f'{mountpoint}/lib'))
            self.__sd_lib = False

