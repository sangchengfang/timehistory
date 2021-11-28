#! /bin/bash
gmt begin Lambeck png,pdf
gmt basemap -R0/35/0/1094.24 -JX15c/5c -Bxa5f1g1+l"time BP" -BWSrt+t"Lambeck's time history" --FONT_ANNOT_PRIMARY=8p,Helvetica --FONT_LABEL=10p,Helvetica

gmt basemap -R0/35/0/1094.24 -JX15c/5c -Byaf100g100+l"Ice Thickness" -BWSrt --FONT_ANNOT_PRIMARY=8p,Helvetica,blue --FONT_LABEL=10p,Helvetica,blue


#gmt basemap -R0/35/0/150 -JX15c/8c -Bxa5f1g1+l"time BP" -BWSrt --FONT_ANNOT_PRIMARY=12p,Helvetica,black
#for ((i=1; i <= 9644; i++ ))
#   do
#        cat ./line/file$i.txt | gmt plot -A -Wblue
#        echo "plot line $i"
#    done

awk '$1!="#" {print $1,$2*1000}' Lamb_norm_TH_plateau.dat | gmt plot -A -Wfatter,orange

awk '$1!="#" {print $1,$2*1094.24}' Lamb_norm_TH.dat | gmt plot -A -Wfat,blue

awk '$1!="#" {print $1,$2*1000}' Lamb_norm_TH_last.dat | gmt plot -A -Wthicker,red

awk '$1!="#" {print $1,$2*1094.24+$4/134.28*1000}' L_residual.dat | gmt plot -A -Wthinner,green,dashed

echo 18.43 1000.00 0.2c | gmt plot -Sa -Gyellow -Wred
echo 5.113 1000.00 0.2c | gmt plot -Sa -Gyellow -Wred
#gmt basemap -R0/35/0/134.28 -JX15c/8c -By+l'ice-volume equivalent sea level' -BlbEn --FONT_ANNOT_PRIMARY=12p,Helvetica,red --FONT_LABEL=16p,Helvetica,red
gmt basemap -R0/35/0/146.934547 -JX15c/5c -By+l'ice-volume equivalent sea level' -BlbEn --FONT_ANNOT_PRIMARY=8p,Helvetica --FONT_LABEL=10p,Helvetica

awk '$1!="#" {print $1,-$3}' Lambeck_TH.dat | gmt plot -A -Wthick,black,dashed

awk '$1!="#" {print $1,$2}' Lambeck_TH_selected_abs_flipped.dat | gmt plot -A -Wthick,black

#awk '$1!="#" {print $1,-$2}' Lamb_norm_TH.dat | gmt plot -A -Wthin,red,dashed

gmt end show
