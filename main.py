from game.entitys.events import Event
from game.game import Game

# fullgame.main()
game: Game = Game()
pl = game.new_lab()
ro = game.buy_room(pl.get_uuid())[1]
game.buy_staff(pl.get_uuid(), ro.get_uuid(), "lab_assistant")
ro = game.buy_room(pl.get_uuid())
game.buy_staff(pl.get_uuid(), ro.get_uuid(), "lab_assistant")
game.buy_room(pl.get_uuid())
Event.action17(pl)
# trade = TradeReq(pl2, [{"type": "equipment", "data": eq2.get_uuid()}, {"type": "room", "data": ro2.get_uuid()}],
# [{"type":| "money", "data": 5}]) trade.accept(pl)
pass
