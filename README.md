# QR Generator
## Usage
`qr-generator [-h] [-o OUTPUTFILENAME] [-qc QRCOLOR] [-qb QRBACKGROUNDCOLOR] [-qs QRSIZE] [-l LOGOADDITION] [-ls LOGOSIZERATIO] [-lc] content`

### Mandatory argument
The content of the QR Code: eg: https://github.com/thewally/qr-generator

### Options

| Option                                                               | Description                                                                    |     
|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `-h`, `--help`                                                       | show this help message and exit                                                |
| `-o [OUTPUTFILENAME]`, `--outputFilename [OUTPUTFILENAME]`           | Output filename, eg: output.png                                                |
| `-qc [QRCOLOR]`, `--qrColor [QRCOLOR]`                               | Color of the generated qr-code. eg: #314a4e                                    |
| `-qb [QRBACKGROUNDCOLOR]`, `--qrBackgroundColor [QRBACKGROUNDCOLOR]` | Color of the generated qr-code, eg: #ffffff                                    |
| `-qs [QRSIZE]`, `--qrSize [QRSIZE]`                                  | qr-code size in pixels, eg: '3000'                                             |
| `-l [LOGOADDITION]`, `--logoAddition [LOGOADDITION]`                 | filename of logo for addition, eg: logo.png                                    |
| `-ls [LOGOSIZERATIO]`, `--logoSizeRatio [LOGOSIZERATIO]`             | size ratio of logo compared to qr-code, eg: '0.25' (for 25 percent of qr code) |


## Examples

### QR code without logo
`./qr-generator "My QR Content: https://github.com/thewally/qr-generator" -o output-qr.png`

### QR code with logo
`./qr-generator "My QR Content: https://github.com/thewally/qr-generator" -o output-qr.png -l logo.png`

