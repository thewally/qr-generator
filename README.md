# QR Generator

## Usage

`qr-generator [-h] [-o OUTPUTFILENAME] [-qc QRCOLOR] [-qb QRBACKGROUNDCOLOR] [-qs QRSIZE] [-l LOGOADDITION] [-ls LOGOSIZERATIO] [-lc] content`

### Mandatory argument

| Argument    | Description                                                              |     
|-------------|--------------------------------------------------------------------------|
| `[CONTENT]` | The content of the QR Code: eg: https://github.com/thewally/qr-generator |

### Optional arguments

| Argument                                                             | Description                                                                    | Default      |    
|----------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------|
| `-h`, `--help`                                                       | show this help message and exit                                                |              |
| `-o [OUTPUTFILENAME]`, `--outputFilename [OUTPUTFILENAME]`           | Output filename, eg: output.png                                                | `output.png` |
| `-qc [QRCOLOR]`, `--qrColor [QRCOLOR]`                               | Color of the generated qr-code. eg: #314a4e                                    | `#000000`      |
| `-qb [QRBACKGROUNDCOLOR]`, `--qrBackgroundColor [QRBACKGROUNDCOLOR]` | Color of the generated qr-code, eg: #ffffff                                    | `#ffffff`      |
| `-qs [QRSIZE]`, `--qrSize [QRSIZE]`                                  | qr-code size in pixels, eg: '3000'                                             | `3000`         |
| `-l [LOGOADDITION]`, `--logoAddition [LOGOADDITION]`                 | filename of logo for addition, eg: logo.png                                    | `logo.png`     |
| `-ls [LOGOSIZERATIO]`, `--logoSizeRatio [LOGOSIZERATIO]`             | size ratio of logo compared to qr-code, eg: '0.25' (for 25 percent of qr code) | `0.25`         |

## How to use (Linux/Mac)

1. Download latest release from: https://github.com/thewally/qr-generator/tree/master/releases
2. Save file
3. Run command `./qr-generator.v1.x.x [CONTENT] [OPTIONS]`

## Examples

### QR code without logo
`./qr-generator "My QR Content: https://github.com/thewally/qr-generator" -o output-qr.png`

### QR code with logo
`./qr-generator "My QR Content: https://github.com/thewally/qr-generator" -o output-qr.png -l -lf logo.png`
