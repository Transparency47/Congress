# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3332
- Title: More Homes on the Market Act
- Congress: 119
- Bill type: S
- Bill number: 3332
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3332",
    "number": "3332",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "More Homes on the Market Act",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
            "date": "2025-12-03T21:14:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-03T21:14:37Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "MT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "WY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "UT"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "LA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3332is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3332\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Cornyn (for himself, Mr. Bennet , Mr. Daines , Mr. Schiff , Mr. Barrasso , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the exclusion of gain from the sale of a principal residence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the More Homes on the Market Act .\n#### 2. Increase of exclusion of gain from sale of principal residence\n##### (a) In general\nSection 121(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking $250,000 and inserting $500,000 each place it appears,\n**(2)**\nby striking 500,000 and inserting $1,000,000 each place it appears,\n**(3)**\nin paragraph (2)(A), in the heading, by striking $500,000 and inserting $1,000,000 , and\n**(4)**\nby adding at the end the following new paragraph:\n(5) Adjustment for inflation In the case of a taxable year beginning after 2025, the $500,000 and $1,000,000 amounts in paragraphs (1), (2), and (4) shall each be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2024 for 2016 in subparagraph (A)(ii) thereof. If any increase under this clause is not a multiple of $100, such increase shall be rounded to the next lowest multiple of $100. .\n##### (b) Effective date\nThe amendments made by this section shall apply to sales and exchanges after the date of the enactment of this Act.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1340",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "More Homes on the Market Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "4856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Revitalizing America\u2019s Housing Act",
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
        "updateDate": "2026-01-06T15:59:17Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3332is.xml"
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
      "title": "More Homes on the Market Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "More Homes on the Market Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the exclusion of gain from the sale of a principal residence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:26Z"
    }
  ]
}
```
