#!/bin/bash

# Get selected task
if [ "$#" -ne 1 ]; then
    task=""
else
    task=$1
fi


# Create PostgreSQL config
set_postgresql() {
    sudo su -l postgres -c "createuser developer -w -s"
    sudo su -l postgres -c "dropdb wundebareklang"
    sudo su -l postgres -c "createdb wundebareklang"
    sudo su -l postgres -c "psql -c \"ALTER USER developer WITH PASSWORD 'developer';\""
    sudo su -l postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE wundebareklang TO developer;\""
}


case ${task} in
    1) prepare_system
    ;;
    2) install_python_packages
    ;;
    3) set_postgresql
    ;;
    4) prepare_db
    ;;
    "") prepare_system
        install_python_packages
        set_postgresql
    ;;
esac
