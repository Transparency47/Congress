# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/367
- Title: Expressing support for the designation of May 2025 as "Motorcycle Safety Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 367
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-14T17:51:22Z
- Update date including text: 2026-05-14T17:51:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House
- Latest action: 2025-05-01: Submitted in House

## Actions

- 2025-05-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/367",
    "number": "367",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-14T17:51:22Z",
    "updateDateIncludingText": "2026-05-14T17:51:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-01T13:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-01T21:19:32Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "SD"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NJ"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "WI"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres367ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 367\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Walberg (for himself, Mr. Johnson of South Dakota , Mr. Balderson , Mr. Norcross , Mr. Van Orden , Ms. Brownley , and Mr. Stauber ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the designation of May 2025 as Motorcycle Safety Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Motorcycle Safety Awareness Month ;\n**(2)**\nrecognizes the contribution of motorcycles to the transportation mix;\n**(3)**\nencourages motorcycle awareness by all road users;\n**(4)**\nrecognizes that motorcyclists have a right to the road and that all motorists should safely share the roadways;\n**(5)**\nencourages rider safety education, training, and proper gear for safe motorcycle operation; and\n**(6)**\nsupports the goals of Motorcycle Safety Awareness Month.",
      "versionDate": "2025-05-01",
      "versionType": "IH"
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "1236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of May 2026 as \"Motorcycle Safety Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-13",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2901; text: CR S2900)"
      },
      "number": "222",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "type": "SRES"
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
            "updateDate": "2025-06-02T15:37:45Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-06-02T15:37:45Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-06-02T15:37:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-20T14:30:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
    "originChamber": "House",
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
          "measure-id": "id119hres367",
          "measure-number": "367",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres367v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of a Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>"
        },
        "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres367.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of a Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres367"
    },
    "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of a Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres367"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres367ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T08:18:29Z"
    },
    {
      "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T08:06:35Z"
    }
  ]
}
```
