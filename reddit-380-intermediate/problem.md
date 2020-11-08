# [2019-08-07] Challenge #380 [Intermediate] Smooshed Morse Code 2
[Challenge #380 [Intermediate]](https://www.reddit.com/r/dailyprogrammer/comments/cn6gz5/20190807_challenge_380_intermediate_smooshed/)

Smooshed Morse code means Morse code with the spaces or other delimiters between encoded letters left out. See this week's Easy challenge for more detail.

A permutation of the alphabet is a 26-character string in which each of the letters a through z appears once.

Given a smooshed Morse code encoding of a permutation of the alphabet, find the permutation it encodes, or any other permutation that produces the same encoding (in general there will be more than one). It's not enough to write a program that will eventually finish after a very long period of time: run your code through to completion for at least one example.

## Examples

```
smalpha(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")
    => "wirnbfzehatqlojpgcvusyxkmd"
smalpha(".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-")
    => "wzjlepdsvothqfxkbgrmyicuna"
smalpha("..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..")
    => "uvfsqmjazxthbidyrkcwegponl"
```

Again, there's more than one valid output for these inputs.

## Optional bonus 1

Here's a list of 1000 inputs. How fast can you find the output for all of them? A good time depends on your language of choice and setup, so there's no specific time to aim for.

## Optional bonus 2

Typically, a valid input will have thousands of possible outputs. The object of this bonus challenge is to find a valid input with as few possible outputs as possible, while still having at least 1. The following encoded string has 41 decodings:

......-..--...---.-....---...--....--.-..---.....---.-.---..---.-....--.-.---.-.--

Can you do better?