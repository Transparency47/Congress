# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/195
- Title: CBP Relocation Act
- Congress: 119
- Bill type: HR
- Bill number: 195
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-24T20:44:30Z
- Update date including text: 2025-02-24T20:44:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-03 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-03 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/195",
    "number": "195",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CBP Relocation Act",
    "type": "HR",
    "updateDate": "2025-02-24T20:44:30Z",
    "updateDateIncludingText": "2025-02-24T20:44:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:19:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-03T18:42:07Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "systemCode": "hshm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr195ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 195\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Secretary of Homeland Security to relocate to the State of Texas the headquarters of U.S. Customs and Border Protection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the U.S. Customs and Border Protection Relocation Act or the CBP Relocation Act .\n#### 2. Relocation of the headquarters of U.S. Customs and Border Protection\n##### (a) In general\nNot later than January 1, 2026, the Secretary of Homeland Security, acting through the Commissioner of U.S. Customs and Border Protection, shall relocate to the State of Texas the headquarters of U.S. Customs and Border Protection, including the functions, personnel, and real assets of such headquarters.\n##### (b) Duties and powers\nIn carrying out the relocation described in subsection (a), the Secretary of Homeland Security, acting through the Commissioner of U.S. Customs and Border Protection\u2014\n**(1)**\nshall collaborate with the Commissioner of the General Land Office of the State of Texas to ensure that the requirement described in subsection (c) is satisfied; and\n**(2)**\nmay acquire any right, title, or interest in or to land in the State of Texas through a written contract that is signed by the Secretary and the individual who is authorized to convey such right, title, or interest, as the case may be.\n##### (c) Headquarters requirement\nThe relocation described in subsection (a) shall be strategically placed with respect to handling a crisis at the border between the United States and Mexico.\n##### (d) Land title\nAny title to land conveyed to the Secretary of Homeland Security in carrying out the relocation described in subsection (a) shall conform to the title approval standards of the Attorney General that are applicable to land acquisitions by the Federal Government.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-02-24T17:07:26Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-02-24T17:07:08Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-24T17:07:20Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-02-24T17:07:33Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-02-24T17:07:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T18:38:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr195",
          "measure-number": "195",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr195v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>U.S. Customs and Border Protection Relocation Act or the CBP Relocation Act</strong></p><p>This bill requires the Department of Homeland Security to relocate the headquarters of U.S. Customs and Border Protection (including the functions, personnel, and real assets of the headquarters) to Texas no later than January 1, 2026.</p>"
        },
        "title": "CBP Relocation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr195.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>U.S. Customs and Border Protection Relocation Act or the CBP Relocation Act</strong></p><p>This bill requires the Department of Homeland Security to relocate the headquarters of U.S. Customs and Border Protection (including the functions, personnel, and real assets of the headquarters) to Texas no later than January 1, 2026.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr195"
    },
    "title": "CBP Relocation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>U.S. Customs and Border Protection Relocation Act or the CBP Relocation Act</strong></p><p>This bill requires the Department of Homeland Security to relocate the headquarters of U.S. Customs and Border Protection (including the functions, personnel, and real assets of the headquarters) to Texas no later than January 1, 2026.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr195"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr195ih.xml"
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
      "title": "CBP Relocation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBP Relocation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T23:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S. Customs and Border Protection Relocation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T23:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to relocate to the State of Texas the headquarters of U.S. Customs and Border Protection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T23:33:15Z"
    }
  ]
}
```
