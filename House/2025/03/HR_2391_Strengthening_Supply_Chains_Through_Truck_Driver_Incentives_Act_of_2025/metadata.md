# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2391?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2391
- Title: Strengthening Supply Chains Through Truck Driver Incentives Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2391
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-02-27T21:41:19Z
- Update date including text: 2026-02-27T21:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2391",
    "number": "2391",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Strengthening Supply Chains Through Truck Driver Incentives Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-27T21:41:19Z",
    "updateDateIncludingText": "2026-02-27T21:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:02:20Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NV"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2391ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2391\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Ryan (for himself, Mr. Nunn of Iowa , and Mr. Amodei of Nevada ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a refundable tax credit for commercial truck drivers.\n#### 1. Short title\nThis Act may be cited as the Strengthening Supply Chains Through Truck Driver Incentives Act of 2025 .\n#### 2. Credit for commercial truck drivers\n##### (a) In general\nThe Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Credit for commercial truck drivers (a) Allowance of credit In the case of an eligible individual, there shall be allowed as a credit against the tax imposed by this subtitle an amount equal to $7,500 for the taxable year. (b) Eligible individual For the purposes of this section, the term eligible taxpayer means, with respect to a taxable year, an individual\u2014 (1) who holds a valid Class A commercial driver\u2019s license (except as provided in subsection (c)) who operates a tractor-trailer combination that qualifies as a Group A vehicle under section 383.91(a)(1) of title 49, Code of Federal Regulations, (2) whose adjusted gross income for the taxable year does not exceed\u2014 (A) in the case of a joint return or surviving spouse, $135,000, (B) in the case of an individual who is a head of household, $112,500, or (C) in the case of any other individual, $90,000, and (3) who drove such a vehicle in the course of a trade or business\u2014 (A) not less than 1900 hours during such taxable year, or (B) in the case of an individual who did not drive a commercial truck in the preceding taxable year, not less than an average of 40 hours per week with respect to weeks during the taxable year in which such individual drove such a vehicle in the course of a trade or business. (c) Special rule for apprentices With respect to an individual enrolled in an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ), who, upon completion or in the course of such apprenticeship program will receive a Class A commercial driver\u2019s license\u2014 (1) the requirements of subsection (b)(1) shall not apply, and (2) such individual may count training hours in such program as hours driving a vehicle described in subsection (b)(1) for the purposes of this section. (d) Special rule for new truck drivers Except as provided in subsection (e), in the case of an eligible taxpayer who did not drive a commercial truck in the course of a trade or business during the preceding taxable year, subsection (a) shall be applied by substituting $10,000 for $7,500 . (e) Special rule for drivers with less than 1420 hours In the case of an eligible taxpayer who did not drive a commercial truck in the preceding taxable year who drives a commercial truck for less than 1420 hours in the course of a trade or business during the taxable year, the amount of the credit allowed by subsection (a) shall be the amount that bears the same proportion to the dollar amount (determined without regard to this subsection) with respect to the individual under subsection (a) as the number of hours such individual drove a commercial truck in the course of a trade or business during such taxable years bears to 1420 hours. (f) Inflation adjustment In the case of any taxable year beginning after 2025, the dollar amounts in this section shall be increased by an amount equal to\u2014 (1) such dollar amount, multiplied by (2) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii). (g) Termination date This section shall not apply to any taxable year beginning after December 31, 2026. .\n##### (b) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting , 36C after 36B .\n**(2)**\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting , 36C after , 36B .\n**(3)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Credit for commercial truck drivers. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending on or after December 31, 2025.",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-05-09T14:50:21Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2391ih.xml"
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
      "title": "Strengthening Supply Chains Through Truck Driver Incentives Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Supply Chains Through Truck Driver Incentives Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a refundable tax credit for commercial truck drivers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:37Z"
    }
  ]
}
```
