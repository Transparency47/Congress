# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3372
- Title: Protect Innocent Victims of Taxation After Fire Extension Act
- Congress: 119
- Bill type: S
- Bill number: 3372
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-04-14T19:59:49Z
- Update date including text: 2026-04-14T19:59:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S8514)
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S8514)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3372",
    "number": "3372",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
    "type": "S",
    "updateDate": "2026-04-14T19:59:49Z",
    "updateDateIncludingText": "2026-04-14T19:59:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S8514)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:15:46Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3372is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3372\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Padilla (for himself, Ms. Lummis , Mr. Wyden , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude qualified wildfire relief payments from gross income, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Innocent Victims of Taxation After Fire Extension Act .\n#### 2. Exclusion from gross income for compensation for losses or damages resulting from wildfires\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Compensation for losses or damages resulting from wildfires (a) In general Gross income shall not include any amount received by an individual as a qualified wildfire relief payment. (b) Qualified wildfire relief payment For purposes of this section\u2014 (1) In general The term qualified wildfire relief payment means any amount received by or on behalf of an individual as compensation for losses, expenses, or damages (including compensation for additional living expenses, lost wages (other than compensation for lost wages paid by the employer which would have otherwise paid such wages), personal injury, death, or emotional distress) incurred as a result of a qualified wildfire disaster, but only to the extent the losses, expenses, or damages compensated by such payment are not compensated for by insurance or otherwise. (2) Qualified wildfire disaster The term qualified wildfire disaster means any federally declared disaster (as defined in section 165(i)(5)(A)) declared, after December 31, 2014, as a result of any forest or range fire. (c) Denial of double benefit Notwithstanding any other provision of this subtitle\u2014 (1) no deduction or credit shall be allowed (to the individual for whose benefit a qualified wildfire relief payment is made) for, or by reason of, any expenditure to the extent of the amount excluded under this section with respect to such expenditure, and (2) no increase in the basis or adjusted basis of any property shall result from any amount excluded under this section with respect to such property. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Compensation for losses or damages resulting from wildfires. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2025.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2026-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7825",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Doug LaMalfa Protect Innocent Victims of Taxation After Fire Extension Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5225",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2744",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Disaster Tax Relief Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-09",
        "text": "Placed on the Union Calendar, Calendar No. 525."
      },
      "number": "5366",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Doug LaMalfa Federal Disaster Tax Relief Certainty Act",
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
        "updateDate": "2026-01-06T16:07:49Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3372is.xml"
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
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude qualified wildfire relief payments from gross income, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:18:14Z"
    }
  ]
}
```
