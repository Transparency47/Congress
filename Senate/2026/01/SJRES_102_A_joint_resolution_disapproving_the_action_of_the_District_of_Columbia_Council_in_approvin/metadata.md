# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/102
- Title: A joint resolution disapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.
- Congress: 119
- Bill type: SJRES
- Bill number: 102
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-02-05T11:56:25Z
- Update date including text: 2026-02-05T11:56:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2026-02-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 314.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2026-02-04 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2026-02-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 314.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/102",
    "number": "102",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.",
    "type": "SJRES",
    "updateDate": "2026-02-05T11:56:25Z",
    "updateDateIncludingText": "2026-02-05T11:56:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 314.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-04",
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
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
            "date": "2026-02-04T16:01:57Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-04T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-27T20:56:29Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "IA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "OK"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "ND"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MO"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres102is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 102\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mr. Scott of Florida introduced the following joint resolution; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nJOINT RESOLUTION\nDisapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.\nThat Congress disapproves of the action of the District of Columbia Council described as follows: D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025 (D.C. Act A26\u20130217), enacted by the District of Columbia Council on December 20, 2025, and transmitted to Congress pursuant to section 602(c)(1) of the District of Columbia Home Rule Act on December 30, 2025.",
      "versionDate": "2026-01-27",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres102rs.xml",
      "text": "IIA\nCalendar No. 314\n119th CONGRESS\n2d Session\nS. J. RES. 102\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mr. Scott of Florida (for himself, Mrs. Blackburn , Ms. Ernst , Mr. Marshall , Mr. Mullin , Mr. Cramer , Mr. Moreno , Mr. Schmitt , and Mrs. Moody ) introduced the following joint resolution; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nFebruary 4, 2026 Reported by Mr. Paul , without amendment\nJOINT RESOLUTION\nDisapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.\nThat Congress disapproves of the action of the District of Columbia Council described as follows: D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025 (D.C. Act A26\u20130217), enacted by the District of Columbia Council on December 20, 2025, and transmitted to Congress pursuant to section 602(c)(1) of the District of Columbia Home Rule Act on December 30, 2025.",
      "versionDate": "2026-02-04",
      "versionType": "RS"
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
        "name": "Taxation",
        "updateDate": "2026-02-03T21:19:34Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres102is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres102rs.xml"
        }
      ],
      "type": "RS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T16:18:18Z"
    },
    {
      "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the D.C. Income and Franchise Tax Conformity and Revision Temporary Amendment Act of 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T11:56:18Z"
    }
  ]
}
```
