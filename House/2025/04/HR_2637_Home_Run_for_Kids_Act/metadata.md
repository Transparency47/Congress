# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2637?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2637
- Title: Home Run for Kids Act
- Congress: 119
- Bill type: HR
- Bill number: 2637
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-08-27T08:05:33Z
- Update date including text: 2025-08-27T08:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2637",
    "number": "2637",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Home Run for Kids Act",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:33Z",
    "updateDateIncludingText": "2025-08-27T08:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:00:10Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2637ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2637\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a nonrefundable credit for certain organized sport equipment expenses.\n#### 1. Short title\nThis Act may be cited as the Home Run for Kids Act .\n#### 2. Credit for organized sport equipment expenses\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 26 the following new section:\n25F. Organized sport equipment expenses (a) In general In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the qualified organized sport equipment expenses paid or incurred by the taxpayer during the taxable year. (b) Limitations (1) Dollar limitation The credit allowed under subsection (a) for the taxable year shall not exceed $200. (2) Income limitation (A) In general The amount allowable as a credit under subsection (a) for any taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount so allowable (determined without regard to this paragraph but with regard to paragraph (1)) as\u2014 (i) the amount (if any) by which the taxpayer\u2019s modified adjusted gross income exceeds $150,000, bears to (ii) $65,000. (B) Modified adjusted gross income For purposes of this paragraph, the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (c) Qualified organized sport equipment expenses For purposes of this section, the term qualified organized sport equipment expenses means expenses which are paid or incurred for equipment in connection with participation of a dependent of the taxpayer (with respect to whom the taxpayer is allowed a deduction under section 151(c)) in an organized sport, game, or hobby program that is conducted primarily for unrelated individuals who have not attained age 19 to engage in such sport, game, or hobby. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting before the item relating to section 26 the following new item:\nSec. 25F. Organized sport equipment expenses. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2023.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-09T16:48:00Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2637ih.xml"
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
      "title": "Home Run for Kids Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home Run for Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T10:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a nonrefundable credit for certain organized sport equipment expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:18:20Z"
    }
  ]
}
```
