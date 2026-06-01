# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/108
- Title: Protecting Higher Education from the Chinese Communist Party Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 108
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-07-30T12:48:18Z
- Update date including text: 2025-07-30T12:48:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/108",
    "number": "108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Protecting Higher Education from the Chinese Communist Party Act of 2025",
    "type": "S",
    "updateDate": "2025-07-30T12:48:18Z",
    "updateDateIncludingText": "2025-07-30T12:48:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T17:39:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s108is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 108\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo make members of the Chinese Communist Party and their family members ineligible for F or J visas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Higher Education from the Chinese Communist Party Act of 2025 .\n#### 2. Ineligibility for certain visas of members of the Chinese Communist Party\n##### (a) Grounds for exclusion\nAn alien may not be accorded status or receive a visa under subparagraph (F) or (J) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) if the alien is a person who is, as of the date of enactment of this Act or at any time thereafter\u2014\n**(1)**\nany member of the Chinese Communist Party, including such a member who has served on the National Congress of the Chinese Communist Party; or\n**(2)**\na family member of a person described in paragraph (1).\n##### (b) Family member\nFor purposes of this section, the term family member means, with respect to a person, that person\u2019s spouse, child, parent, sibling, grandchild, niece, or nephew.\n##### (c) Exception To comply with United Nations Headquarters Agreement\nSubsection (a) shall not apply to an individual if admitting the individual to the United States is necessary to permit the United States to comply with the Agreement between the United Nations and the United States of America regarding the Headquarters of the United Nations, signed June 26, 1947, and entered into force November 21, 1947, and other applicable international obligations.\n##### (d) National security waiver\nThe President, or a designee of the President, may waive the application of subsection (a) if the President or such designee certifies in writing to the appropriate congressional committees that such waiver is in the national security interest of the United States.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
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
        "name": "Immigration",
        "updateDate": "2025-02-19T13:30:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s108",
          "measure-number": "108",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s108v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Higher Education from the Chinese Communist Party Act of 2025</strong></p><p>This bill prohibits certain members of the Chinese Communist Party (CCP) and their families from receiving an F (academic student) or J (exchange visitor) visa.</p><p>Specifically, this prohibition shall apply to any CCP member who has served in any position in the CCP since this bill's enactment. The prohibition shall also apply to a spouse, child, parent, sibling, grandchild, niece, or nephew of such an individual.</p><p>These prohibitions do not apply if an individual must be admitted for compliance with the United Nations headquarters agreement or other international obligations.\u00a0</p><p>The President may waive these prohibitions by certifying to Congress that the waiver is in the U.S. national interest.</p>"
        },
        "title": "Protecting Higher Education from the Chinese Communist Party Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s108.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Higher Education from the Chinese Communist Party Act of 2025</strong></p><p>This bill prohibits certain members of the Chinese Communist Party (CCP) and their families from receiving an F (academic student) or J (exchange visitor) visa.</p><p>Specifically, this prohibition shall apply to any CCP member who has served in any position in the CCP since this bill's enactment. The prohibition shall also apply to a spouse, child, parent, sibling, grandchild, niece, or nephew of such an individual.</p><p>These prohibitions do not apply if an individual must be admitted for compliance with the United Nations headquarters agreement or other international obligations.\u00a0</p><p>The President may waive these prohibitions by certifying to Congress that the waiver is in the U.S. national interest.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s108"
    },
    "title": "Protecting Higher Education from the Chinese Communist Party Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Higher Education from the Chinese Communist Party Act of 2025</strong></p><p>This bill prohibits certain members of the Chinese Communist Party (CCP) and their families from receiving an F (academic student) or J (exchange visitor) visa.</p><p>Specifically, this prohibition shall apply to any CCP member who has served in any position in the CCP since this bill's enactment. The prohibition shall also apply to a spouse, child, parent, sibling, grandchild, niece, or nephew of such an individual.</p><p>These prohibitions do not apply if an individual must be admitted for compliance with the United Nations headquarters agreement or other international obligations.\u00a0</p><p>The President may waive these prohibitions by certifying to Congress that the waiver is in the U.S. national interest.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s108"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s108is.xml"
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
      "title": "Protecting Higher Education from the Chinese Communist Party Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Higher Education from the Chinese Communist Party Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make members of the Chinese Communist Party and their family members ineligible for F or J visas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:22Z"
    }
  ]
}
```
