# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/605
- Title: Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.
- Congress: 119
- Bill type: HRES
- Bill number: 605
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-02-05T01:06:13Z
- Update date including text: 2026-02-05T01:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Rules.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-09-03 14:07:30 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House.
- 2025-09-03 14:07:30 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House. (consideration: CR H3780; text: CR H3780)
- Latest action: 2025-07-23: Submitted in House

## Actions

- 2025-07-23 - IntroReferral: Referred to the House Committee on Rules.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-09-03 14:07:30 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House.
- 2025-09-03 14:07:30 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House. (consideration: CR H3780; text: CR H3780)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/605",
    "number": "605",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.",
    "type": "HRES",
    "updateDate": "2026-02-05T01:06:13Z",
    "updateDateIncludingText": "2026-02-05T01:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-09-03",
      "actionTime": "14:07:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House. (consideration: CR H3780; text: CR H3780)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-09-03",
      "actionTime": "14:07:30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Pursuant to the provisions of H. Res. 672, H. Res. 605 is considered passed House.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:12:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres605ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 605\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Loudermilk submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nEstablishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.\n#### 1. Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021\n##### (a) Establishment; composition\n**(1) Establishment**\nThere is hereby established for the One Hundred Nineteenth Congress a select investigative subcommittee of the Committee on the Judiciary called the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021 (hereinafter referred to as the \u201cselect subcommittee\u201d).\n**(2) Composition**\n**(A)**\nThe select subcommittee shall be composed of not more than 8 Members, Delegates, or the Resident Commissioner appointed by the Speaker, of whom not more than 3 shall be appointed in consultation with the minority leader. The Speaker shall designate one member of the select subcommittee as its chair. Any vacancy in the select subcommittee shall be filled in the same manner as the original appointment.\n**(B)**\nEach member appointed to the select subcommittee shall be treated as though a member of the Committee on the Judiciary for purposes of the select subcommittee.\n**(C)**\nThe chair and ranking minority member of the Committee on the Judiciary shall be ex officio members of the select subcommittee but shall have no vote in the select subcommittee and may not be counted for purposes of determining a quorum thereof.\n**(3) Service**\nService on the select subcommittee shall not count against the limitations in clause 5(b)(2)(A) of rule X of the Rules of the House of Representatives.\n##### (b) Investigative functions and authority\nThe select subcommittee is authorized and directed to conduct a full and complete investigation and study and issue a final report of the events surrounding January 6, 2021 regarding matters within the jurisdiction of the Committee on the Judiciary under clause 1(l) of rule X of the Rules of the House of Representatives. The select subcommittee may not hold a markup of legislation.\n##### (c) Procedure\n**(1)**\nRule XI of the Rules of the House of Representatives and the rules of the Committee on the Judiciary shall apply to the select subcommittee in the same manner as a subcommittee except as follows:\n**(A)**\nThe chair of the select subcommittee may, after consultation with the ranking minority member, recognize\u2014\n**(i)**\nmembers of the select subcommittee to question a witness for periods longer than five minutes as though pursuant to clause 2(j)(2)(B) of such rule XI; and\n**(ii)**\nstaff of the select subcommittee or staff of the Committee on the Judiciary to question a witness as though pursuant to clause 2(j)(2)(C) of such rule XI.\n**(B)**\nThe chair of the select subcommittee may authorize and issue subpoenas pursuant to clause 2(m) of rule XI in the investigation, study, and report conducted pursuant to subsection (b), including for the purpose of taking depositions.\n**(C)**\nWith regard to the full scope of investigative authority under subsection (b), the select subcommittee shall be authorized to receive information available to the Permanent Select Committee on Intelligence, consistent with congressional reporting requirements for intelligence and intelligence-related activities, and any such information received shall be subject to the terms and conditions applicable under clause 11 of rule X.\n**(2)**\nThe chair of the select subcommittee is authorized to compel by subpoena the furnishing of information by interrogatory.\n**(3)**\n**(A)**\nThe chair of the select subcommittee, upon consultation with the ranking minority member, may order the taking of depositions, including pursuant to subpoena, by a Member, counsel of the select subcommittee, or counsel of the Committee on the Judiciary, in the same manner as a standing committee pursuant to section 3(t) of House Resolution 5, One Hundred Nineteenth Congress.\n**(B)**\nDepositions taken under the authority prescribed in this paragraph shall be governed by the procedures submitted by the chair of the Committee on Rules for printing in the Congressional Record on January 14, 2025.\n**(4)**\nSubpoenas authorized pursuant to this resolution may be signed by the chair of the select subcommittee or a designee.\n**(5)**\nThe provisions of this resolution shall govern the proceedings of the select subcommittee in the event of any conflict with the rules of the House or of the Committee on the Judiciary.\n##### (d) Transfer of records\nThe Committee on House Administration is directed to transfer any records in any form relating to the matters described in subsection (b) to the select subcommittee not later than seven days after adoption of the resolution by the House. Such records shall become the records of the select subcommittee.\n##### (e) Successor\nThe Committee on the Judiciary is the \u201csuccessor in interest\u201d to the select subcommittee for purposes of clause 8(c) of rule II of the Rules of the House of Representatives.\n##### (f) Final report\nThe final report of the select subcommittee shall be submitted to the Committee on the Judiciary by December 31, 2026.\n##### (g) Termination\nThe select subcommittee shall terminate\u2014\n**(1)**\n30 days after filing the final report under subsection (f); or\n**(2)**\non the last day of the One Hundred Nineteenth Congress,\nwhichever occurs earlier.",
      "versionDate": "2025-07-23",
      "versionType": "IH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres605eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 605\nIn the House of Representatives, U. S.,\nSeptember 3, 2025\nRESOLUTION\nEstablishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.\n#### 1. Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021\n##### (a) Establishment; composition\n**(1) Establishment**\nThere is hereby established for the One Hundred Nineteenth Congress a select investigative subcommittee of the Committee on the Judiciary called the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021 (hereinafter referred to as the \u201cselect subcommittee\u201d).\n**(2) Composition**\n**(A)**\nThe select subcommittee shall be composed of not more than 8 Members, Delegates, or the Resident Commissioner appointed by the Speaker, of whom not more than 3 shall be appointed in consultation with the minority leader. The Speaker shall designate one member of the select subcommittee as its chair. Any vacancy in the select subcommittee shall be filled in the same manner as the original appointment.\n**(B)**\nEach member appointed to the select subcommittee shall be treated as though a member of the Committee on the Judiciary for purposes of the select subcommittee.\n**(C)**\nThe chair and ranking minority member of the Committee on the Judiciary shall be ex officio members of the select subcommittee but shall have no vote in the select subcommittee and may not be counted for purposes of determining a quorum thereof.\n**(3) Service**\nService on the select subcommittee shall not count against the limitations in clause 5(b)(2)(A) of rule X of the Rules of the House of Representatives.\n##### (b) Investigative functions and authority\nThe select subcommittee is authorized and directed to conduct a full and complete investigation and study and issue a final report of the events surrounding January 6, 2021 regarding matters within the jurisdiction of the Committee on the Judiciary under clause 1(l) of rule X of the Rules of the House of Representatives. The select subcommittee may not hold a markup of legislation.\n##### (c) Procedure\n**(1)**\nRule XI of the Rules of the House of Representatives and the rules of the Committee on the Judiciary shall apply to the select subcommittee in the same manner as a subcommittee except as follows:\n**(A)**\nThe chair of the select subcommittee may, after consultation with the ranking minority member, recognize\u2014\n**(i)**\nmembers of the select subcommittee to question a witness for periods longer than five minutes as though pursuant to clause 2(j)(2)(B) of such rule XI; and\n**(ii)**\nstaff of the select subcommittee or staff of the Committee on the Judiciary to question a witness as though pursuant to clause 2(j)(2)(C) of such rule XI.\n**(B)**\nThe chair of the select subcommittee may authorize and issue subpoenas pursuant to clause 2(m) of rule XI in the investigation, study, and report conducted pursuant to subsection (b), including for the purpose of taking depositions.\n**(C)**\nWith regard to the full scope of investigative authority under subsection (b), the select subcommittee shall be authorized to receive information available to the Permanent Select Committee on Intelligence, consistent with congressional reporting requirements for intelligence and intelligence-related activities, and any such information received shall be subject to the terms and conditions applicable under clause 11 of rule X.\n**(2)**\nThe chair of the select subcommittee is authorized to compel by subpoena the furnishing of information by interrogatory.\n**(3)**\n**(A)**\nThe chair of the select subcommittee, upon consultation with the ranking minority member, may order the taking of depositions, including pursuant to subpoena, by a Member, counsel of the select subcommittee, or counsel of the Committee on the Judiciary, in the same manner as a standing committee pursuant to section 3(t) of House Resolution 5, One Hundred Nineteenth Congress.\n**(B)**\nDepositions taken under the authority prescribed in this paragraph shall be governed by the procedures submitted by the chair of the Committee on Rules for printing in the Congressional Record on January 14, 2025.\n**(4)**\nSubpoenas authorized pursuant to this resolution may be signed by the chair of the select subcommittee or a designee.\n**(5)**\nThe provisions of this resolution shall govern the proceedings of the select subcommittee in the event of any conflict with the rules of the House or of the Committee on the Judiciary.\n##### (d) Transfer of records\nThe Committee on House Administration is directed to transfer any records in any form relating to the matters described in subsection (b) to the select subcommittee not later than seven days after adoption of the resolution by the House. Such records shall become the records of the select subcommittee.\n##### (e) Successor\nThe Committee on the Judiciary is the \u201csuccessor in interest\u201d to the select subcommittee for purposes of clause 8(c) of rule II of the Rules of the House of Representatives.\n##### (f) Final report\nThe final report of the select subcommittee shall be submitted to the Committee on the Judiciary by December 31, 2026.\n##### (g) Termination\nThe select subcommittee shall terminate\u2014\n**(1)**\n30 days after filing the final report under subsection (f); or\n**(2)**\non the last day of the One Hundred Nineteenth Congress,\nwhichever occurs earlier.",
      "versionDate": "2025-09-03",
      "versionType": "EH"
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
        "actionDate": "2025-09-03",
        "actionTime": "14:06:12",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "672",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Procedurally related"
        }
      },
      "title": "Providing for consideration of the bill (H.R. 4553) making appropriations for energy and water development and related agencies for the fiscal year ending September 30, 2026, and for other purposes; providing for consideration of the joint resolution (H.J. Res. 104) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Miles City Field Office Record of Decision and Approved Resource Management Plan Amendment''; providing for consideration of the joint resolution (H.J. Res. 105) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''North Dakota Field Office Record of Decision and Approved Resource Management Plan''; providing for consideration of the joint resolution (H.J. Res. 106) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Central Yukon Record of Decision and Approved Resource Management Plan''; and for other purposes.",
      "type": "HRES"
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
            "name": "Congressional committees",
            "updateDate": "2025-09-15T15:54:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-15T15:55:04Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-09-15T15:55:08Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-15T15:54:58Z"
          },
          {
            "name": "House Committee on the Judiciary",
            "updateDate": "2025-09-15T15:54:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-03T13:21:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hres605",
          "measure-number": "605",
          "measure-type": "hres",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-09-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres605v00",
            "update-date": "2025-09-04"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution establishes a select investigative subcommittee of the Committee on the Judiciary called the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.\u00a0</p><p>The select subcommittee shall be composed of not more than eight Members, Delegates, or the Resident Commissioner appointed by the Speaker of the House, of whom not more than three shall be appointed in consultation with the minority leader.\u00a0</p><p>The resolution authorizes and directs the select subcommittee to conduct a full and complete investigation and study and issue a final report of the events surrounding January 6, 2021. </p><p>The resolution authorizes the chair of the select subcommittee to receive information available to the Permanent Select Committee on Intelligence; to extend certain periods for questioning witnesses; and to use depositions, subpoenas, and interrogatories to collect information. The select subcommittee may not hold a markup of legislation. </p><p>The select subcommittee's final report shall be submitted to the Committee on the Judiciary by December 31, 2026. The select subcommittee terminates\u00a030 days after filing the final report or on the last day of the 119th Congress, whichever comes first.\u00a0</p>"
        },
        "title": "Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres605.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes a select investigative subcommittee of the Committee on the Judiciary called the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.\u00a0</p><p>The select subcommittee shall be composed of not more than eight Members, Delegates, or the Resident Commissioner appointed by the Speaker of the House, of whom not more than three shall be appointed in consultation with the minority leader.\u00a0</p><p>The resolution authorizes and directs the select subcommittee to conduct a full and complete investigation and study and issue a final report of the events surrounding January 6, 2021. </p><p>The resolution authorizes the chair of the select subcommittee to receive information available to the Permanent Select Committee on Intelligence; to extend certain periods for questioning witnesses; and to use depositions, subpoenas, and interrogatories to collect information. The select subcommittee may not hold a markup of legislation. </p><p>The select subcommittee's final report shall be submitted to the Committee on the Judiciary by December 31, 2026. The select subcommittee terminates\u00a030 days after filing the final report or on the last day of the 119th Congress, whichever comes first.\u00a0</p>",
      "updateDate": "2025-09-04",
      "versionCode": "id119hres605"
    },
    "title": "Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021."
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes a select investigative subcommittee of the Committee on the Judiciary called the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.\u00a0</p><p>The select subcommittee shall be composed of not more than eight Members, Delegates, or the Resident Commissioner appointed by the Speaker of the House, of whom not more than three shall be appointed in consultation with the minority leader.\u00a0</p><p>The resolution authorizes and directs the select subcommittee to conduct a full and complete investigation and study and issue a final report of the events surrounding January 6, 2021. </p><p>The resolution authorizes the chair of the select subcommittee to receive information available to the Permanent Select Committee on Intelligence; to extend certain periods for questioning witnesses; and to use depositions, subpoenas, and interrogatories to collect information. The select subcommittee may not hold a markup of legislation. </p><p>The select subcommittee's final report shall be submitted to the Committee on the Judiciary by December 31, 2026. The select subcommittee terminates\u00a030 days after filing the final report or on the last day of the 119th Congress, whichever comes first.\u00a0</p>",
      "updateDate": "2025-09-04",
      "versionCode": "id119hres605"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres605ih.xml"
        }
      ],
      "type": "IH"
    },
    {
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres605eh.xml"
        }
      ],
      "type": "EH"
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
      "title": "Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:36Z"
    },
    {
      "title": "Establishing the Select Subcommittee to Investigate the Remaining Questions Surrounding January 6, 2021.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:05Z"
    }
  ]
}
```
