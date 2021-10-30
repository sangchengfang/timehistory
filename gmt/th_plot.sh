#! /bin/bash
gmt begin norm_th png

gmt basemap -R0/35/0/1100 -JX20c/10c -Bxa10f5g5+l"time BP (ka)" -Bya500f100g100+l"ice thickness" -BWSen+t""

#for ((i=1; i <= 9644; i++ ))
#   do
#        cat ./line/file$i.txt | gmt plot -A -Wblue
#        echo "plot line $i"
#    done

cat ./norm_th.txt | gmt plot -A -Wthick,blue

gmt end show
