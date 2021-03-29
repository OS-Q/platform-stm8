# Copyright 2018-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://arduino.cc/en/Reference/HomePage
"""

import os
import sys

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoststm8")
assert os.path.isdir(FRAMEWORK_DIR)


def inject_dummy_reference_to_main():
    build_dir = env.subst("$BUILD_DIR")
    dummy_file = os.path.join(build_dir, "_pio_main_ref.c")
    if not os.path.isfile(dummy_file):
        if not os.path.isdir(build_dir):
            os.makedirs(build_dir)
        with open(dummy_file, "w") as fp:
            fp.write("void main(void);void (*dummy_variable) () = main;")

    env.Append(PIOBUILDFILES=dummy_file)


env.Append(
    CCFLAGS=[
        "--less-pedantic"
    ],

    CPPDEFINES=[
        "ARDUINO_ARCH_STM8",
        ("ARDUINO", 10802),
        ("double", "float"),
        "USE_STDINT",
        "__PROG_TYPES_COMPAT__"
    ],

    CPPPATH=[
        os.path.join(FRAMEWORK_DIR, "cores", env.BoardConfig().get("build.core")),
        os.path.join(FRAMEWORK_DIR, "STM8S_StdPeriph_Driver", "inc")
    ],

    LIBPATH=[
        os.path.join(FRAMEWORK_DIR, "STM8S_StdPeriph_Driver", "lib")
    ],

    LIBS=[board_config.get("build.mcu")[0:8].upper()],

    LIBSOURCE_DIRS=[
        os.path.join(FRAMEWORK_DIR, "libraries")
    ]
)

# Fixes possible issue with "ASlink-Warning-No definition of area SSEG" error.
# This message means that main.c is not pulled in by the linker because there was no
# reference to main() anywhere. Details: https://tenbaht.github.io/sduino/usage/faq/
inject_dummy_reference_to_main()

# By default PlatformIO generates "main.cpp" for the Arduino framework.
# But Sduino doesn't support C++ sources. Exit if a file with a C++
# extension is detected.
for root, _, files in os.walk(env.subst("$PROJECT_SRC_DIR")):
    for f in files:
        if f.endswith((".cpp", ".cxx", ".cc")):
            sys.stderr.write(
                "Error: Detected C++ file `%s` which is not compatible with Arduino"
                " framework as only C/ASM sources are allowed.\n"
                % os.path.join(root, f)
            )
            env.Exit(1)

#
# Target: Build Core Library
#

libs = []

if "build.variant" in env.BoardConfig():
    env.Append(
        CPPPATH=[
            os.path.join(
                FRAMEWORK_DIR, "variants", env.BoardConfig().get("build.variant"))
        ]
    )
    libs.append(env.BuildLibrary(
        os.path.join("$BUILD_DIR", "FrameworkArduinoVariant"),
        os.path.join(FRAMEWORK_DIR, "variants", env.BoardConfig().get("build.variant"))
    ))

libs.append(env.BuildLibrary(
    os.path.join("$BUILD_DIR", "FrameworkArduino"),
    os.path.join(FRAMEWORK_DIR, "cores", env.BoardConfig().get("build.core"))
))

env.Prepend(LIBS=libs)
