#! /bin/sh

# Change the next three lines to setup the script
role_name="ansible-role-mariadb" # name of project folder: refer to playbook.yml after completion
copy_folder="." # do NOT forget "/." at end of directory
destination_folder="/home/mmccann/projects/github/ansible-role-mariadb" #change to project to which you want to write

echo "***************** Creating Molecule Template *****************"
echo creating molecule project for ... $role_name
molecule init scenario -r $role_name
echo "***************** Copy Contents from Copy Folder Template *****************"
echo copying contents ...
cp -a $copy_folder $destination_folder
echo "***************** Finished Creating Your Molecule Template *****************"
rm -rf molecule