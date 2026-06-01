# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/155?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/155
- Title: MAILS Act
- Congress: 119
- Bill type: S
- Bill number: 155
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-12-05T22:05:35Z
- Update date including text: 2025-12-05T22:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/155",
    "number": "155",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "MAILS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:05:35Z",
    "updateDateIncludingText": "2025-12-05T22:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T16:38:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "ID"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s155is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 155\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Crapo (for himself, Mr. Risch , and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo improve communication between the United States Postal Service and local communities relating to the relocation and establishment of Postal Service retail service facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Post office**\nThe term post office \u2014\n**(A)**\nmeans a facility that\u2014\n**(i)**\nis owned or leased by the Postal Service;\n**(ii)**\nis managed by a Postmaster;\n**(iii)**\nhas responsibility for\u2014\n**(I)**\ncustomer services;\n**(II)**\nlocal delivery; and\n**(III)**\nreceipt and dispatch of all classes of mail; and\n**(iv)**\nmay have responsibility for processing and distribution of mail for other such facilities in the surrounding geographic area; and\n**(B)**\nincludes a remotely managed post office, a part-time post office, and an administrative post office.\n**(2) Postal service**\nThe term Postal Service means the United States Postal Service.\n**(3) Temporary relocation**\nThe term temporary relocation means a temporary relocation of retail services from a post office to support Postal Service business for a holiday, special event, or overflow business, as described in paragraph (a)(2)(i) of section 241.4 of title 39, Code of Federal Regulations.\n#### 3. Requests for new post offices\nNot later than 90 days after the date of enactment of this Act, the Postal Service shall establish by regulation a formal process for a local government official to request a new post office within the locality.\n#### 4. Communication relating to post office relocation\nThe Postal Service shall amend section 241.4 of title 39, Code of Federal Regulations, to provide the following:\n**(1) Community input**\nThe Postal Service may not implement a temporary relocation, including for a commemorative event, for a period longer than 2 days without collecting and considering community input under paragraph (c) of that section.\n**(2) Notification**\n**(A) Elected officials**\nNot later than 30 days before the date of a temporary relocation, the Postal Service shall\u2014\n**(i)**\nsubmit to 1 or more local elected officials in the area in which the affected post office is located a written outline of the proposal; and\n**(ii)**\noffer to discuss the proposal with the elected official under paragraph (c) of that section.\n**(B) Public presentation**\nThe Postal Service shall\u2014\n**(i)**\nnot later than 15 days before the date of a temporary relocation, provide public notice of the temporary relocation in the area in which the affected post office is located; and\n**(ii)**\nnot later than 15 days after providing notice to local elected officials under subparagraph (A)(i), hold a public presentation under paragraph (c) of that section.\n**(3) Periodic updates**\nNot later than 60 days after the end of the initial 30-day comment period under paragraph (c) of that section, and every 60 days thereafter until the date that is 60 days after the last day of a temporary relocation, the Postal Service shall submit to relevant local government officials updates on the status of the temporary relocation.\n#### 5. Report\n##### (a) Report required\nWith respect to any temporary relocation for a period that is longer than 180 days (whether due to the originally projected length of the relocation or due to an extension), not later than 30 days after the first day of the temporary relocation (or of the extension that caused the length of the relocation to exceed 180 days, if applicable), the Postal Service shall submit a report relating to the temporary relocation or extension to\u2014\n**(1)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(2)**\nthe Committee on Oversight and Accountability of the House of Representatives ; and\n**(3)**\nthe members of Congress who represent the congressional district or State in which the affected post office is located.\n##### (b) Contents of report\nEach report described in subsection (a) shall include a discussion of\u2014\n**(1)**\nwhether the communication requirements were met within the required timelines, and if not, an explanation for the failure to comply with the requirements; and\n**(2)**\nwhether the period of the temporary relocation is being extended, and if so, an explanation for the extension.",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "765",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MAILS Act",
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
            "updateDate": "2025-03-03T17:57:55Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-03T17:57:50Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-03-03T17:57:35Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-03T17:58:02Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-03-03T17:57:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-25T19:42:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s155",
          "measure-number": "155",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s155v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>"
        },
        "title": "MAILS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s155.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s155"
    },
    "title": "MAILS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mandating Advisable and Informed Locations and Solutions Act or the MAILS Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to\u00a0(1) establish a formal process for a local government official to request a new post office, and (2) modify how it communicates with local officials and the public about certain topics.</p><p>Specifically, USPS must modify existing regulations with respect to temporary relocations of postal retail services for holidays, special events, overflow business, and commemorative events. USPS may not implement any such temporary relocation for more than two days unless it first collects and considers community input. USPS must also provide specified notifications to local officials and the public, periodic updates to local officials, and a public presentation about such a relocation.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s155"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s155is.xml"
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
      "title": "MAILS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MAILS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mandating Advisable and Informed Locations and Solutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve communication between the United States Postal Service and local communities relating to the relocation and establishment of Postal Service retail service facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:26Z"
    }
  ]
}
```
