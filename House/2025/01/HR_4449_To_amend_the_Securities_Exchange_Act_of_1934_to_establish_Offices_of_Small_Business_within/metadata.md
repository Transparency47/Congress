# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4449
- Title: Advocating for Small Business Act
- Congress: 119
- Bill type: HR
- Bill number: 4449
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-02-04T04:26:30Z
- Update date including text: 2026-02-04T04:26:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 50 - 4.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 207.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-250.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-250.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 50 - 4.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 207.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-250.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-250.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4449",
    "number": "4449",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000581",
        "district": "34",
        "firstName": "Vicente",
        "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
        "lastName": "Gonzalez",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Advocating for Small Business Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:30Z",
    "updateDateIncludingText": "2026-02-04T04:26:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-09-08",
      "calendarNumber": {
        "calendar": "U00207"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 207.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-250.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-250.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 50 - 4.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
        "item": [
          {
            "date": "2025-09-08T17:47:05Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-22T15:48:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-16T14:06:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4449ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4449\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Vicente Gonzalez of Texas (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to establish Offices of Small Business within rule writing divisions of the Securities and Exchange Commission to coordinate on rules and policy priorities related to capital formation.\n#### 1. Short title\nThis Act may be cited as the Advocating for Small Business Act .\n#### 2. Making the SEC even more small business friendly\nSection 4 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78d ) is amended by adding at the end the following:\n(l) Offices of Small Business The Commission shall establish, within each division of the Commission that performs rule writing activities, an Office of Small Business, which shall coordinate with the Office of the Advocate for Small Business Capital Formation on rules and policy priorities related to capital formation. .",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4449rh.xml",
      "text": "IB\nUnion Calendar No. 207\n119th CONGRESS\n1st Session\nH. R. 4449\n[Report No. 119\u2013250]\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Vicente Gonzalez of Texas (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Financial Services\nSeptember 8, 2025 Additional sponsor: Mr. Fitzpatrick\nSeptember 8, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Securities Exchange Act of 1934 to establish Offices of Small Business within rule writing divisions of the Securities and Exchange Commission to coordinate on rules and policy priorities related to capital formation.\n#### 1. Short title\nThis Act may be cited as the Advocating for Small Business Act .\n#### 2. Making the SEC even more small business friendly\nSection 4 of the Securities Exchange Act of 1934 (15 U.S.C. 78d) is amended by adding at the end the following:\n(l) Offices of Small Business The Commission shall establish, within each division of the Commission that performs rule writing activities, an Office of Small Business, which shall coordinate with the Office of the Advocate for Small Business Capital Formation on rules and policy priorities related to capital formation. .",
      "versionDate": "",
      "versionType": "Reported in House"
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-28T13:03:07Z"
          },
          {
            "name": "Business investment and capital",
            "updateDate": "2025-08-28T13:00:28Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-08-28T13:00:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-29T13:42:46Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4449ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4449rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Advocating for Small Business Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-09T07:08:25Z"
    },
    {
      "title": "Advocating for Small Business Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advocating for Small Business Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-18T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to establish Offices of Small Business within rule writing divisions of the Securities and Exchange Commission to coordinate on rules and policy priorities related to capital formation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-18T08:48:16Z"
    }
  ]
}
```
