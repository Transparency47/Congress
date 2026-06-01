# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7419?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7419
- Title: Foster Care Stabilization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7419
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-27T16:09:21Z
- Update date including text: 2026-02-27T16:09:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7419",
    "number": "7419",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Foster Care Stabilization Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-27T16:09:21Z",
    "updateDateIncludingText": "2026-02-27T16:09:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:03:10Z",
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
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7419ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7419\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Bacon (for himself, Ms. Scanlon , Mr. Nunn of Iowa , and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title IV of the Social Security Act to establish a demonstration grant program to provide emergency relief to foster youth and improve pre-placement services offered by foster care stabilization agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foster Care Stabilization Act of 2026 .\n#### 2. Grants to improve pre-placement services for foster youth\nSection 426 of the Social Security Act ( 42 U.S.C. 626 ) is amended by adding at the end the following:\n(d) Grants To improve pre-Placement services for foster youth (1) Establishment The Secretary shall award 3 demonstration grants of not more than $1,000,000 to foster care stabilization agencies for the purpose of providing emergency relief to foster youth and improving pre-placement services for foster youth waiting for placement. (2) Duration A foster care stabilization agency that receives a grant under this subsection shall have 3 years to spend funds awarded by the grant and return any unused grant funds to the Secretary. (3) Application A foster care stabilization agency that desires to receive a grant under this subsection shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, that shall include the following: (A) A description of how grant funds will be used to provide emergency relief to foster youth by the foster care stabilization agency. (B) A description of how grant funds will be used to improve pre-placement services offered by the foster care stabilization agency. (4) Application dissemination The Secretary shall ensure that the solicitation of applications for a grant under this subsection is posted publicly on the website of the Administration for Children and Families and shall make special dissemination efforts to rural areas and among Indian Tribes, Tribal organizations, and Native Hawaiian organizations. (5) Use of funds A grant awarded under this subsection may be used to carry out any of the following activities: (A) Hiring of personnel necessary to provide emergency relief to foster youth and ensure that services, resources, and assistance reach such youth. (B) Provision of clothing and other personal necessities to a foster youth for a total not to exceed $250 per foster youth, per year. (C) Purchase of food and equipment needed to prepare food for foster youth. (D) Provision of service and support to prevent and respond to occurrences of child abuse and neglect with respect to foster youth. (E) Any other extraordinary or emergency assistance needed to promote the safety and self-sufficiency of foster youth. (F) Any other purpose that the Secretary determines appropriate. (6) Reservation The Secretary shall reserve $45,000 of any amounts referred to in paragraph (9) for administration, oversight, and technical assistance activities related to this subsection. (7) Report The Secretary shall submit to the Congress a report that\u2014 (A) describes how grants awarded under this subsection have been used to provide emergency relief to foster youth; (B) describes how grants awarded under this subsection have been used on pre-placement services; (C) contains data on the extent of clothing and other necessities purchased with grant funds awarded under this subsection that have been provided to foster youth; (D) provides an evaluation of case outcomes for foster youth who have benefitted from grant funds; and (E) states the number of home transfers for each foster youth that has benefitted from grant funds. (8) Definitions In this subsection: (A) Foster care stabilization agency The term foster care stabilization agency means a local public or private nonprofit entity, including a community or faith-based organization, with expertise and experience providing direct services to 1 or more of the following: (i) Children who are under the care and placement responsibility of a State or tribal agency that administers a plan under this part or part E. (ii) Foster youth who have not attained 18 years of age. (iii) Foster youth who have attained 18 years of age. (B) Foster youth The term foster youth means an individual in foster care who has not attained 26 years of age. (C) Home transfer The term home transfer means the initial placement of a foster youth in foster care, and any subsequent placement of that foster youth while in foster care. (9) Funding To the extent that the total of the amounts made available under subsection (a) for a fiscal year exceeds $5,000,000 more than the amount so made available for the previous fiscal year, the Secretary shall use the amounts to carry out this subsection. .",
      "versionDate": "2026-02-09",
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
        "actionDate": "2026-02-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3802",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Foster Care Stabilization Act of 2026",
      "type": "S"
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
        "name": "Families",
        "updateDate": "2026-02-18T16:55:09Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7419ih.xml"
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
      "title": "Foster Care Stabilization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T04:43:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foster Care Stabilization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T04:43:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title IV of the Social Security Act to establish a demonstration grant program to provide emergency relief to foster youth and improve pre-placement services offered by foster care stabilization agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:18:37Z"
    }
  ]
}
```
