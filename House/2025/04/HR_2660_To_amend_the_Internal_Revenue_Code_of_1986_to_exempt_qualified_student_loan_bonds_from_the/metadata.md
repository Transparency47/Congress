# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2660
- Title: To amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.
- Congress: 119
- Bill type: HR
- Bill number: 2660
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-04-17T08:07:21Z
- Update date including text: 2026-04-17T08:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2660",
    "number": "2660",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:21Z",
    "updateDateIncludingText": "2026-04-17T08:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:02:50Z",
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
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
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
      "sponsorshipDate": "2025-12-12",
      "state": "RI"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "PA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2660ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2660\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Feenstra introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.\n#### 1. Qualified student loan bonds exempt from volume cap and alternative minimum tax\n##### (a) Exemption from volume cap\n**(1) In general**\nSection 146(g) of the Internal Revenue Code of 1986 is amended by redesignating paragraphs (2) through (6) as paragraphs (3) through (7), respectively, and by inserting after paragraph (1) the following new paragraph:\n(2) any qualified student loan bond, .\n**(2) Special rule for application of pooled financing bond rules**\nSection 149(f)(6) of such Code is amended by adding at the end the following new subparagraph:\n(C) Special rule for qualified student loan bonds For purposes of subparagraph (A), in the case of any qualified student loan bond, the term ultimate borrower shall not include any student borrower. .\n**(3) Conforming amendment**\nSection 146(g) of such Code is amended by striking Paragraphs (4) and (5) in the last sentence and inserting Paragraphs (5) and (6) .\n##### (b) Exemption from alternative minimum tax\nSection 57(a)(5)(C) of such Code is amended by redesignating clauses (iv), (v), and (vi) as clauses (v), (vi), and (vii), respectively, and by inserting after clause (iii) the following new clause:\n(iv) Exception for qualified student loan bonds For purposes of clause (i), the term private activity bond shall not include any bond issued after the date of the enactment of this clause if such bond is a qualified student loan bond (as defined in section 144(b)). The preceding sentence shall not apply to any refunding bond unless such preceding sentence applied to the refunded bond (or in the case of a series of refundings, the original bond). .\n##### (c) Effective dates\nThe amendments made by this section shall apply to obligations issued after the date of the enactment of this Act.",
      "versionDate": "2025-04-07",
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
        "actionDate": "2026-02-03",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3761",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Loan Bond Expansion Act of 2026",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T16:45:07Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2660ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:23Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to exempt qualified student loan bonds from the volume cap and the alternative minimum tax.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T08:05:27Z"
    }
  ]
}
```
