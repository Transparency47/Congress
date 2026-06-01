# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1111
- Title: A bill to amend the Internal Revenue Code of 1986 to allow for payments to certain individuals who dye fuel, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1111
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-05-08T19:29:51Z
- Update date including text: 2025-05-08T19:29:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1111",
    "number": "1111",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to allow for payments to certain individuals who dye fuel, and for other purposes.",
    "type": "S",
    "updateDate": "2025-05-08T19:29:51Z",
    "updateDateIncludingText": "2025-05-08T19:29:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T16:52:32Z",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1111is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1111\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Johnson (for himself and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for payments to certain individuals who dye fuel, and for other purposes.\n#### 1. Payment to certain individuals who dye fuel\n##### (a) In general\nSubchapter B of chapter 65 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6434. Dyed fuel (a) In general If a person establishes to the satisfaction of the Secretary that such person meets the requirements of subsection (b) with respect to diesel fuel or kerosene, then the Secretary shall pay to such person an amount (without interest) equal to the tax described in subsection (b)(2)(A) with respect to such diesel fuel or kerosene. (b) Requirements (1) In general A person meets the requirements of this subsection with respect to diesel fuel or kerosene if such person removes from a terminal eligible indelibly dyed diesel fuel or kerosene. (2) Eligible indelibly dyed diesel fuel or kerosene defined The term eligible indelibly dyed diesel fuel or kerosene means diesel fuel or kerosene\u2014 (A) with respect to which a tax under section 4081 was previously paid (and not credited or refunded), and (B) which is exempt from taxation under section 4082(a). (c) Cross reference For civil penalty for excessive claims under this section, see section 6675. .\n##### (b) Conforming amendments\n**(1)**\nSection 6206 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking or 6427 each place it appears and inserting 6427, or 6434 ; and\n**(B)**\nby striking 6420 and 6421 and inserting 6420, 6421, and 6434 .\n**(2)**\nSection 6430 of such Code is amended\u2014\n**(A)**\nby striking or at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , or , and by adding at the end the following new paragraph:\n(4) which are removed as eligible indelibly dyed diesel fuel or kerosene under section 6434. .\n**(3)**\nSection 6675 of such Code is amended\u2014\n**(A)**\nin subsection (a), by striking or 6427 (relating to fuels not used for taxable purposes) and inserting 6427 (relating to fuels not used for taxable purposes), or 6434 (relating to eligible indelibly dyed fuel) ; and\n**(B)**\nin subsection (b)(1), by striking 6421, or 6427, and inserting 6421, 6427, or 6434, .\n**(4)**\nThe table of sections for subchapter B of chapter 65 of such Code is amended by adding at the end the following new item:\nSec. 6434. Dyed fuel. .\n##### (c) Effective date\nThe amendments made by this section shall apply to eligible indelibly dyed diesel fuel or kerosene removed on or after the date that is 180 days after the date of the enactment of this section.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-08T19:29:51Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1111is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow for payments to certain individuals who dye fuel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:21Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow for payments to certain individuals who dye fuel, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T10:56:26Z"
    }
  ]
}
```
