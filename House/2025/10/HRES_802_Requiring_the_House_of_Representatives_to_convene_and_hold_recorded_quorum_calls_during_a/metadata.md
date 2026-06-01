# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/802?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/802
- Title: Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 802
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-11-11T09:05:16Z
- Update date including text: 2025-11-11T09:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House
- Latest action: 2025-10-10: Submitted in House

## Actions

- 2025-10-10 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/802",
    "number": "802",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-11-11T09:05:16Z",
    "updateDateIncludingText": "2025-11-11T09:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-10T16:32:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-10T16:32:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sponsorshipDate": "2025-10-10",
      "state": "OR"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NV"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "MD"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "DE"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "WA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "HI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OH"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NV"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CT"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "WA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VT"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "GA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "TX"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "WA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "AZ"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres802ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 802\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Moskowitz (for himself, Ms. Hoyle of Oregon , Mr. Whitesides , Mr. Horsford , Ms. Wasserman Schultz , Mrs. McClain Delaney , Mr. Frost , Ms. McBride , Ms. Friedman , Ms. Wilson of Florida , Ms. Jayapal , Mr. Min , Ms. Tokuda , and Mr. Landsman ) submitted the following resolution; which was referred to the Committee on Rules , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nRequiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes.\n#### 1. Requiring House to convene during Government shutdown\n##### (a) In general\nExcept as provided under subsection (b), on each day on which a Government shutdown is in effect, the Speaker of the House of Representatives shall convene a meeting of the House.\n##### (b) Restrictions on recess or adjournment\nDuring a meeting of the House on a day on which a Government shutdown is in effect, it shall not be in order for the House to consider a motion to adjourn or for the Speaker to declare a recess unless\u2014\n**(1)**\nthe House met for each of the first 5 consecutive calendar days on which the Government shutdown is in effect;\n**(2)**\nthe proposed period of adjournment or recess does not last for more than 2 consecutive calendar days; and\n**(3)**\nthe House has met for at least 5 consecutive calendar days since the expiration of the most recent period of adjournment or recess under this subsection.\n#### 2. Mandatory recorded quorum calls\n##### (a) Requirement\nOn each day on which the House is in session while a Government shutdown is in effect, there shall be one or more recorded quorum calls under which each Member of the House shall record the Member\u2019s presence by electronic device.\n##### (b) Imposition of fines for failure To record presence\n**(1) Imposition by Sergeant-at-Arms**\n**(A)**\nThe Sergeant-at-Arms is authorized and directed to impose a fine against a Member for failure to record the presence of the Member on a quorum call under subsection (a) on 2 or more consecutive days, except that the Sergeant-at-Arms may not impose a fine against a Member who notifies the Speaker that the reason for the failure is the illness of the Member or the illness of a member of the Member\u2019s family.\n**(B)**\nA fine imposed pursuant to this resolution shall be $500 for a first offense and $2,500 for any subsequent offense.\n**(C)**\nThe Sergeant-at-Arms shall promptly notify in writing the Member, the Speaker, the Minority Leader, the Committee on Ethics, and the Chief Administrative Officer of any fine under this subsection. Such notification shall include findings detailing the violation and shall also be made publicly available by the chair of the Committee on Ethics.\n**(2) Appeal to Committee on Ethics**\n**(A)**\nThe Member may appeal the fine imposed under subsection (a) in writing to the Committee on Ethics not later than 30 calendar days or five legislative days, whichever is later, after notification pursuant to paragraph (1)(C). Such appeal shall include a response to the findings issued by the Sergeant-at-Arms pursuant to such paragraph.\n**(B)**\nUpon receipt of an appeal pursuant to subparagraph (A), the Committee on Ethics shall have a period of 30 calendar days or five legislative days, whichever is later, to consider the appeal. The fine will be upheld unless the appeal is agreed to by a majority of the Committee. Upon a determination regarding the appeal or if no appeal has been filed at the expiration of the period specified in subparagraph (A), the chair of the Committee on Ethics shall promptly notify the Member, the Speaker, the Sergeant-at-Arms, and the Chief Administrative Officer, and shall make such notification publicly available. The Speaker shall promptly lay such notification before the House.\n**(C)**\nIf a Member files an appeal under subparagraph (A) prior to the date on which the Committee on Ethics has adopted written rules, the period for the Committee\u2019s consideration of the appeal under subparagraph (B) shall begin on the date on which the chair of the Committee notifies the Member that the Committee has adopted such rules.\n**(3) Deducting fine from pay**\n**(A)**\nIf a Member against whom a fine is imposed by the Sergeant-at-Arms under paragraph (1) has not paid the fine prior to the expiration of the 90-calendar day period which begins on the date described in subparagraph (B), the Chief Administrative Officer shall deduct the amount of the fine from the net salary otherwise due the Member, in accordance with timetables and procedures established by the Committee on House Administration for purposes of carrying out this subsection.\n**(B)**\nThe date described in this subparagraph is, with respect to a fine imposed on a Member\u2014\n**(i)**\nthe date of the determination of the Committee on Ethics under paragraph (2)(B); or\n**(ii)**\nif the Member does not file an appeal with the Committee on Ethics prior to the expiration of the period specified in paragraph (2)(B), the first day after the expiration of such period.\n**(4) Prohibiting use of campaign or official funds to pay fines**\nA Member may not use campaign funds or official funds, including amounts in the Members\u2019 Representational Allowance, to pay a fine imposed under this section.\n**(5) Policies and procedures**\nThe Sergeant-at-Arms, Committee on Ethics, Committee on House Administration, and Chief Administrative Officer are authorized to establish policies and procedures for the implementation of this section.\n#### 3. No effect on other business\nNothing in this resolution may be construed to prohibit or otherwise affect the authority of the House of Representatives to conduct any business on a day on which a Government shutdown is in effect which is consistent with the Rules of the House.\n#### 4. Period of Government shutdown\nFor purposes of this resolution, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 5. Application to Delegates and Resident Commissioner\nIn this resolution, the term Member of the House of Representatives includes a Delegate or Resident Commissioner to the Congress.",
      "versionDate": "2025-10-10",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2025-10-14T13:43:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-10",
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
          "measure-id": "id119hres802",
          "measure-number": "802",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-10",
          "originChamber": "HOUSE",
          "update-date": "2025-10-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres802v00",
            "update-date": "2025-10-14"
          },
          "action-date": "2025-10-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution requires the House of Representatives to convene and hold recorded quorum calls during a government shutdown. It also limits recesses and adjournments during a government shutdown.\u00a0</p><p>Under the resolution, a government shutdown occurs when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p><p>The resolution requires the House to convene on each day on which a government shutdown is in effect unless a recess or adjournment is permitted. Under the resolution, such a recess or adjournment is only permitted if\u00a0</p><ul><li>the House has met for each of the first five consecutive calendar days on which the government shutdown is in effect,</li><li>the proposed period of adjournment or recess does not last for more than two consecutive calendar days, and</li><li>the House has met for at least five consecutive calendar days since the expiration of the most recent period of adjournment or recess.</li></ul><p>The resolution also requires the House to hold at least one recorded quorum call on each day that the House is in session during a government shutdown.\u00a0</p><p>Members of the House who fail to record their presence during a quorum call on two or more consecutive days must be fined $500 for a first offense and $2,500 for any subsequent offense unless the failure is due to an illness. A Member may not use official or campaign funds to pay the fine.\u00a0\u00a0</p>"
        },
        "title": "Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres802.xml",
    "summary": {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution requires the House of Representatives to convene and hold recorded quorum calls during a government shutdown. It also limits recesses and adjournments during a government shutdown.\u00a0</p><p>Under the resolution, a government shutdown occurs when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p><p>The resolution requires the House to convene on each day on which a government shutdown is in effect unless a recess or adjournment is permitted. Under the resolution, such a recess or adjournment is only permitted if\u00a0</p><ul><li>the House has met for each of the first five consecutive calendar days on which the government shutdown is in effect,</li><li>the proposed period of adjournment or recess does not last for more than two consecutive calendar days, and</li><li>the House has met for at least five consecutive calendar days since the expiration of the most recent period of adjournment or recess.</li></ul><p>The resolution also requires the House to hold at least one recorded quorum call on each day that the House is in session during a government shutdown.\u00a0</p><p>Members of the House who fail to record their presence during a quorum call on two or more consecutive days must be fined $500 for a first offense and $2,500 for any subsequent offense unless the failure is due to an illness. A Member may not use official or campaign funds to pay the fine.\u00a0\u00a0</p>",
      "updateDate": "2025-10-14",
      "versionCode": "id119hres802"
    },
    "title": "Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution requires the House of Representatives to convene and hold recorded quorum calls during a government shutdown. It also limits recesses and adjournments during a government shutdown.\u00a0</p><p>Under the resolution, a government shutdown occurs when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p><p>The resolution requires the House to convene on each day on which a government shutdown is in effect unless a recess or adjournment is permitted. Under the resolution, such a recess or adjournment is only permitted if\u00a0</p><ul><li>the House has met for each of the first five consecutive calendar days on which the government shutdown is in effect,</li><li>the proposed period of adjournment or recess does not last for more than two consecutive calendar days, and</li><li>the House has met for at least five consecutive calendar days since the expiration of the most recent period of adjournment or recess.</li></ul><p>The resolution also requires the House to hold at least one recorded quorum call on each day that the House is in session during a government shutdown.\u00a0</p><p>Members of the House who fail to record their presence during a quorum call on two or more consecutive days must be fined $500 for a first offense and $2,500 for any subsequent offense unless the failure is due to an illness. A Member may not use official or campaign funds to pay the fine.\u00a0\u00a0</p>",
      "updateDate": "2025-10-14",
      "versionCode": "id119hres802"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres802ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T08:18:17Z"
    },
    {
      "title": "Requiring the House of Representatives to convene and hold recorded quorum calls during a Government shutdown, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-11T08:05:14Z"
    }
  ]
}
```
