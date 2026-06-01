# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2524
- Title: Restoring Essential Healthcare Act
- Congress: 119
- Bill type: S
- Bill number: 2524
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-12-05T22:53:26Z
- Update date including text: 2025-12-05T22:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2524",
    "number": "2524",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Restoring Essential Healthcare Act",
    "type": "S",
    "updateDate": "2025-12-05T22:53:26Z",
    "updateDateIncludingText": "2025-12-05T22:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T22:17:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sponsorshipDate": "2025-07-29",
      "state": "IL"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "RI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NM"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "DE"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sponsorshipDate": "2025-07-29",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OR"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NV"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2524is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2524\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Ms. Smith (for herself, Mrs. Murray , Ms. Baldwin , Ms. Duckworth , Mr. Durbin , Mr. Reed , Mr. Blumenthal , Mr. Schiff , Mr. Heinrich , Mr. Van Hollen , Ms. Klobuchar , Mr. Coons , Mr. Sanders , Ms. Warren , Mr. Whitehouse , Mr. Luj\u00e1n , Mr. Merkley , Mr. King , Mr. Booker , Ms. Hirono , Mr. Padilla , Mr. Welch , Mr. Hickenlooper , Ms. Slotkin , Mr. Fetterman , Mrs. Gillibrand , Mr. Markey , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend Public Law 119\u201321 to repeal the prohibition on making payments under the Medicaid program to certain entities.\n#### 1. Short title\nThis Act may be cited as the Restoring Essential Healthcare Act .\n#### 2. Repealing prohibition on Medicaid payments to certain entities\nSection 71113 of Public Law 119\u201321 is repealed, and, in the case of any items or services furnished as medical assistance under a State plan (or a waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) by a prohibited entity (as defined in subsection (b)(1) of such section 71113) during the period beginning on the date of enactment of Public Law 119\u201321 and ending on the date of enactment of this section, payment for such items and services shall be made as if such section 71113 had not been enacted into law.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4796",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restoring Essential Healthcare Act",
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
        "name": "Health",
        "updateDate": "2025-09-17T15:36:01Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2524is.xml"
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
      "title": "Restoring Essential Healthcare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Essential Healthcare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend Public Law 119-21 to repeal the prohibition on making payments under the Medicaid program to certain entities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:42Z"
    }
  ]
}
```
