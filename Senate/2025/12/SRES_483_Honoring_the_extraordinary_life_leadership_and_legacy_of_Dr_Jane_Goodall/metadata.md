# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/483
- Title: A resolution honoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.
- Congress: 119
- Bill type: SRES
- Bill number: 483
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2025-12-15T16:55:55Z
- Update date including text: 2025-12-15T16:55:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-12-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-09 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8580-8581; text: CR 11/5/2025 S7927-7928)
- 2025-12-09 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-09 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-12-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-09 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8580-8581; text: CR 11/5/2025 S7927-7928)
- 2025-12-09 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-09 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/483",
    "number": "483",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution honoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.",
    "type": "SRES",
    "updateDate": "2025-12-15T16:55:55Z",
    "updateDateIncludingText": "2025-12-15T16:55:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8580-8581; text: CR 11/5/2025 S7927-7928)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-11-05",
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
      "actionDate": "2025-11-05",
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
            "date": "2025-12-09T23:17:31Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-11-05T16:14:52Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NH"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "IL"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "HI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NM"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "WA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "GA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "OR"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "MA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-11-09",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres483is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 483\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mr. Welch (for himself, Mr. Coons , Mrs. Shaheen , Mr. Booker , Mr. Durbin , Mr. Schatz , Mr. Heinrich , Mrs. Murray , Mr. Ossoff , Mr. Schiff , Ms. Rosen , Mr. Hickenlooper , Mr. Merkley , Mr. Wyden , Ms. Klobuchar , Mr. Markey , and Mrs. Gillibrand ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.\nThat the Senate\u2014\n**(1)**\npays tribute to Dr. Jane Goodall\u2019s lifelong dedication to the survival and ethical treatment of chimpanzees and other living things and to wildlife conservation throughout the world;\n**(2)**\ncommends her tireless efforts to educate the public and especially children about the importance of protecting the natural environment;\n**(3)**\nextends its deepest condolences and sympathies to Jane Goodall\u2019s family and the staff at the Jane Goodall Institute and the Roots and Shoots Program in this time of loss; and\n**(4)**\nhonors the extraordinary life, leadership, and legacy of Jane Goodall, whose efforts to protect wildlife and the natural world continue to inspire people of every nationality on every continent.",
      "versionDate": "2025-11-05",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres483ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 483\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mr. Welch (for himself, Mr. Coons , Mrs. Shaheen , Mr. Booker , Mr. Durbin , Mr. Schatz , Mr. Heinrich , Mrs. Murray , Mr. Ossoff , Mr. Schiff , Ms. Rosen , Mr. Hickenlooper , Mr. Merkley , Mr. Wyden , Ms. Klobuchar , Mr. Markey , Mrs. Gillibrand , and Mr. Tillis ) submitted the following resolution; which was referred to the Committee on the Judiciary\nDecember 9, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nHonoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.\nThat the Senate\u2014\n**(1)**\npays tribute to Dr. Jane Goodall\u2019s lifelong dedication to the survival and ethical treatment of chimpanzees and other living things and to wildlife conservation throughout the world;\n**(2)**\ncommends her tireless efforts to educate the public and especially children about the importance of protecting the natural environment;\n**(3)**\nextends its deepest condolences and sympathies to Jane Goodall\u2019s family and the staff at the Jane Goodall Institute and the Roots and Shoots Program in this time of loss; and\n**(4)**\nhonors the extraordinary life, leadership, and legacy of Jane Goodall, whose efforts to protect wildlife and the natural world continue to inspire people of every nationality on every continent.",
      "versionDate": "2025-12-09",
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
            "name": "Biological and life sciences",
            "updateDate": "2025-12-15T16:55:10Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-12-15T16:55:54Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-12-15T16:55:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-11-25T20:13:40Z"
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
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres483is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres483ats.xml"
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
      "title": "A resolution honoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T04:48:17Z"
    },
    {
      "title": "A resolution honoring the extraordinary life, leadership, and legacy of Dr. Jane Goodall.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T11:56:15Z"
    }
  ]
}
```
