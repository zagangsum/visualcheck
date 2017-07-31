__author__ = 'gareth.cripps'
import ftplib

#Open ftp connection
ftp = ftplib.FTP('ftp.g7wjw.co.uk', 'line1', '7Summ3R7')

#List the files in the current directory

ftp.dir(remoteFileList.append)


for filename in remoteFileList:
        extensiontest = filename[-3:]
        if extensiontest == "jpg" or extensiontest == "JPG":
            ftpFileList.append(filename[-8:])

for line in ftpFileList:
    print line
ftp.quit()

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print os.path.join(dirname, subdirname)

    # print path to all filenames.

    for filename in filenames:
        extensiontest = filename[-3:]
        if extensiontest == "jpg" or extensiontest == "JPG":
            try:
                inlist = ftpFileList.index(filename)
            except:
                try:
                    localfile = filename
                    if len(localfile) == 8:
                        ftp = ftplib.FTP('192.168.0.8', 'line1', 'bread')
                        ftp.retrbinary("RETR " + filename, open(localfile, 'wb').write)
                        ftp.close()
                        os.unlink(localfile)
                except:
                    print "Error"

        ftp.close()
#try:
#    f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
#except ftplib.error_perm:
#    print 'ERROR: cannot read file "%s"' % FILE
#    os.unlink(FILE)
#else:
#    print '*** Downloaded "%s" to CWD' % FILE
#f.quit()


ftp.quit()






print "\nReadme File Output:"
gFile = open("readme.txt", "r")
buff = gFile.read()
print buff
gFile.close()