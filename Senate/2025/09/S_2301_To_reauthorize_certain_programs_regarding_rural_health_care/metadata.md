# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2301
- Title: Improving Care in Rural America Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2301
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-01-05T21:35:19Z
- Update date including text: 2026-01-05T21:35:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 153.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 153.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2301",
    "number": "2301",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Improving Care in Rural America Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-05T21:35:19Z",
    "updateDateIncludingText": "2026-01-05T21:35:19Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 153.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
            "date": "2025-09-08T21:24:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-16T15:39:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "WY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2301is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2301\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Scott of South Carolina (for himself, Ms. Smith , Ms. Lummis , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize certain programs regarding rural health care.\n#### 1. Short title\nThis Act may be cited as the Improving Care in Rural America Reauthorization Act of 2025 .\n#### 2. Rural health care services outreach, rural health network development, and small health care provider quality improvement grant programs\n##### (a) Rural health care services outreach grants\nSection 330A(e) of the Public Health Service Act ( 42 U.S.C. 254c(e) ) is amended by adding at the end the following:\n(4) Use of funds for rural underserved populations In awarding a grant under this subsection, the Director shall ensure that the funds made available through the grant will be used, as appropriate\u2014 (A) to meet the health care needs of rural underserved populations in the local community or region to be served; and (B) for other activities to ensure the rural underserved populations in the local community or region to be served will be involved in the development and ongoing operations of the project. .\n##### (b) Rural health network development grants\nSection 330A(f) of the Public Health Service Act ( 42 U.S.C. 254c(f) ) is amended by adding at the end the following:\n(4) Use of funds for rural underserved populations In awarding a grant under this subsection, the Director shall ensure that the funds made available through the grant will be used, as appropriate\u2014 (A) to increase access to quality health care services through integrated health care networks for the rural underserved populations in the local community or region to be served; and (B) for other activities to ensure the rural underserved populations in the local community or region to be served will benefit from and be involved in the planning, development, and ongoing implementation of the network. .\n##### (c) Reauthorization\nSection 330A(j) of the Public Health Service Act ( 42 U.S.C. 254c(j) ) is amended by striking 2021 through 2025 and inserting 2026 through 2030 .",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2301rs.xml",
      "text": "II\nCalendar No. 153\n119th CONGRESS\n1st Session\nS. 2301\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Scott of South Carolina (for himself, Ms. Smith , Ms. Lummis , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nSeptember 8, 2025 Reported by Mr. Cassidy , without amendment\nA BILL\nTo reauthorize certain programs regarding rural health care.\n#### 1. Short title\nThis Act may be cited as the Improving Care in Rural America Reauthorization Act of 2025 .\n#### 2. Rural health care services outreach, rural health network development, and small health care provider quality improvement grant programs\n##### (a) Rural health care services outreach grants\nSection 330A(e) of the Public Health Service Act ( 42 U.S.C. 254c(e) ) is amended by adding at the end the following:\n(4) Use of funds for rural underserved populations In awarding a grant under this subsection, the Director shall ensure that the funds made available through the grant will be used, as appropriate\u2014 (A) to meet the health care needs of rural underserved populations in the local community or region to be served; and (B) for other activities to ensure the rural underserved populations in the local community or region to be served will be involved in the development and ongoing operations of the project. .\n##### (b) Rural health network development grants\nSection 330A(f) of the Public Health Service Act ( 42 U.S.C. 254c(f) ) is amended by adding at the end the following:\n(4) Use of funds for rural underserved populations In awarding a grant under this subsection, the Director shall ensure that the funds made available through the grant will be used, as appropriate\u2014 (A) to increase access to quality health care services through integrated health care networks for the rural underserved populations in the local community or region to be served; and (B) for other activities to ensure the rural underserved populations in the local community or region to be served will benefit from and be involved in the planning, development, and ongoing implementation of the network. .\n##### (c) Reauthorization\nSection 330A(j) of the Public Health Service Act ( 42 U.S.C. 254c(j) ) is amended by striking 2021 through 2025 and inserting 2026 through 2030 .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-10-03",
        "text": "Placed on the Union Calendar, Calendar No. 278."
      },
      "number": "2493",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Care in Rural America Reauthorization Act of 2025",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-09-16T14:08:28Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:08:28Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-09-16T14:08:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-05T15:10:01Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2301is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2301rs.xml"
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
      "title": "Improving Care in Rural America Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-10T04:08:22Z"
    },
    {
      "title": "Improving Care in Rural America Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Care in Rural America Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T12:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize certain programs regarding rural health care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T12:18:22Z"
    }
  ]
}
```
