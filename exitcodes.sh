#!/bin/bash

package=NetworkManager-ppp.x86_64 

sudo dnf install $package >> package_install_results.log


if  [  $? -eq 0 ]
then
   echo "The package $package  was installed successfully"
else
   echo "The exit code is" $?
   echo "The package  $package was not installed. Please check again or confirm if package exist" >> package_install_failure.log
fi

