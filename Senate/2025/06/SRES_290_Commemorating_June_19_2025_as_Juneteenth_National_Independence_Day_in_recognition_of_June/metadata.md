# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/290
- Title: A resolution commemorating June 19, 2025, as "Juneteenth National Independence Day" in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.
- Congress: 119
- Bill type: SRES
- Bill number: 290
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:40:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-06-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-25 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3536; text: 6/18/2025 CR S3475)
- 2025-06-25 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-25 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-06-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-25 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3536; text: 6/18/2025 CR S3475)
- 2025-06-25 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-25 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/290",
    "number": "290",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A resolution commemorating June 19, 2025, as \"Juneteenth National Independence Day\" in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:40:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3536; text: 6/18/2025 CR S3475)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
        "item": [
          {
            "date": "2025-06-25T22:17:57Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-18T19:05:33Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NY"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "LA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NV"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-18",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ND"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "GA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "AZ"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "HI"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MS"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CO"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "SC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ND"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "TN"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WV"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "AL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-18",
      "state": "VT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "VA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NJ"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres290is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 290\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cornyn (for himself, Mrs. Gillibrand , Mr. Cassidy , Ms. Cortez Masto , Ms. Collins , Mr. King , Mr. Blumenthal , Mr. Cramer , Mrs. Shaheen , Mr. Warnock , Mr. Kelly , Mr. Johnson , Mr. Whitehouse , Ms. Cantwell , Ms. Hirono , Mrs. Hyde-Smith , Mr. Hickenlooper , Mr. Scott of South Carolina , Mr. Hoeven , Mr. Wicker , Mr. Young , Mrs. Blackburn , Mr. Justice , Mrs. Britt , Mr. Sanders , Mr. Kaine , Mr. Durbin , Mr. Wyden , Mr. Merkley , Mr. Padilla , Mr. Booker , and Mr. Cruz ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommemorating June 19, 2025, as Juneteenth National Independence Day in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.\nThat the Senate\u2014\n**(1)**\ncommemorates June 19, 2025, as Juneteenth National Independence Day ;\n**(2)**\nrecognizes the historical significance of Juneteenth National Independence Day to the United States;\n**(3)**\nsupports the continued nationwide celebration of Juneteenth National Independence Day to provide an opportunity for the people of the United States to learn more about the past and to better understand the experiences that have shaped the United States; and\n**(4)**\nrecognizes that the observance of the end of slavery is part of the history and heritage of the United States.",
      "versionDate": "2025-06-18",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres290ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 290\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cornyn (for himself, Mrs. Gillibrand , Mr. Cassidy , Ms. Cortez Masto , Ms. Collins , Mr. King , Mr. Blumenthal , Mr. Cramer , Mrs. Shaheen , Mr. Warnock , Mr. Kelly , Mr. Johnson , Mr. Whitehouse , Ms. Cantwell , Ms. Hirono , Mrs. Hyde-Smith , Mr. Hickenlooper , Mr. Scott of South Carolina , Mr. Hoeven , Mr. Wicker , Mr. Young , Mrs. Blackburn , Mr. Justice , Mrs. Britt , Mr. Sanders , Mr. Kaine , Mr. Durbin , Mr. Wyden , Mr. Merkley , Mr. Padilla , Mr. Booker , and Mr. Cruz ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJune 25 (legislative day, June 24), 2025 Committee discharged; considered and agreed to\nRESOLUTION\nCommemorating June 19, 2025, as Juneteenth National Independence Day in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.\nThat the Senate\u2014\n**(1)**\ncommemorates June 19, 2025, as Juneteenth National Independence Day ;\n**(2)**\nrecognizes the historical significance of Juneteenth National Independence Day to the United States;\n**(3)**\nsupports the continued nationwide celebration of Juneteenth National Independence Day to provide an opportunity for the people of the United States to learn more about the past and to better understand the experiences that have shaped the United States; and\n**(4)**\nrecognizes that the observance of the end of slavery is part of the history and heritage of the United States.",
      "versionDate": "2025-06-25",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-02T19:18:02Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-02T19:18:02Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-07-02T19:18:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-07-02T18:24:47Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres290is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres290ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution commemorating June 19, 2025, as \"Juneteenth National Independence Day\" in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-20T13:48:16Z"
    },
    {
      "title": "A resolution commemorating June 19, 2025, as \"Juneteenth National Independence Day\" in recognition of June 19, 1865, the date on which news of the end of slavery reached the slaves in the Southwestern States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T10:56:26Z"
    }
  ]
}
```
