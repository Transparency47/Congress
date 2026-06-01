# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2033
- Title: Cross-Boundary Wildfire Solutions Act
- Congress: 119
- Bill type: S
- Bill number: 2033
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2033",
    "number": "2033",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Cross-Boundary Wildfire Solutions Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-11",
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
            "date": "2025-12-17T14:30:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-11T17:57:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:44Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2033is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2033\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Gallego introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Comptroller General of the United States to conduct a study on existing programs, rules, and authorities that enable or inhibit wildfire mitigation across land ownership boundaries on Federal and non-Federal land.\n#### 1. Short title\nThis Act may be cited as the Cross-Boundary Wildfire Solutions Act .\n#### 2. Study on wildfire mitigation across land ownership boundaries\n##### (a) Study required\nThe Comptroller General of the United States shall conduct a study on\u2014\n**(1)**\nthe existing Federal programs, rules, and authorities that enable or inhibit wildfire mitigation from being completed across land ownership boundaries on Federal and non-Federal land;\n**(2)**\nwhether changes to any program, rule, or authority identified pursuant to paragraph (1) would allow Federal land management agencies (as defined in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 )), the Secretary of Agriculture, acting through the Chief of the Natural Resources Conservation Service, the Secretary of Homeland Security, acting through the Administrator of the Federal Emergency Management Agency, the U.S. Fire Administration, States, local governments, and Tribal governments increased capacity or access to funding to mitigate wildfires; and\n**(3)**\nthe activities carried out pursuant to subsection (e) of section 103 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6513 ), including\u2014\n**(A)**\nhow to improve the efficacy of such activities with respect to mitigating wildfire; and\n**(B)**\nwhether the enactment of such subsection has increased the access of Federal land management agencies and States to funding to mitigate wildfires.\n##### (b) Report\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report that contains\u2014\n**(1)**\nthe results of the study required under subsection (a); and\n**(2)**\nrecommendations to simplify cross-boundary wildfire mitigation between Federal land management agencies and State, local, and Tribal governments.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2026-02-11",
        "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by Unanimous Consent."
      },
      "number": "3922",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Cross-Boundary Wildfire Solutions Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-23T18:22:23Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-01-23T18:22:23Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-23T18:22:23Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-23T18:22:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-24T21:50:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-11",
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
          "measure-id": "id119s2033",
          "measure-number": "2033",
          "measure-type": "s",
          "orig-publish-date": "2025-06-11",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2033v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-06-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Cross-Boundary Wildfire Solutions Act</strong></p><p>This bill directs the Government Accountability Office to study wildfire mitigation across land ownership boundaries and make recommendations to simplify cross-boundary wildfire mitigation between federal land management agencies and state, local, and Indian tribal governments.</p>"
        },
        "title": "Cross-Boundary Wildfire Solutions Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2033.xml",
    "summary": {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Cross-Boundary Wildfire Solutions Act</strong></p><p>This bill directs the Government Accountability Office to study wildfire mitigation across land ownership boundaries and make recommendations to simplify cross-boundary wildfire mitigation between federal land management agencies and state, local, and Indian tribal governments.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s2033"
    },
    "title": "Cross-Boundary Wildfire Solutions Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Cross-Boundary Wildfire Solutions Act</strong></p><p>This bill directs the Government Accountability Office to study wildfire mitigation across land ownership boundaries and make recommendations to simplify cross-boundary wildfire mitigation between federal land management agencies and state, local, and Indian tribal governments.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s2033"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2033is.xml"
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
      "title": "Cross-Boundary Wildfire Solutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cross-Boundary Wildfire Solutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Comptroller General of the United States to conduct a study on existing programs, rules, and authorities that enable or inhibit wildfire mitigation across land ownership boundaries on Federal and non-Federal land.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:23Z"
    }
  ]
}
```
