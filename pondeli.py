from datetime import date
import unittest

#konstanty pro navraceni kodu
MISS = -1 #nejake obdobi chybi
OK = 0
OVER = 1 #nejake obdobi je fakturovano navic


#testovani, vola se napr pomoci: python3 -m unittest pondeli.py
#manual viz https://docs.python.org/3/library/unittest.html
class TestKontrolaPausaly(unittest.TestCase):
  def test_porovnani_terminu(self):
    """Test porovnani terminu.
    """
    termin_pripojen = (
      #od                 do
      (date(2025, 4,  3), date(2025, 4, 12)),
      (date(2025, 4, 28), date(2025, 5, 18))
    )
    termin_fakturovano = (
      #od                 do
      (date(2025, 4, 17), date(2025, 5, 16)),
    )

    self.assertEqual(
      porovnej_terminy(termin_pripojen, termin_fakturovano),
      (MISS,
        ( #od                 do
          (date(2025, 4,  3), date(2025, 4, 12)),
          (date(2025, 5, 17), date(2025, 5, 18))
        )
      )
    )

  def test_vytvor_terminy(self):
    """Test vytvoreni terminu z datumu.
    """
    datumy = (
      date(2025, 4,  3),
      date(2025, 4,  4),
      date(2025, 4,  5),
      date(2025, 4,  6),
      date(2025, 4,  7),
      date(2025, 4,  8),
      date(2025, 4,  9),
      date(2025, 4, 10),
      date(2025, 4, 11),
      date(2025, 4, 12),
      date(2025, 5, 17),
      date(2025, 5, 18),
    )

    self.assertEqual(
      vytvor_terminy(datumy),
        ( #od                 do
          (date(2025, 4,  3), date(2025, 4, 12)),
          (date(2025, 5, 17), date(2025, 5, 18))
        )
    )


def vytvor_terminy(datumy, max_mezera=1):
    """Ze zadaných dat vytvoří spojité termíny (intervaly).
    @param datumy (tuple of date): Jednotlivé datumy.
    @param max_mezera (int): Největší povolená mezera (ve dnech) mezi daty, která se ještě spojují.
    @return (tuple of (date, date)): Souvislé termíny.
    """

    terminy = []

    start = datumy[0]
    end = datumy[0]

    for d in datumy[1:]:
        if d <= end + timedelta(days=max_mezera):
            end = d
        else:
            terminy.append((start, end))
            start = end = d

    terminy.append((start, end))
    return tuple(terminy)


  
  #TODO naprogramovat
#  return (
    #od                 do
 #   (date(2025, 4,  3), date(2025, 4, 12)),
  #  (date(2025, 5, 17), date(2025, 5, 18))
  #)


from datetime import date, timedelta

MISS = -1
OK = 0
OVER = 1

def porovnej_terminy(termin_pripojen, termin_fakturovano):
    """
    Porovna zadane terminy. Vychazi z termin_pripojen, zjistuje jestli v termin_fakturovano neco chybi, pripadne prebyva.
    Nejdriv kontroluje jestli neco chybi, pak az prebyva.

    @param termin_pripojen (tuple of (date, date)): Terminy pripojeni.
    @param termin_fakturovano (tuple of (date, date)): Vyfakturovane terminy.
    @return (tuple): (stav, (terminy))
        stav (int): MISS | OK | OVER
        terminy (tuple of (date,date)): Terminy od-do, s timto stavem.
    """

    def odecti(interval, odecti_intervals):
        """Vrátí části z `interval`, které nejsou pokryty žádným z `odecti_intervals`."""
        aktualni_od, aktualni_do = interval

        casy = [(aktualni_od, aktualni_do)]

        for od_f, do_f in sorted(odecti_intervals):
            nove = []
            for od, do in casy:
                if do < od_f or od > do_f:
                    nove.append((od, do))
                else:
                    if od < od_f:
                        nove.append((od, od_f - timedelta(days=1)))
                    if do > do_f:
                        nove.append((do_f + timedelta(days=1), do))
            casy = nove

        return casy

    chybi = []
    for od_p, do_p in termin_pripojen:
        chybici_useky = odecti((od_p, do_p), termin_fakturovano)
        chybi.extend(chybici_useky)

    if chybi:
        return MISS, tuple(chybi)


    prebyva = []
    for od_f, do_f in termin_fakturovano:
        prebytecne_useky = odecti((od_f, do_f), termin_pripojen)
        prebyva.extend(prebytecne_useky)

    if prebyva:
        return OVER, tuple(prebyva)


    return OK, tuple(termin_fakturovano)








#  #TODO naprogramovat
#  return MISS, (
#    #od                 do
#    (date(2025, 4,  3), date(2025, 4, 12)),
#    (date(2025, 5, 17), date(2025, 5, 18))
#  )


if __name__ == "__main__":
  # vytvor_terminy
  datumy = (
    date(2025, 4,  3),
    date(2025, 4,  4),
    date(2025, 4,  5),
    date(2025, 4,  6),
    date(2025, 4,  7),
    date(2025, 4,  8),
    date(2025, 4,  9),
    date(2025, 4, 10),
    date(2025, 4, 11),
    date(2025, 4, 12),
    date(2025, 5, 17),
    date(2025, 5, 18),
  )

  vysl = vytvor_terminy(datumy)
  print(vysl)

  # porovnej_terminy
  termin_pripojen = (
    #od                 do
    (date(2025, 4,  3), date(2025, 4, 12)),
    (date(2025, 4, 28), date(2025, 5, 18))
  )
  termin_fakturovano = (
    #od                 do
    (date(2025, 4, 17), date(2025, 5, 16)),
  )

  vysl = porovnej_terminy(termin_pripojen, termin_fakturovano)
  print(vysl)
