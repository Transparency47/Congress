# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6943?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6943
- Title: Veterans Burial Allowance and Reimbursement Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6943
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-03-27T08:06:15Z
- Update date including text: 2026-03-27T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6943",
    "number": "6943",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Veterans Burial Allowance and Reimbursement Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:15Z",
    "updateDateIncludingText": "2026-03-27T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
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
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T23:30:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-27T03:15:06Z",
                "name": "Reported by"
              },
              {
                "date": "2026-03-26T14:27:52Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-03T16:51:39Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-29T16:42:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6943ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6943\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Mr. Evans of Colorado introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to standardize the payment of burial and funeral expenses and plot allowances for deceased veterans under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Burial Allowance and Reimbursement Act of 2026 .\n#### 2. Standardization of certain burial benefits available under laws administered by the Secretary of Veterans Affairs\n##### (a) In general\nSection 2303 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking the heading and inserting Deceased veterans: burial and funeral expenses; plot allowance ;\n**(2)**\nin subsection (a)(2)\u2014\n**(A)**\nby striking who is not covered by section 2307 of this title and ;\n**(B)**\nby redesignating subparagraphs (A) through (C) as subparagraphs (B) through (D), respectively; and\n**(C)**\nby inserting before subparagraph (B), as so redesignated, the following new subparagraph:\n(A) The deceased veteran dies as a result of a service-connected disability or disabilities. ; and\n**(3)**\nin subsection (d), by striking subparagraph (B) or (C) and inserting subparagraph (C) or (D) .\n##### (b) Conforming repeal\nSection 2307 of such title is repealed.\n##### (c) Clerical amendments\nSuch title is further amended\u2014\n**(1)**\nin section 2303(b)(1)(B)(ii), by striking the period at the end and inserting ; and ;\n**(2)**\nin section 2308\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking in subparagraph (B) or (C) and inserting subparagraph (C) or (D) ; and\n**(ii)**\nby striking , or pursuant to section 2307 of this title, ; and\n**(B)**\nin subsection (b), by striking subsection (a)(2)(C) and inserting subsection (a)(2)(D) ; and\n**(3)**\nin section 5101, by striking sections 2303, 2307, and 5121 and inserting sections 2303 and 5121 .",
      "versionDate": "2026-01-06",
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
        "updateDate": "2026-01-21T16:08:55Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6943ih.xml"
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
      "title": "Veterans Burial Allowance and Reimbursement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Burial Allowance and Reimbursement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to standardize the payment of burial and funeral expenses and plot allowances for deceased veterans under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:22Z"
    }
  ]
}
```
