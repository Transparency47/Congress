# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6324
- Title: Retirement Simplification and Clarity Act
- Congress: 119
- Bill type: HR
- Bill number: 6324
- Origin chamber: House
- Introduced date: 2025-11-28
- Update date: 2026-05-27T08:06:26Z
- Update date including text: 2026-05-27T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-28: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-28: Introduced in House

## Actions

- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-28",
    "latestAction": {
      "actionDate": "2025-11-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6324",
    "number": "6324",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Retirement Simplification and Clarity Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:26Z",
    "updateDateIncludingText": "2026-05-27T08:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-28",
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
      "actionDate": "2025-11-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-28",
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
          "date": "2025-11-28T15:01:15Z",
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
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "IL"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "OH"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-28",
      "state": "IL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "TX"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "WA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "IL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "PA"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "PA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "IA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6324ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6324\nIN THE HOUSE OF REPRESENTATIVES\nNovember 28, 2025 Mr. Panetta (for himself, Mr. LaHood , Mr. Miller of Ohio , Mr. Fitzpatrick , Mr. Davis of Illinois , Mr. Moran , Ms. DelBene , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for in-service rollovers for individual retirement annuity purchases.\n#### 1. Short title\nThis Act may be cited as the Retirement Simplification and Clarity Act .\n#### 2. In-service rollovers for annuity purchases\n##### (a) In general\nSection 401(k) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n**\u201c(17) Special rule for pre-retirement rollover**\nNotwithstanding the requirements of paragraph (2)(B)(i), a plan may permit a participant who has attained age 50 or older to elect a direct rollover of all or a portion the accrued benefit of the participant attributable to employer contributions made pursuant to the employee\u2019s election to an individual retirement annuity (as defined in section 408(b)).\u201d.\n##### (b) Safe Harbor\nSection 402(f) of such Code is amended by redesignating paragraph (2) as paragraph (3) and by inserting after paragraph (1) the following new paragraph:\n(2) Safe harbor (A) In general A written explanation shall satisfy the requirements of paragraph (1) if it includes the following information in concise, plain language: (i) The taxpayer has 30 days to review such explanation before they must take any action. (ii) Distributions made directly to the taxpayer will be subject to income tax withholding and added to gross income to the extent taxable. (iii) The taxpayer may owe an additional 10 percent tax on a distribution issued before the taxpayer attains age 59\u00bd. (iv) A 20 percent income tax withholding will apply to distributions that are not eligible for rollover. (v) A taxpayer can defer Federal income tax on eligible distributions by rolling such distribution over to another qualified plan or individual retirement arrangement. (vi) A taxpayer may not rollover\u2014 (I) required minimum distributions, (II) hardship distributions, (III) a series of payments to be made over a number of years, (IV) employee stock ownership plan dividends, or (V) corrective distributions. (vii) The plan administrator can be contacted for information regarding whether all or a portion of a payment to the taxpayer is eligible for rollover. (viii) A plan may require the taxpayer to take a distribution upon the taxpayer\u2019s attainment of the plan\u2019s retirement age, or in the case of a benefit that is less than $7,000, the plan may automatically pay the benefit directly to the taxpayer or in a rollover to a traditional IRA or, for designated Roth amounts, a Roth IRA it establishes for the taxpayer. (ix) Eligible amounts may be rolled over to a new plan or to an IRA when a taxpayer changes jobs, and the administrator of the new plan can confirm how to accomplish such a rollover. (x) The taxpayer may choose to leave eligible amounts in their original plan. (xi) The taxpayer may rollover an eligible distribution to a traditional IRA, individual retirement annuity, or a Roth IRA for designated Roth contributions. (xii) Direct rollovers are not subject to the mandatory 20 percent withholding, and the distribution may be in the form of a check payable to the new plan or arrangement or by electronic transfer. (xiii) If the taxpayer receives a payment directly, the taxpayer has up to 60 days from the date of distribution to rollover an amount equal to the eligible amount received plus the dollar amount that was withheld and sent to the Internal Revenue Service. (xiv) The taxpayer may obtain additional information from the Internal Revenue Service. (B) Regulations and Guidance The Secretary may promulgate such regulations and guidance as are necessary to administer this section, including regulations updating the list in subparagraph (A) as necessary. .\n##### (c) Effective Date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-11-28",
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
        "updateDate": "2025-12-16T17:05:24Z"
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
      "date": "2025-11-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6324ih.xml"
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
      "title": "Retirement Simplification and Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retirement Simplification and Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for in-service rollovers for individual retirement annuity purchases.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T12:18:15Z"
    }
  ]
}
```
