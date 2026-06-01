# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7770
- Title: Hearing Aid Assistance Tax Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 7770
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-04-28T08:06:38Z
- Update date including text: 2026-04-28T08:06:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7770",
    "number": "7770",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Hearing Aid Assistance Tax Credit Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:38Z",
    "updateDateIncludingText": "2026-04-28T08:06:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:35Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
      "state": "VA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7770ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7770\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Mullin introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against income tax for the purchase of hearing aids.\n#### 1. Short title\nThis Act may be cited as the Hearing Aid Assistance Tax Credit Act .\n#### 2. Credit for hearing aids\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25D the following new section:\n25F. Credit for hearing aids (a) Allowance of credit In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter an amount equal to so much of the amount paid during the taxable year, not compensated by insurance or otherwise, by the taxpayer for the purchase of any qualified hearing aid as does not exceed $1,000. (b) Income limitation (1) In general No credit shall be allowed under subsection (a) to any individual if the modified adjusted gross income of such individual exceeds\u2014 (A) $300,000 in the case of a head of household or a joint return, or (B) $150,000 in the case of any other individual. (2) Modified adjusted gross income For purposes of this subsection, the term modified adjusted gross income means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (c) Qualified hearing Aid For purposes of this section, the term qualified hearing aid means a hearing aid\u2014 (1) which is described in sections 874.3300 and 874.3305 of title 21, Code of Federal Regulations, and is authorized under the Federal Food, Drug, and Cosmetic Act for commercial distribution, and (2) which is intended for use\u2014 (A) by the taxpayer, or (B) by an individual with respect to whom the taxpayer, for the taxable year, is allowed a deduction under section 151(c) (relating to deduction for personal exemptions for dependents). (d) Election once every 5 years This section shall apply with respect to any individual for any taxable year only if there is an election in effect with respect to such individual (at such time and in such manner as the Secretary may by regulations prescribe) to have this section apply for such taxable year. An election to have this section apply with respect to any individual may not be made for any taxable year if such an election is in effect with respect to such individual for any of the 4 taxable years preceding such taxable year. (e) Denial of double benefit No credit shall be allowed under subsection (a) for any expense for which a deduction or credit is allowed under any other provision of this chapter. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 25D the following new item:\nSec. 25F. Credit for hearing aids. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-20T15:25:57Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7770ih.xml"
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
      "title": "Hearing Aid Assistance Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hearing Aid Assistance Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against income tax for the purchase of hearing aids.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:23Z"
    }
  ]
}
```
