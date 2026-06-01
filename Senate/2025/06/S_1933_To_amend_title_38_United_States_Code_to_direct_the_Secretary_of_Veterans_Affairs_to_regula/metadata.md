# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1933?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1933
- Title: Informing VETS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1933
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2026-03-27T13:58:03Z
- Update date including text: 2026-03-27T13:58:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1933",
    "number": "1933",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Informing VETS Act of 2025",
    "type": "S",
    "updateDate": "2026-03-27T13:58:03Z",
    "updateDateIncludingText": "2026-03-27T13:58:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T18:48:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1933is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1933\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Mr. Cassidy (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to regularly promote programs under chapter 31 of such title.\n#### 1. Short title\nThis Act may be cited as the Informing Veterans on Education for Transitioning Servicemembers Act of 2025 or the Informing VETS Act of 2025 .\n#### 2. Information campaign regarding Veteran Readiness and Employment Program\nSection 3116 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(c) The Secretary shall regularly promote programs under this chapter by\u2014 (1) sending a letter to each veteran entitled to such a program that explains the educational benefits of such programs; and (2) providing a side-by-side comparison of benefits between such programs and educational assistance under chapter 33 of this title\u2014 (A) with each letter under paragraph (1); and (B) on a publicly accessible website of the Department. .",
      "versionDate": "2025-06-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T18:07:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-03",
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
          "measure-id": "id119s1933",
          "measure-number": "1933",
          "measure-type": "s",
          "orig-publish-date": "2025-06-03",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1933v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-06-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Informing Veterans on Education for Transitioning Servicemembers Act of 2025 or the Informing VETS Act</strong> <strong>of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to regularly promote the Veteran Readiness and Employment program by sending a letter to each veteran entitled to the program. The letter must explain the educational benefits of the program and provide\u00a0a side-by-side comparison of benefits between the program and Post-9/11 GI Bill educational assistance. Such comparison must also be made available online.</p>"
        },
        "title": "Informing VETS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1933.xml",
    "summary": {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Informing Veterans on Education for Transitioning Servicemembers Act of 2025 or the Informing VETS Act</strong> <strong>of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to regularly promote the Veteran Readiness and Employment program by sending a letter to each veteran entitled to the program. The letter must explain the educational benefits of the program and provide\u00a0a side-by-side comparison of benefits between the program and Post-9/11 GI Bill educational assistance. Such comparison must also be made available online.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1933"
    },
    "title": "Informing VETS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Informing Veterans on Education for Transitioning Servicemembers Act of 2025 or the Informing VETS Act</strong> <strong>of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to regularly promote the Veteran Readiness and Employment program by sending a letter to each veteran entitled to the program. The letter must explain the educational benefits of the program and provide\u00a0a side-by-side comparison of benefits between the program and Post-9/11 GI Bill educational assistance. Such comparison must also be made available online.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1933"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1933is.xml"
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
      "title": "Informing VETS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Informing VETS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Informing Veterans on Education for Transitioning Servicemembers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to regularly promote programs under chapter 31 of such title.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:16Z"
    }
  ]
}
```
