from csv import reader

from os.path import exists
from discapp.models import DiscsData


def accordion_data():
    discs = DiscsData.objects.all()
    discnames = []
    
    def render_card_body(i):
        for i in discs:
            i = i.name
            
            return f'<h2>{i}</h2>'

    def card_content(i, active):
        card = dict(id=i, title=f'Disc {i + 1}', body=render_card_body(i))
        if i == active:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    return [card_content(i, 0) for i in range(4)]

def card_data(title="Card", body="text", color='bg-primary', width='col-lg-12'):
    
    return dict(title=title, body=body, color=color, width=width)


def cards_data():
    return [
                card_data("Disc One", "Innova TeeDevil \n This is one of the msot challenging discs to use, due to the amount of spin required to get a decent throw. However,  it has grown to be one of my most used discs in my bag."),
                card_data("Disc Two", "MVP Inertia \n This is one of the newer discs in my bag and it is one of the only discs I will purchase again after losing one. I feel it is a must have in any player's bag. It can be controlled very easily by any intermediate player and is always reliable in any wind conditions.",  "bg-warning", 'col-lg-4'),
                card_data("Disc Three", "Innova Beast \n This was the first disc I ever bought for myself and I still have the original disc. However, I have lost many of these - except for the original of course - as a result of how much I used it.", "bg-success", 'col-lg-4'),
                card_data("Disc Four", "MVP Skullboy \n As a putter, there's not really much to it. But the unique design on the top as well as its durability has made it one of my most utilized putters. It is even reliable for short distance drives!",   "bg-danger",  'col-lg-4'),
            ]



def table_data(path):
    return [row[:5] for row in reader(open(path))]


def tabs_data():

    def options(i, tab, selected):
        if selected:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='active', show='show', selected='true')
        else:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='', show='', selected='false')
    
    def set_options(tabs):
        return [options(i, tab, i == 2) for i, tab in enumerate(tabs)]
    
    return set_options(cards_data())