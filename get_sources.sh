#!/bin/sh
SVNURL="http://skype4pidgin.googlecode.com/svn/trunk/"
SVNREV=$(svn info $SVNURL | grep "Revision:" | awk '{ print $NF }')
SVNDATE=$(svn info $SVNURL | grep "Last Changed Date:" | awk '{ print $4 }' | sed 's!-!!g')

svn co http://skype4pidgin.googlecode.com/svn/trunk/ skype4pidgin/

tar cjvf skype4pidgin-${SVNDATE}svn${SVNREV}.tar.bz2 skype4pidgin --exclude=.svn

md5sum skype4pidgin-${SVNDATE}svn${SVNREV}.tar.bz2 > sources
