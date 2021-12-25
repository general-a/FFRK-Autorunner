from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class RedCombatPainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(3, 'COMBAT', 'redcombat.png', location)

    
if __name__ == '__main__':
    t = RedCombatPainting((1,1))
    print(t.startEvent())
    print(t.nextAction())
    print(t.nextAction())
    print(t.nextAction())
    print(t.nextAction())
    print(t.nextAction())
    print(t.nextAction())
        
