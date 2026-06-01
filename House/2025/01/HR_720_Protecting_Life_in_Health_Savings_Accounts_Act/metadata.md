# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/720
- Title: Protecting Life in Health Savings Accounts Act
- Congress: 119
- Bill type: HR
- Bill number: 720
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-12-05T21:59:04Z
- Update date including text: 2025-12-05T21:59:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/720",
    "number": "720",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Protecting Life in Health Savings Accounts Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:59:04Z",
    "updateDateIncludingText": "2025-12-05T21:59:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:01:05Z",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "LA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr720ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 720\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Brecheen (for himself, Mr. Webster of Florida , Mrs. Miller of Illinois , Mr. Higgins of Louisiana , Mr. Crenshaw , Mr. Ogles , and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to prohibit treatment of certain distributions and reimbursements for certain abortions as qualified medical expenses.\n#### 1. Short title\nThis Act may be cited as the Protecting Life in Health Savings Accounts Act .\n#### 2. Distributions for certain abortions not qualified\n##### (a) HSAs\n**(1) In general**\nSubparagraph (A) of section 223(d)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following: Such term shall not include any amount paid for an abortion (other than an excluded abortion). .\n**(2) Excluded abortion**\nSection 223(d)(2) of such Code is amended by adding at the end the following new subparagraph:\n(E) Excluded abortion For purposes of this paragraph, the term excluded abortion means any abortion\u2014 (i) with respect to a pregnancy that is the result of an act of rape or incest, or (ii) with respect to which the woman suffers from a physical disorder, physical injury, or physical illness, including a life-endangering physical condition caused by or arising from the pregnancy itself, that would, as certified by a physician, place the woman in danger of death unless the abortion is performed. .\n##### (b) Archer MSAs\nSubparagraph (A) of section 220(d)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following: Such term shall not include any amount paid for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E)). .\n##### (c) Health flexible spending arrangements and health reimbursement arrangements\nSection 106 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(h) Prohibition on reimbursements for abortions For purposes of this section and section 105, reimbursement for expenses incurred for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E)) shall not be treated as a reimbursement for medical expenses. .\n##### (d) Retiree health accounts\nSection 401(h) of the Internal Revenue Code of 1986 is amended by inserting (other than an expense for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E))) after sickness, accident, hospitalization, and medical expenses in the matter preceding paragraph (1).\n##### (e) Effective dates\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to amounts paid with respect to taxable years beginning after December 31, 2025.\n**(2) Reimbursements**\nThe amendment made by subsection (c) shall apply to expenses incurred with respect to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-01-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "251",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Life in Health Savings Accounts Act",
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
        "name": "Taxation",
        "updateDate": "2025-02-25T20:55:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr720",
          "measure-number": "720",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr720v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>"
        },
        "title": "Protecting Life in Health Savings Accounts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr720.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr720"
    },
    "title": "Protecting Life in Health Savings Accounts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr720"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr720ih.xml"
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
      "title": "Protecting Life in Health Savings Accounts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Life in Health Savings Accounts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to prohibit treatment of certain distributions and reimbursements for certain abortions as qualified medical expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:04Z"
    }
  ]
}
```
