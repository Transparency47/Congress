# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1023
- Title: Social Security Overpayment Relief Act
- Congress: 119
- Bill type: S
- Bill number: 1023
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-05T22:51:57Z
- Update date including text: 2025-12-05T22:51:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1023",
    "number": "1023",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Social Security Overpayment Relief Act",
    "type": "S",
    "updateDate": "2025-12-05T22:51:57Z",
    "updateDateIncludingText": "2025-12-05T22:51:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
        "item": {
          "date": "2025-03-13T16:40:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1023is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1023\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Gallego (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Social Security Act to limit the recovery of overpayments under titles II and XVI to a 10-year period.\n#### 1. Short title\nThis Act may be cited as the Social Security Overpayment Relief Act .\n#### 2. Limitation on recovery of overpayments\n##### (a) Title II limitation\nSection 204 of the Social Security Act ( 42 U.S.C. 404 ) is amended by adding at the end the following:\n(h) In any case in which more than the correct amount of payment has been made, there shall be no adjustment of payments to, or recovery by the United States from, any person of an overpayment that occurred 10 or more years prior to the date on which the Commissioner finds that more than the correct amount of payment has been made to such person. .\n##### (b) Title XVI limitation\nSection 1631(b) of such Act ( 42 U.S.C. 1383(b) ) is amended by adding at the end the following:\n(9) In any case in which more than the correct amount of payment has been made, there shall be no adjustment of payments to, or recovery by the United States from, any person of an overpayment that occurred 10 or more years prior to the date on which the Commissioner finds that more than the correct amount of payment has been made to such person. .",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2142",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Social Security Overpayment Relief Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-31T14:30:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1023",
          "measure-number": "1023",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1023v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>"
        },
        "title": "Social Security Overpayment Relief Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1023.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s1023"
    },
    "title": "Social Security Overpayment Relief Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Social Security Overpayment Relief Act</strong></p><p>This bill prohibits the Social Security Administration from collecting overpayments made in error to Social Security or Supplemental Security Income recipients 10 or more years prior to the discovery of the error by the administration. This prohibition extends to the collection of funds directly from overpaid recipients and to the adjustment of future payments to those recipients.\u00a0</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s1023"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1023is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-03-28T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Social Security Overpayment Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Social Security Act to limit the recovery of overpayments under titles II and XVI to a 10-year period.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:38Z"
    }
  ]
}
```
