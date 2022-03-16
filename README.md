# Mnemonic Splitter

Split mnemonic phrases over multiple locations/sheets. E.g. you have 3 places to store your phrases, but you don't want each place to include the full mnemonic phrase. You want that at least 2 sheets are required to build the full phrase -> This program splits the phrases over multiple sheets accordingly.

## Disclaimer

Use this at your own risk.


## Example

Two sheets can recover your seed. If you loose one sheet you have no problem. If someone else gets access over one sheet you have no problem.

| number | sheet 1  | sheet 2  | sheet 3  |
|--------|----------|----------|----------|
| 1      | phrase1  |          | phrase1  |
| 2      |          | phrase2  | phrase2  |
| 3      | phrase3  | phrase3  |          |
| 4      | phrase4  | phrase4  |          |
| 5      | phrase5  | phrase5  |          |
| 6      |          | phrase6  | phrase6  |
| 7      |          | phrase7  | phrase7  |
| 8      | phrase8  |          | phrase8  |
| 9      | phrase9  |          | phrase9  |
| 10     | phrase10 |          | phrase10 |
| 11     | phrase11 | phrase11 |          |
| 12     |          | phrase12 | phrase12 |


## Usage

Either paste your mnemonic seed in the phrase.txt file, or use the space holders to copy the phrases from hand. Run `python3 splitter.py` for a random generated distribution of the phrases over the sheets. It may also be possible to change the amount of sheets, phrases and so on. Alternatively, you can just use the example distribution from above.


## To do

I think I have an easier solution/algorithm for this problem in mind.


## License

GNU General Public License Version 3, see [License](./License.md)
