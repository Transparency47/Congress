# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4787
- Title: To amend the Internal Revenue Code of 1986 to extend the deduction for film and television productions and to make certain changes with respect to the calculation of such deduction.
- Congress: 119
- Bill type: HR
- Bill number: 4787
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-05-22T18:40:32Z
- Update date including text: 2026-05-22T18:40:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4787",
    "number": "4787",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to extend the deduction for film and television productions and to make certain changes with respect to the calculation of such deduction.",
    "type": "HR",
    "updateDate": "2026-05-22T18:40:32Z",
    "updateDateIncludingText": "2026-05-22T18:40:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:05:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4787ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4787\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Chu introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the deduction for film and television productions and to make certain changes with respect to the calculation of such deduction.\n#### 1. Film and television production deduction amendments\n##### (a) Extension\nSection 181(g) of the Internal Revenue Code of 1986 is amended by striking December 31, 2025 and inserting December 31, 2030 .\n##### (b) Increase in dollar limitation\nSection 181(a)(2)(A) of such Code is amended to read as follows:\n(A) In general Paragraph (1) shall not apply to so much of the aggregate cost of any qualified film or television production or any qualified live theatrical production as exceeds $30,000,000. .\n##### (c) Higher dollar limitation for productions in certain areas\nSection 181(a)(2)(B) of such Code is amended in the matter following clause (ii) by striking substituting $20,000,000 for $15,000,000 and inserting substituting $40,000,000 for $30,000,000 .\n##### (d) Inflation adjustment\nSection 181(a)(2) of such Code is amended by adding at the end the following new subparagraph:\n(C) Inflation adjustment (i) In general In the case of any taxable year beginning in a calendar year after 2026, each dollar amount in subparagraph (A) or (B) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding.\u2014Any increase determined under clause (i) shall be rounded to the nearest multiple of $1,000. .\n##### (e) Effective date\nThe amendments made by this section shall apply to productions commencing after the date of the enactment of this Act.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2026-05-20",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "7007",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Governing for the People Act",
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
        "updateDate": "2025-08-06T18:59:45Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4787ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to extend the deduction for film and television productions and to make certain changes with respect to the calculation of such deduction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:18:47Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to extend the deduction for film and television productions and to make certain changes with respect to the calculation of such deduction.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:15Z"
    }
  ]
}
```
