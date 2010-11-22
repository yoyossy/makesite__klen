VIRTUALENVDIR={{ virtualenvdir  }}
PIP_PROJECTFILE={{ pip_projectfile }}

REQ_SUM=$(md5sum $PIP_PROJECTFILE)
OLD_REQ_SUM=$(cat $VIRTUALENVDIR/.reqsum)

# Check pip
if ! which pip >/dev/null; then echo "  * I require pip but it's not installed."; exit 0; fi

if [ -f $PIP_PROJECTFILE ]; then
    echo "  * Update virtualenv requirements '$PIP_PROJECTFILE'."
    if [ "$REQ_SUM" = "$OLD_REQ_SUM" ]; then
        echo "  * Changes not found."
    else
        sudo pip -E $VIRTUALENVDIR install -r $PIP_PROJECTFILE
    fi
fi
