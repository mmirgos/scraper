# scraper
## Etap 1 - Pobranie składowych pojedynczej opinii o konkretnym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
1. Pobranie kodu pojedynczej strony z opiniami o produkcie
2. Analiza struktury kodu pojedynczej opinii

| Składowa                  | Selektor CSS                                                       | Nazwa zmiennej  | Typ danych      |
|:--------------------------|:-------------------------------------------------------------------|:----------------|:----------------|
| Opinia                    | div.js_product-review                                              | review          |                 |
| Identyfikator opinii      | ["data-entry-id"]                                                  | review_id       |                 |
| Autor                     | span.user-post__author-name                                        | author          |                 |
| Rekomendacja              | span.user-post__author-recomendation                               | rec             |                 |
| Liczba gwiazdek           | span.user-post__score-count                                        | stars           |                 |
| Treść opinii              | div.user-post__text                                                | content         |                 |
| Lista zalet               | div.review-feature__title--positives ~ review-feature__item        | pros            |                 |
| Lista wad                 | div.review-feature__title--negatives ~ review-feature__item        | cons            |                 |
| Dla ilu osób przydatna    | button.vote-yes["data-total-vote"]                                 | useful          |                 |
| Dla ilu osób nieprzydatna | button.vote-no["data-total-vote"]                                  | useless         |                 |
| Czy potwierdzona zakupem  | div.review-pz                                                      | purchased       |                 |
| Data wystawienia opinii   | span.user-post__published > time:nth-child(1)["datetime"]          | review_date     |                 |
| Data zakupu produktu      | span.user-post__published > time:nth-child(2)["datetime"]          | purchase_date   |                 |
