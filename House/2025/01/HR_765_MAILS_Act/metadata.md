# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/765?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/765
- Title: MAILS Act
- Congress: 119
- Bill type: HR
- Bill number: 765
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T22:48:40Z
- Update date including text: 2025-12-05T22:48:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/765",
    "number": "765",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "MAILS Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:48:40Z",
    "updateDateIncludingText": "2025-12-05T22:48:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:07:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr765ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 765\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Fulcher (for himself and Mr. Simpson ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo improve communication between the United States Postal Service and local communities relating to the relocation and establishment of Postal Service retail service facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Post office**\nThe term post office \u2014\n**(A)**\nmeans a facility that\u2014\n**(i)**\nis owned or leased by the Postal Service;\n**(ii)**\nis managed by a Postmaster;\n**(iii)**\nhas responsibility for\u2014\n**(I)**\ncustomer services;\n**(II)**\nlocal delivery; and\n**(III)**\nreceipt and dispatch of all classes of mail; and\n**(iv)**\nmay have responsibility for processing and distribution of mail for other such facilities in the surrounding geographic area; and\n**(B)**\nincludes a remotely managed post office, a part-time post office, and an administrative post office.\n**(2) Postal service**\nThe term Postal Service means the United States Postal Service.\n**(3) Temporary relocation**\nThe term temporary relocation means a temporary relocation of retail services from a post office to support Postal Service business for a holiday, special event, or overflow business, as described in paragraph (a)(2)(i) of section 241.4 of title 39, Code of Federal Regulations.\n#### 3. Requests for new post offices\nNot later than 90 days after the date of enactment of this Act, the Postal Service shall establish by regulation a formal process for a local government official to request a new post office within the locality.\n#### 4. Communication relating to post office relocation\nThe Postal Service shall amend section 241.4 of title 39, Code of Federal Regulations, to provide the following:\n**(1) Community input**\nThe Postal Service may not implement a temporary relocation, including for a commemorative event, for a period longer than 2 days without collecting and considering community input under paragraph (c) of that section.\n**(2) Notification**\n**(A) Elected officials**\nNot later than 30 days before the date of a temporary relocation, the Postal Service shall\u2014\n**(i)**\nsubmit to 1 or more local elected officials in the area in which the affected post office is located a written outline of the proposal; and\n**(ii)**\noffer to discuss the proposal with the elected official under paragraph (c) of that section.\n**(B) Public presentation**\nThe Postal Service shall\u2014\n**(i)**\nnot later than 15 days before the date of a temporary relocation, provide public notice of the temporary relocation in the area in which the affected post office is located; and\n**(ii)**\nnot later than 15 days after providing notice to local elected officials under subparagraph (A)(i), hold a public presentation under paragraph (c) of that section.\n**(3) Periodic updates**\nNot later than 60 days after the end of the initial 30-day comment period under paragraph (c) of that section, and every 60 days thereafter until the date that is 60 days after the last day of a temporary relocation, the Postal Service shall submit to relevant local government officials updates on the status of the temporary relocation.\n#### 5. Report\n##### (a) Report required\nWith respect to any temporary relocation for a period that is longer than 180 days (whether due to the originally projected length of the relocation or due to an extension), not later than 30 days after the first day of the temporary relocation (or of the extension that caused the length of the relocation to exceed 180 days, if applicable), the Postal Service shall submit a report relating to the temporary relocation or extension to\u2014\n**(1)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(2)**\nthe Committee on Oversight and Accountability of the House of Representatives ; and\n**(3)**\nthe members of Congress who represent the congressional district or State in which the affected post office is located.\n##### (b) Contents of report\nEach report described in subsection (a) shall include a discussion of\u2014\n**(1)**\nwhether the communication requirements were met within the required timelines, and if not, an explanation for the failure to comply with the requirements; and\n**(2)**\nwhether the period of the temporary relocation is being extended, and if so, an explanation for the extension.",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-21",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MAILS Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-28T13:22:48Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-28T13:22:48Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-04-28T13:22:48Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-28T13:22:48Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-04-28T13:22:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-17T18:14:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr765",
          "measure-number": "765",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr765v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>"
        },
        "title": "MAILS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr765.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr765"
    },
    "title": "MAILS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr765"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr765ih.xml"
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
      "title": "MAILS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAILS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mandating Advisable and Informed Locations and Solutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve communication between the United States Postal Service and local communities relating to the relocation and establishment of Postal Service retail service facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:32Z"
    }
  ]
}
```
