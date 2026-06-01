# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1026
- Title: Tar Sands Tax Loophole Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 1026
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-05T21:32:53Z
- Update date including text: 2025-12-05T21:32:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1026",
    "number": "1026",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Tar Sands Tax Loophole Elimination Act",
    "type": "S",
    "updateDate": "2025-12-05T21:32:53Z",
    "updateDateIncludingText": "2025-12-05T21:32:53Z"
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
          "date": "2025-03-13T16:49:26Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "VT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-13",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1026is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1026\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Markey (for himself, Ms. Warren , Mr. Whitehouse , Mr. Merkley , Mr. Welch , Mr. Sanders , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to clarify that products derived from tar sands are crude oil for purposes of the Federal excise tax on petroleum, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tar Sands Tax Loophole Elimination Act .\n#### 2. Clarification of tar sands as crude oil for excise tax purposes\n##### (a) In general\nParagraph (1) of section 4612(a) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) Crude oil The term crude oil includes crude oil condensates, natural gasoline, any bitumen or bituminous mixture, any oil derived from a bitumen or bituminous mixture (including oil derived from tar sands), and any oil derived from kerogen-bearing sources (including oil derived from oil shale). .\n##### (b) Regulatory authority To address other types of crude oil and petroleum products\nSubsection (a) of section 4612 of such Code is amended by adding at the end the following new paragraph:\n(10) Regulatory authority to address other types of crude oil and petroleum products Under such regulations as the Secretary may prescribe, the Secretary may include as crude oil or as a petroleum product subject to tax under section 4611, any fuel feedstock or finished fuel product customarily transported by pipeline, vessel, railcar, or tanker truck if the Secretary determines that\u2014 (A) the classification of such fuel feedstock or finished fuel product is consistent with the definition of oil under the Oil Pollution Act of 1990, and (B) such fuel feedstock or finished fuel product is produced in sufficient commercial quantities as to pose a significant risk of hazard in the event of a discharge. .\n##### (c) Technical amendment\nParagraph (2) of section 4612(a) of such Code is amended by striking from a well located .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act.",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Transportation and Infrastructure, and Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5983",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Resilience and Recovery Fund Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2224",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tar Sands Tax Loophole Elimination Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "383",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Oil and Gas Tax Subsidies Act of 2025",
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
        "updateDate": "2025-04-04T17:04:07Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1026is.xml"
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
      "title": "Tar Sands Tax Loophole Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tar Sands Tax Loophole Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to clarify that products derived from tar sands are crude oil for purposes of the Federal excise tax on petroleum, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:37Z"
    }
  ]
}
```
