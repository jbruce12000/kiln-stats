import os
import re
import sys

def addpdf(inpdf,outpdf):
    '''uses pdftk to add a page at the end of a pdf file.
    if outpdf does not exist, it is created, otherwise the page is appended.
    '''
    if os.path.exists(outpdf):
        cmd = "mv -f '%s' temp.pdf" % (outpdf)
        os.system(cmd)
        cmd = "pdftk A=temp.pdf B='%s' cat A1-end B output %s" % (inpdf,outpdf)
        os.system(cmd)
    else:
        cmd = "pdftk B='%s' cat B output %s" % (inpdf,outpdf)
        os.system(cmd)

    if os.path.exists("temp.pdf"):
        os.unlink("temp.pdf")

    print ("added '%s' to %s" % (inpdf,outpdf))
    
def formatbookmark(title,level,page):
    if level < 1:
        level = 1

    # strip off the .pdf extension
    title = os.path.splitext(title)[0]
    title = re.sub('sort[a-z]\-','',title)

    bookmark = "BookmarkBegin\nBookmarkTitle: %s\nBookmarkLevel: %d\nBookmarkPageNumber: %s\n" % (title,level,page)
    return bookmark

def writebookmarks(bookmarks,outpdf):

    # write booksmarks to bookmarks.txt
    bookfile = open("bookmarks.txt", "w")
    bookfile.write(bookmarks)
    bookfile.close()

    # add bookmarks to output pdf file
    cmd = "mv -f '%s' temp.pdf" % (outpdf)
    os.system(cmd)
    cmd = "pdftk temp.pdf update_info bookmarks.txt output '%s'" % (outpdf)
    os.system(cmd)

    # clean up
    os.unlink("temp.pdf")
    os.unlink("bookmarks.txt")

walk_dir = sys.argv[1]
outpdf = os.path.join(walk_dir, "final.pdf")

bookmarks = ""
page=0

for root, subdirs, files in os.walk(walk_dir):
    depth = root[len(walk_dir):].count(os.sep)

    # need to grab last directory at end of path
    last = root.split(os.sep)[-1]
    if depth > 0:
        bookmarks = bookmarks + formatbookmark(last,depth,-1) 

    subdirs.sort()
    files.sort()

    for filename in files:
        file_path = os.path.join(root, filename)
        #print('\t- file %s (full path: %s)(depth: %d)' % (filename, file_path, depth))

        if filename.endswith(".pdf"):
            addpdf(file_path,outpdf)
            page = page + 1
            bookmarks = bookmarks + formatbookmark(filename,depth+1,page)

writebookmarks(bookmarks,outpdf)
