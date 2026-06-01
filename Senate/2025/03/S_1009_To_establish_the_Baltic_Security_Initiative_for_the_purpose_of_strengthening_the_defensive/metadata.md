# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1009
- Title: Baltic Security Initiative Act
- Congress: 119
- Bill type: S
- Bill number: 1009
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-06-11T11:03:16Z
- Update date including text: 2025-06-11T11:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S1715-1716)
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S1715-1716)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1009",
    "number": "1009",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Baltic Security Initiative Act",
    "type": "S",
    "updateDate": "2025-06-11T11:03:16Z",
    "updateDateIncludingText": "2025-06-11T11:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations. (text: CR S1715-1716)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T22:00:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "IA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-12",
      "state": "ME"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "LA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1009is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1009\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Durbin (for himself, Mr. Grassley , Mr. Booker , Mr. Padilla , Mr. King , Ms. Slotkin , Ms. Baldwin , Ms. Rosen , Ms. Klobuchar , Mr. Cassidy , Mr. Merkley , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo establish the Baltic Security Initiative for the purpose of strengthening the defensive capabilities of the Baltic countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baltic Security Initiative Act .\n#### 2. Baltic Security Initiative\n##### (a) Establishment\nPursuant to the authority provided in chapter 16 of title 10, United States Code, the Secretary of Defense shall establish and carry out an initiative, to be known as the Baltic Security Initiative (in this section referred to as the Initiative ), for the purpose of deepening security cooperation with the military forces of the Baltic countries.\n##### (b) Relationship to existing authorities\nThe Initiative required by subsection (a) shall be carried out pursuant to the authorities provided in title 10, United States Code.\n##### (c) Objectives\nThe objectives of the Initiative shall be\u2014\n**(1)**\nto achieve United States national security objectives by\u2014\n**(A)**\ndeterring aggression by the Russian Federation; and\n**(B)**\nimplementing the North Atlantic Treaty Organization's new Strategic Concept, which seeks to strengthen the alliance's deterrence and defense posture by denying potential adversaries any possible opportunities for aggression;\n**(2)**\nto enhance regional planning and cooperation among the military forces of the Baltic countries, particularly with respect to long-term regional capability projects, including\u2014\n**(A)**\nlong-range precision fire systems and capabilities;\n**(B)**\nintegrated air and missile defense;\n**(C)**\nmaritime domain awareness;\n**(D)**\nland forces development, including stockpiling large caliber ammunition;\n**(E)**\ncommand, control, communications, computers, intelligence, surveillance, and reconnaissance;\n**(F)**\nspecial operations forces development;\n**(G)**\ncoordination with and security enhancements for Poland, which is a neighboring North Atlantic Treaty Organization ally; and\n**(H)**\nother military capabilities, as determined by the Secretary of Defense; and\n**(3)**\nwith respect to the military forces of the Baltic countries, to improve cyber defenses and resilience to hybrid threats.\n##### (d) Strategy\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report setting forth a strategy for the Department of Defense to achieve the objectives described in subsection (b).\n**(2) Considerations**\nThe strategy required by this subsection shall include a consideration of\u2014\n**(A)**\nsecurity assistance programs for the Baltic countries authorized as of the date on which the strategy is submitted;\n**(B)**\nthe ongoing security threats to the North Atlantic Treaty Organization's eastern flank posed by Russian aggression, including as a result of the Russian Federation\u2019s 2022 invasion of Ukraine with support from Belarus; and\n**(C)**\nthe ongoing security threats to the Baltic countries posed by the presence, coercive economic policies, and other malign activities of the People\u2019s Republic of China.\n##### (e) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Secretary of Defense $350,000,000 for each of the fiscal years 2026, 2027, and 2028 to carry out the Initiative.\n**(2) Sense of Congress**\nIt is the sense of Congress that the Secretary of Defense should seek to require matching funds from each of the Baltic countries that participate in the Initiative in amounts commensurate with amounts provided by the Department of Defense for the Initiative.\n##### (f) Baltic countries defined\nIn this section, the term Baltic countries means\u2014\n**(1)**\nEstonia;\n**(2)**\nLatvia; and\n**(3)**\nLithuania.",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2025-05-15T00:50:43Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1009is.xml"
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
      "title": "Baltic Security Initiative Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Baltic Security Initiative Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:09:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Baltic Security Initiative for the purpose of strengthening the defensive capabilities of the Baltic countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:08:21Z"
    }
  ]
}
```
