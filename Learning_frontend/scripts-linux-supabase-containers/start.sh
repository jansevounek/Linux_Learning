#! /bin/bash

read -p "Are you sure you want to start supabase conatainers? [Y/n]: " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

sudo docker start supabase-storage && echo "started"

sudo docker start supabase-meta && echo "started"

sudo docker start supabase-studio && echo "started"

sudo docker start realtime-dev.supabase-realtime && echo "started"

sudo docker start supabase-kong && echo "started"

sudo docker start supabase-auth && echo "started"

sudo docker start supabase-rest && echo "started"

sudo docker start supabase-edge-functions && echo "started"

sudo docker start supabase-analytics && echo "started"

sudo docker start supabase-db && echo "started"

sudo docker start supabase-vector && echo "started"

sudo docker start supabase-imgproxy && echo "started"