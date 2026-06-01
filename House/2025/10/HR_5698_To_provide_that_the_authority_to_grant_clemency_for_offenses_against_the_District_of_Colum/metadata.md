# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5698
- Title: District of Columbia Clemency Home Rule Act
- Congress: 119
- Bill type: HR
- Bill number: 5698
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2026-04-29T17:17:53Z
- Update date including text: 2026-04-29T17:17:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5698",
    "number": "5698",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "District of Columbia Clemency Home Rule Act",
    "type": "HR",
    "updateDate": "2026-04-29T17:17:53Z",
    "updateDateIncludingText": "2026-04-29T17:17:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
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
          "date": "2025-10-06T19:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5698ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5698\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo provide that the authority to grant clemency for offenses against the District of Columbia shall be exercised in accordance with law enacted by the District of Columbia.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Clemency Home Rule Act .\n#### 2. Authority to grant clemency for crimes under laws of the District of Columbia\n##### (a) Authority described\nThe authority to grant clemency for crimes under the laws of the District of Columbia shall be exercised by such person or persons, and under such terms and conditions, as may be provided under law enacted by the District of Columbia.\n##### (b) Rule of Construction\nNothing in this Act may be construed\u2014\n**(1)**\nto affect any authority exercised by the President or the Mayor of the District of Columbia prior to the effective date of any law enacted by the District of Columbia pursuant to this Act with respect to the authority to grant clemency for crimes under the laws of the District of Columbia; or\n**(2)**\nto limit the authority described in subsection (a) from being exercised with respect to crimes committed before, on, or after the date of the enactment of this Act.\n##### (c) Clemency Defined\nIn this Act, the term clemency means a pardon, reprieve, or commutation of sentence, or a remission of a fine or other financial penalty.",
      "versionDate": "2025-10-06",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-02T21:50:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119hr5698",
          "measure-number": "5698",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5698v00",
            "update-date": "2026-04-29"
          },
          "action-date": "2025-10-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>District of Columbia Clemency Home Rule Act</b></p> <p>This bill authorizes the District of Columbia to legislate the terms and conditions under which clemency may be granted for violations of District criminal laws. Under the bill, <i>clemency</i> is defined as a pardon, reprieve, or a commutation of a sentence, or a remission of a fine or other financial penalty.</p>"
        },
        "title": "District of Columbia Clemency Home Rule Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5698.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>District of Columbia Clemency Home Rule Act</b></p> <p>This bill authorizes the District of Columbia to legislate the terms and conditions under which clemency may be granted for violations of District criminal laws. Under the bill, <i>clemency</i> is defined as a pardon, reprieve, or a commutation of a sentence, or a remission of a fine or other financial penalty.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr5698"
    },
    "title": "District of Columbia Clemency Home Rule Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>District of Columbia Clemency Home Rule Act</b></p> <p>This bill authorizes the District of Columbia to legislate the terms and conditions under which clemency may be granted for violations of District criminal laws. Under the bill, <i>clemency</i> is defined as a pardon, reprieve, or a commutation of a sentence, or a remission of a fine or other financial penalty.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr5698"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5698ih.xml"
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
      "title": "District of Columbia Clemency Home Rule Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "District of Columbia Clemency Home Rule Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the authority to grant clemency for offenses against the District of Columbia shall be exercised in accordance with law enacted by the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:25Z"
    }
  ]
}
```
