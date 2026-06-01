# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3662?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3662
- Title: ACCESS Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3662
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-03-18T20:13:02Z
- Update date including text: 2026-03-18T20:13:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3662",
    "number": "3662",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "ACCESS Act of 2026",
    "type": "S",
    "updateDate": "2026-03-18T20:13:02Z",
    "updateDateIncludingText": "2026-03-18T20:13:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T17:16:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3662is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3662\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. McCormick (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Securities Act of 1933 to raise the offering amount threshold for when issuers using the crowdfunding exemption are required to file financial statements reviewed by a public accountant who is independent of the issuer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2026 or the ACCESS Act of 2026 .\n#### 2. Offering threshold for reviews by public accountant\n##### (a) In general\nSection 4A of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131 ) is amended\u2014\n**(1)**\nin subsection (b)(1)(D)\u2014\n**(A)**\nin clause (i), in the matter preceding subclause (I), by striking $100,000 and inserting $250,000 ; and\n**(B)**\nin clause (ii), by striking $100,000 and inserting $250,000 ; and\n**(2)**\nby adding at the end the following:\n(i) Discretion To adjust amount The Commission may increase the amount described in clauses (i) and (ii) of subsection (b)(1)(D) from $250,000 to an amount that is not greater than $400,000 upon the recommendation of the Office of the Advocate for Small Business Capital Formation and the Office of the Investor Advocate. .\n##### (b) Technical corrections\nSection 4A of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131 ) is amended\u2014\n**(1)**\nby striking section 4(6) each place that term appears and inserting section 4(a)(6) ; and\n**(2)**\nby striking section 4(6)(B) each place that term appears and inserting section 4(a)(6)(B) .",
      "versionDate": "2026-01-15",
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
        "actionDate": "2025-07-15",
        "text": "Placed on the Union Calendar, Calendar No. 166."
      },
      "number": "3645",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACCESS Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-02-10T17:41:43Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3662is.xml"
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
      "title": "ACCESS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACCESS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Securities Act of 1933 to raise the offering amount threshold for when issuers using the crowdfunding exemption are required to file financial statements reviewed by a public accountant who is independent of the issuer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:25Z"
    }
  ]
}
```
