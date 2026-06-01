# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8477
- Title: To amend the Internal Revenue Code of 1986 to reverse certain energy-related modifications enacted by Public Law 119-21.
- Congress: 119
- Bill type: HR
- Bill number: 8477
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-13T08:06:37Z
- Update date including text: 2026-05-13T08:06:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8477",
    "number": "8477",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to reverse certain energy-related modifications enacted by Public Law 119-21.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:37Z",
    "updateDateIncludingText": "2026-05-13T08:06:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:00:05Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-23",
      "state": "OH"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "OH"
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
      "sponsorshipDate": "2026-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8477ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8477\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Fitzpatrick (for himself, Mr. Lawler , Mr. Miller of Ohio , and Mr. Carey ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to reverse certain energy-related modifications enacted by Public Law 119\u201321 .\n#### 1. Reversal of certain energy-related modifications enacted by Public Law 119\u201321\n##### (a) Energy efficient commercial buildings deduction\n**(1) Termination**\nSection 179D of the Internal Revenue Code of 1986 is amended by striking subsection (i).\n**(2) Effective date**\nThe amendment made by this subsection shall take effect as if included in section 70507 of Public Law 119\u201321 .\n##### (b) New energy efficient home credit\n**(1) Termination**\nSection 45L(h) of such Code is amended by striking June 30, 2026 and inserting December 31, 2032 .\n**(2) Effective date**\nThe amendment made by this subsection shall take effect as if included in section 70508 of Public Law 119\u201321 .\n##### (c) Clean hydrogen production credit\n**(1) Facility construction date**\nSection 45V(c)(3)(C) of such Code is amended by striking January 1, 2028 and inserting January 1, 2033 .\n**(2) Effective date**\nThe amendment made by this subsection shall take effect as if included in section 70511 of Public Law 119\u201321 .\n##### (d) Clean electricity production credit\n**(1) Termination**\nSection 45Y(d) of such Code is amended\u2014\n**(A)**\nin paragraph (1), by striking Subject to paragraph (4), the amount of and inserting The amount of , and\n**(B)**\nby striking paragraph (4).\n**(2) Phase-out**\nSection 45Y(d)(3) of such Code is amended by striking calendar year 2032. and inserting\nthe later of\u2014 (A) the calendar year in which the Secretary determines that the annual greenhouse gas emissions from the production of electricity in the United States are equal to or less than 25 percent of the annual greenhouse gas emissions from the production of electricity in the United States for calendar year 2022, or (B) 2032. .\n**(3) Effective date**\nThe amendments made by this subsection shall take effect as if included in section 70512(a) of Public Law 119\u201321 .\n##### (e) Clean electricity investment credit\n**(1) Termination**\nSection 48E(e) of such Code is amended\u2014\n**(A)**\nin paragraph (1), by striking Subject to paragraph (4), the amount of and inserting The amount of , and\n**(B)**\nby striking paragraph (4).\n**(2) Effective date**\nThe amendments made by this subsection shall take effect as if included in section 70513(a) of Public Law 119\u201321 .",
      "versionDate": "2026-04-23",
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
        "updateDate": "2026-05-07T02:45:56Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8477ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to reverse certain energy-related modifications enacted by Public Law 119-21.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:33:26Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to reverse certain energy-related modifications enacted by Public Law 119-21.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:06:33Z"
    }
  ]
}
```
