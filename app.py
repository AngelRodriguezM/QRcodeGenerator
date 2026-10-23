from reactpy import component, html, run
import index

@component
def App():
    return index.indexApp()

run(App)