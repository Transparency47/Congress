# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/931?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/931
- Title: To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 931
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-02-26T00:26:17Z
- Update date including text: 2026-02-26T00:26:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-05-20 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-05-20 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/931",
    "number": "931",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-26T00:26:17Z",
    "updateDateIncludingText": "2026-02-26T00:26:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-05-20T21:14:35Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-13T14:58:20Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr931ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 931\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Downing (for himself and Mr. Zinke ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.\n#### 1. Authorization to mine Federal minerals\n##### (a) Definition of Bull Mountains mining plan modification\nIn this Act, the term Bull Mountains Mining Plan Modification means Amendment 3, Bull Mountains Mine No. 1, Mining Plan Modification for Federal Coal Lease MTM 97988, that was approved by Department of the Interior Principal Deputy Assistant Secretary for Land and Minerals Management in a concurrence memorandum, dated November 18, 2020.\n##### (b) Mining of Federal minerals\n**(1) In general**\nAll Federal coal reserves leased under Federal Coal Lease MTM 97988 located in the Federal land described in subsection (c) are authorized to be mined in accordance with the Bull Mountains Mining Plan Modification.\n**(2) Requirement**\nNot later than 30 days after the date of enactment of this Act, the Secretary of the Interior shall, without modification or delay, approve the Bull Mountains Mining Plan Modification to the extent necessary to mine the Federal land described in subsection (c).\n##### (c) Description of Federal land\nThe Federal land referred to in subsection (b) is the following land, comprising 800 acres, more or less, located in T. 6 N., R. 27 E., Montana Principal Meridian, Musselshell County, Montana:\n**(1)**\nThe NE 1/4 of section 8.\n**(2)**\nThe SW 1/4 of section 10.\n**(3)**\nThe W 1/2 , SE 1/4 of section 22.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2026-02-11",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 332."
      },
      "number": "362",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-05-22T14:32:52Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-05-22T14:32:52Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-05-22T14:32:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-06T15:32:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr931",
          "measure-number": "931",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr931v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill authorizes coal to be mined on approximately 800 acres of federal land in Musselshell County, Montana. Specifically, it allows all federal coal reserves in such federal land and leased under Federal Coal Lease MTM 97988 to be mined in accordance with the 2020 Bull Mountains Mining Plan Modification.\u00a0The Bull Mountains Mine is operated by Signal Peak Energy.</p><p>This bill directs the Department of the Interior, without modification or delay, to approve the Bull Mountains Mining Plan Modification to the extent necessary to mine such land.</p>"
        },
        "title": "To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr931.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill authorizes coal to be mined on approximately 800 acres of federal land in Musselshell County, Montana. Specifically, it allows all federal coal reserves in such federal land and leased under Federal Coal Lease MTM 97988 to be mined in accordance with the 2020 Bull Mountains Mining Plan Modification.\u00a0The Bull Mountains Mine is operated by Signal Peak Energy.</p><p>This bill directs the Department of the Interior, without modification or delay, to approve the Bull Mountains Mining Plan Modification to the extent necessary to mine such land.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr931"
    },
    "title": "To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill authorizes coal to be mined on approximately 800 acres of federal land in Musselshell County, Montana. Specifically, it allows all federal coal reserves in such federal land and leased under Federal Coal Lease MTM 97988 to be mined in accordance with the 2020 Bull Mountains Mining Plan Modification.\u00a0The Bull Mountains Mine is operated by Signal Peak Energy.</p><p>This bill directs the Department of the Interior, without modification or delay, to approve the Bull Mountains Mining Plan Modification to the extent necessary to mine such land.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr931"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr931ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:23Z"
    },
    {
      "title": "To allow certain Federal minerals to be mined consistent with the Bull Mountains Mining Plan Modification, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:06:16Z"
    }
  ]
}
```
