# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3698
- Title: Living Organ Donor Tax Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 3698
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2026-01-08T09:07:16Z
- Update date including text: 2026-01-08T09:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3698",
    "number": "3698",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Living Organ Donor Tax Credit Act",
    "type": "HR",
    "updateDate": "2026-01-08T09:07:16Z",
    "updateDateIncludingText": "2026-01-08T09:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-03T16:02:40Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "KS"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3698ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3698\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Wilson of South Carolina (for himself and Mr. Nadler ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a refundable credit to individuals who donate certain life-saving organs.\n#### 1. Short title\nThis Act may be cited as the Living Organ Donor Tax Credit Act .\n#### 2. Credit for donation of certain life-saving organs\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Donation of certain life-saving organs (a) In general In the case of an individual who donates a qualified life-saving organ of such individual for transplantation into another individual during the taxable year, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to the sum of\u2014 (1) costs paid by the taxpayer in connection with such transplantation, (2) travel, lodging, and other logistical expenses, (3) medical expenses related to donation and follow-up care, (4) paperwork or legal costs related to donation, and (5) any lost wages of the individual in connection with such transplantation. (b) Limitation The credit allowed under subsection (a) with respect to any individual for any taxable year shall not exceed $5,000. (c) Definitions and special rules For purposes of this section\u2014 (1) Qualified life-saving organ The term qualified life-saving organ means kidney, liver, lung, pancreas, intestine, bone marrow, or any part thereof. (2) Restriction to living donors Credit shall not be allowed under subsection (a) unless the individual is alive when the qualified life-saving organ is removed from such individual. (3) Transplant must be in accordance with United States law Credit shall not be allowed under subsection (a) unless the donation and transplantation occurs within, and in accordance with the laws of, the United States. (4) Donation Except as provided in regulations by the Secretary, an organ shall not be treated as donated unless and until such organ is removed from the donor. (5) Reimbursed expenses not taken into account There shall not be taken into account under subsection (a) any amounts reimbursed by any person or entity, public or private. .\n##### (b) Public Health Service Act and National Organ Transplant Act amendments\n**(1) Coordination with Federal living organ donation grants**\nSection 377(d) of the Public Health Service Act is amended by inserting that such individual has been allowed, or reasonably expects to be allowed, a tax credit under section 36C of the Internal Revenue Code of 1986 or before that payment has been made .\n**(2) Tax credit not unlawful compensation**\nSection 301(c)(2) of the National Organ Transplant Act is amended by inserting the tax credit allowed under section 36C of the Internal Revenue Code of 1986 or after does not include .\n##### (c) Conforming amendment\nSection 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n##### (d) Clerical amendment\nThe table of sections of such subpart is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Donation of certain life-saving organs. .\n##### (e) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n**(2) Public Health Service Act and National Organ Transplant Act amendments**\nThe amendments made by subsection (b) shall take effect on the date of the enactment of this Act.",
      "versionDate": "2025-06-03",
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
        "updateDate": "2025-06-25T20:18:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-03",
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
          "measure-id": "id119hr3698",
          "measure-number": "3698",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-03",
          "originChamber": "HOUSE",
          "update-date": "2025-07-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3698v00",
            "update-date": "2025-07-10"
          },
          "action-date": "2025-06-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Living Organ Donor Tax Credit Act</strong></p><p>This bill establishes a refundable tax credit of up to $5,000 for expenses related to the removal and donation of all or part of a kidney, liver, lung, pancreas, intestine, or bone marrow by a living individual for transplant into another individual.\u00a0</p><p>Expenses that may be included in the calculation of this tax credit include travel, lodging, medical expenses related to donation and follow-up care, paperwork and legal costs, lost wages, and any other costs paid by the taxpayer in connection with the transplant.\u00a0</p><p>Expenses related to the transplant that are reimbursed by any person or entity (public or private) may not be included in the calculation of the credit amount.</p>"
        },
        "title": "Living Organ Donor Tax Credit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3698.xml",
    "summary": {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Living Organ Donor Tax Credit Act</strong></p><p>This bill establishes a refundable tax credit of up to $5,000 for expenses related to the removal and donation of all or part of a kidney, liver, lung, pancreas, intestine, or bone marrow by a living individual for transplant into another individual.\u00a0</p><p>Expenses that may be included in the calculation of this tax credit include travel, lodging, medical expenses related to donation and follow-up care, paperwork and legal costs, lost wages, and any other costs paid by the taxpayer in connection with the transplant.\u00a0</p><p>Expenses related to the transplant that are reimbursed by any person or entity (public or private) may not be included in the calculation of the credit amount.</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119hr3698"
    },
    "title": "Living Organ Donor Tax Credit Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Living Organ Donor Tax Credit Act</strong></p><p>This bill establishes a refundable tax credit of up to $5,000 for expenses related to the removal and donation of all or part of a kidney, liver, lung, pancreas, intestine, or bone marrow by a living individual for transplant into another individual.\u00a0</p><p>Expenses that may be included in the calculation of this tax credit include travel, lodging, medical expenses related to donation and follow-up care, paperwork and legal costs, lost wages, and any other costs paid by the taxpayer in connection with the transplant.\u00a0</p><p>Expenses related to the transplant that are reimbursed by any person or entity (public or private) may not be included in the calculation of the credit amount.</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119hr3698"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3698ih.xml"
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
      "title": "Living Organ Donor Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Living Organ Donor Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a refundable credit to individuals who donate certain life-saving organs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:18Z"
    }
  ]
}
```
