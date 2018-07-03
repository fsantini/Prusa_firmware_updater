# Prusa firmware updater
Stand-alone updater for Prusa Mk3 firmware, including language packs.

Run it with Python 2.7 as the following:

`python prusaFlash.py [COM port] [hex file or url]`

This program requires a custom build of avrdude by Prusa Research, available here: https://github.com/prusa3d/Slic3r/tree/master/xs/src/avrdude

This build has been here modified to work as a standalone program, and the modified source is available in the avrdude_src directory of the repository.

Included in this repository, there is a binary build of avrdude for the **Raspberry Pi**. If you need a different platform, please recompile it from source.

# Disclaimer

I am in **NO WAY** affiliated with Prusa Research.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.


