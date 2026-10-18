# TextDrop

A quick notepad for NVDA.

## What it is

TextDrop opens a simple text box with one keyboard shortcut, from any program. Type or paste text, watch a live character count, and save it to a file if you want. There is no need to open another program or switch windows, and everything works with the keyboard and a screen reader.

## What it is useful for

- Drafting a message or a post with a character limit, such as on X, while knowing how much you have written
- Jotting down a quick note while you are doing something else
- Writing a longer text in a calm place before pasting it into a page or an app
- Saving that text to a file with a single button

## Requirements

NVDA 2026.2 or later.

## Installation

1. Download the file with the nvda-addon extension from the [Releases](https://github.com/MauricioCelesta/text_drop/releases) section of this repository.
2. With NVDA running, open the file with Enter.
3. Confirm the installation and restart NVDA when asked.

## How to use it

1. Press NVDA+0 anywhere. The Text drop window opens with the cursor in the text box.
2. Type or paste your text.
3. Press Tab to reach the character count. It is a read-only field that updates every time you type or delete.
4. Press Tab again to reach the Guardar and Cancelar buttons. Guardar means Save and Cancelar means Cancel.

Save opens the standard Windows save dialog, where you choose the folder and the file name. The file is saved as plain text with UTF-8 encoding, so accents and symbols are not corrupted when you open it later. If the file already exists, you are asked before it is replaced. The window stays open after saving.

Cancel closes the window and discards what you wrote. TextDrop does not store anything on its own.

## Settings

The default shortcut is NVDA+0. To change it, open the NVDA menu, go to Preferences, then Input gestures, find the command with the description `Abre el cuadro de edición de textDrop` and assign the shortcut you prefer. That description is shown in Spanish.

## Privacy

TextDrop works completely offline and sends nothing to the internet. It only writes a file when you press Save.

## Interface language

The text inside the window is currently in Spanish. The window title is Text drop, the buttons are Guardar and Cancelar, and the character count reads, for example, 12 caracteres.

## Building from source

Zip the manifest.ini file and the globalPlugins folder, leaving out the LICENSE file, the README file and the git folder, then change the zip extension to nvda-addon.

## License and contact

Released under the GNU General Public License version 2. See the LICENSE file.

Author: Mauricio Pedroza Garza.

For questions or to report a problem, open an issue in this repository or [contact me here](https://mauriciocelesta.com/contacto/).

## Changelog

- 1.1.1: added this README and the project address to the manifest, with no changes to how the add-on works
- 1.1.0: default shortcut NVDA+0
- 1.0.0: first release