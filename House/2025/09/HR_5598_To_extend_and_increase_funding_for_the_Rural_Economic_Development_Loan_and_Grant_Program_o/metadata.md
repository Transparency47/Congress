# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5598
- Title: Revitalizing Rural Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5598
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-02-03T09:05:46Z
- Update date including text: 2026-02-03T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5598",
    "number": "5598",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Revitalizing Rural Communities Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:46Z",
    "updateDateIncludingText": "2026-02-03T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5598ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5598\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Nunn of Iowa (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo extend and increase funding for the Rural Economic Development Loan and Grant Program of the Department of Agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Revitalizing Rural Communities Act of 2025 .\n#### 2. Extension of, and increase in funding for, the Rural Economic Development Loan and Grant Program\nSection 313B of the Rural Electrification Act of 1936 ( 7 U.S.C. 940c\u20132 ) is amended by striking $10,000,000 for each of fiscal years 2019 through 2023 and inserting $12,000,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-09-26",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-29T18:22:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-26",
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
          "measure-id": "id119hr5598",
          "measure-number": "5598",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-26",
          "originChamber": "HOUSE",
          "update-date": "2025-09-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5598v00",
            "update-date": "2025-09-30"
          },
          "action-date": "2025-09-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Revitalizing Rural Communities Act of 2025 </strong></p><p>This bill reauthorizes the Department of Agriculture's Rural Economic Development Loan and Grant program through FY2030\u00a0to provide funding for rural projects through local utility organizations.</p>"
        },
        "title": "Revitalizing Rural Communities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5598.xml",
    "summary": {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Revitalizing Rural Communities Act of 2025 </strong></p><p>This bill reauthorizes the Department of Agriculture's Rural Economic Development Loan and Grant program through FY2030\u00a0to provide funding for rural projects through local utility organizations.</p>",
      "updateDate": "2025-09-30",
      "versionCode": "id119hr5598"
    },
    "title": "Revitalizing Rural Communities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Revitalizing Rural Communities Act of 2025 </strong></p><p>This bill reauthorizes the Department of Agriculture's Rural Economic Development Loan and Grant program through FY2030\u00a0to provide funding for rural projects through local utility organizations.</p>",
      "updateDate": "2025-09-30",
      "versionCode": "id119hr5598"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5598ih.xml"
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
      "title": "Revitalizing Rural Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Revitalizing Rural Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T08:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To extend and increase funding for the Rural Economic Development Loan and Grant Program of the Department of Agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T08:18:27Z"
    }
  ]
}
```
