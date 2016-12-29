import rake
import operator

rake_object = rake.Rake("SmartStoplist.txt", 5, 3, 4)
sample_file = open("data/docs/fao_test/w2167e.txt", 'r')
text = sample_file.read()
keywords = rake_object.run(text)
print "Keywords:", keywords