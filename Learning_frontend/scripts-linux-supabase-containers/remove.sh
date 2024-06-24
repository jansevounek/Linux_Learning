#! /bin/bash

read -p "Are you sure you want to stop the supabase containers? [Y/n]: " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

sudo docker stop supabase-storage && echo "stoped"

sudo docker stop supabase-meta && echo "stoped"

sudo docker stop supabase-studio && echo "stoped"

sudo docker stop realtime-dev.supabase-realtime && echo "stoped"

sudo docker stop supabase-kong && echo "stoped"

sudo docker stop supabase-auth && echo "stoped"

sudo docker stop supabase-rest && echo "stoped"

sudo docker stop supabase-edge-functions && echo "stoped"

sudo docker stop supabase-analytics && echo "stoped"

sudo docker stop supabase-db && echo "stoped"

sudo docker stop supabase-vector && echo "stoped"

sudo docker stop supabase-imgproxy && echo "stoped"


sudo docker rm supabase-storage

sudo docker rm supabase-meta

sudo docker rm supabase-studio

sudo docker rm realtime-dev.supabase-realtime

sudo docker rm supabase-kong

sudo docker rm supabase-auth

sudo docker rm supabase-rest

sudo docker rm supabase-edge-functions

sudo docker rm supabase-analytics

sudo docker rm supabase-db

sudo docker rm supabase-vector

sudo docker rm supabase-imgproxy