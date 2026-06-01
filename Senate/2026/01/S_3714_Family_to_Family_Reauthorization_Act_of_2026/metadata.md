# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3714?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3714
- Title: Family-to-Family Reauthorization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3714
- Origin chamber: Senate
- Introduced date: 2026-01-28
- Update date: 2026-02-20T13:49:16Z
- Update date including text: 2026-04-21T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-28: Introduced in Senate
- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-28: Introduced in Senate

## Actions

- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-28",
    "latestAction": {
      "actionDate": "2026-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3714",
    "number": "3714",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Family-to-Family Reauthorization Act of 2026",
    "type": "S",
    "updateDate": "2026-02-20T13:49:16Z",
    "updateDateIncludingText": "2026-04-21T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-28",
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
      "actionDate": "2026-01-28",
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
          "date": "2026-01-28T20:35:01Z",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3714is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3714\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2026 Ms. Hassan (for herself and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title V of the Social Security Act to extend funding for the family-to-family health information centers.\n#### 1. Short title\nThis Act may be cited as the Family-to-Family Reauthorization Act of 2026 .\n#### 2. Extension of funding for family-to-family health information centers\nSection 501(c)(1)(A) of the Social Security Act ( 42 U.S.C. 701(c)(1)(A) ), as amended by section 6303 of division F of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026 ( Public Law 119\u201337 ; 139 Stat. 636) is amended\u2014\n**(1)**\nin clause (viii), by striking and at the end;\n**(2)**\nin clause (ix), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(x) for the period beginning on January 31, 2026, and ending on September 30, 2026, an amount equal to the pro rata portion of the amount appropriated for fiscal year 2025; and (xi) $6,000,000 for each of fiscal years 2027 through 2030. .",
      "versionDate": "2026-01-28",
      "versionType": "Introduced in Senate"
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
        "name": "Health",
        "updateDate": "2026-02-20T13:49:16Z"
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
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3714is.xml"
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
      "title": "Family-to-Family Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Family-to-Family Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title V of the Social Security Act to extend funding for the family-to-family health information centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:31Z"
    }
  ]
}
```
