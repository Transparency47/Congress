# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8294
- Title: Millionaires Surtax Act
- Congress: 119
- Bill type: HR
- Bill number: 8294
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-30T08:05:45Z
- Update date including text: 2026-05-30T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8294",
    "number": "8294",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Millionaires Surtax Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:45Z",
    "updateDateIncludingText": "2026-05-30T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:03:50Z",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8294ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8294\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Beyer (for himself, Mr. Cohen , Mr. Deluzio , Ms. Norton , Ms. Tlaib , and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a surtax on high income individuals.\n#### 1. Short title\nThis Act may be cited as the Millionaires Surtax Act .\n#### 2. Surcharge on high income individuals\n##### (a) In general\nSubchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nVIII Surcharge on high income individuals Sec. 59B. Surcharge on high income individuals. 59B. Surcharge on high income individuals (a) General rule In the case of a taxpayer other than a corporation, there is hereby imposed (in addition to any other tax imposed by this subtitle) a tax equal to 10 percent of so much of the modified adjusted gross income of the taxpayer as exceeds $2,000,000. (b) Taxpayers not making a joint return In the case of any taxpayer other than a taxpayer making a joint return under section 6013 or a surviving spouse (as defined in section 2(a)), subsection (a) shall be applied by substituting $1,000,000 for $2,000,000 . (c) Modified adjusted gross income For purposes of this section, the term modified adjusted gross income means adjusted gross income reduced by any deduction (not taken into account in determining adjusted gross income) allowed for investment interest (as defined in section 163(d)). In the case of an estate or trust, adjusted gross income shall be determined as provided in section 67(e). (d) Special rules (1) Nonresident alien In the case of a nonresident alien individual, only amounts taken into account in connection with the tax imposed under section 871(b) shall be taken into account under this section. (2) Citizens and residents living abroad The dollar amount in effect under subsection (a) (after the application of subsection (b)) shall be decreased by the excess of\u2014 (A) the amounts excluded from the taxpayer\u2019s gross income under section 911, over (B) the amounts of any deductions or exclusions disallowed under section 911(d)(6) with respect to the amounts described in subparagraph (A). (3) Charitable trusts Subsection (a) shall not apply to a trust all the unexpired interests in which are devoted to one or more of the purposes described in section 170(c)(2)(B). (4) Not treated as tax imposed by this chapter for certain purposes The tax imposed under this section shall not be treated as tax imposed by this chapter for purposes of determining the amount of any credit under this chapter or for purposes of section 55. .\n##### (b) Clerical amendment\nThe table of parts for subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPart VIII\u2014Surcharge on high income individuals .\n##### (c) Section 15 not To apply\nThe amendment made by subsection (a) shall not be treated as a change in a rate of tax for purposes of section 15 of the Internal Revenue Code of 1986.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-04-15",
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
        "actionDate": "2026-04-15",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4306",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Millionaires Surtax Act",
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
        "updateDate": "2026-04-27T22:32:21Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8294ih.xml"
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
      "title": "Millionaires Surtax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Millionaires Surtax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to impose a surtax on high income individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:39Z"
    }
  ]
}
```
