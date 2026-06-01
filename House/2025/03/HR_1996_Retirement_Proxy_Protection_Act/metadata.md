# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1996?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1996
- Title: Retirement Proxy Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 1996
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-04-21T17:45:32Z
- Update date including text: 2026-04-21T17:45:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1996",
    "number": "1996",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Retirement Proxy Protection Act",
    "type": "HR",
    "updateDate": "2026-04-21T17:45:32Z",
    "updateDateIncludingText": "2026-04-21T17:45:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "UT"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1996ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1996\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Houchin (for herself, Mr. Owens , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to clarify the application of prudence and exclusive purpose duties to the exercise of shareholder rights.\n#### 1. Short title\nThis Act may be cited as the Retirement Proxy Protection Act .\n#### 2. Exercise of shareholder rights\n##### (a) In general\nSection 404 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104 ) is amended by adding at the end the following new subsection:\n(f) Exercise of shareholder rights (1) Authority to exercise shareholder rights (A) In general The fiduciary duty to manage plan assets that are shares of stock includes the management of shareholder rights appurtenant to those shares, including the right to vote proxies. When deciding whether to exercise a shareholder right and in exercising such right, including the voting of proxies, a fiduciary must act prudently and solely in the interests of participants and beneficiaries and for the exclusive purpose of providing benefits to participants and beneficiaries and defraying the reasonable expenses of administering the plan. The fiduciary duty to manage shareholder rights appurtenant to shares of stock does not require the voting of every proxy or the exercise of every shareholder right. (B) Exception This subsection shall not apply to voting, tender, and similar rights with respect to securities that are passed through pursuant to the terms of an individual account plan to participants and beneficiaries with accounts holding such securities. (2) Requirements for exercise of shareholder rights A fiduciary, when deciding whether to exercise a shareholder right and when exercising a shareholder right\u2014 (A) shall\u2014 (i) act solely in accordance with the economic interest of the plan and its participants and beneficiaries; (ii) consider any costs involved; (iii) evaluate material facts that form the basis for any particular proxy vote or exercise of shareholder rights; and (iv) maintain a record of any proxy vote, proxy voting activity, or other exercise of a shareholder right, including any attempt to influence management; and (B) shall not subordinate the interests of participants and beneficiaries in their retirement income or financial benefits under the plan to any non-pecuniary objective, or promote non-pecuniary benefits or goals unrelated to those financial interests of the plan\u2019s participants and beneficiaries. (3) Monitoring A fiduciary shall exercise prudence and diligence in the selection and monitoring of a person, if any, selected to advise or otherwise assist with the exercise of shareholder rights, including by providing research and analysis, recommendations on exercise of proxy voting or other shareholder rights, administrative services with respect to voting proxies, and recordkeeping and reporting services. (4) Investment managers and proxy advisory firms Where the authority to vote proxies or exercise other shareholder rights has been delegated to an investment manager pursuant to section 403(a), or a proxy voting advisory firm or other person who performs advisory services as to the voting of proxies or the exercise of other shareholder rights, a responsible plan fiduciary shall prudently monitor the proxy voting activities of such investment manager or advisory firm and determine whether such activities are in compliance with paragraphs (1) and (2). (5) Voting policies (A) In general In deciding whether to vote a proxy pursuant to this subsection, the plan fiduciary may adopt a proxy voting policy, including a safe harbor proxy voting policy described in subparagraph (B), providing that the authority to vote a proxy shall be exercised pursuant to specific parameters designed to serve the economic interest of the plan. (B) Safe harbor voting policy With respect to a decision not to vote a proxy, a fiduciary shall satisfy the fiduciary responsibilities under this subsection if such fiduciary adopts and is following a safe harbor proxy voting policy that\u2014 (i) limits voting resources to particular types of proposals that the fiduciary has prudently determined are substantially related to the business activities of the issuer or are expected to have a material effect on the value of the plan investment; or (ii) establishes that the fiduciary will refrain from voting on proposals or particular types of proposals when the assets of a plan invested in the issuer relative to the total assets of such plan are below 5 percent (or, in the event such assets are under management, when the assets under management invested in the issuer are below 5 percent of the total assets under management). (C) Exception No proxy voting policy adopted pursuant to this paragraph shall preclude a fiduciary from submitting a proxy vote when the fiduciary determines that the matter being voted on is expected to have a material economic effect on the investment performance of a plan\u2019s portfolio (or the investment performance of assets under management in the case of an investment manager); provided, however, that in all cases compliance with a safe harbor voting policy shall be presumed to satisfy fiduciary responsibilities with respect to decisions not to vote. (6) Review A fiduciary shall periodically review any policy adopted under this subsection. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to an exercise of shareholder rights occurring on or after January 1, 2026.",
      "versionDate": "2025-03-10",
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
        "actionDate": "2025-10-30",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3086",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Restoring Integrity in Fiduciary Duty Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-26",
        "text": "Received in the Senate and Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2988",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Prudent Investment of Retirement Savings Act",
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
            "name": "Employee benefits and pensions",
            "updateDate": "2026-02-11T17:27:23Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-02-11T17:27:23Z"
          },
          {
            "name": "Securities",
            "updateDate": "2026-02-11T17:27:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-05-09T15:35:13Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1996ih.xml"
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
      "title": "Retirement Proxy Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retirement Proxy Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 to clarify the application of prudence and exclusive purpose duties to the exercise of shareholder rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:25Z"
    }
  ]
}
```
