# 🐟 printfihh

`printfihh` is a fun, lightweight Python library that prints your terminal messages inside the mouths of giant ASCII-art fish and crocodiles! 

It automatically dynamically scales and aligns the speech bubbles to perfectly fit whatever message you provide.

## Installation

You can install `printfihh` easily via pip:

```bash
pip install printfihh
```

## Usage

The library currently provides three distinct aquatic creatures you can use to display your messages.

### 1. The Fihh (`printfihh`)

```python
from printfihh import printfihh

printfihh("Blub blub... Hello World!")
```

### 2. The Unlucky Fihh (`printdeadfihh`)

```python
from printfihh import printdeadfihh

printdeadfihh("supp?")
```

### 3. The Crocodile (`printcroc`)

```python
from printfihh import printcroc

printcroc("The Arts aint mine but they were open source")
```

## Example Output

```text
=== Testing printcroc (Crocodile) ===
                                                               _  _
.----------------------------------------------.     _ _      (0)(0)-._  _.-'^^'^^'^^'^^'^^'--.
| The Arts aint mine but they were open source  >    (.(.)----'`        ^^'                /^   ^^-._
'----------------------------------------------'    (    `                 \             |    _    ^^-._
                                                     VvvvvvvVv~~`__,/.._>  /:/:/:/:/:/:/:/\  (_..,______^^-.
                                                      `^^^^^^^^`/  /   /  /`^^^^^^^^^>^^>^`>  >        _`)  )
                                                               (((`   (((`          (((`  (((`        `'--'^
```

## License
MIT License
