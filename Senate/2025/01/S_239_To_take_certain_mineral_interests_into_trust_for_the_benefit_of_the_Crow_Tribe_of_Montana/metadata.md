# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/239?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/239
- Title: Crow Revenue Act
- Congress: 119
- Bill type: S
- Bill number: 239
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-12-05T21:58:55Z
- Update date including text: 2025-12-05T21:58:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/239",
    "number": "239",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Crow Revenue Act",
    "type": "S",
    "updateDate": "2025-12-05T21:58:55Z",
    "updateDateIncludingText": "2025-12-05T21:58:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
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
        "item": {
          "date": "2025-01-24T15:29:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s239is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 239\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Daines (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo take certain mineral interests into trust for the benefit of the Crow Tribe of Montana, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crow Revenue Act .\n#### 2. Definitions\nIn this Act:\n**(1) Bull Mountains Lease**\nThe term Bull Mountains Lease means the Bureau of Land Management Lease MTM\u201397988 dated June 1, 2012.\n**(2) Bull Mountains Tracts**\nThe term Bull Mountains Tracts means the mineral interests that\u2014\n**(A)**\nare located in Musselshell County, Montana;\n**(B)**\ncomprise approximately 4,530 acres of subsurface interests owned by the United States located in\u2014\n**(i)**\nT. 6 N., R. 26 E., sec. 2;\n**(ii)**\nT. 6 N., R. 26 E., sec. 24;\n**(iii)**\nT. 6 N., R. 27 E., sec. 4;\n**(iv)**\nT. 6 N., R. 27 E., sec. 8;\n**(v)**\nT. 6 N., R. 27 E., sec. 10;\n**(vi)**\nT. 6 N., R. 27 E., sec. 14;\n**(vii)**\nT. 6 N., R. 27 E., sec. 22;\n**(viii)**\nT. 7 N., R. 26 E., sec. 24;\n**(ix)**\nT. 7 N., R. 26 E., sec. 26;\n**(x)**\nT. 7 N., R. 26 E., sec. 34;\n**(xi)**\nT. 7 N., R. 27 E., sec. 20; and\n**(xii)**\nT. 7 N., R. 27 E., sec. 22;\n**(C)**\ncomprise approximately 940 acres of surface interests owned by the United States located in\u2014\n**(i)**\nT. 6 N., R. 26 E., sec. 2;\n**(ii)**\nT. 6 N., R. 27 E., sec. 8;\n**(iii)**\nT. 6 N., R. 27 E., sec. 10;\n**(iv)**\nT. 6 N., R. 28 E., sec. 8; and\n**(v)**\nT. 7 N., R. 27 E., sec. 34; and\n**(D)**\nare generally depicted on the map entitled Bull Mountains Tracts and dated January 30, 2024.\n**(3) Hope Family Tracts**\nThe term Hope Family Tracts means the aggregate mineral interests that\u2014\n**(A)**\nare located in Big Horn County, Montana, within the boundaries of the Crow Reservation;\n**(B)**\ncomprise approximately 4,660 acres of subsurface interests owned by the Hope Family Trust located in\u2014\n**(i)**\nT. 4 S., R. 37 E., sec. 33;\n**(ii)**\nT. 4 S., R. 37 E., sec. 34;\n**(iii)**\nT. 5 S., R. 37 E., sec. 1;\n**(iv)**\nT. 5 S., R. 37 E., sec. 2;\n**(v)**\nT. 5 S., R. 37 E., sec. 3;\n**(vi)**\nT. 5 S., R. 37 E., sec. 10;\n**(vii)**\nT. 5 S., R. 37 E., sec. 11;\n**(viii)**\nT. 5 S., R. 37 E., sec. 12;\n**(ix)**\nT. 5 S., R. 37 E., sec. 13;\n**(x)**\nT. 5 S., R. 37 E., sec. 14;\n**(xi)**\nT. 5 S., R. 37 E., sec. 15;\n**(xii)**\nT. 5 S., R. 38 E., sec. 5;\n**(xiii)**\nT. 5 S., R. 38 E., sec. 8;\n**(xiv)**\nT. 5 S., R. 38 E., sec. 9;\n**(xv)**\nT. 5 S., R. 38 E., sec. 16; and\n**(xvi)**\nT. 5 S., R. 38 E., sec. 17; and\n**(C)**\nare generally depicted on the map entitled Hope Family Tracts and dated January 30, 2024.\n**(4) Hope family trust**\nThe term Hope Family Trust means the Joe and Barbara Hope Mineral Trust.\n**(5) Lessee**\nThe term Lessee means the lessee for the Bull Mountains Lease.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(7) State**\nThe term State means the State of Montana.\n**(8) Tribe**\nThe term Tribe means the Crow Tribe of Montana.\n#### 3. Mineral rights to be taken into trust\n##### (a) Completion of mineral conveyances\nNot later than 60 days after the date of enactment of this Act, in a single transaction\u2014\n**(1)**\nnotwithstanding any other provision of law, including sections 3480.0\u20136(d)(8) and 3452.1 through 3452.1\u20133 of title 43, Code of Federal Regulations (or successor regulations), if the Lessee offers to relinquish the Bull Mountains Lease, the Secretary shall accept the relinquishment;\n**(2)**\nthe Hope Family Trust shall convey to the Tribe all right, title, and interest in and to the mineral interests in the Hope Family Tracts; and\n**(3)**\nsubject to valid existing rights, and on relinquishment of the Bull Mountains Lease, the Secretary shall convey to the Hope Family Trust all right, title, and interest of the United States in and to the mineral interests and surface land in the Bull Mountains Tracts.\n##### (b) Trust status\nOn the request of the Tribe, the mineral interests conveyed to the Tribe under subsection (a)(2) shall be held in trust by the United States for the benefit of the Tribe.\n##### (c) No State taxation\nThe mineral interests conveyed to the Tribe under subsection (a)(2) shall not be subject to taxation by the State (including any political subdivision of the State).\n##### (d) Revenue sharing agreement\nBefore the conveyances under subsection (a), the Tribe shall notify the Secretary, in writing, that the Tribe and the Hope Family Trust have agreed on a formula for sharing revenue from development of the mineral and surface interests described in subsection (a)(3) if those mineral or surface interests are developed at a later date.\n##### (e) Withdrawal prior To exchange\nSubject to valid existing rights, pending the conveyances under paragraphs (2) and (3) of subsection (a), the tracts conveyed under those paragraphs shall be withdrawn from\u2014\n**(1)**\nall forms of entry, appropriation, and disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n#### 4. Eligibility for other Federal benefits\nNo amounts or other benefits provided to the Tribe under this Act shall result in the reduction or denial of any Federal services, benefits, or programs to the Tribe or any member of the Tribe to which the Tribe or member of the Tribe is entitled or eligible because of\u2014\n**(1)**\nthe status of the Tribe as a federally recognized Indian Tribe; or\n**(2)**\nthe status of the member as a member of the Tribe.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-06-25",
        "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16."
      },
      "number": "725",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Crow Revenue Act",
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
            "name": "Federal-Indian relations",
            "updateDate": "2025-04-14T17:23:44Z"
          },
          {
            "name": "Indian claims",
            "updateDate": "2025-04-14T17:23:44Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-04-14T17:23:44Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-04-14T17:23:44Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-04-14T17:23:44Z"
          },
          {
            "name": "State and local taxation",
            "updateDate": "2025-04-14T17:23:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-01T20:56:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s239",
          "measure-number": "239",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s239v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Crow Revenue Act</strong></p><p>This bill addresses the exchange of mineral interests in Montana involving the federal government, the Crow Tribe of Montana, and a private party.</p><p>Specifically, the bill requires\u00a0</p><ul><li>the Department of the Interior to accept the relinquishment of a specified federal coal lease associated with the Bull Mountains Mine near Roundup, Montana (the current operator of the mine is Signal Peak Energy);\u00a0</li><li>the Joe and Barbara Hope Mineral Trust (Hope Family Trust) to convey approximately 4,660 acres of subsurface mineral interests located within the boundaries of the Crow Indian Reservation in Big Horn County, Montana, to the tribe; and\u00a0</li><li>Interior to convey approximately 4,530 acres of subsurface mineral interests and 940 acres of surface interests located in Musselshell County, Montana, to the Hope Family Trust.\u00a0</li></ul><p>Prior to these conveyances, the tribe must notify Interior that the tribe and the Hope Family Trust have agreed on a revenue-sharing formula for the development of the mineral and surface interests in\u00a0Musselshell County, Montana.</p><p>The mineral interests conveyed by the Hope Family Trust to the tribe shall be held in trust by the United States for the benefit of the tribe, upon the tribe's request. These mineral interests shall not be subject to state or local taxation.</p>"
        },
        "title": "Crow Revenue Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s239.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Crow Revenue Act</strong></p><p>This bill addresses the exchange of mineral interests in Montana involving the federal government, the Crow Tribe of Montana, and a private party.</p><p>Specifically, the bill requires\u00a0</p><ul><li>the Department of the Interior to accept the relinquishment of a specified federal coal lease associated with the Bull Mountains Mine near Roundup, Montana (the current operator of the mine is Signal Peak Energy);\u00a0</li><li>the Joe and Barbara Hope Mineral Trust (Hope Family Trust) to convey approximately 4,660 acres of subsurface mineral interests located within the boundaries of the Crow Indian Reservation in Big Horn County, Montana, to the tribe; and\u00a0</li><li>Interior to convey approximately 4,530 acres of subsurface mineral interests and 940 acres of surface interests located in Musselshell County, Montana, to the Hope Family Trust.\u00a0</li></ul><p>Prior to these conveyances, the tribe must notify Interior that the tribe and the Hope Family Trust have agreed on a revenue-sharing formula for the development of the mineral and surface interests in\u00a0Musselshell County, Montana.</p><p>The mineral interests conveyed by the Hope Family Trust to the tribe shall be held in trust by the United States for the benefit of the tribe, upon the tribe's request. These mineral interests shall not be subject to state or local taxation.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s239"
    },
    "title": "Crow Revenue Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Crow Revenue Act</strong></p><p>This bill addresses the exchange of mineral interests in Montana involving the federal government, the Crow Tribe of Montana, and a private party.</p><p>Specifically, the bill requires\u00a0</p><ul><li>the Department of the Interior to accept the relinquishment of a specified federal coal lease associated with the Bull Mountains Mine near Roundup, Montana (the current operator of the mine is Signal Peak Energy);\u00a0</li><li>the Joe and Barbara Hope Mineral Trust (Hope Family Trust) to convey approximately 4,660 acres of subsurface mineral interests located within the boundaries of the Crow Indian Reservation in Big Horn County, Montana, to the tribe; and\u00a0</li><li>Interior to convey approximately 4,530 acres of subsurface mineral interests and 940 acres of surface interests located in Musselshell County, Montana, to the Hope Family Trust.\u00a0</li></ul><p>Prior to these conveyances, the tribe must notify Interior that the tribe and the Hope Family Trust have agreed on a revenue-sharing formula for the development of the mineral and surface interests in\u00a0Musselshell County, Montana.</p><p>The mineral interests conveyed by the Hope Family Trust to the tribe shall be held in trust by the United States for the benefit of the tribe, upon the tribe's request. These mineral interests shall not be subject to state or local taxation.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s239"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s239is.xml"
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
      "title": "Crow Revenue Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Crow Revenue Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to take certain mineral interests into trust for the benefit of the Crow Tribe of Montana, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:39Z"
    }
  ]
}
```
