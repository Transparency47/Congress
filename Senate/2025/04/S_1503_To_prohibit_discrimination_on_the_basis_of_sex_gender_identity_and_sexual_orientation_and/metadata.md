# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1503
- Title: Equality Act
- Congress: 119
- Bill type: S
- Bill number: 1503
- Origin chamber: Senate
- Introduced date: 2025-04-29
- Update date: 2026-04-29T17:04:54Z
- Update date including text: 2026-04-29T17:04:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in Senate
- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-29: Introduced in Senate

## Actions

- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1503",
    "number": "1503",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Equality Act",
    "type": "S",
    "updateDate": "2026-04-29T17:04:54Z",
    "updateDateIncludingText": "2026-04-29T17:04:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-04-29T15:52:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-29",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1503is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1503\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2025 Mr. Merkley (for himself, Ms. Baldwin , Mr. Booker , Ms. Alsobrooks , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Murphy , Mrs. Murray , Mr. Ossoff , Mr. Padilla , Mr. Peters , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mr. Schumer , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit discrimination on the basis of sex, gender identity, and sexual orientation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Equality Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nDiscrimination can occur on the basis of the sex, sexual orientation, gender identity, pregnancy, childbirth, or a related medical condition of an individual, as well as because of sex-based stereotypes. Each of these factors alone can serve as the basis for discrimination, and each is a form of sex discrimination.\n**(2)**\nA single instance of discrimination may have more than one basis. For example, discrimination against a married same-sex couple could be based on the sex stereotype that marriage should only be between heterosexual couples, the sexual orientation of the two individuals in the couple, or both. In addition, some persons are subjected to discrimination based on a combination or the intersection of multiple protected characteristics. Discrimination against a pregnant lesbian could be based on her sex, her sexual orientation, her pregnancy, or on the basis of multiple factors.\n**(3)**\nLesbian, gay, bisexual, transgender, and queer (referred to as LGBTQ ) people commonly experience discrimination in securing access to public accommodations\u2014including restaurants, senior centers, stores, places of or establishments that provide entertainment, health care facilities, shelters, government offices, youth service providers including adoption and foster care providers, and transportation. Forms of discrimination include the exclusion and denial of entry, unequal or unfair treatment, harassment, and violence. This discrimination prevents the full participation of LGBTQ people in society and disrupts the free flow of commerce.\n**(4)**\nWomen also have faced discrimination in many establishments such as stores and restaurants, and places or establishments that provide other goods or services, such as entertainment or transportation, including sexual harassment, differential pricing for substantially similar products and services, and denial of services because they are pregnant or breastfeeding.\n**(5)**\nMany employers already and continue to take proactive steps, beyond those required by some States and localities, to ensure they are fostering positive and respectful cultures for all employees. Many places of public accommodation also recognize the economic imperative to offer goods and services to as many consumers as possible.\n**(6)**\nRegular and ongoing discrimination against LGBTQ people, as well as women, in accessing public accommodations contributes to negative social and economic outcomes, and in the case of public accommodations operated by State and local governments, abridges individuals\u2019 constitutional rights.\n**(7)**\nThe discredited practice known as conversion therapy is a form of discrimination that harms LGBTQ people by undermining individuals\u2019 sense of self worth, increasing suicide ideation and substance abuse, exacerbating family conflict, and contributing to second-class status.\n**(8)**\nBoth LGBTQ people and women face widespread discrimination in employment and various services, including by entities that receive Federal financial assistance. Such discrimination\u2014\n**(A)**\nis particularly troubling and inappropriate for programs and services funded wholly or in part by the Federal Government;\n**(B)**\nundermines national progress toward equal treatment regardless of sex, sexual orientation, or gender identity; and\n**(C)**\nis inconsistent with the constitutional principle of equal protection under the Fourteenth Amendment to the Constitution of the United States.\n**(9)**\nFederal courts have widely recognized that, in enacting the Civil Rights Act of 1964, Congress validly invoked its powers under the Fourteenth Amendment to provide a full range of remedies in response to persistent, widespread, and pervasive discrimination by both private and government actors.\n**(10)**\nDiscrimination by State and local governments on the basis of sexual orientation or gender identity in employment, housing, and public accommodations, and in programs and activities receiving Federal financial assistance, violates the Equal Protection Clause of the Fourteenth Amendment to the Constitution of the United States. In many circumstances, such discrimination also violates other constitutional rights such as those of liberty and privacy under the due process clause of the Fourteenth Amendment.\n**(11)**\nIndividuals who are LGBTQ, or are perceived to be LGBTQ, have been subjected to a history and pattern of persistent, widespread, and pervasive discrimination on the bases of sexual orientation and gender identity by both private sector and Federal, State, and local government actors, including in employment, housing, and public accommodations, and in programs and activities receiving Federal financial assistance. This discrimination inflicts a range of tangible and intangible harms, sometimes even including serious physical injury or death. An explicit and comprehensive national solution is needed to address this discrimination, including the full range of remedies available under the Civil Rights Act of 1964.\n**(12)**\nDiscrimination based on sexual orientation includes discrimination based on an individual\u2019s actual or perceived romantic, emotional, physical, or sexual attraction to other persons, or lack thereof, on the basis of gender. LGBTQ people, including gender nonbinary people, also commonly experience discrimination because of sex-based stereotypes. Many people are subjected to discrimination because of others\u2019 perceptions or beliefs regarding their sexual orientation. Even if these perceptions are incorrect, the identity imputed by others forms the basis of discrimination.\n**(13)**\nNumerous provisions of Federal law expressly prohibit discrimination on the basis of sex, and Federal courts and agencies have correctly interpreted these prohibitions on sex discrimination to include discrimination based on sexual orientation, gender identity, and sex stereotypes. In particular, the Supreme Court of the United States correctly held in Bostock v. Clayton County, 140 S. Ct. 1731 (2020) that the prohibition on employment discrimination because of sex under title VII of the Civil Rights Act of 1964 inherently includes discrimination because of sexual orientation or transgender status.\n**(14)**\nThis Act makes explicit that existing Federal statutes prohibiting sex discrimination in employment (including in access to benefits), healthcare, housing, education, credit, and jury service also prohibit sexual orientation and gender identity discrimination.\n**(15)**\nLGBTQ people often face discrimination when seeking to rent or purchase housing, as well as in every other aspect of obtaining and maintaining housing. LGBTQ people in same-sex relationships are often discriminated against when two names associated with one gender appear on a housing application, and transgender people often encounter discrimination when credit checks or inquiries reveal a former name.\n**(16)**\nNational surveys, including a study commissioned by the Department of Housing and Urban Development, show that housing discrimination against LGBTQ people is very prevalent. For instance, when same-sex couples inquire about housing that is available for rent, they are less likely to receive positive responses from landlords. A national matched-pair testing investigation found that nearly one-half of same-sex couples had encountered adverse, differential treatment when seeking elder housing. According to other studies, transgender people have half the homeownership rate of non-transgender people and about 1 in 5 transgender people experience homelessness. Another survey found that 82 percent of gender nonbinary people experiencing homelessness lacked access to shelter.\n**(17)**\nAs a result of the absence of explicit prohibitions against discrimination on the basis of sexual orientation and gender identity, credit applicants who are LGBTQ, or are perceived to be LGBTQ, have unequal opportunities to establish credit. LGBTQ people can experience being denied a mortgage, credit card, student loan, or many other types of credit simply because of their sexual orientation or gender identity.\n**(18)**\nNumerous studies demonstrate that LGBTQ people, especially transgender people and women, are economically disadvantaged and at a higher risk for poverty compared with other groups of people. For example, the poverty rate for older women in same-sex couples is twice that of older different-sex couples.\n**(19)**\nThe right to an impartial jury of one\u2019s peers and the reciprocal right to jury service are fundamental to the free and democratic system of justice in the United States and are based in the Bill of Rights. There is, however, an unfortunate and long-documented history in the United States of attorneys discriminating against LGBTQ individuals, or those perceived to be LGBTQ, in jury selection. Failure to bar peremptory challenges based on the actual or perceived sexual orientation or gender identity of an individual not only erodes a fundamental right, duty, and obligation of being a citizen of the United States, but also unfairly creates a second class of citizenship for LGBTQ victims, witnesses, plaintiffs, and defendants.\n**(20)**\nNumerous studies document the shortage of qualified and available homes for the approximately 424,000 youth in the child welfare system and the negative outcomes for the many youth who live in group care as opposed to a loving home or who age out of care without a permanent family placement. Although same-sex couples are 7 times more likely to foster or adopt than their different-sex counterparts, many child-placing agencies refuse to serve same-sex couples and LGBTQ individuals. This has resulted in a reduction of the pool of qualified and available homes for youth in the child welfare system who need placement on a temporary or permanent basis. It also sends a negative message about LGBTQ people to children and youth in the child welfare system about who is, and who is not, considered fit to be a parent. While the priority should be on providing the supports necessary to keep children with their families, when removal is required, barring discrimination in foster care and adoption will increase the number of homes available to foster children waiting for foster and adoptive families.\n**(21)**\nLGBTQ youth are overrepresented in the foster care system by at least a factor of two and report twice the rate of poor treatment while in care compared to their non-LGBTQ counterparts. LGBTQ youth in foster care have a higher average number of placements, higher likelihood of living in a group home, and higher rates of hospitalization for emotional reasons and of juvenile justice involvement than their non-LGBTQ peers because of the high level of bias and discrimination that they face and the difficulty of finding affirming foster placements. Further, due to their physical distance from friends and family, traumatic experiences, and potentially unstable living situations, all youth involved with child welfare services are at risk for being targeted by traffickers seeking to exploit children. Barring discrimination in child welfare services will ensure improved treatment and outcomes for LGBTQ foster children.\n**(22)**\nCourts consistently have found that the government has a compelling interest in preventing and remedying discrimination. For example, the Supreme Court of the United States found there to be a compelling government interest in eliminating sex discrimination in Board of Directors of Rotary International v. Rotary Club of Duarte, 481 U.S. 537, 549 (1987). Because discrimination based on sexual orientation or gender identity inherently is a form of sex discrimination, as held in Bostock v. Clayton County, 140 S. Ct. 1731 (2020), this Act furthers the compelling government interest in providing redress for the serious harms to mental and physical health, financial security and well-being, civic participation, freedom of movement and opportunity, personal dignity, and physical safety that result from discrimination. Consistent with the role nondiscrimination laws play in protecting lives and livelihoods, alleviating suffering, and improving individual and public health, the Supreme Court of the United States has long recognized, under the decision in Heart of Atlanta Motel, Inc. v. United States, 379 U.S. 241 (1964), that these laws also benefit society as a whole by ending the disruptive effect discrimination has on travel and commerce, and by creating a level field for all participants in a given sector.\n**(23)**\nAs with all prohibitions on invidious discrimination, this Act furthers the government\u2019s compelling interest in the least restrictive way because only by forbidding discrimination is it possible to avert or redress the harms described in this subsection.\n##### (b) Purpose\nIt is the purpose of this Act to expand as well as clarify, confirm and create greater consistency in the protections and remedies against discrimination on the basis of all covered characteristics and to provide guidance and notice to individuals, organizations, corporations, and agencies regarding their obligations under the law.\n#### 3. Public accommodations\n##### (a) Prohibition on discrimination or segregation in public accommodations\nSection 201 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a ) is amended\u2014\n**(1)**\nin subsection (a), by inserting sex (including sexual orientation and gender identity), before or national origin ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by striking stadium and all that follows and inserting stadium or other place of or establishment that provides exhibition, entertainment, recreation, exercise, amusement, public gathering, or public display; ;\n**(B)**\nby redesignating paragraph (4) as paragraph (6); and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) any establishment that provides a good, service, or program, including a store, shopping center, online retailer or service provider, salon, bank, gas station, food bank, service or care center, shelter, travel agency, or funeral parlor, or establishment that provides health care, accounting, or legal services; (5) any train service, bus service, car service, taxi service, airline service, station, depot, or other place of or establishment that provides transportation service; and .\n##### (b) Prohibition on discrimination or segregation under law\nSection 202 of such Act ( 42 U.S.C. 2000a\u20131 ) is amended by inserting sex (including sexual orientation and gender identity), before or national origin .\n##### (c) Rule of construction\nTitle II of such Act ( 42 U.S.C. 2000a et seq. ) is amended by adding at the end the following:\n208. Rule of construction A reference in this title to an establishment\u2014 (1) shall be construed to include an individual whose operations affect commerce and who is a provider of a good, service, or program; and (2) shall not be construed to be limited to a physical facility or place. .\n#### 4. Desegregation of public facilities\nSection 301(a) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000b(a) ) is amended by inserting sex (including sexual orientation and gender identity), before or national origin .\n#### 5. Desegregation of public education\n##### (a) Definitions\nSection 401(b) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000c(b) ) is amended by inserting (including sexual orientation and gender identity), before or national origin .\n##### (b) Civil actions by the Attorney General\nSection 407 of such Act ( 42 U.S.C. 2000c\u20136 ) is amended, in subsection (a)(2), by inserting (including sexual orientation and gender identity), before or national origin .\n##### (c) Classification and assignment\nSection 410 of such Act ( 42 U.S.C. 2000c\u20139 ) is amended by inserting (including sexual orientation and gender identity), before or national origin .\n#### 6. Federal funding\nSection 601 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d ) is amended by inserting sex (including sexual orientation and gender identity), before or national origin, .\n#### 7. Employment\n##### (a) Rules of construction\nTitle VII of the Civil Rights Act of 1964 is amended by inserting after section 701 ( 42 U.S.C. 2000e ) the following:\n701A. Rules of construction Section 1106 shall apply to this title except that for purposes of that application, a reference in that section to an unlawful practice shall be considered to be a reference to an unlawful employment practice . .\n##### (b) Unlawful employment practices\nSection 703 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20132 ) is amended\u2014\n**(1)**\nin the section header, by striking sex, and inserting sex (including sexual orientation and gender identity), ;\n**(2)**\nexcept in subsection (e), by striking sex, each place it appears and inserting sex (including sexual orientation and gender identity), ;\n**(3)**\nin subsection (e)(1), by striking enterprise, and inserting enterprise, if, in a situation in which sex is a bona fide occupational qualification, individuals are recognized as qualified in accordance with their gender identity, ; and\n**(4)**\nin subsection (h), by striking sex the second place it appears and inserting sex (including sexual orientation and gender identity), .\n##### (c) Other unlawful employment practices\nSection 704(b) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20133(b) ) is amended\u2014\n**(1)**\nby striking sex, the first place it appears and inserting sex (including sexual orientation and gender identity), ; and\n**(2)**\nby striking employment. and inserting employment, if, in a situation in which sex is a bona fide occupational qualification, individuals are recognized as qualified in accordance with their gender identity. .\n##### (d) Claims\nSection 706(g)(2)(A) of the Civil Rights Act of 1964 (2000e\u20135(g)(2)(A)) is amended by striking sex, and inserting sex (including sexual orientation and gender identity), .\n##### (e) Employment by Federal Government\nSection 717 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u201316 ) is amended\u2014\n**(1)**\nin subsection (a), by striking sex, and inserting sex (including sexual orientation and gender identity), ; and\n**(2)**\nin subsection (c), by striking sex and inserting sex (including sexual orientation and gender identity), .\n##### (f) Government Employee Rights Act of 1991\nThe Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316a et seq.) is amended\u2014\n**(1)**\nin section 301(b), by striking sex, and inserting sex (including sexual orientation and gender identity), ;\n**(2)**\nin section 302(a)(1), by striking sex, and inserting sex (including sexual orientation and gender identity), ; and\n**(3)**\nby adding at the end the following:\n305. Rules of construction and claims Sections 1101(b), 1106, and 1107 of the Civil Rights Act of 1964 shall apply to this title except that for purposes of that application, a reference in that section 1106 to race, color, religion, sex (including sexual orientation and gender identity), or national origin shall be considered to be a reference to race, color, religion, sex, sexual orientation, gender identity, national origin, age, or disability . .\n##### (g) Congressional Accountability Act of 1995\nThe Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ) is amended\u2014\n**(1)**\nin section 201(a)(1) ( 2 U.S.C. 1311(a)(1) ) by inserting (including sexual orientation and gender identity), before or national origin, ; and\n**(2)**\nby adding at the end of title II ( 42 U.S.C. 1311 et seq. ) the following:\n209. Rules of construction and claims Sections 1101(b), 1106, and 1107 of the Civil Rights Act of 1964 shall apply to section 201 (and remedial provisions of this Act related to section 201) except that for purposes of that application, a reference in that section 1106 to race, color, religion, sex (including sexual orientation and gender identity), or national origin shall be considered to be a reference to race, color, religion, sex (including sexual orientation and gender identity), national origin, age, or disability . .\n##### (h) Civil Service Reform Act of 1978\nChapter 23 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 2301(b)(2), by striking sex, and inserting sex (including sexual orientation and gender identity), ;\n**(2)**\nin section 2302\u2014\n**(A)**\nin subsection (b)(1)(A), by inserting (including sexual orientation and gender identity), before or national origin, ; and\n**(B)**\nin subsection (d)(1), by inserting (including sexual orientation and gender identity), before or national origin; ; and\n**(3)**\nby adding at the end the following:\n2307. Rules of construction and claims Sections 1101(b), 1106, and 1107 of the Civil Rights Act of 1964 shall apply to this chapter (and remedial provisions of this title related to this chapter) except that for purposes of that application, a reference in that section 1106 to race, color, religion, sex (including sexual orientation and gender identity), or national origin shall be considered to be a reference to race, color, religion, sex (including sexual orientation and gender identity), national origin, age, a handicapping condition, marital status, or political affiliation . .\n#### 8. Intervention\nSection 902 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000h\u20132 ) is amended by inserting (including sexual orientation and gender identity), before or national origin, .\n#### 9. Miscellaneous\nTitle XI of the Civil Rights Act of 1964 is amended\u2014\n**(1)**\nby redesignating sections 1101 through 1104 ( 42 U.S.C. 2000h et seq. ) and sections 1105 and 1106 ( 42 U.S.C. 2000h\u20135 , 2000h\u20136) as sections 1102 through 1105 and sections 1108 and 1109, respectively;\n**(2)**\nby inserting after the title heading the following:\n1101. Definitions and rules (a) Definitions In titles II, III, IV, VI, VII, and IX (referred to individually in sections 1106 and 1107 as a covered title ): (1) Race; color; religion; sex; sexual orientation; gender identity; national origin The term race , color , religion , sex (including sexual orientation and gender identity ), or national origin , used with respect to an individual, includes\u2014 (A) the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of another person with whom the individual is associated or has been associated; and (B) a perception or belief, even if inaccurate, concerning the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of the individual. (2) Gender identity The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth. (3) Including The term including means including, but not limited to, consistent with the term's standard meaning in Federal law. (4) Sex The term sex includes\u2014 (A) a sex stereotype; (B) pregnancy, childbirth, or a related medical condition; (C) sexual orientation or gender identity; and (D) sex characteristics, including intersex traits. (5) Sexual orientation The term sexual orientation means homosexuality, heterosexuality, or bisexuality. (b) Rules In a covered title referred to in subsection (a)\u2014 (1) (with respect to sex) pregnancy, childbirth, or a related medical condition shall not receive less favorable treatment than other physical conditions; and (2) (with respect to gender identity) an individual shall not be denied access to a shared facility, including a restroom, a locker room, and a dressing room, that is in accordance with the individual's gender identity. ; and\n**(3)**\nby inserting after section 1105 the following:\n1106. Rules of construction (a) Sex Nothing in section 1101 or the provisions of a covered title incorporating a term defined or a rule specified in that section shall be construed\u2014 (1) to limit the protection against an unlawful practice on the basis of pregnancy, childbirth, or a related medical condition provided by section 701(k); or (2) to limit the protection against an unlawful practice on the basis of sex available under any provision of Federal law other than that covered title, prohibiting a practice on the basis of sex. (b) Claims and remedies not precluded Nothing in section 1101 or a covered title shall be construed to limit the claims or remedies available to any individual for an unlawful practice on the basis of race, color, religion, sex (including sexual orientation and gender identity), or national origin including claims brought pursuant to section 1979 or 1980 of the Revised Statutes ( 42 U.S.C. 1983 , 1985) or any other law, including a Federal law amended by the Equality Act, regulation, or policy. (c) No negative inference Nothing in section 1101 or a covered title shall be construed to support any inference that any Federal law prohibiting a practice on the basis of sex does not prohibit discrimination on the basis of pregnancy, childbirth, or a related medical condition, sexual orientation, gender identity, or a sex stereotype. 1107. Claims The Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ) shall not provide a claim concerning, or a defense to a claim under, a covered title, or provide a basis for challenging the application or enforcement of a covered title. .\n#### 10. Housing\n##### (a) Fair Housing Act\nThe Fair Housing Act ( 42 U.S.C. 3601 et seq. ) is amended\u2014\n**(1)**\nin section 802 ( 42 U.S.C. 3602 ), by adding at the end the following:\n(p) Gender identity , sex , and sexual orientation have the meanings given those terms in section 1101(a) of the Civil Rights Act of 1964. (q) Race , color , religion , sex (including sexual orientation and gender identity ), handicap , familial status , or national origin , used with respect to an individual, includes\u2014 (1) the race, color, religion, sex (including sexual orientation and gender identity), handicap, familial status, or national origin, respectively, of another person with whom the individual is associated or has been associated; and (2) a perception or belief, even if inaccurate, concerning the race, color, religion, sex (including sexual orientation and gender identity), handicap, familial status, or national origin, respectively, of the individual. ;\n**(2)**\nin section 804 ( 42 U.S.C. 3604 ), by inserting (including sexual orientation and gender identity), after sex, each place that term appears;\n**(3)**\nin section 805 ( 42 U.S.C. 3605 ), by inserting (including sexual orientation and gender identity), after sex, each place that term appears;\n**(4)**\nin section 806 ( 42 U.S.C. 3606 ), by inserting (including sexual orientation and gender identity), after sex, ;\n**(5)**\nin section 808(e)(6) ( 42 U.S.C. 3608(e)(6) ), by inserting (including sexual orientation and gender identity), after sex, ; and\n**(6)**\nby adding at the end the following:\n821. Rules of construction Sections 1101(b) and 1106 of the Civil Rights Act of 1964 shall apply to this title and section 901, except that for purposes of that application, a reference in that section 1101(b) or 1106 to a covered title shall be considered a reference to this title and section 901 . 822. Claims Section 1107 of the Civil Rights Act of 1964 shall apply to this title and section 901, except that for purposes of that application, a reference in that section 1107 to a covered title shall be considered a reference to this title and section 901 . .\n##### (b) Prevention of intimidation in fair housing cases\nSection 901 of the Civil Rights Act of 1968 ( 42 U.S.C. 3631 ) is amended by inserting (including sexual orientation (as such term is defined in section 802 of this Act) and gender identity (as such term is defined in section 802 of this Act)), after sex, each place that term appears.\n#### 11. Equal credit opportunity\n##### (a) Prohibited discrimination\nSection 701(a)(1) of the Equal Credit Opportunity Act ( 15 U.S.C. 1691(a)(1) ) is amended by inserting (including sexual orientation and gender identity), after sex .\n##### (b) Definitions\nSection 702 of the Equal Credit Opportunity Act ( 15 U.S.C. 1691a ) is amended\u2014\n**(1)**\nby redesignating subsections (f) and (g) as subsections (h) and (i), respectively;\n**(2)**\nby inserting after subsection (e) the following:\n(f) The terms gender identity , sex , and sexual orientation have the meanings given those terms in section 1101(a) of the Civil Rights Act of 1964. (g) The term race , color , religion , national origin , sex (including sexual orientation and gender identity ), marital status , or age , used with respect to an individual, includes\u2014 (1) the race, color, religion, national origin, sex (including sexual orientation and gender identity), marital status, or age, respectively, of another person with whom the individual is associated or has been associated; and (2) a perception or belief, even if inaccurate, concerning the race, color, religion, national origin, sex (including sexual orientation and gender identity), marital status, or age, respectively, of the individual. ; and\n**(3)**\nby adding at the end the following:\n(j) Sections 1101(b) and 1106 of the Civil Rights Act of 1964 shall apply to this title, except that for purposes of that application\u2014 (1) a reference in those sections to a covered title shall be considered a reference to this title ; and (2) paragraph (1) of such section 1101(b) shall apply with respect to all aspects of a credit transaction. .\n##### (c) Relation to State laws\nSection 705(a) of the Equal Credit Opportunity Act ( 15 U.S.C. 1691d(a) ) is amended by inserting (including sexual orientation and gender identity), after sex .\n##### (d) Civil liability\nSection 706 of the Equal Credit Opportunity Act ( 15 U.S.C. 1691e ) is amended by adding at the end the following:\n(l) Section 1107 of the Civil Rights Act of 1964 shall apply to this title, except that for purposes of that application, a reference in that section to a covered title shall be considered a reference to this title . .\n#### 12. Juries\n##### (a) In general\nChapter 121 of title 28, United States Code, is amended\u2014\n**(1)**\nin section 1862, by inserting (including sexual orientation and gender identity), after sex, ;\n**(2)**\nin section 1867(e), in the second sentence, by inserting (including sexual orientation and gender identity), after sex, ;\n**(3)**\nin section 1869\u2014\n**(A)**\nin subsection (j), by striking and at the end;\n**(B)**\nin subsection (k), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(l) gender identity , sex , and sexual orientation have the meanings given such terms under section 1101(a) of the Civil Rights Act of 1964; and (m) race , color , religion , sex (including sexual orientation and gender identity ), economic status , or national origin , used with respect to an individual, includes\u2014 (1) the race, color, religion, sex (including sexual orientation and gender identity), economic status, or national origin, respectively, of another person with whom the individual is associated or has been associated; and (2) a perception or belief, even if inaccurate, concerning the race, color, religion, sex (including sexual orientation and gender identity), economic status, or national origin, respectively, of the individual. ; and\n**(4)**\nby adding at the end the following:\n1879. Rules of construction and claims Sections 1101(b), 1106, and 1107 of the Civil Rights Act of 1964 shall apply to this chapter, except that for purposes of that application, a reference in those sections to a covered title shall be considered a reference to this chapter . .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 121 of title 28, United States Code, is amended by adding at the end the following:\n1879. Rules of construction and claims. .",
      "versionDate": "2025-04-29",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-09",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7005",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Customer Non-Discrimination Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Education and Workforce, Financial Services, House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "15",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equality Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-05-21T13:07:28Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1503is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Equality Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equality Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit discrimination on the basis of sex, gender identity, and sexual orientation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:32Z"
    }
  ]
}
```
