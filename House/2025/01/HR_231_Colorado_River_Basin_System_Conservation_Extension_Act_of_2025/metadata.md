# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/231
- Title: Colorado River Basin System Conservation Extension Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 231
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2026-01-14T09:07:07Z
- Update date including text: 2026-01-14T09:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-21 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-01-23 - Committee: Subcommittee Hearings Held
- 2025-02-12 - Committee: Committee Consideration and Mark-up Session Held.
- 2025-02-12 - Committee: Ordered to be Reported (Amended) by Unanimous Consent.
- 2025-02-12 - Committee: Subcommittee on Water, Wildlife and Fisheries Discharged
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-21 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-01-23 - Committee: Subcommittee Hearings Held
- 2025-02-12 - Committee: Committee Consideration and Mark-up Session Held.
- 2025-02-12 - Committee: Ordered to be Reported (Amended) by Unanimous Consent.
- 2025-02-12 - Committee: Subcommittee on Water, Wildlife and Fisheries Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/231",
    "number": "231",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Colorado River Basin System Conservation Extension Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T09:07:07Z",
    "updateDateIncludingText": "2026-01-14T09:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Water, Wildlife and Fisheries Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
        "item": [
          {
            "date": "2025-02-12T22:24:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-12T21:37:01Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-01-07T16:01:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-01-23T18:52:45Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-01-21T22:14:55Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "UT"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr231ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 231\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Energy and Water Development and Related Agencies Appropriations Act, 2015, to reauthorize the Colorado River System conservation pilot program.\n#### 1. Short title\nThis Act may be cited as the Colorado River Basin System Conservation Extension Act of 2025 .\n#### 2. Reauthorization of Colorado River System conservation pilot program\nSection 206 of the Energy and Water Development and Related Agencies Appropriations Act, 2015 ( 43 U.S.C. 620 note; Public Law 113\u2013235 ), is amended\u2014\n**(1)**\nin subsection (b)(2), by striking this Act and inserting the Colorado River Basin System Conservation Extension Act of 2025 ;\n**(2)**\nin subsection (c)(2), by striking 2024 and inserting 2026 ; and\n**(3)**\nin subsection (d), by striking 2025 and inserting 2027 .",
      "versionDate": "2025-01-07",
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
        "actionDate": "2025-06-23",
        "actionTime": "15:28:39",
        "text": "Held at the desk."
      },
      "number": "154",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Colorado River Basin System Conservation Extension Act",
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
            "name": "Arizona",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "California",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-02-21T15:37:31Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-02-21T15:37:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-02-18T20:27:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr231",
          "measure-number": "231",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr231v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Colorado River Basin System Conservation Extension Act of 2025</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>"
        },
        "title": "Colorado River Basin System Conservation Extension Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr231.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Colorado River Basin System Conservation Extension Act of 2025</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr231"
    },
    "title": "Colorado River Basin System Conservation Extension Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Colorado River Basin System Conservation Extension Act of 2025</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr231"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr231ih.xml"
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
      "title": "Colorado River Basin System Conservation Extension Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Colorado River Basin System Conservation Extension Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy and Water Development and Related Agencies Appropriations Act, 2015, to reauthorize the Colorado River System conservation pilot program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:26Z"
    }
  ]
}
```
