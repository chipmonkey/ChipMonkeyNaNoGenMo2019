# ProcJam2019

Borrowing heavily from these open source products
* gpt-2: https://github.com/minimaxir/gpt-2-simple
* textworld: https://github.com/microsoft/TextWorld

Steps:
1. Run finetune_gpt2.py to train GPT2 on Grimm's fairy tales
2. Run make_a_novel.py

make_a_novel.py generates a story with TextWorld and walks through
a play run (that part isn't fully automated yet).
It then takes the narrative from the playthrough and passes it through
gpt2 to add lots of words, which are hopefully embellishments on the story
thus generating a novel.

It's not very coherent yet, but ya know.

As a shortcut, if you have a gpt-2 model, and want to use the example text you should be able to just do:

```
import make_a_novel
make_a_novel.makethenovel()
```
which will load a model available to gpt-2-simple and generate text from a pre-played TextWorld output storyguide.

Check out notes here:
* http://www.chiplynch.com/wiki/index.php/NaNoGenMo_2019_-_GPT-2_Edition

And the NaNoGenMo topic here:
* https://github.com/NaNoGenMo/2019/issues/76
