# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5776
- Title: EGG SAVE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5776
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-04-15T08:05:40Z
- Update date including text: 2026-04-15T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5776",
    "number": "5776",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "EGG SAVE Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:40Z",
    "updateDateIncludingText": "2026-04-15T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:02:50Z",
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
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
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
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "PA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5776ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5776\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Ms. Malliotakis (for herself, Ms. Escobar , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax credit for layer operation efficiency equipment.\n#### 1. Short title\nThis Act may be cited as the Efficiency Gains through Grading Standards And Viable Enhancement Act of 2025 or the EGG SAVE Act of 2025 .\n#### 2. Layer operation efficiency equipment credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Layer operation efficiency equipment credit (a) General rule For purposes of section 38, the layer operation efficiency equipment credit for any taxable year is an amount equal to the applicable percentage of the qualified equipment expenditures paid or incurred by the taxpayer during such taxable year. (b) Applicable percentage For purposes of this section, the applicable percentage is\u2014 (1) 50 percent, in the case of property placed in service during calendar year 2026, (2) 40 percent, in the case of property placed in service during calendar year 2027, and (3) 30 percent, in the case of property placed in service during calendar year 2028. (c) Qualified equipment expenditures For purposes of this section\u2014 (1) In general The term qualified equipment expenditures means amounts paid or incurred for\u2014 (A) the purchase of qualified in-ovo sex identification equipment, (B) the installation of such equipment, and (C) facility modifications necessary for the operation of such equipment. (2) Qualified in-ovo sex identification equipment The term qualified in-ovo sex identification equipment means equipment which\u2014 (A) utilizes optical or non-optical technology to determine the sex of avian embryos before hatch, (B) is placed in service at a commercial egg hatchery facility located in the United States, (C) achieves an accuracy rate of not less than 95 percent in sex determination, and (D) meets such other requirements as the Secretary may prescribe. (3) Limitation to property placed in service No expenditure shall be taken into account under paragraph (1) with respect to any equipment unless such equipment is placed in service by the taxpayer. (d) Other rules (1) Basis reduction For purposes of this subtitle, if a credit is determined under this section with respect to any property, the basis of such property shall be reduced by the amount of the credit so determined. If during any taxable year there is a recapture amount determined with respect to any property the basis of which was reduced under the preceding sentence, the basis of such property (immediately before the event resulting in such recapture) shall be increased by an amount equal to such recapture amount. (2) Recapture The Secretary shall, by regulations, provide for recapturing the benefit of any credit allowable under subsection (a) with respect to any property which ceases to be property eligible for such credit (including recapture in cases where the taxpayer ceases to be engaged in the trade or business of operating a commercial egg hatchery). (3) Property used outside united states not qualified No credit shall be allowable under subsection (a) with respect to any property which is used predominantly outside the United States. The preceding sentence shall not apply to any property described in section 50(b)(2). (4) Certain rules to apply Rules similar to the rules of section 50 shall apply for purposes of this section. (e) Definitions For purposes of this section, the term commercial egg hatchery facility means a facility the primary purpose of which is to hatch chicks for commercial egg production. (f) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this section. (g) Termination This section shall not apply to property placed in service after December 31, 2028. .\n##### (b) Credit made part of general business credit\nSection 38(b) of the Internal Revenue Code of 1986 (relating to current year business credit) is amended by striking the period at the end of paragraph (41) and inserting a comma, and by adding at the end the following new paragraph:\n(42) the layer operation efficiency equipment credit determined under section 45BB(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Layer operation efficiency equipment credit. .\n##### (d) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to property placed in service after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2025-10-17",
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
        "updateDate": "2025-11-20T18:00:21Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5776ih.xml"
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
      "title": "EGG SAVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EGG SAVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Efficiency Gains through Grading Standards And Viable Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a tax credit for layer operation efficiency equipment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T06:03:20Z"
    }
  ]
}
```
