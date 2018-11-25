T=` echo $3 |sed "s@/DOWNLOAD/PATH/aria2/@@"`


python3 tg_notify.py aria2 "*$T*
Download Completed"
