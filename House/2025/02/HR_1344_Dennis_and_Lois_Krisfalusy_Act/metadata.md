# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1344
- Title: Dennis and Lois Krisfalusy Act
- Congress: 119
- Bill type: HR
- Bill number: 1344
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-05-01T08:09:19Z
- Update date including text: 2026-05-01T08:09:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1344",
    "number": "1344",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000610",
        "district": "14",
        "firstName": "Guy",
        "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
        "lastName": "Reschenthaler",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Dennis and Lois Krisfalusy Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:09:19Z",
    "updateDateIncludingText": "2026-05-01T08:09:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-13T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-03-26T17:55:07Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-21T17:54:52Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NV"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "VA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1344ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1344\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Reschenthaler (for himself, Mr. Meuser , Mr. Thompson of Pennsylvania , Mr. Kelly of Pennsylvania , Mr. Deluzio , and Ms. Brownley ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for headstones, markers, and burial receptacles under the laws administered by the Secretary of Veterans Affairs to certain individuals who died before November 11, 1998.\n#### 1. Short title\nThis Act may be cited as the Dennis and Lois Krisfalusy Act .\n#### 2. Expansion of eligibility for Department of Veterans Affairs headstones, markers, and burial receptacles for certain individuals\nSection 2306(b)(2) of title 38, United States Code, is amended in subparagraphs (B) and (C) by striking who dies on or after November 11, 1998, each place it appears.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
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
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "1127",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dennis and Lois Krisfalusy Act",
      "type": "S"
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
            "name": "Cemeteries and funerals",
            "updateDate": "2025-04-01T15:25:59Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-04-01T15:25:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:33:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1344",
          "measure-number": "1344",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1344v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>"
        },
        "title": "Dennis and Lois Krisfalusy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1344.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1344"
    },
    "title": "Dennis and Lois Krisfalusy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1344"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1344ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Dennis and Lois Krisfalusy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dennis and Lois Krisfalusy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand eligibility for headstones, markers, and burial receptacles under the laws administered by the Secretary of Veterans Affairs to certain individuals who died before November 11, 1998.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:27Z"
    }
  ]
}
```
