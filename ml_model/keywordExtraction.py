from rake import rake

__author__ = 'revanurambareesh'


def rakeUP(inputFile):
    rake_object = rake.Rake("ml_model/SmartStoplist.txt", 5, 1, 3)
    sample_file = open(inputFile, 'r')
    text = sample_file.read()
    keywords = rake_object.run(text)

    return keywords
