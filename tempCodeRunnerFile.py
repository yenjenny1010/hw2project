def keepgoing():
    stopmusic()
    play()
    global running
    if running ==True:
        stopmusic()
        play()
    running = True
    run()