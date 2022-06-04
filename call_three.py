from json import load
from re import A
import os
import sys
sys.path.append('../')
from abehiroshi_time import loading_time
from py_weather import weather
from youtube_py import upgrade_hololive_subscriber
from youtube_py import upgrade_hololive_videocount

#それぞれのディレクトリに移動する
os.chdir('../')
os.chdir('py_weather')
print('weather running')
weather.main()
os.chdir('../')
os.chdir('youtube_py')
print('upgrade_hololive_subscriber running')
upgrade_hololive_subscriber.main()
print('upgrade_hololive_videocount running')
upgrade_hololive_videocount.main()
os.chdir('../')
os.chdir('abehiroshi_time')
print('loading_time running')
loading_time.main()
os.chdir('../')
print('all runned')
