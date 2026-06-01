# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4974?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4974
- Title: DETECT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4974
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-04-08T16:57:10Z
- Update date including text: 2026-04-08T16:57:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4974",
    "number": "4974",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "DETECT Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T16:57:10Z",
    "updateDateIncludingText": "2026-04-08T16:57:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
        "item": {
          "date": "2025-08-15T16:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "AZ"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "IA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "WA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4974ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4974\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Buchanan (for himself, Mr. Schweikert , Ms. Tenney , Mr. Bean of Florida , Mr. Feenstra , Mr. Smith of Washington , and Mr. Moran ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Comptroller General to submit a report to the appropriate committees of Congress on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.\n#### 1. Short title\nThis Act may be cited as the Digital Evaluation for Tax Enforcement and Compliance Tracking Act of 2025 or the DETECT Act of 2025 .\n#### 2. Report on potential for use of artificial intelligence to detect tax fraud\nThe Comptroller General shall, not later than 180 days after the date of the enactment of this Act, submit a report to the Committee on Ways and Means of the House of Representatives and to the Committee on Finance of the Senate on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.",
      "versionDate": "2025-08-15",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-05T16:06:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-15",
    "originChamber": "House",
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
          "measure-id": "id119hr4974",
          "measure-number": "4974",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-15",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4974v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-08-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Digital Evaluation for Tax Enforcement and Compliance Tracking Act of 2025 or the DETECT Act of 2025</strong></p><p>This bill directs the Government Accountability Office to submit a report to Congress within 180 days from the date of enactment on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.</p>"
        },
        "title": "DETECT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4974.xml",
    "summary": {
      "actionDate": "2025-08-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Digital Evaluation for Tax Enforcement and Compliance Tracking Act of 2025 or the DETECT Act of 2025</strong></p><p>This bill directs the Government Accountability Office to submit a report to Congress within 180 days from the date of enactment on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr4974"
    },
    "title": "DETECT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-08-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Digital Evaluation for Tax Enforcement and Compliance Tracking Act of 2025 or the DETECT Act of 2025</strong></p><p>This bill directs the Government Accountability Office to submit a report to Congress within 180 days from the date of enactment on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr4974"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4974ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "DETECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DETECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Digital Evaluation for Tax Enforcement and Compliance Tracking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General to submit a report to the appropriate committees of Congress on the potential of artificial intelligence to assist the Internal Revenue Service in detecting tax fraud.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T06:33:22Z"
    }
  ]
}
```
