# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/419?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/419
- Title: Reauthorizing Support and Treatment for Officers in Crisis Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 419
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-12-05T21:51:32Z
- Update date including text: 2025-12-05T21:51:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 79.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 79.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/419",
    "number": "419",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:51:32Z",
    "updateDateIncludingText": "2025-12-05T21:51:32Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 79.",
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
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
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
            "date": "2025-05-20T20:21:33Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-05T20:08:04Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "RI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "HI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "DE"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "IA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "MT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NV"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "GA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s419is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 419\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Hawley (for himself, Mr. Whitehouse , Mr. Blumenthal , Ms. Hirono , Mr. Coons , Mr. Grassley , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to reauthorize grants to support law enforcement officers and families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reauthorizing Support and Treatment for Officers in Crisis Act of 2025 .\n#### 2. Reauthorization\nSection 1001(a)(21) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a)(21) ) is amended by striking 2020 through 2024 and inserting 2025 through 2029 .",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s419rs.xml",
      "text": "II\nCalendar No. 79\n119th CONGRESS\n1st Session\nS. 419\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Hawley (for himself, Mr. Whitehouse , Mr. Blumenthal , Ms. Hirono , Mr. Coons , Mr. Grassley , Mr. Welch , Mr. Booker , Ms. Klobuchar , Mr. Durbin , Mr. Sheehy , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to reauthorize grants to support law enforcement officers and families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reauthorizing Support and Treatment for Officers in Crisis Act of 2025 .\n#### 2. Reauthorization\nSection 1001(a)(21) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a)(21) ) is amended by striking 2020 through 2024 and inserting 2025 through 2029 .",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5282",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025",
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
            "name": "Family services",
            "updateDate": "2025-04-11T18:44:28Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-04-11T18:44:28Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-04-11T18:44:28Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-11T18:44:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-11T13:05:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s419",
          "measure-number": "419",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s419v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Reauthorizing Support and Treatment for Officers in Crisis Act of 2025</strong></p><p>This bill reauthorizes through FY2029 grants for\u00a0state and local law enforcement agencies and other organizations to provide family support services and mental health services to law enforcement personnel.</p>"
        },
        "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s419.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reauthorizing Support and Treatment for Officers in Crisis Act of 2025</strong></p><p>This bill reauthorizes through FY2029 grants for\u00a0state and local law enforcement agencies and other organizations to provide family support services and mental health services to law enforcement personnel.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s419"
    },
    "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reauthorizing Support and Treatment for Officers in Crisis Act of 2025</strong></p><p>This bill reauthorizes through FY2029 grants for\u00a0state and local law enforcement agencies and other organizations to provide family support services and mental health services to law enforcement personnel.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s419"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s419is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s419rs.xml"
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
      "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T11:03:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to reauthorize grants to support law enforcement officers and families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:50Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reauthorizing Support and Treatment for Officers in Crisis Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:26:25Z"
    }
  ]
}
```
