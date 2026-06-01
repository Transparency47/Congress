# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1081
- Title: Comprehensive NASA Reporting Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1081
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2026-03-13T14:23:56Z
- Update date including text: 2026-03-13T14:23:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-09-08 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.
- 2025-09-08 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 150.
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-09-08 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.
- 2025-09-08 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 150.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1081",
    "number": "1081",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Comprehensive NASA Reporting Act of 2025",
    "type": "S",
    "updateDate": "2026-03-13T14:23:56Z",
    "updateDateIncludingText": "2026-03-13T14:23:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 150.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-62.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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
            "date": "2025-09-08T20:13:59Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-14T20:50:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1081is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1081\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Cruz (for himself and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the National Aeronautics and Space Administration to submit certain reports to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Comprehensive NASA Reporting Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Aeronautics and Space Administration.\n**(2) NASA**\nThe term NASA means the National Aeronautics and Space Administration.\n#### 3. Reports to Congress\n##### (a) Congressional reports and notices\nAny report or notice provided to Congress by NASA shall be provided to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives, concurrently with its delivery to any other committee or office.\n##### (b) Privileged reports and reprogramming requests\nNonpublic reports, including privileged reports, reprogramming requests, and spend plans provided to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives pursuant to subsection (a) shall be treated as confidential committee documents and shall not to be disclosed publicly.\n##### (c) Reports on international agreements\nIf the United States becomes a signatory to an international agreement or nonbinding instrument concerning activities in outer space involving NASA, the Administrator shall, not later than 15 days after the date on which the United States becomes a signatory, submit to the Committee on Commerce, Science, and Transportation and the Committee on Foreign Relations of the Senate and the Committee on Science, Space, and Technology and the Committee on Foreign Affairs of the House of Representatives a report containing a copy of such agreement or instrument.",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1081rs.xml",
      "text": "II\nCalendar No. 150\n119th CONGRESS\n1st Session\nS. 1081\n[Report No. 119\u201362]\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Cruz (for himself and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 8, 2025 Reported by Mr. Cruz , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo require the Administrator of the National Aeronautics and Space Administration to submit certain reports to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Comprehensive NASA Reporting Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Aeronautics and Space Administration.\n**(2) NASA**\nThe term NASA means the National Aeronautics and Space Administration.\n#### 3. Reports to Congress\n##### (a) Congressional reports and notices\nAny report or notice final report or notification required by law that is provided to Congress by NASA shall be provided to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives , concurrently with not later than 10 days after its delivery to any other committee or office.\n##### (b) Privileged reports and reprogramming requests\nNonpublic reports, including privileged reports, reprogramming requests, and spend plans provided to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives pursuant to subsection (a) shall be treated as confidential committee documents and shall not to be disclosed publicly.\n##### (c) Reports on international agreements\nIf the United States becomes a signatory to an international agreement or nonbinding instrument concerning activities in outer space involving NASA, the Administrator shall, not later than 15 days after the date on which the United States becomes a signatory, submit to the Committee on Commerce, Science, and Transportation and the Committee on Foreign Relations of the Senate and the Committee on Science, Space, and Technology and the Committee on Foreign Affairs of the House of Representatives a report containing a copy of such agreement or instrument.",
      "versionDate": "2025-09-08",
      "versionType": "Reported in Senate"
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
            "updateDate": "2025-05-12T18:46:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-12T18:47:07Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-13T14:23:56Z"
          },
          {
            "name": "National Aeronautics and Space Administration",
            "updateDate": "2025-05-12T18:46:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-09T13:43:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119s1081",
          "measure-number": "1081",
          "measure-type": "s",
          "orig-publish-date": "2025-03-14",
          "originChamber": "SENATE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1081v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Comprehensive NASA Reporting Act of 2025</strong></p><p>This bill sets forth general requirements for the submission of reports and notices to Congress by the National Aeronautics and Space Administration (NASA).\u00a0</p><p>The bill also requires NASA to provide Congress with a copy of any international agreement or nonbinding instrument entered into by the United States that concerns NASA\u2019s activities in space.\u00a0</p>"
        },
        "title": "Comprehensive NASA Reporting Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1081.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Comprehensive NASA Reporting Act of 2025</strong></p><p>This bill sets forth general requirements for the submission of reports and notices to Congress by the National Aeronautics and Space Administration (NASA).\u00a0</p><p>The bill also requires NASA to provide Congress with a copy of any international agreement or nonbinding instrument entered into by the United States that concerns NASA\u2019s activities in space.\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1081"
    },
    "title": "Comprehensive NASA Reporting Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Comprehensive NASA Reporting Act of 2025</strong></p><p>This bill sets forth general requirements for the submission of reports and notices to Congress by the National Aeronautics and Space Administration (NASA).\u00a0</p><p>The bill also requires NASA to provide Congress with a copy of any international agreement or nonbinding instrument entered into by the United States that concerns NASA\u2019s activities in space.\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1081"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1081is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1081rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Comprehensive NASA Reporting Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-10T04:23:21Z"
    },
    {
      "title": "Comprehensive NASA Reporting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive NASA Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the National Aeronautics and Space Administration to submit certain reports to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:16Z"
    }
  ]
}
```
