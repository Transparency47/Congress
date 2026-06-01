# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/268
- Title: Saving American Workers’ Benefits Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 268
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2025-04-07T16:29:29Z
- Update date including text: 2025-04-07T16:29:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/268",
    "number": "268",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Saving American Workers\u2019 Benefits Act of 2025",
    "type": "S",
    "updateDate": "2025-04-07T16:29:29Z",
    "updateDateIncludingText": "2025-04-07T16:29:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T17:21:35Z",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s268is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 268\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mrs. Hyde-Smith (for herself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to require taxpayers claiming the child and earned income tax credits, and their qualifying children, to have a valid social security number for employment purposes.\n#### 1. Short title\nThis Act may be cited as the Saving American Workers\u2019 Benefits Act of 2025 .\n#### 2. Child tax credit identification requirements\n##### (a) In general\nSubsection (e) of section 24 of the Internal Revenue Code of 1986 is amended to read as follows:\n(e) Identification requirements (1) In general No credit shall be allowed under this section to a taxpayer with respect to any qualifying child unless the taxpayer includes the social security number of\u2014 (A) such child, and (B) the taxpayer (and, in the case of a joint return, the taxpayer's spouse), on the return of tax for the taxable year. (2) Social security number For purposes of paragraph (1), with respect to an individual and a taxable year, the term social security number means a social security number issued to an individual by the Social Security Administration, but only if the social security number is issued\u2014 (A) to a citizen of the United States or pursuant to subclause (I) (or that portion of subclause (III) that relates to subclause (I)) of section 205(c)(2)(B)(i) of the Social Security Act, and (B) before the due date for the return of tax for such taxable year. Such term shall not include any social security number which does not indicate that the individual to whom the number is issued is authorized to work in the United States. .\n##### (b) Math error authority\n**(1)**\nSubparagraph (I) of section 6213(g)(2) of the Internal Revenue Code of 1986 is amended by striking TIN and inserting social security number .\n**(2)**\nSubparagraph (L) of section 6213(g)(2) of such Code is amended\u2014\n**(A)**\nby striking a TIN and inserting a TIN or social security number, as applicable, , and\n**(B)**\nby striking such TIN both places it appears and inserting such TIN or social security number .\n##### (c) Conforming amendment\nSubsection (h) of section 24 of the Internal Revenue Code of 1986 is amended by striking paragraph (7).\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Earned income credit identification requirements\n##### (a) In general\nSubsection (m) of section 32 of the Internal Revenue Code of 1986 is amended by striking clause (II) (or that portion of clause (III) that relates to clause (II)) of section 205(c)(2)(B)(i) of the Social Security Act and inserting subclause (II) (or that portion of subclause (III) that relates to subclause (II)) of section 205(c)(2)(B)(i) of the Social Security Act, or any other social security number which does not indicate that the individual to whom the number is issued is authorized to work in the United States .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-28",
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
        "name": "Taxation",
        "updateDate": "2025-04-07T16:29:29Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s268is.xml"
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
      "title": "Saving American Workers\u2019 Benefits Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving American Workers\u2019 Benefits Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to require taxpayers claiming the child and earned income tax credits, and their qualifying children, to have a valid social security number for employment purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:16Z"
    }
  ]
}
```
