# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2323?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2323
- Title: HEADWAY Act
- Congress: 119
- Bill type: S
- Bill number: 2323
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-08T15:25:13Z
- Update date including text: 2026-04-08T15:25:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2323",
    "number": "2323",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "HEADWAY Act",
    "type": "S",
    "updateDate": "2026-04-08T15:25:13Z",
    "updateDateIncludingText": "2026-04-08T15:25:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
        "item": [
          {
            "date": "2026-03-19T14:00:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-17T16:24:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "NM"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2323is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2323\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Warnock (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Head Start Act to permit some teachers in Early Head Start programs to teach while earning a child development associate credential.\n#### 1. Short title\nThis Act may be cited as the Head start Education And Development Workforce Advancement and Yield Act or the HEADWAY Act .\n#### 2. Teachers in Early Head Start programs\nSection 645A(h) of the Head Start Act ( 42 U.S.C. 9840a(h) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking , not later than September 30, 2010, all teachers and inserting at least one teacher per classroom who is ;\n**(B)**\nby striking Early Head Start programs located in Early Head Start centers, have a minimum and inserting an Early Head Start program located in an Early Head Start center, has a minimum ;\n**(C)**\nby striking have been trained (or have and inserting has been trained (or has ; and\n**(D)**\nby striking and at the end;\n**(2)**\nby redesignating paragraph (2) as paragraph (3);\n**(3)**\nby inserting after paragraph (1) the following:\n(2) ensure that\u2014 (A) each additional teacher providing direct services to children and families described in paragraph (1) is working towards earning a credential that is, at a minimum, a child development associate credential and towards completing training (or equivalent coursework in early childhood development); and (B) during the period in which such a teacher is working towards earning that credential and completing that training or coursework, the Early Head Start agency employing the teacher shall provide a mentor to oversee the progress and guide the work of the teacher towards earning that credential and completing that training or coursework; and ; and\n**(4)**\nin paragraph (3), as so redesignated\u2014\n**(A)**\nby striking not later than September 30, 2012, all such teachers and inserting at least one teacher per classroom providing direct services to children and families described in paragraph (1) has ;\n**(B)**\nby striking (or have and inserting (or has ; and\n**(C)**\nby striking the period at the end and inserting , and that each additional teacher providing direct services to such children and families is working towards completing that training or coursework. .",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HEADWAY Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Preschool education",
            "updateDate": "2026-03-20T14:33:39Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-03-20T14:33:39Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2026-03-20T14:33:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-09-05T16:11:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s2323",
          "measure-number": "2323",
          "measure-type": "s",
          "orig-publish-date": "2025-07-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2323v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Head start Education And Development Workforce Advancement and Yield Act or the HEADWAY Act</strong></p><p>This bill allows some teachers in Early Head Start programs to teach while in the process of earning their Child Development Associate (CDA) credential and completing training.</p><p>Currently, the Department of Health and Human Services (HHS) must ensure that all teachers providing direct services to children and families in Early Head Start centers (1) have a minimum of a CDA credential and have been trained in early childhood development, and (2) have been trained in early childhood development with a focus on infant and toddler development.</p><p>The bill revises this requirement by requiring at least one teacher per classroom (instead of all teachers) to have a CDA credential and training. In particular, the bill requires HHS to ensure that (1) each additional teacher providing direct services to children and families is in the process of earning a CDA credential and completing training, and (2) the Early Head Start agency provides a mentor to oversee the progress and guide the work of a teacher who is in the process of earning a CDA credential and completing training.</p>"
        },
        "title": "HEADWAY Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2323.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Head start Education And Development Workforce Advancement and Yield Act or the HEADWAY Act</strong></p><p>This bill allows some teachers in Early Head Start programs to teach while in the process of earning their Child Development Associate (CDA) credential and completing training.</p><p>Currently, the Department of Health and Human Services (HHS) must ensure that all teachers providing direct services to children and families in Early Head Start centers (1) have a minimum of a CDA credential and have been trained in early childhood development, and (2) have been trained in early childhood development with a focus on infant and toddler development.</p><p>The bill revises this requirement by requiring at least one teacher per classroom (instead of all teachers) to have a CDA credential and training. In particular, the bill requires HHS to ensure that (1) each additional teacher providing direct services to children and families is in the process of earning a CDA credential and completing training, and (2) the Early Head Start agency provides a mentor to oversee the progress and guide the work of a teacher who is in the process of earning a CDA credential and completing training.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2323"
    },
    "title": "HEADWAY Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Head start Education And Development Workforce Advancement and Yield Act or the HEADWAY Act</strong></p><p>This bill allows some teachers in Early Head Start programs to teach while in the process of earning their Child Development Associate (CDA) credential and completing training.</p><p>Currently, the Department of Health and Human Services (HHS) must ensure that all teachers providing direct services to children and families in Early Head Start centers (1) have a minimum of a CDA credential and have been trained in early childhood development, and (2) have been trained in early childhood development with a focus on infant and toddler development.</p><p>The bill revises this requirement by requiring at least one teacher per classroom (instead of all teachers) to have a CDA credential and training. In particular, the bill requires HHS to ensure that (1) each additional teacher providing direct services to children and families is in the process of earning a CDA credential and completing training, and (2) the Early Head Start agency provides a mentor to oversee the progress and guide the work of a teacher who is in the process of earning a CDA credential and completing training.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2323"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2323is.xml"
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
      "title": "HEADWAY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HEADWAY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Head start Education And Development Workforce Advancement and Yield Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Head Start Act to permit some teachers in Early Head Start programs to teach while earning a child development associate credential.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:19Z"
    }
  ]
}
```
