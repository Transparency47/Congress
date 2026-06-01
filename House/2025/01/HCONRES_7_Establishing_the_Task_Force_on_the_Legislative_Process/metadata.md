# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/7?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/7
- Title: Establishing the Task Force on the Legislative Process.
- Congress: 119
- Bill type: HCONRES
- Bill number: 7
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-04-25T08:05:42Z
- Update date including text: 2025-04-25T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/7",
    "number": "7",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Establishing the Task Force on the Legislative Process.",
    "type": "HCONRES",
    "updateDate": "2025-04-25T08:05:42Z",
    "updateDateIncludingText": "2025-04-25T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:07:30Z",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres7ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 7\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Williams of Georgia submitted the following concurrent resolution; which was referred to the Committee on Rules\nCONCURRENT RESOLUTION\nEstablishing the Task Force on the Legislative Process.\n#### 1. Purpose\nThe purpose of this concurrent resolution is to implement the 131st recommendation of the Select Committee on the Modernization of Congress, passed by the Select Committee during the 117th Congress, to create a Task Force on the Legislative Process that analyzes the range of legislative processes by which, if adopted by both Houses, each House would provide expedited consideration of legislation that was passed by the other House with wide and bipartisan support.\n#### 2. Establishment of Task Force\n##### (a) Establishment; purpose\nThere is hereby established the Task Force on the Legislative Process (hereafter referred to as the Task Force ) whose purpose shall be to analyze the range of options for bicameral legislation expedition.\n##### (b) Definition\nIn this concurrent resolution, the term bicameral legislation expedition means any legislative process by which each House of Congress jointly provides for expedited consideration of legislation which was passed by the other House by unanimous consent, by voice vote, or with the approval of not fewer than 2/3 of the members voting.\n#### 3. Membership\n##### (a) Composition\nThe Task Force shall be composed of 12 members appointed as follows:\n**(1)**\nThe Speaker of the House of Representatives shall appoint 3 individuals who are Members of the House of Representatives, of whom at least one shall be a majority member of the Committee on Rules of the House.\n**(2)**\nThe Minority Leader of the House shall appoint 3 individuals who are Members of the House of Representatives, of whom at least one shall be a minority member of the Committee on Rules of the House.\n**(3)**\nThe Majority Leader of the Senate shall appoint 3 individuals who are Members of the Senate, of whom at least one shall be a majority member of the Committee on Rules and Administration of the Senate.\n**(4)**\nThe Minority Leader of the Senate shall appoint 3 individuals who are Members of the Senate, of whom at least one shall be a minority member of the Committee on Rules and Administration of the Senate.\n##### (b) Co-Chairs\nThe Speaker, Minority Leader of the House, Majority Leader of the Senate, and Minority Leader of the Senate shall jointly select 2 of the members of the Task Force to serve as co-chairs of the Task Force.\n##### (c) Vacancies\nA vacancy in the membership of the Task Force shall be filled in the same manner as the original appointment.\n##### (d) Inclusion of Delegates and Resident Commissioner\nFor purposes of this section, a Member of the House of Representatives includes a Delegate or Resident Commissioner to the Congress.\n#### 4. Duties\n##### (a) Procedures\nThe Task Force shall establish a process to solicit information, input, and legislative proposals which are directly related to the purpose of the Task Force under section 2.\n##### (b) Report\n**(1) Contents**\nThe Task Force shall issue a report to the Speaker of the House, the Minority Leader of the House, the Majority Leader of the Senate, the Minority Leader of the Senate, the Committee on Rules of the House of Representatives, and the Committee on Rules and Administration of the Senate, and shall include in the report\u2014\n**(A)**\nan analysis of the range of options for bicameral legislation expedition; and\n**(B)**\nany recommendations relating to bicameral legislation expedition which are approved by not fewer than 9 of its members.\n**(2) Deadline**\nThe Task Force shall issue the report required under paragraph (1) not later than one year after the date of the adoption of this concurrent resolution.\n##### (c) Use of staff\nThe Task Force may use the services of staff of the House and Senate to assist it in carrying out its duties.\n#### 5. Posting of proposals by Committees\nUpon receiving the report issued by the Task Force under section 4(b), the Committee on Rules of the House of Representatives and the Committee on Rules and Administration of the Senate shall each publicly post the report on a public page of its website.\n#### 6. Termination\n##### (a) In general\nThe Task Force shall terminate upon issuing the report required under section 4(b).\n##### (b) Disposition of records\nUpon its termination, the records of the Task Force shall be transferred to, and shall become part of, the records of the Committee on Rules of the House of Representatives and the Committee on Rules and Administration of the Senate.",
      "versionDate": "2025-01-28",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-03-20T16:00:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-20T16:00:26Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-20T16:00:26Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-20T16:00:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-31T14:25:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hconres7",
          "measure-number": "7",
          "measure-type": "hconres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres7v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution temporarily establishes a bipartisan and bicameral Task Force on the Legislative Process. The task force must analyze and\u00a0report on ways to expedite the consideration of legislation that passed in its originating chamber with wide and bipartisan support.</p><p>The task force must submit a final report of its recommendations within one year of the passage of this concurrent resolution. Congress must make the report publicly available<strong>.</strong></p><p>The task force terminates upon the submission of the report.</p>"
        },
        "title": "Establishing the Task Force on the Legislative Process."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres7.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution temporarily establishes a bipartisan and bicameral Task Force on the Legislative Process. The task force must analyze and\u00a0report on ways to expedite the consideration of legislation that passed in its originating chamber with wide and bipartisan support.</p><p>The task force must submit a final report of its recommendations within one year of the passage of this concurrent resolution. Congress must make the report publicly available<strong>.</strong></p><p>The task force terminates upon the submission of the report.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hconres7"
    },
    "title": "Establishing the Task Force on the Legislative Process."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution temporarily establishes a bipartisan and bicameral Task Force on the Legislative Process. The task force must analyze and\u00a0report on ways to expedite the consideration of legislation that passed in its originating chamber with wide and bipartisan support.</p><p>The task force must submit a final report of its recommendations within one year of the passage of this concurrent resolution. Congress must make the report publicly available<strong>.</strong></p><p>The task force terminates upon the submission of the report.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hconres7"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres7ih.xml"
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
      "title": "Establishing the Task Force on the Legislative Process.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:17Z"
    },
    {
      "title": "Establishing the Task Force on the Legislative Process.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:05:33Z"
    }
  ]
}
```
