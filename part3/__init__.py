import warnings
import inspect
import ipywidgets as widgets

def show(object):
    def getvalue(object):
        return str(object)
    def gettype(object):
        return str(type(object))
    def getattributes(object):
        return "\n".join(dir(object))
    topics = [getvalue, gettype, getattributes, inspect.getdoc, inspect.getsource, inspect.getabsfile]
    children = []
    titles = []
    for topic in topics:
        try:
            content = topic(object)
            if len(content) > 0:
                if len(content) >= 80:
                    area = widgets.Textarea(content, layout=widgets.Layout(width="100%", height="20em"))
                else:
                    area = widgets.Text(content, layout=widgets.Layout(width="100%"))
                children.append(area)
                titles.append(topic.__name__)
        except TypeError:
            pass
    pane = widgets.Tab(children)
    for i,title in enumerate(titles):
        pane.set_title(i, title)
    display(pane)