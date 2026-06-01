# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5277?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5277
- Title: HEAL Act
- Congress: 119
- Bill type: HR
- Bill number: 5277
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-04-10T16:22:56Z
- Update date including text: 2026-04-10T16:22:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-09-22 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-09-22 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5277",
    "number": "5277",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "HEAL Act",
    "type": "HR",
    "updateDate": "2026-04-10T16:22:56Z",
    "updateDateIncludingText": "2026-04-10T16:22:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-22",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-22T17:10:37Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5277ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5277\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the payments or allowances that individuals, including veterans service organizations, receive for transportation of veterans to or from facilities of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heroes Earned Affordable Lifts Act or the HEAL Act .\n#### 2. Expansion of payments or allowances for transportation of veterans to or from Department facilities\n##### (a) Milage reimbursement rate\nSection 111 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking at a rate of 41.5 cents per mile and inserting at the rate prescribed under subsection (g) ;\n**(2)**\nin subsection (b)(1), by striking Except as provided in subsection (c) of this section and notwithstanding subsection (g)(2) of this section or and inserting Notwithstanding ; and\n**(3)**\nby amending subsection (g) to read as follows:\n(g) The Secretary shall set the mileage rate under subsection (a) to be equal to the rate for a privately owned automobile when no Government vehicle is available, as prescribed by the Administrator of General Services under section 5707(b) of title 5. .\n##### (b) Prohibition on certain deductible payments\nSection 111(c) of such title is amended to read as follows:\n(c) The Secretary may not require a deductible for travel for examination, treatment, or care under this section. .\n##### (c) Veterans service organizations\n**(1)**\nSection 111(e)(2)(B) of such title is amended\u2014\n**(A)**\nby striking subparagraph is and all that follows and inserting subparagraph is\u2014 ; and\n**(B)**\nby adding at the end the following new clauses:\n(i) a provider of personal care services for such veteran who is approved under paragraph (6) of section 1720G(a) of this title or designated under paragraph (7) of such section 1720G(a); (ii) a veterans service organization that provides transportation for such veteran under section 111A of this title; or (iii) a veterans service agency of a local government, including an employee or a volunteer of such agency, that provides transportation for such veteran. .\n**(2)**\nSection 111A(b) of such title is amended\u2014\n**(A)**\nby striking veterans\u2019 service and inserting veterans service ; and\n**(B)**\nby striking , without reimbursement from the Department, and inserting (reimbursable by the Department only to the extent allowable under section 111 of this title) .",
      "versionDate": "",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-18T15:50:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-10",
    "originChamber": "House",
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
          "measure-id": "id119hr5277",
          "measure-number": "5277",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5277v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-09-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Heroes Earned Affordable Lifts Act or the HEAL Act</strong></p><p>This bill modifies the administration of the Department of Veteran Affairs (VA) beneficiary travel benefit available to individuals traveling for vocational rehabilitation, required counseling, or for examination, treatment, or care.</p><p>The bill increases the mileage reimbursement rate for beneficiary travel to or from VA facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment or care. Specifically, the bill raises the rate from 41.5 cents per mile to the rate for a privately owned automobile when no government vehicle is available (currently 70 cents per mile).</p><p>The bill prohibits the VA from requiring a deductible for beneficiary travel for examination, treatment, or care.</p><p>The bill also provides that veterans service organizations and veterans service agencies that provide transportation for examinations, treatment, or care to veterans may be allowed expenses of travel upon the same basis as such veteran beneficiaries.</p>"
        },
        "title": "HEAL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5277.xml",
    "summary": {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heroes Earned Affordable Lifts Act or the HEAL Act</strong></p><p>This bill modifies the administration of the Department of Veteran Affairs (VA) beneficiary travel benefit available to individuals traveling for vocational rehabilitation, required counseling, or for examination, treatment, or care.</p><p>The bill increases the mileage reimbursement rate for beneficiary travel to or from VA facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment or care. Specifically, the bill raises the rate from 41.5 cents per mile to the rate for a privately owned automobile when no government vehicle is available (currently 70 cents per mile).</p><p>The bill prohibits the VA from requiring a deductible for beneficiary travel for examination, treatment, or care.</p><p>The bill also provides that veterans service organizations and veterans service agencies that provide transportation for examinations, treatment, or care to veterans may be allowed expenses of travel upon the same basis as such veteran beneficiaries.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr5277"
    },
    "title": "HEAL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heroes Earned Affordable Lifts Act or the HEAL Act</strong></p><p>This bill modifies the administration of the Department of Veteran Affairs (VA) beneficiary travel benefit available to individuals traveling for vocational rehabilitation, required counseling, or for examination, treatment, or care.</p><p>The bill increases the mileage reimbursement rate for beneficiary travel to or from VA facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment or care. Specifically, the bill raises the rate from 41.5 cents per mile to the rate for a privately owned automobile when no government vehicle is available (currently 70 cents per mile).</p><p>The bill prohibits the VA from requiring a deductible for beneficiary travel for examination, treatment, or care.</p><p>The bill also provides that veterans service organizations and veterans service agencies that provide transportation for examinations, treatment, or care to veterans may be allowed expenses of travel upon the same basis as such veteran beneficiaries.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr5277"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5277ih.xml"
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
      "title": "HEAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heroes Earned Affordable Lifts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to increase the payments or allowances that individuals, including veterans service organizations, receive for transportation of veterans to or from facilities of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:32Z"
    }
  ]
}
```
