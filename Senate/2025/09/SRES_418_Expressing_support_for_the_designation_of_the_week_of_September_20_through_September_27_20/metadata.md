# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/418
- Title: A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as "National Estuaries Week".
- Congress: 119
- Bill type: SRES
- Bill number: 418
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2026-04-08T15:24:20Z
- Update date including text: 2026-04-08T15:24:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Referred to the Committee on Environment and Public Works.
- 2025-09-29 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-09-29 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: CR 9/19/2025 S6795-6796)
- 2025-09-29 - Committee: Senate Committee on Environment and Public Works discharged by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on Environment and Public Works discharged by Unanimous Consent. (consideration: CR S6844)
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Referred to the Committee on Environment and Public Works.
- 2025-09-29 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-09-29 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: CR 9/19/2025 S6795-6796)
- 2025-09-29 - Committee: Senate Committee on Environment and Public Works discharged by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on Environment and Public Works discharged by Unanimous Consent. (consideration: CR S6844)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/418",
    "number": "418",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\".",
    "type": "SRES",
    "updateDate": "2026-04-08T15:24:20Z",
    "updateDateIncludingText": "2026-04-08T15:24:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: CR 9/19/2025 S6795-6796)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Environment and Public Works discharged by Unanimous Consent. (consideration: CR S6844)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Environment and Public Works discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-19",
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
            "date": "2025-09-30T01:53:47Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-09-19T18:52:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "LA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "ME"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "DE"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "HI"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "MS"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "VA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "LA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sponsorshipDate": "2025-09-19",
      "state": "ME"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sponsorshipDate": "2025-09-19",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "MS"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres418is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 418\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Whitehouse (for himself, Mr. Cassidy , Ms. Alsobrooks , Ms. Baldwin , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Ms. Collins , Mr. Coons , Ms. Hassan , Ms. Hirono , Mrs. Hyde-Smith , Mr. Kaine , Mr. Kennedy , Mr. Kim , Mr. King , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Mr. Van Hollen , Mr. Warner , Ms. Warren , Mr. Wicker , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on Environment and Public Works\nRESOLUTION\nExpressing support for the designation of the week of September 20 through September 27, 2025, as National Estuaries Week .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of National Estuaries Week ;\n**(2)**\nsupports the goals and ideals of National Estuaries Week;\n**(3)**\nacknowledges the importance of estuaries to sustaining employment in the United States and to the economic well-being and prosperity of the United States;\n**(4)**\nrecognizes that persistent threats undermine the health of estuaries;\n**(5)**\napplauds the work of national and community organizations and public partners that promote public awareness, understanding, protection, and restoration of estuaries;\n**(6)**\nsupports the scientific study, preservation, protection, and restoration of estuaries; and\n**(7)**\nexpresses the intent of the Senate to continue working to understand, protect, and restore the estuaries of the United States.",
      "versionDate": "2025-09-19",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres418ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 418\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Whitehouse (for himself, Mr. Cassidy , Ms. Alsobrooks , Ms. Baldwin , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Ms. Collins , Mr. Coons , Ms. Hassan , Ms. Hirono , Mrs. Hyde-Smith , Mr. Kaine , Mr. Kennedy , Mr. Kim , Mr. King , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Mr. Van Hollen , Mr. Warner , Ms. Warren , Mr. Wicker , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on Environment and Public Works\nSeptember 29, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nExpressing support for the designation of the week of September 20 through September 27, 2025, as National Estuaries Week .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of National Estuaries Week ;\n**(2)**\nsupports the goals and ideals of National Estuaries Week;\n**(3)**\nacknowledges the importance of estuaries to sustaining employment in the United States and to the economic well-being and prosperity of the United States;\n**(4)**\nrecognizes that persistent threats undermine the health of estuaries;\n**(5)**\napplauds the work of national and community organizations and public partners that promote public awareness, understanding, protection, and restoration of estuaries;\n**(6)**\nsupports the scientific study, preservation, protection, and restoration of estuaries; and\n**(7)**\nexpresses the intent of the Senate to continue working to understand, protect, and restore the estuaries of the United States.",
      "versionDate": "2025-09-29",
      "versionType": "ATS"
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "733",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\".",
      "type": "HRES"
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
            "updateDate": "2025-09-30T17:28:09Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-30T17:35:37Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-09-30T17:32:47Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-09-30T17:30:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-09-24T13:33:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-19",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres418",
          "measure-number": "418",
          "measure-type": "sres",
          "orig-publish-date": "2025-09-19",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": [
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119sres418v55",
              "update-date": "2026-04-08"
            },
            "action-date": "2025-09-29",
            "action-desc": "Passed Senate",
            "summary-text": "<p>This resolution expresses support for the designation of National Estuaries Week.</p>"
          },
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119sres418v00",
              "update-date": "2026-04-08"
            },
            "action-date": "2025-09-19",
            "action-desc": "Introduced in Senate",
            "summary-text": "<p>This resolution expresses support for the designation of National Estuaries Week.</p>"
          }
        ],
        "title": "A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres418.xml",
    "summary": {
      "actionDate": "2025-09-29",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for the designation of National Estuaries Week.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres418"
    },
    "title": "A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-29",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for the designation of National Estuaries Week.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres418"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres418is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres418ats.xml"
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
      "title": "A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:18Z"
    },
    {
      "title": "A resolution expressing support for the designation of the week of September 20 through September 27, 2025, as \"National Estuaries Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T10:56:17Z"
    }
  ]
}
```
