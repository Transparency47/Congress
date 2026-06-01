# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2142
- Title: Social Security Overpayment Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2142
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-03-25T08:06:00Z
- Update date including text: 2026-03-25T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2142",
    "number": "2142",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Social Security Overpayment Relief Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:00Z",
    "updateDateIncludingText": "2026-03-25T08:06:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:00:30Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "IA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "RI"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2142ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2142\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Ms. McDonald Rivet (for herself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Social Security Act to limit the recovery of overpayments under titles II and XVI to a ten-year period.\n#### 1. Short title\nThis Act may be cited as the Social Security Overpayment Relief Act .\n#### 2. Limitation on recovery of overpayments\n##### (a) Title II limitation\nSection 204 of the Social Security Act ( 42 U.S.C. 404 ) is amended by adding at the end the following:\n(h) In any case in which more than the correct amount of payment has been made, there shall be no adjustment of payments to, or recovery by the United States from, any person of an overpayment that occurred 10 or more years prior to the date on which the Commissioner finds that more than the correct amount of payment has been made to such person. .\n##### (b) Title XVI limitation\nSection 1631(b) of such Act ( 42 U.S.C. 1383(b) ) is amended by adding at the end the following:\n(9) In any case in which more than the correct amount of payment has been made, there shall be no adjustment of payments to, or recovery by the United States from, any person of an overpayment that occurred 10 or more years prior to the date on which the Commissioner finds that more than the correct amount of payment has been made to such person. .",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1023",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Social Security Overpayment Relief Act",
      "type": "S"
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
        "name": "Social Welfare",
        "updateDate": "2025-03-31T16:16:16Z"
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
          "measure-id": "id119hr2142",
          "measure-number": "2142",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2142v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>"
        },
        "title": "Social Security Overpayment Relief Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2142.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2142"
    },
    "title": "Social Security Overpayment Relief Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2142"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2142ih.xml"
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
      "title": "Social Security Overpayment Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Overpayment Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Social Security Act to limit the recovery of overpayments under titles II and XVI to a ten-year period.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:05Z"
    }
  ]
}
```
