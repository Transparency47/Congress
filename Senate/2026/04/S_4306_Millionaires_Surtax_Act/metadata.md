# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4306
- Title: Millionaires Surtax Act
- Congress: 119
- Bill type: S
- Bill number: 4306
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-07T02:49:14Z
- Update date including text: 2026-05-07T02:49:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4306",
    "number": "4306",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Millionaires Surtax Act",
    "type": "S",
    "updateDate": "2026-05-07T02:49:14Z",
    "updateDateIncludingText": "2026-05-07T02:49:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T20:00:55Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NM"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4306is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4306\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Van Hollen (for himself, Mr. Merkley , Mr. Luj\u00e1n , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a surtax on high income individuals.\n#### 1. Short title\nThis Act may be cited as the Millionaires Surtax Act .\n#### 2. Surcharge on high income individuals\n##### (a) In general\nSubchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nVIII Surcharge on high income individuals Sec. 59B. Surcharge on high income individuals. 59B. Surcharge on high income individuals (a) General rule In the case of a taxpayer other than a corporation, there is hereby imposed (in addition to any other tax imposed by this subtitle) a tax equal to 10 percent of so much of the modified adjusted gross income of the taxpayer as exceeds $2,000,000. (b) Taxpayers not making a joint return In the case of any taxpayer other than a taxpayer making a joint return under section 6013 or a surviving spouse (as defined in section 2(a)), subsection (a) shall be applied by substituting $1,000,000 for $2,000,000 . (c) Modified adjusted gross income For purposes of this section, the term modified adjusted gross income means adjusted gross income reduced by any deduction (not taken into account in determining adjusted gross income) allowed for investment interest (as defined in section 163(d)). In the case of an estate or trust, adjusted gross income shall be determined as provided in section 67(e). (d) Special rules (1) Nonresident alien In the case of a nonresident alien individual, only amounts taken into account in connection with the tax imposed under section 871(b) shall be taken into account under this section. (2) Citizens and residents living abroad The dollar amount in effect under subsection (a) (after the application of subsection (b)) shall be decreased by the excess of\u2014 (A) the amounts excluded from the taxpayer\u2019s gross income under section 911, over (B) the amounts of any deductions or exclusions disallowed under section 911(d)(6) with respect to the amounts described in subparagraph (A). (3) Charitable trusts Subsection (a) shall not apply to a trust all the unexpired interests in which are devoted to one or more of the purposes described in section 170(c)(2)(B). (4) Not treated as tax imposed by this chapter for certain purposes The tax imposed under this section shall not be treated as tax imposed by this chapter for purposes of determining the amount of any credit under this chapter or for purposes of section 55. .\n##### (b) Clerical amendment\nThe table of parts for subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPart VIII\u2014Surcharge on high income individuals .\n##### (c) Section 15 not To apply\nThe amendment made by subsection (a) shall not be treated as a change in a rate of tax for purposes of section 15 of the Internal Revenue Code of 1986.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-04-15",
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
        "actionDate": "2026-04-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8294",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Millionaires Surtax Act",
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
        "updateDate": "2026-05-07T02:49:14Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4306is.xml"
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
      "title": "Millionaires Surtax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Millionaires Surtax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose a surtax on high income individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:49Z"
    }
  ]
}
```
