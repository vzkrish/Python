#! /bin/bash
clear
read -p "enter a name " n
if [[ -f $n ]]
then
	printf "file\n"
elif [[ -d $n ]]
then
	printf "directory\n"
else
	printf "other entry\n"
fi

