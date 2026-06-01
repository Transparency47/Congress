# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/808?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/808
- Title: Fairness for the Trades Act
- Congress: 119
- Bill type: HR
- Bill number: 808
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-02-04T09:07:22Z
- Update date including text: 2026-02-04T09:07:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/808",
    "number": "808",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Fairness for the Trades Act",
    "type": "HR",
    "updateDate": "2026-02-04T09:07:22Z",
    "updateDateIncludingText": "2026-02-04T09:07:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:04:00Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr808ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 808\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Perez (for herself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to permit qualified business trade expenses to be treated as qualified higher education expenses for purposes of 529 accounts.\n#### 1. Short title\nThis Act may be cited as the Fairness for the Trades Act .\n#### 2. Qualified business trade expenses treated as qualified higher education expenses for purposes of 529 accounts\n##### (a) In general\nSection 529(e)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Qualified business trade expenses The term qualified higher education expenses includes qualified business trade expenses (as defined in subsection (f)). .\n##### (b) Qualified business trade expenses\nSection 529 is amended by redesignating subsection (f) as subsection (g) and by inserting after subsection (e) the following new subsection:\n(f) Qualified business trade expenses For purposes of this section\u2014 (1) In general The term qualified post business trade expenses means amounts paid by the designated beneficiary for specified business property used by the designated beneficiary in a qualified trade field. (2) Specified business property The term specified business property means tangible property (other than buildings) which is of a character subject to the allowance for depreciation. (3) Qualified trade field The term qualified trade field means any field which is described by one of the following National industry codes of the North American Industry Classification System: 113110, 113210, 113310, 114111, 114112, 114119, 114210, 115310, 236115, 236116, 236117, 236118, 236210, 236220, 237110, 237120, 237130, 237210, 237310, 237990, 238110, 238120, 238130, 238140, 238150, 238160, 238170, 238190, 238210, 238220, 238290, 238310, 238320, 238330, 238340, 238350, 238390, 238910, 238990, 811111, 811114, 811198, 811210, 811310, 811411, 811412, 811420, 811430, or 811490. .\n##### (c) Effective date\nThe amendments made by this section shall apply to expenses paid in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-04-07T16:17:49Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr808ih.xml"
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
      "title": "Fairness for the Trades Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness for the Trades Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to permit qualified business trade expenses to be treated as qualified higher education expenses for purposes of 529 accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:44Z"
    }
  ]
}
```
