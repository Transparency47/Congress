# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/445?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/445
- Title: Border Security Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 445
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-18T22:02:53Z
- Update date including text: 2025-03-18T22:02:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/445",
    "number": "445",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Border Security Investment Act",
    "type": "HR",
    "updateDate": "2025-03-18T22:02:53Z",
    "updateDateIncludingText": "2025-03-18T22:02:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-15T18:45:02Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-15T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr445ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 445\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Moran (for himself, Mr. Ellzey , Mr. Self , Mr. Babin , Mr. Gooden , Mr. Nehls , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish trust funds relating to border security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Border Security Investment Act .\n#### 2. Establishment of trust funds relating to border security\n##### (a) Additional remittance transfer fees\nSection 920 of the Electronic Fund Transfer Act (relating to remittance transfers) ( 15 U.S.C. 1693o\u20131 ) is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h); and\n**(2)**\nby inserting after subsection (f) the following:\n(g) Additional remittance fees (1) In general A remittance transfer provider that is a money services business shall impose a fee on each person sending a remittance transfer to a covered country in an amount equal to 37 percent of the remittance transfer amount. (2) Transfer of fees All fees collected under this subsection shall be submitted to the Department of the Treasury for deposit in the general fund, in such form and in such manner as the Secretary of the Treasury shall establish by rule. (3) Definitions In this subsection: (A) Covered country With respect to a fiscal year, the term covered country means each country identified by the Commissioner of U.S. Customs and Border Protection as one of the 5 countries that had the most citizens or nationals unlawfully enter the United States during the previous fiscal year. (B) Money services business The term money services business has the meaning given that term under section 1010.100 of title 31, Code of Federal Regulations. .\n##### (b) Border Security State Reimbursement Trust Fund\n**(1) In general**\nThere is established in the Treasury a trust fund, to be known as the Border Security State Reimbursement Trust Fund (in this section referred to as the Reimbursement Fund ), consisting of amounts transferred under paragraph (2) and any amounts credited under paragraph (3).\n**(2) Transfer**\nIn the fiscal year that begins immediately after the date of the enactment of this Act and each fiscal year thereafter, the Secretary of the Treasury shall transfer to the Reimbursement Fund, from the general fund of the Treasury, an amount equal to fifty percent of the total amount of remittance fees collected under subsection (g)(2) of section 920 of the Electronic Fund Transfer Act (relating to remittance transfers; 15 U.S.C. 1693o\u20131 ) during the immediately preceding fiscal year.\n**(3) Investment of amounts**\n**(A) In general**\nThe Secretary of the Treasury shall invest such portion of the Reimbursement Fund as is not required to meet current withdrawals in interest-bearing obligations of the United States or in obligations guaranteed as to both principal and interest by the United States.\n**(B) Interest and proceeds**\nThe interest on, and the proceeds from the sale or redemption of, any obligations held in the Reimbursement Fund shall be credited to the Reimbursement Fund.\n**(4) Purpose; application**\n**(A) In general**\nAmounts in the Reimbursement Fund shall be available to the Secretary of Homeland Security, without further appropriation, to reimburse border States for expenditures incurred by such States relating to border security enforcement measures.\n**(B) Application**\nNot later than 30 days after the date of the enactment of this Act, a border State may apply to the Secretary to receive amounts from the Reimbursement Fund by submitting receipts, in such form and manner as the Secretary deems appropriate, of expenditures relating to border security enforcement measures made during the immediately preceding fiscal year.\n**(C) Amount**\nThe Secretary shall promptly distribute from the Reimbursement Fund, to any border State that submits an application under subparagraph (B), an amount equal to the proportion that the amount expended by such a border State in the applicable immediately preceding fiscal year bears to the total amount expended in such fiscal year by all such border States so submitting an application.\n**(D) Border security enforcement measures**\nIn this subparagraph, an expenditure by a border State shall be deemed to be related to border security enforcement measures if that expenditure directly or indirectly was used for the mission of deterring unlawful crossings, detecting unlawful activity and entry into the United States, or for gaining operational control of the southwest border.\n##### (c) Border Security Trust Fund\n**(1) In general**\nThere is established in the Treasury a trust fund, to be known as the Border Security Trust Fund (in this section referred to as the Security Fund ), consisting of amounts transferred under paragraph (2) and any amounts credited under paragraph (3).\n**(2) Transfers**\nIn the fiscal year that begins immediately after the date of the enactment of this Act and each fiscal year thereafter, the Secretary of the Treasury shall transfer to the Security Fund, from the general fund of the Treasury, an amount equal to fifty percent of the total amount of remittance fees collected under subsection (g)(2) of section 920 of the Electronic Fund Transfer Act (relating to remittance transfers; 15 U.S.C. 1693o\u20131 ) during the immediately preceding fiscal year.\n**(3) Investment of amounts**\n**(A) In general**\nThe Secretary of the Treasury shall invest such portion of the Security Fund as is not required to meet current withdrawals in interest-bearing obligations of the United States or in obligations guaranteed as to both principal and interest by the United States.\n**(B) Interest and proceeds**\nThe interest on, and the proceeds from the sale or redemption of, any obligations held in the Security Fund shall be credited to the Security Fund.\n**(4) Purposes**\nAmounts in the Security Fund shall be available to the Secretary of Homeland Security, without further appropriation, for the following purposes:\n**(A)**\nThe deployment of technology intended to detect and prevent unlawful crossings along the United States-Mexico border.\n**(B)**\nThe installation of physical barriers at the southern border.\n**(C)**\nWages and salaries for U.S. Border Patrol agents.\n##### (d) Rescission of excess amounts\nIf the sum of the total funds in each of the Reimbursement Fund and the Security Fund is greater than $50,000,000,000, an amount equal to the funds in excess of $50,000,000,000 shall be\u2014\n**(1)**\npermanently rescinded from such total funds; and\n**(2)**\ndeposited in the general fund of the Treasury where such funds shall be\u2014\n**(A)**\ndedicated for the sole purpose of deficit reduction; and\n**(B)**\nprohibited from use as an offset for other spending increases or revenue reductions.\n##### (e) Effective date\nThis Act and the amendment made by this Act shall take effect and apply not later than 30 days after the date of the enactment of this Act.",
      "versionDate": "2025-01-15",
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
        "name": "Immigration",
        "updateDate": "2025-02-13T15:15:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr445",
          "measure-number": "445",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr445v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Border Security Investment Act</strong></p><p>This bill imposes a fee on the electronic transfer of funds (i.e.,\u00a0remittances) sent to certain countries and provides funding for border security activities from the collected amounts.</p><p>Specifically, the fee shall apply to remittances sent through money services business to one of the five countries that had the most citizens or nationals unlawfully enter the United States in the previous fiscal year, as determined by U.S. Customs and Border Protection. The fee must be 37% of the amount sent.</p><p>Half of the money collected by the fee must be placed in a trust fund for reimbursing border states for expenses incurred for border security enforcement measures. The other half must be placed in another trust fund for (1) deploying technology and installing physical barriers along the U.S.-Mexico border, and (2) paying the wages and salaries of U.S. Border Patrol agents.</p><p>If the amount in the trust funds exceeds a certain threshold, the excess money must be used only for deficit reduction.</p>"
        },
        "title": "Border Security Investment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr445.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Border Security Investment Act</strong></p><p>This bill imposes a fee on the electronic transfer of funds (i.e.,\u00a0remittances) sent to certain countries and provides funding for border security activities from the collected amounts.</p><p>Specifically, the fee shall apply to remittances sent through money services business to one of the five countries that had the most citizens or nationals unlawfully enter the United States in the previous fiscal year, as determined by U.S. Customs and Border Protection. The fee must be 37% of the amount sent.</p><p>Half of the money collected by the fee must be placed in a trust fund for reimbursing border states for expenses incurred for border security enforcement measures. The other half must be placed in another trust fund for (1) deploying technology and installing physical barriers along the U.S.-Mexico border, and (2) paying the wages and salaries of U.S. Border Patrol agents.</p><p>If the amount in the trust funds exceeds a certain threshold, the excess money must be used only for deficit reduction.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr445"
    },
    "title": "Border Security Investment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Border Security Investment Act</strong></p><p>This bill imposes a fee on the electronic transfer of funds (i.e.,\u00a0remittances) sent to certain countries and provides funding for border security activities from the collected amounts.</p><p>Specifically, the fee shall apply to remittances sent through money services business to one of the five countries that had the most citizens or nationals unlawfully enter the United States in the previous fiscal year, as determined by U.S. Customs and Border Protection. The fee must be 37% of the amount sent.</p><p>Half of the money collected by the fee must be placed in a trust fund for reimbursing border states for expenses incurred for border security enforcement measures. The other half must be placed in another trust fund for (1) deploying technology and installing physical barriers along the U.S.-Mexico border, and (2) paying the wages and salaries of U.S. Border Patrol agents.</p><p>If the amount in the trust funds exceeds a certain threshold, the excess money must be used only for deficit reduction.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr445"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr445ih.xml"
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
      "title": "Border Security Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Border Security Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish trust funds relating to border security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:19Z"
    }
  ]
}
```
