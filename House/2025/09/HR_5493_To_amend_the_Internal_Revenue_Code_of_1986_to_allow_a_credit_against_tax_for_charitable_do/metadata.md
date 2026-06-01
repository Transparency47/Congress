# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5493
- Title: USA Workforce Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 5493
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-11-21T15:58:20Z
- Update date including text: 2025-11-21T15:58:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5493",
    "number": "5493",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "USA Workforce Investment Act",
    "type": "HR",
    "updateDate": "2025-11-21T15:58:20Z",
    "updateDateIncludingText": "2025-11-21T15:58:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:07:05Z",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NE"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5493ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5493\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Smucker (for himself, Mr. Smith of Nebraska , Mr. Kelly of Pennsylvania , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing workforce training.\n#### 1. Short title\nThis Act may be cited as the USA Workforce Investment Act .\n#### 2. Tax credit for contributions of individuals to workforce development or apprenticeship training programs\n##### (a) Allowance of credit\n**(1) In general**\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25F the following new section:\n25G. Contributions to workforce development and apprenticeship training programs (a) Allowance of credit In the case of an individual who is a citizen or resident of the United States (within the meaning of section 7701(a)(9)), there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the aggregate amount of qualified contributions made by the taxpayer during the year. (b) Limitations (1) In general The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed $1,700. (2) Reduction based on State credit The amount allowed as a credit under subsection (a) for a taxable year shall be reduced by the amount allowed as a credit on any State tax return of the taxpayer for qualified contributions made by the taxpayer during the taxable year. (c) Definitions For purposes of this section\u2014 (1) Qualified contribution The term qualified contribution means a charitable contribution (as defined by section 170(c)) to a workforce development or apprenticeship training organization in the form of cash if such contribution is designated by such organization to be used only for the purpose of providing workforce development or apprenticeship training programs. (2) Workforce development or apprenticeship training organization The term workforce development or apprenticeship training organization means any organization which\u2014 (A) is described in section 501(c)(3), is exempt from tax under section 501(a), and is not a private foundation, and (B) is included on a list of providers prepared under subsection (d) of section 122 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152 ) by reason of having been determined to be eligible to offer a program under such section. (3) Workforce development or apprenticeship training program The term workforce development or apprenticeship training program means a program to provide training services (within the meaning of section 134(c)(3) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3174(c)(3) )). (d) Denial of double benefit Any qualified contribution for which a credit is allowed under this section shall not be taken into account as a charitable contribution for purposes of section 170. (e) Carryforward of unused credit (1) In general If the credit allowable under subsection (a) for any taxable year exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section and sections 23, 25D, and 25E), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year following the fifth taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in first-out basis. .\n**(2) Conforming amendments**\n**(A)**\nSection 25(e)(1)(C) of such Code is amended by striking and 25F and inserting 25F, and 25G .\n**(B)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25G. Contributions to workforce development and apprenticeship training programs. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-11-21T15:58:20Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5493ih.xml"
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
      "title": "USA Workforce Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA Workforce Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing workforce training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:48:39Z"
    }
  ]
}
```
