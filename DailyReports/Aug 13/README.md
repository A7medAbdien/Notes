# Sat, 13 Aug

1. Disable filtering (DONE)
2. Manager sees the Dashboard as a default rather than Kanban view (UNAPPLICABLE)

## Disable Default filtering, 'My Pipeline'

Edit "Window Action">"Context"

```py
{'default_type': 'opportunity','search_default_assigned_to_me': 1}
#to
{'default_type': 'opportunity'}
```

## Manager sees the Dashboard as a default rather than Kanban view

require code access

1. create a 'is_manager' method
2. use t-if to change the sequence value of the view

__IDK__ how to play with methods from model to Qweb that well
