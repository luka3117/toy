\score {
  \new Staff <<
    \new Voice \relative c''' {
      \set midiInstrument = #"flute"
      \voiceOne
      \key d \minor
      \time 2/4
      r2 g-"Flute" ~
      a fis ~
      fis4 g8 fis e2 ~
      e4 d8 cis d2
    }
  >>
  \layout { }
  \midi {
    \context {
      \Staff
      \remove "Staff_performer"
    }

    \tempo 2 = 72
  }
}
