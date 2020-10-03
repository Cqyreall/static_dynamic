### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:            # no second '=' dign
      return True
    else                          # no colon sign after else
      return False
   

  dif highest_card(self, card1 card2):       # 'def' spelt wrong, no comma between the card1 and card2
  if card1.value > card2.value:              # wrong indentation
    return card                              # Card undefined
  else:                                      # wrong indentation                   
    return card2
  


def cards_total(self, cards):
  total                                   # total does not equal anything
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
