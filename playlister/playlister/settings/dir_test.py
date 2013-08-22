from os.path import abspath, dirname, basename

print '__file__: ' + __file__
print 'abspath(__file__): ' + abspath(__file__)
print 'dirname(abspath(__file__)): ' + dirname(abspath(__file__))
print 'dirname(dirname(abspath(__file__))): ' + dirname(dirname(abspath(__file__)))
print 'dirname(dirname(dirname(abspath(__file__)))): ' + dirname(dirname(dirname(abspath(__file__))))
print 'basename(dirname(dirname(abspath(__file__)))): ' + basename(dirname(dirname(abspath(__file__))))

