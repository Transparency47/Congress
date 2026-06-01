# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/972
- Title: Fairness in Veterans' Education Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 972
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-01-22T20:42:02Z
- Update date including text: 2026-01-22T20:42:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 288.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 288.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/972",
    "number": "972",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Fairness in Veterans' Education Act of 2025",
    "type": "S",
    "updateDate": "2026-01-22T20:42:02Z",
    "updateDateIncludingText": "2026-01-22T20:42:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 288.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
            "date": "2025-12-09T17:52:58Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T20:00:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T22:56:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "AZ"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s972is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 972\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2025 Mr. Banks (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to ensure that the Secretary of Veterans Affairs repays members of the Armed Forces for certain contributions made by such members towards Post-9/11 Educational Assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness in Veterans' Education Act of 2025 .\n#### 2. Repayment of members of the Armed Forces for contributions toward Post-9/11 Educational Assistance\n##### (a) In general\nSection 3327(f)(3) of title 38, United States Code, is amended by striking together and all that follows through (as applicable), .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on August 1, 2025.",
      "versionDate": "2025-03-11",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s972rs.xml",
      "text": "II\nCalendar No. 288\n119th CONGRESS\n1st Session\nS. 972\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2025 Mr. Banks (for himself, Mr. Gallego , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nDecember 9, 2025 Reported by Mr. Moran , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend title 38, United States Code, to ensure that the Secretary of Veterans Affairs repays members of the Armed Forces for certain contributions made by such members towards Post-9/11 Educational Assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness in Veterans' Education Act of 2025 .\n#### 2. Repayment of members of the Armed Forces for contributions toward Post-9/11 Educational Assistance\n##### (a) In general\nSection 3327(f)(3) of title 38, United States Code, is amended by striking together and all that follows through (as applicable), .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on August 1, 2025.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2025-09-26",
        "text": "Placed on the Union Calendar, Calendar No. 262."
      },
      "number": "1458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "VETS Opportunity Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-09",
        "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote."
      },
      "number": "1872",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fairness in Veterans\u2019 Education Act",
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
            "name": "Higher education",
            "updateDate": "2025-04-01T15:31:40Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-04-01T15:31:40Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-04-01T15:31:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T15:42:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s972",
          "measure-number": "972",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s972v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fairness in Veterans\u2019 Education Act of 2025</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>"
        },
        "title": "Fairness in Veterans' Education Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s972.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness in Veterans\u2019 Education Act of 2025</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s972"
    },
    "title": "Fairness in Veterans' Education Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness in Veterans\u2019 Education Act of 2025</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s972"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s972is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s972rs.xml"
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
      "title": "Fairness in Veterans' Education Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-12-11T04:08:20Z"
    },
    {
      "title": "Fairness in Veterans' Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness in Veterans' Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to ensure that the Secretary of Veterans Affairs repays members of the Armed Forces for certain contributions made by such members towards Post-9/11 Educational Assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T10:48:21Z"
    }
  ]
}
```
