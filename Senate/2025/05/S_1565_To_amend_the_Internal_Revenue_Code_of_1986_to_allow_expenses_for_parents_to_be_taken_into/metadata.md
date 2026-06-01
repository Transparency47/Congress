# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1565?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1565
- Title: Lowering Costs for Caregivers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1565
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1565",
    "number": "1565",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Lowering Costs for Caregivers Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
            "date": "2025-05-01T16:53:06Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T16:53:06Z",
            "name": "Referred To"
          }
        ]
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
      "sponsorshipDate": "2025-05-01",
      "state": "LA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "TN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1565is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1565\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Ms. Rosen (for herself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow expenses for parents to be taken into account as medical expenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering Costs for Caregivers Act of 2025 .\n#### 2. Health savings accounts\n##### (a) In general\nSubparagraph (A) of section 223(d)(2) of the Internal Revenue Code of 1986 is amended by inserting , any parent of either such individual or such spouse after the spouse of such individual .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid after December 31, 2025.\n#### 3. Flexible spending and health reimbursement arrangements\n##### (a) In general\nSubsection (b) of section 105 of the Internal Revenue Code of 1986 is amended by adding at the end the following: A health flexible spending arrangement or health reimbursement arrangement shall not fail to be treated as meeting the requirements of this subsection or section 106, and no amount shall be included in gross income of the taxpayer, solely because, under the arrangement, the taxpayer may use amounts contributed to such arrangement for medical care (as defined in section 213(d), without regard to paragraph (1)(D) thereof) for a parent of the taxpayer or of the spouse of the taxpayer. .\n##### (b) Effective date\nThe amendment made by this section shall apply to expenses incurred after December 31, 2025.\n#### 4. Archer MSAs\n##### (a) In general\nSubparagraph (A) of section 220(d)(2) of the Internal Revenue Code of 1986 is amended by inserting , any parent of either such individual or such spouse after the spouse of such individual .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid after December 31, 2025.",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "138",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lowering Costs for Caregivers Act of 2025",
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
        "updateDate": "2025-06-04T15:19:54Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1565is.xml"
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
      "title": "Lowering Costs for Caregivers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lowering Costs for Caregivers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow expenses for parents to be taken into account as medical expenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:19Z"
    }
  ]
}
```
