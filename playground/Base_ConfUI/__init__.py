import configparser

cf = configparser.ConfigParser()
#cf.read('app.settings')

cf.add_section('APPLICATION')
cf['APPLICATION']['lang'] = "en"

cf.write(open('app.settings','w'))