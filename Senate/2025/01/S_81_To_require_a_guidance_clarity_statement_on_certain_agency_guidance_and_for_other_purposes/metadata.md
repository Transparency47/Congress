# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/81?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/81
- Title: Guidance Clarity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 81
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 250.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 250.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/81",
    "number": "81",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Guidance Clarity Act of 2025",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 250.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
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
            "date": "2025-11-03T21:58:10Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-13T23:26:53Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "WI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "FL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s81is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 81\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Lankford (for himself and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require a guidance clarity statement on certain agency guidance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guidance Clarity Act of 2025 .\n#### 2. Guidance clarity statement required\n##### (a) Requirement\nEach agency, as defined in section 551 of title 5, United States Code, shall include a guidance clarity statement as described in subsection (b) on any guidance issued by that agency under section 553(b)(3)(A) of title 5, United States Code, on and after the date that is 30 days after the date on which the Director of the Office of Management and Budget issues the guidance required under subsection (c).\n##### (b) Guidance clarity statement\nA guidance clarity statement required under subsection (a) shall\u2014\n**(1)**\nbe displayed prominently on the first page of the document; and\n**(2)**\ninclude the following: The contents of this document do not have the force and effect of law and do not, of themselves, bind the public or the agency. This document is intended only to provide clarity to the public regarding existing requirements under the law or agency policies. .\n##### (c) OMB guidance\nNot later than 90 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall issue guidance to implement this Act.",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s81rs.xml",
      "text": "II\nCalendar No. 250\n119th CONGRESS\n1st Session\nS. 81\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Lankford (for himself, Mr. Johnson , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nNovember 3, 2025 Reported by Mr. Paul , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require a guidance clarity statement on certain agency guidance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guidance Clarity Act of 2025 .\n#### 2. Guidance clarity statement required\n##### (a) Requirement\nEach agency, as defined in section 551 of title 5, United States Code, shall include a guidance clarity statement as described in subsection (b) on any guidance issued by that agency under section 553(b)(3)(A) of title 5, United States Code, on and after the date that is 30 days after the date on which the Director of the Office of Management and Budget issues the guidance required under subsection (c).\n##### (b) Guidance clarity statement\nA guidance clarity statement required under subsection (a) shall\u2014\n**(1)**\nbe displayed prominently on the first page of the document; and\n**(2)**\ninclude the following: The contents of this document do not have the force and effect of law and do not, of themselves, bind the public or the agency. This document is intended only to provide clarity to the public regarding existing requirements under the law or agency policies. .\n##### (c) OMB guidance\nNot later than 90 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall issue guidance to implement this Act.",
      "versionDate": "",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-24",
        "text": "Placed on the Union Calendar, Calendar No. 490."
      },
      "number": "2409",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Related bill"
          },
          {
            "identifiedBy": "CRS",
            "type": "Identical bill"
          }
        ]
      },
      "title": "Guidance Clarity Act of 2025",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-24T19:41:12Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-24T19:41:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T16:00:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119s81",
          "measure-number": "81",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s81v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Guidance Clarity Act of 2025</strong><br/><br/>This bill requires federal agencies to state on the first page of guidance documents that such guidance (1) does not have the force and effect of law, and (2) is intended only to provide clarity to the public about existing legal requirements or agency policies.</p>"
        },
        "title": "Guidance Clarity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s81.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guidance Clarity Act of 2025</strong><br/><br/>This bill requires federal agencies to state on the first page of guidance documents that such guidance (1) does not have the force and effect of law, and (2) is intended only to provide clarity to the public about existing legal requirements or agency policies.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119s81"
    },
    "title": "Guidance Clarity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guidance Clarity Act of 2025</strong><br/><br/>This bill requires federal agencies to state on the first page of guidance documents that such guidance (1) does not have the force and effect of law, and (2) is intended only to provide clarity to the public about existing legal requirements or agency policies.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119s81"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s81is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s81rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Guidance Clarity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Guidance Clarity Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guidance Clarity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a guidance clarity statement on certain agency guidance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:30Z"
    }
  ]
}
```
