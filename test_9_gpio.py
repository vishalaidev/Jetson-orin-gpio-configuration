/dts-v1/;
/plugin/;

/ {
    jetson-header-name = "Jetson 40pin Header";
    overlay-name = "GPIO Enable for Pins 12,16,18,22,32,33,35,38,40";

    compatible = 
        "nvidia,p3768-0000+p3767-0000",
        "nvidia,p3768-0000+p3767-0001",
        "nvidia,p3768-0000+p3767-0003",
        "nvidia,p3768-0000+p3767-0004",
        "nvidia,p3768-0000+p3767-0005",
        "nvidia,p3768-0000+p3767-0000-super",
        "nvidia,p3768-0000+p3767-0001-super",
        "nvidia,p3768-0000+p3767-0003-super",
        "nvidia,p3768-0000+p3767-0004-super",
        "nvidia,p3768-0000+p3767-0005-super",
        "nvidia,p3509-0000+p3767-0000",
        "nvidia,p3509-0000+p3767-0001",
        "nvidia,p3509-0000+p3767-0003",
        "nvidia,p3509-0000+p3767-0004",
        "nvidia,p3509-0000+p3767-0005";

    fragment@0 {
        target = <&pinmux>;

        __overlay__ {
            pinctrl-names = "default";
            pinctrl-0 = <&jetson_io_pinmux>;

            jetson_io_pinmux: exp-header-pinmux {

                /* ---- Pin 12 (PH7) ---- */
                hdr40-pin12 {
                    nvidia,pins = "soc_gpio41_ph7";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 16 (PY4) ---- */
                hdr40-pin16 {
                    nvidia,pins = "spi3_cs1_py4";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 18 (PY3) ---- */
                hdr40-pin18 {
                    nvidia,pins = "spi3_cs0_py3";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 22 (PY1) ---- */
                hdr40-pin22 {
                    nvidia,pins = "spi3_miso_py1";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 32 (PG6) ---- */
                hdr40-pin32 {
                    nvidia,pins = "soc_gpio19_pg6";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 33 (PH0) ---- */
                hdr40-pin33 {
                    nvidia,pins = "soc_gpio21_ph0";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 35 (PI2) ---- */
                hdr40-pin35 {
                    nvidia,pins = "soc_gpio44_pi2";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 38 (PI1) ---- */
                hdr40-pin38 {
                    nvidia,pins = "soc_gpio43_pi1";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

                /* ---- Pin 40 (PI0) ---- */
                hdr40-pin40 {
                    nvidia,pins = "soc_gpio42_pi0";
                    nvidia,tristate = <0>;
                    nvidia,enable-input = <1>;
                    nvidia,pull = <0>;
                };

            };
        };
    };
};
