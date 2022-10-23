## Triviale Komprimierung

Weniger Platz => effizient / monitär Sparsamer.

Wenn die Anzahl möglicher Werte, die ein Typ darstellen soll, kleiner ist als die Anzahl
der Werte, die mithilfe der zur Speicherung verwendeten Bits dargestellt werden kann, 
ist es wahrscheinlich möglich, diesen Typ effizienter zu Speichern.

Bsp die Nukleotide, die in der DNA ein Gen bilden.

Nukleotide: A, C, G oder T.

Wird das Gen als String gespeichert, entspricht das eine Sammlung von Unicode Zeichen mit
einer Bitbreite von 16bit. Vier werde benötigen aber nur 2bit zur Speicherung.

Bsp; 

Value   Wert        komprimierter Wert
A   =>  0110 0001 => 00
C   =>  0110 0011 => 01
G   =>  0110 0111 => 10
T   =>  0111 0100 => 11

So kann as der Folge - ACCGT folgende Bit kombination erstellt werden.
Normal: 0110 0001 0110 0011 0110 0011 0110 0111 0111 0100 44bit
Komprimiert : 00 01 01 10 11 10bit

Einsparung: 100 - (10/44 * 100) = 77.3%

