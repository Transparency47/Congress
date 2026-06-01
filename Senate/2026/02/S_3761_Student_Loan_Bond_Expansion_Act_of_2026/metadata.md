# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3761
- Title: Student Loan Bond Expansion Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3761
- Origin chamber: Senate
- Introduced date: 2026-02-03
- Update date: 2026-03-03T12:03:27Z
- Update date including text: 2026-03-03T12:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in Senate
- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-03: Introduced in Senate

## Actions

- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3761",
    "number": "3761",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Student Loan Bond Expansion Act of 2026",
    "type": "S",
    "updateDate": "2026-03-03T12:03:27Z",
    "updateDateIncludingText": "2026-03-03T12:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:40:46Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "VT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "RI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3761is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3761\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2026 Mr. Grassley (for himself, Mr. Welch , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.\n#### 1. Short title\nThis Act may be cited as the Student Loan Bond Expansion Act of 2026 .\n#### 2. Qualified student loan bonds exempt from volume cap and alternative minimum tax\n##### (a) Exemption from volume cap\n**(1) In general**\nSection 146(g) of the Internal Revenue Code of 1986 is amended by redesignating paragraphs (2) through (6) as paragraphs (3) through (7), respectively, and by inserting after paragraph (1) the following new paragraph:\n(2) any qualified student loan bond, .\n**(2) Special rule for application of pooled financing bond rules**\nSection 149(f)(6) of such Code is amended by adding at the end the following new subparagraph:\n(C) Special rule for qualified student loan bonds For purposes of subparagraph (A), in the case of any qualified student loan bond, the term ultimate borrower shall not include any student borrower. .\n**(3) Conforming amendment**\nSection 146(g) of such Code is amended by striking Paragraphs (4) and (5) in the last sentence and inserting Paragraphs (5) and (6) .\n##### (b) Exemption from alternative minimum tax\nSection 57(a)(5)(C) of the Internal Revenue Code of 1986 is amended by redesignating clauses (iv), (v), and (vi) as clauses (v), (vi), and (vii), respectively, and by inserting after clause (iii) the following new clause:\n(iv) Exception for qualified student loan bonds For purposes of clause (i), the term private activity bond shall not include any bond issued after the date of the enactment of this clause if such bond is a qualified student loan bond (as defined in section 144(b)). The preceding sentence shall not apply to any refunding bond unless such preceding sentence applied to the refunded bond (or in the case of a series of refundings, the original bond). .\n##### (c) Effective dates\nThe amendments made by this section shall apply to obligations issued after the date of the enactment of this Act.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2660",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.",
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
        "name": "Taxation",
        "updateDate": "2026-02-23T16:27:37Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3761is.xml"
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
      "title": "Student Loan Bond Expansion Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Student Loan Bond Expansion Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:30Z"
    }
  ]
}
```
