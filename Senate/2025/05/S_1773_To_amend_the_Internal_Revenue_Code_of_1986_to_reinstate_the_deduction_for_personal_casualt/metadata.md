# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1773?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1773
- Title: Tax Relief for Victims of Crimes, Scams, and Disasters Act
- Congress: 119
- Bill type: S
- Bill number: 1773
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-01-31T13:48:18Z
- Update date including text: 2026-01-31T13:48:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1773",
    "number": "1773",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Tax Relief for Victims of Crimes, Scams, and Disasters Act",
    "type": "S",
    "updateDate": "2026-01-31T13:48:18Z",
    "updateDateIncludingText": "2026-01-31T13:48:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
            "date": "2025-05-15T15:15:05Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-15T15:15:05Z",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "WV"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1773is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1773\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Ms. Baldwin (for herself, Mrs. Moody , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to reinstate the deduction for personal casualty losses as in effect prior to the enactment of Public Law 115\u201397.\n#### 1. Short title\nThis Act may be cited as the Tax Relief for Victims of Crimes, Scams, and Disasters Act .\n#### 2. Reinstatement of deduction for personal casualty loss\n##### (a) In general\nSection 165(h) of the Internal Revenue Code of 1986 is amended by striking paragraph (5).\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2017.\n#### 3. Extension of time to file claim for credit or refund for personal casualty loss deduction\n##### (a) In general\nIn the case of a taxpayer who filed a return for a taxable year ending before January 1, 2025, with respect to which a deduction could have been taken by the taxpayer under section 165(a) of the Internal Revenue Code of 1986 but for the fact that such deduction was suspended under section 165(h)(5) at the time of filing\u2014\n**(1)**\nthe period of limitation prescribed by section 6511(a) of such Code on filing a claim for credit or refund for any such taxable year shall be extended until the date prescribed by law (including extensions) for filing the return of tax for the taxable year that includes the date of the enactment of this Act, and\n**(2)**\nsection 6511(b)(2) of such Code shall not apply to any claim of credit or refund with respect to such return.\n##### (b) Extension restricted to personal casualty loss deduction\nSubsection (a) shall apply only with respect to a claim for credit or refund of a taxpayer to the extent such claim relates to an overpayment attributable to the deduction under section 165(a) for personal casualty losses described in section 165(c)(3) of the Internal Revenue Code of 1986.",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3469",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tax Relief for Victims of Crimes, Scams, and Disasters Act",
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
        "updateDate": "2025-06-06T20:28:22Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1773is.xml"
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
      "title": "Tax Relief for Victims of Crimes, Scams, and Disasters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T13:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Relief for Victims of Crimes, Scams, and Disasters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to reinstate the deduction for personal casualty losses as in effect prior to the enactment of Public Law 115-97.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:21Z"
    }
  ]
}
```
