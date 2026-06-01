# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/180?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/180
- Title: Protecting First Responders from Secondary Exposure Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 180
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 77.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 77.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/180",
    "number": "180",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Protecting First Responders from Secondary Exposure Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 77.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
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
            "date": "2025-05-20T20:22:53Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-22T16:32:41Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "DE"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s180is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 180\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Grassley (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize the use of grant amounts for providing training and resources for first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances, and purchasing such containment devices for use by first responders.\n#### 1. Short title\nThis Act may be cited as the Protecting First Responders from Secondary Exposure Act of 2025 .\n#### 2. Preventing first responder secondary exposure to fentanyl\nSection 3021(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (4) through (10) as paragraphs (5) through (11), respectively; and\n**(2)**\nby inserting after paragraph (3) the following:\n(4) Providing training and resources for first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances, and purchasing such containment devices for use by first responders. .",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s180rs.xml",
      "text": "II\nCalendar No. 77\n119th CONGRESS\n1st Session\nS. 180\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Grassley (for himself, Ms. Klobuchar , Mr. Durbin , Mrs. Moody , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize the use of grant amounts for providing training and resources for first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances, and purchasing such containment devices for use by first responders.\n#### 1. Short title\nThis Act may be cited as the Protecting First Responders from Secondary Exposure Act of 2025 .\n#### 2. Preventing first responder secondary exposure to fentanyl\nSection 3021(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (4) through (10) as paragraphs (5) through (11), respectively; and\n**(2)**\nby inserting after paragraph (3) the following:\n(4) Providing training and resources for first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances, and purchasing such containment devices for use by first responders. .",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "621",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting First Responders from Secondary Exposure Act of 2025",
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
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-03-17T14:53:55Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-17T14:53:55Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-03-17T14:53:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-21T15:15:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119s180",
          "measure-number": "180",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s180v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting First Responders from Secondary Exposure Act of 2025\u00a0</strong></p><p>This bill expands the allowable uses of grant funds under the Comprehensive Opioid, Stimulant, and Substance Use\u00a0Program administered by the Department of Justice.</p><p>Specifically, the bill allows grants to be used for purchasing containment devices for first responders and training first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances.</p>"
        },
        "title": "Protecting First Responders from Secondary Exposure Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s180.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting First Responders from Secondary Exposure Act of 2025\u00a0</strong></p><p>This bill expands the allowable uses of grant funds under the Comprehensive Opioid, Stimulant, and Substance Use\u00a0Program administered by the Department of Justice.</p><p>Specifically, the bill allows grants to be used for purchasing containment devices for first responders and training first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s180"
    },
    "title": "Protecting First Responders from Secondary Exposure Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting First Responders from Secondary Exposure Act of 2025\u00a0</strong></p><p>This bill expands the allowable uses of grant funds under the Comprehensive Opioid, Stimulant, and Substance Use\u00a0Program administered by the Department of Justice.</p><p>Specifically, the bill allows grants to be used for purchasing containment devices for first responders and training first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s180"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s180is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s180rs.xml"
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
      "title": "Protecting First Responders from Secondary Exposure Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Protecting First Responders from Secondary Exposure Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting First Responders from Secondary Exposure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize the use of grant amounts for providing training and resources for first responders on the use of containment devices to prevent secondary exposure to fentanyl and other potentially lethal substances, and purchasing such containment devices for use by first responders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:24Z"
    }
  ]
}
```
