import multiprocessing

for car in ('Car1', 'Car2', 'Car3',\
            'Car4', 'Car5', 'Car6',\
            'Car7', 'Car8', 'Car9', 'Car10'):
    p = multiprocessing.Process(target=lambda:__import__(car))
    p.start()
