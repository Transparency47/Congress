# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4551
- Title: Restoring Overtime Pay Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4551
- Origin chamber: Senate
- Introduced date: 2026-05-18
- Update date: 2026-05-29T07:38:44Z
- Update date including text: 2026-05-29T07:38:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-18: Introduced in Senate
- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-05-18: Introduced in Senate

## Actions

- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-18",
    "latestAction": {
      "actionDate": "2026-05-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4551",
    "number": "4551",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Restoring Overtime Pay Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T07:38:44Z",
    "updateDateIncludingText": "2026-05-29T07:38:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-18",
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
          "date": "2026-05-18T20:08:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NY"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "WI"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "WA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "RI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "PA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "WA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "AZ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "OR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "RI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NM"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "DE"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4551is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4551\nIN THE SENATE OF THE UNITED STATES\nMay 18, 2026 Mr. Sanders (for himself, Mr. Schumer , Mr. Padilla , Mr. Schatz , Ms. Duckworth , Ms. Warren , Ms. Baldwin , Mrs. Murray , Mr. Markey , Mr. Whitehouse , Mr. Booker , Mr. Blumenthal , Mr. Fetterman , Ms. Cantwell , Mr. Murphy , Mr. Gallego , Mr. Wyden , Mr. Merkley , Mr. Durbin , Mr. Welch , Ms. Hirono , Mr. Kim , Ms. Alsobrooks , Mr. Reed , Mr. Luj\u00e1n , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to establish a minimum salary threshold for bona fide executive, administrative, and professional employees exempt from Federal overtime compensation requirements, and automatically update such threshold each year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Overtime Pay Act of 2026 .\n#### 2. Minimum salary threshold for bona fide executive, administrative, and professional employees exempt from Federal overtime compensation requirements\n##### (a) In general\nSection 13 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 213 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby inserting subsection (k) and after subject to ; and\n**(B)**\nby inserting (except as provided under subsection (k)(2)(C)) after Administrative Procedure Act ; and\n**(2)**\nby adding at the end the following:\n(k) Minimum salary threshold (1) In general Beginning on the effective date of the Restoring Overtime Pay Act of 2026 , the Secretary shall require that an employee described in subsection (a)(1), as a requirement for exemption under such subsection, be compensated on a salary basis, or equivalent fee basis, within the meaning of such terms in subpart G of part 541 of title 29, Code of Federal Regulations (or any successor regulation), at a rate per week that is not less than the weekly rate of the applicable annualized salary threshold under paragraph (2). (2) Salary threshold (A) In general Subject to subparagraphs (B) and (C), the applicable annualized salary threshold shall be\u2014 (i) $45,000, beginning on the effective date of the Restoring Overtime Pay Act of 2026 ; (ii) $55,000, beginning on January 1, 2027; (iii) $65,000, beginning on January 1, 2028; (iv) $75,000, beginning on January 1, 2029; and (v) beginning on January 1, 2030, an annualized amount that is equal to the rate of the 55th percentile of weekly earnings of full-time salaried workers nationally, as determined by the Bureau of Labor Statistics based on data from the second quarter of 2029. (B) Increased threshold The Secretary may establish, through notice and comment rulemaking under section 553 of title 5, United States Code, a salary threshold that is a rate that\u2014 (i) is greater than the applicable annualized salary threshold under subparagraph (A); and (ii) is calculated based on a data set and methodology established by the Secretary that are capable of being updated in accordance with subparagraph (C). (C) Automatic updates (i) In general Not later than 1 year after the salary threshold first takes effect under subparagraph (A)(v), and annually thereafter, or, in the case in which the Secretary establishes an increased salary threshold under subparagraph (B), annually after establishing such increased salary threshold, the Secretary shall update the rate of the salary threshold in effect under subparagraph (A)(v) or (B), as applicable, so that such rate is equal to\u2014 (I) in the case in which the Secretary does not establish an increased salary threshold under subparagraph (B), the 55th percentile of weekly earnings of full-time salaried workers nationally, as determined by the Bureau of Labor Statistics based on data from the second quarter of the calendar year preceding the calendar year in which such updated amount is to take effect; and (II) in the case in which the Secretary establishes an increased salary threshold under subparagraph (B), the greater of\u2014 (aa) the 55th percentile described in subclause (I); and (bb) the increased salary threshold established under subparagraph (B), as updated in accordance with the data set and methodology established by the Secretary under subparagraph (B)(ii). (ii) Nonapplicability of rulemaking Section 553 of title 5, United States Code, shall not apply to any update described in this subparagraph. (D) Notice requirement Not later than 60 days before a revised salary threshold under this paragraph takes effect, the Secretary shall publish a notice announcing the amount in the Federal Register and on the internet website of the Department of Labor. .\n##### (b) Publication of earnings\nNot later than 21 days after the end of each calendar quarter, the Bureau of Labor Statistics shall publish on its public website, for each week of such quarter, data on the weekly earnings of full-time salaried workers by census region (as designated by the Bureau of the Census).\n#### 3. Nonexempt duties limit for bona fide executive, administrative, or professional employees\nSection 13(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 213(a)(1) ), as amended in section 2(a)(1), is further amended\u2014\n**(1)**\nby striking of a retail or service establishment shall not and inserting shall ;\n**(2)**\nby striking because of and all that follows through administrative activities, ;\n**(3)**\nby striking less than 40 and inserting not less than 20 ; and\n**(4)**\nby striking such activities and inserting activities not directly or closely related to the performance of executive or administrative activities .\n#### 4. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the first day of the third month that begins after the date of enactment of this Act.",
      "versionDate": "2026-05-18",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4551is.xml"
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
      "title": "Restoring Overtime Pay Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:38:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Overtime Pay Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:38:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Labor Standards Act of 1938 to establish a minimum salary threshold for bona fide executive, administrative, and professional employees exempt from Federal overtime compensation requirements, and automatically update such threshold each year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:33:45Z"
    }
  ]
}
```
