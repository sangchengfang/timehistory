#! /bin/bash
gmt begin Wanghs png,pdf
gmt set MAP_FRAME_PEN thick,black
gmt basemap -R0/93/0/1094.24 -JX15c/5c -Bxa5f1g1+l"time BP" -BWSrt+t"Wang's time history" --FONT_ANNOT_PRIMARY=8p,Helvetica --FONT_LABEL=10p,Helvetica
gmt basemap -R0/93/0/1094.24 -JX15c/5c -Byaf100g100+l"Ice Thickness" -BWSrt --FONT_ANNOT_PRIMARY=8p,Helvetica,blue --FONT_LABEL=10p,Helvetica,blue

awk '$1!="#" {print $1,$2*1094.24}' Whs_norm_TH.dat | gmt plot -A -Wfat,blue

awk '$1!="#" {print $1,$3*1000}' Whs_norm_TH1000.dat | gmt plot -A -Wthicker,red
awk '$1!="#" {print $1,$2*1094.24-$4}' W_residual.dat | gmt plot -A -Wthinner,green,dashed

echo 18.837 1000.00 0.2c | gmt plot -Sa -Gyellow -Wred

#gmt basemap -R0/35/0/134.28 -JX15c/8c -By+l'ice-volume equivalent sea level' -BlbEn --FONT_ANNOT_PRIMARY=12p,Helvetica,red --FONT_LABEL=16p,Helvetica,red
#gmt basemap -R0/95/0/1094.24 -JX15c/5c -By+l'ice-volume equivalent sea level' -BlbEn --FONT_ANNOT_PRIMARY=8p,Helvetica --FONT_LABEL=10p,Helvetica

awk '$1!="#" {print $1,$2}' Wanghs_TH.dat | gmt plot -A -Wthick,DARKORANGE1

#awk '$1!="#" {print $1,-$2}' Lambeck_TH_selected.dat | gmt plot -A -Wdefault,white

#awk '$1!="#" {print $1,-$2}' Lamb_norm_TH.dat | gmt plot -A -Wthin,red,dashed

gmt end show
