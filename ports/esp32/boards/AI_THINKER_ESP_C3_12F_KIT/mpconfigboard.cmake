set(IDF_TARGET esp32c3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.ble
    ${MICROPY_BOARD_DIR}/sdkconfig.board
)
