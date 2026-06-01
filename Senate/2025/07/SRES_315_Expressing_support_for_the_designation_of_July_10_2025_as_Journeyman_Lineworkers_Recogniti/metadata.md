# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/315
- Title: A resolution expressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.
- Congress: 119
- Bill type: SRES
- Bill number: 315
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Referred to the Committee on Energy and Natural Resources.
- 2025-07-10 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-10 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 7/8/2025 CR S4260)
- 2025-07-10 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-07-10 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S4321)
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Referred to the Committee on Energy and Natural Resources.
- 2025-07-10 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-10 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 7/8/2025 CR S4260)
- 2025-07-10 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-07-10 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S4321)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/315",
    "number": "315",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "A resolution expressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.",
    "type": "SRES",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 7/8/2025 CR S4260)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S4321)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
            "date": "2025-07-10T18:41:32Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-08T21:26:12Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "ND"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "ID"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "WV"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MI"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "HI"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "IL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NV"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "DE"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "ID"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "ND"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "AZ"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "AK"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "GA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres315is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 315\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Ms. Cortez Masto (for herself, Mr. Cramer , Mr. Risch , Mr. Heinrich , Mr. Blumenthal , Mr. Justice , Ms. Slotkin , Ms. Hirono , Mr. Hickenlooper , Ms. Duckworth , Ms. Rosen , Mr. Padilla , Ms. Blunt Rochester , Mr. Crapo , Mr. Hoeven , Mr. Van Hollen , Mr. Booker , Mr. Markey , Mr. Schiff , Mr. Gallego , and Mr. Sullivan ) submitted the following resolution; which was referred to the Committee on Energy and Natural Resources\nRESOLUTION\nExpressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.\nThat the Senate\u2014\n**(1)**\nsupports the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day;\n**(2)**\nhonors and recognizes the contributions and sacrifices of countless journeyman lineworkers who often place themselves in harm\u2019s way to serve their customers and their communities; and\n**(3)**\nencourages the people of the United States to observe Journeyman Lineworkers Recognition Day with appropriate reflection.",
      "versionDate": "2025-07-08",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres315ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 315\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Ms. Cortez Masto (for herself, Mr. Cramer , Mr. Risch , Mr. Heinrich , Mr. Blumenthal , Mr. Justice , Ms. Slotkin , Ms. Hirono , Mr. Hickenlooper , Ms. Duckworth , Ms. Rosen , Mr. Padilla , Ms. Blunt Rochester , Mr. Crapo , Mr. Hoeven , Mr. Van Hollen , Mr. Booker , Mr. Markey , Mr. Schiff , Mr. Gallego , Mr. Sullivan , Mr. Ossoff , and Mr. Scott of Florida ) submitted the following resolution; which was referred to the Committee on Energy and Natural Resources\nJuly 10, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nExpressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.\nThat the Senate\u2014\n**(1)**\nsupports the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day;\n**(2)**\nhonors and recognizes the contributions and sacrifices of countless journeyman lineworkers who often place themselves in harm\u2019s way to serve their customers and their communities; and\n**(3)**\nencourages the people of the United States to observe Journeyman Lineworkers Recognition Day with appropriate reflection.",
      "versionDate": "2025-07-10",
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
            "updateDate": "2025-07-17T15:19:57Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2025-07-17T15:19:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-07-17T10:56:11Z"
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
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres315is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres315ats.xml"
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
      "title": "A resolution expressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T03:03:23Z"
    },
    {
      "title": "A resolution expressing support for the designation of July 10, 2025, as Journeyman Lineworkers Recognition Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T10:56:23Z"
    }
  ]
}
```
