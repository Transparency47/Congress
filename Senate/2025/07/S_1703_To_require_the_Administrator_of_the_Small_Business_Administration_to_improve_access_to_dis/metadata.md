# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1703?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1703
- Title: Rural Small Business Resilience Act
- Congress: 119
- Bill type: S
- Bill number: 1703
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-04-16T13:36:37Z
- Update date including text: 2026-04-16T13:36:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-16 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.
- 2025-07-29 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-07-29 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 131.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-16 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.
- 2025-07-29 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-07-29 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 131.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1703",
    "number": "1703",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Rural Small Business Resilience Act",
    "type": "S",
    "updateDate": "2026-04-16T13:36:37Z",
    "updateDateIncludingText": "2026-04-16T13:36:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 131.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
            "date": "2025-07-29T14:35:57Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-16T18:42:21Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-08T19:33:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1703is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1703\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Ms. Klobuchar (for herself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo require the Administrator of the Small Business Administration to improve access to disaster assistance for individuals located in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Small Business Resilience Act .\n#### 2. Access to disaster assistance for individuals located in rural areas\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Small Business Administration shall ensure that the Associate Administrator of the Office of Disaster Recovery and Resilience of the Administration takes such actions as necessary to ensure that individuals located in rural areas (as defined in paragraph (16) of section 7(b) of the Small Business Act ( 15 U.S.C. 636(b)(16) )) for which a disaster declaration has been made under such section 7(b) have full access to assistance provided under such section, including by providing targeted outreach and marketing materials to those individuals.\n#### 3. Technical amendment\nThe second paragraph (16) (relating to the statute of limitations) of section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is redesignated as paragraph (17).",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1703rs.xml",
      "text": "II\nCalendar No. 131\n119th CONGRESS\n1st Session\nS. 1703\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Ms. Klobuchar (for herself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nJuly 29, 2025 Reported by Ms. Ernst , without amendment\nA BILL\nTo require the Administrator of the Small Business Administration to improve access to disaster assistance for individuals located in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Small Business Resilience Act .\n#### 2. Access to disaster assistance for individuals located in rural areas\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Small Business Administration shall ensure that the Associate Administrator of the Office of Disaster Recovery and Resilience of the Administration takes such actions as necessary to ensure that individuals located in rural areas (as defined in paragraph (16) of section 7(b) of the Small Business Act ( 15 U.S.C. 636(b)(16) )) for which a disaster declaration has been made under such section 7(b) have full access to assistance provided under such section, including by providing targeted outreach and marketing materials to those individuals.\n#### 3. Technical amendment\nThe second paragraph (16) (relating to the statute of limitations) of section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is redesignated as paragraph (17).",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-02-26",
        "text": "Received in the Senate and Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "804",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Small Business Resilience Act",
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
            "name": "Disaster relief and insurance",
            "updateDate": "2025-08-28T19:45:51Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-08-28T19:45:51Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-08-28T19:45:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-28T13:33:51Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1703is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1703rs.xml"
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
      "title": "Rural Small Business Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Rural Small Business Resilience Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Small Business Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Small Business Administration to improve access to disaster assistance for individuals located in rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:19Z"
    }
  ]
}
```
