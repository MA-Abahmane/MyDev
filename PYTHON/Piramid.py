"""
Make a program that takes the number of blocks and returns the hite of the piramid
Ex:
               *
              * *                     *
             * * *    hight: 4       * *     hight: 3          *     hight: 2
            * * * *                 * * *                     * *
           Blocks: 10             Blocks: 6                 Blocks: 3
"""


blk = int(input('Enter the number of blocks\t'))

i = 1
count = 0
while (blk):
    blk -= i
    count += 1

    i += 1

print(count)