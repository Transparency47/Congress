# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/657
- Title: VA CPE Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 657
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-11-13T09:05:39Z
- Update date including text: 2025-11-13T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/657",
    "number": "657",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "VA CPE Modernization Act",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:39Z",
    "updateDateIncludingText": "2025-11-13T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T22:40:50Z",
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
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "RI"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "DC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr657ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 657\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Brownley (for herself, Ms. Hoyle of Oregon , Ms. Tlaib , and Mr. Jackson of Illinois ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the reimbursement of continuing professional education expenses for health care professionals of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Department of Veterans Affairs Continuing Professional Education Modernization Act or the VA CPE Modernization Act .\n#### 2. Improvement to reimbursement of continuing professional education expenses for health care professionals of Department of Veterans Affairs\n##### (a) Reimbursement\nSection 7411 of title 38, United States Code, is amended to read as follows:\n7411. Reimbursement of continuing professional education expenses (a) Reimbursement The Secretary shall reimburse certain full-time health care professionals of the Department for expenses incurred for continuing professional education in amounts as follows: (1) With respect to any physician, dentist, podiatrist, registered nurse, or physician assistant appointed under section 7401(1) of this title, not more than $2,000 per year for each such individual. (2) With respect to any psychologist, licensed practical or vocational nurse, medical technologist, diagnostic radiologic technologist, or social worker appointed under section 7401(3) of this title, not more than $2,000 per year for each such individual. (b) Adjustment The Secretary may from time to time adjust the dollar amounts specified in subsection (a), so long as such adjustment does not result in a reimbursement of less than $2,000 per year for each individual specified in subsection (a). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 74 of such title is amended by striking the item relating to section 7411 and inserting the following new item:\n7411. Reimbursement of continuing professional education expenses. .",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Adult education and literacy",
            "updateDate": "2025-03-19T18:32:12Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-03-19T18:32:06Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-19T18:31:45Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-03-19T18:31:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:56:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr657",
          "measure-number": "657",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr657v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Department of Veterans Affairs Continuing Professional Education Modernization Act or the VA CPE Modernization Act</strong></p> <p>This bill modifies the program under which the Department of Veterans Affairs (VA) reimburses certain full-time health care professionals for continuing professional education expenses.</p> <p>Under current law, only board-certified physicians and dentists are eligible for such reimbursement. The bill expands the program to require reimbursement for various specified full-time health care professionals (e.g., registered nurses) and increases the amount available for a physician or dentist. Additionally, the bill removes the requirement that an individual be board-certified to receive reimbursement.</p> <p>The VA may adjust the amount of the reimbursement, so long as the adjustment does not result in a reimbursement of less than $2,000 per year for each specified position.<br/> </p>"
        },
        "title": "VA CPE Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr657.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Department of Veterans Affairs Continuing Professional Education Modernization Act or the VA CPE Modernization Act</strong></p> <p>This bill modifies the program under which the Department of Veterans Affairs (VA) reimburses certain full-time health care professionals for continuing professional education expenses.</p> <p>Under current law, only board-certified physicians and dentists are eligible for such reimbursement. The bill expands the program to require reimbursement for various specified full-time health care professionals (e.g., registered nurses) and increases the amount available for a physician or dentist. Additionally, the bill removes the requirement that an individual be board-certified to receive reimbursement.</p> <p>The VA may adjust the amount of the reimbursement, so long as the adjustment does not result in a reimbursement of less than $2,000 per year for each specified position.<br/> </p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr657"
    },
    "title": "VA CPE Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Department of Veterans Affairs Continuing Professional Education Modernization Act or the VA CPE Modernization Act</strong></p> <p>This bill modifies the program under which the Department of Veterans Affairs (VA) reimburses certain full-time health care professionals for continuing professional education expenses.</p> <p>Under current law, only board-certified physicians and dentists are eligible for such reimbursement. The bill expands the program to require reimbursement for various specified full-time health care professionals (e.g., registered nurses) and increases the amount available for a physician or dentist. Additionally, the bill removes the requirement that an individual be board-certified to receive reimbursement.</p> <p>The VA may adjust the amount of the reimbursement, so long as the adjustment does not result in a reimbursement of less than $2,000 per year for each specified position.<br/> </p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr657"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr657ih.xml"
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
      "title": "VA CPE Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA CPE Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Department of Veterans Affairs Continuing Professional Education Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the reimbursement of continuing professional education expenses for health care professionals of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:17Z"
    }
  ]
}
```
