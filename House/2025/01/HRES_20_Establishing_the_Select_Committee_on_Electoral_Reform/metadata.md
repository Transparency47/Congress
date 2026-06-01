# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/20?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/20
- Title: Establishing the Select Committee on Electoral Reform.
- Congress: 119
- Bill type: HRES
- Bill number: 20
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-04-22T13:36:54Z
- Update date including text: 2025-04-22T13:36:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-07 - Committee: Submitted in House
- 2025-01-07 - IntroReferral: Submitted in House
- Latest action: 2025-01-07: Submitted in House

## Actions

- 2025-01-07 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-07 - Committee: Submitted in House
- 2025-01-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/20",
    "number": "20",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Establishing the Select Committee on Electoral Reform.",
    "type": "HRES",
    "updateDate": "2025-04-22T13:36:54Z",
    "updateDateIncludingText": "2025-04-22T13:36:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:00:30Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres20ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 20\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Perez (for herself and Mr. Golden of Maine ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nEstablishing the Select Committee on Electoral Reform.\n#### 1. Establishment\nThere is hereby established the Select Committee on Electoral Reform (hereafter referred to as the Select Committee ).\n#### 2. Composition\n##### (a) Appointment of members\nThe Speaker shall appoint 14 Members to the Select Committee, 7 of whom shall be appointed after consultation with the minority leader.\n##### (b) Designation of co-Chairs\nThe Speaker shall designate one Member to serve as co-chair of the Select Committee. The minority leader shall designate one member to serve as co-chair of the Select Committee.\n##### (c) Vacancies\nAny vacancy in the Select Committee shall be filled in the same manner as the original appointment.\n#### 3. Duties\n##### (a) In general\nThe duties of the Select Committee are the following:\n**(1)**\nTo examine the current methods by which citizens of the United States elect Members of Congress.\n**(2)**\nTo examine alternatives to these methods to determine how such alternatives would affect the responsiveness, accountability, and functionality of Congress, including\u2014\n**(A)**\nadopting multi-member congressional districts with proportional representation;\n**(B)**\nadjusting the number of Members of the House of Representatives;\n**(C)**\nadopting alternative methods of voting, such as ranked-choice voting and cumulative voting, as well as changes to ballot design such as fusion voting, in which parties may nominate candidates also nominated by another party;\n**(D)**\nholding open and nonpartisan primaries; and\n**(E)**\nestablishing independent congressional redistricting commissions.\n**(3)**\nTo conduct hearings to take testimony and receive evidence from witnesses selected for their relevant expertise, including\u2014\n**(A)**\npolitical scientists;\n**(B)**\ncurrent and former Members of Congress;\n**(C)**\nofficials from States and local governments that have previously adopted one or more of the alternative methods to be examined by the Select Committee; and\n**(D)**\nofficials from countries which currently use one or more of the alternative methods to be examined by the Select Committee.\n**(4)**\nTo examine Federal barriers to State experimentation with alternative electoral systems, including the Act entitled An Act for the relief of Doctor Ricardo Vallejo Samala and to provide for congressional redistricting , approved December 14, 1967 ( 2 U.S.C. 2c ), commonly known as the Uniform Congressional District Act, and its requirement that States use single-member districts.\n##### (b) Report\nNot later than 1 year after the first meeting of the Select Committee, the Select Committee shall issue a final report to Congress and the President, and shall include in the report such recommendations as it considers appropriate.\n#### 4. Meetings\n##### (a) Meetings\nThe Select Committee shall hold its first meeting not later than 30 days after all of its members have been appointed, and shall meet at the call of the co-chairs or a majority of its members.\n##### (b) Quorum\nTwelve members of the Select Committee shall constitute a quorum, but a lesser number may hold hearings.\n#### 5. Rules and procedures\n##### (a) In general\nExcept as otherwise provided in this section, the Select Committee shall have the authorities and responsibilities of, and shall be subject to the same limitations and restrictions as, a standing committee of the House, and shall be deemed a committee of the House for all purposes of law or rule.\n##### (b) Applicability of general rules for standing committees\nRules X and XI of the Rules of the House of Representatives shall apply to the Select Committee except as follows:\n**(1)**\nService on the Select Committee shall not count against the limitations in clause 5(b)(2) of rule X.\n**(2)**\nClause 2(m)(1)(B) of rule XI, clause 2(m)(3) of rule XI, and section 3(r) of House Resolution 5, One Hundred Nineteenth Congress, shall not apply to the Select Committee, but the Select Committee may recommend subpoenas and depositions and submit such recommendations to the relevant standing committee.\n**(3)**\nClause 2(d) of rule X shall not apply to the Select Committee.\n##### (c) No legislative jurisdiction\nThe Select Committee shall not have legislative jurisdiction and shall have no authority to take legislative action on any bill or resolution.\n#### 6. Funding\nTo enable the Select Committee to carry out the purposes of this resolution\u2014\n**(1)**\nthe Select Committee may use the services of staff of the House; and\n**(2)**\nthe Select Committee shall be eligible for interim funding pursuant to clause 7 of rule X of the Rules of the House of Representatives.\n#### 7. Termination\nThe Select Committee shall terminate 30 days after filing the final report under section 3.",
      "versionDate": "2025-01-07",
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
            "name": "Congressional committees",
            "updateDate": "2025-01-15T18:42:52Z"
          },
          {
            "name": "Congressional districts and representation",
            "updateDate": "2025-01-15T18:43:22Z"
          },
          {
            "name": "Congressional elections",
            "updateDate": "2025-01-15T18:43:46Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:43:00Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-15T18:43:33Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-01-15T18:43:14Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:43:39Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:43:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T16:31:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hres20",
          "measure-number": "20",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres20v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution establishes\u00a0the House Select Committee on Electoral Reform to examine current methods of electing Members of Congress, consider alternative\u00a0methods of election, and report appropriate recommendations to Congress and the President.</p><p>Specifically, the committee must (1) determine how alternative methods of election would affect the responsiveness, accountability, and functionality of Congress; (2) conduct hearings to take testimony and receive evidence from appropriate expert witnesses; and (3) examine federal barriers to state experimentation with alternative electoral systems.\u00a0The committee must consider alternatives to current methods that include\u00a0adopting multi-member congressional districts with proportional representation;\u00a0adjusting the total number of Members of the House of Representatives; adopting alternative methods of voting (e.g., ranked-choice voting); and holding open and nonpartisan primaries.</p><p>The committee shall be made up of 14 Members of Congress appointed by the Speaker of the House, 7 of whom shall be appointed in consultation with the minority leader. The committee's co-chairs shall be designated by the Speaker and minority leader, respectively.\u00a0The resolution provides that the committee must hold its first meeting within 30 days after all of its members have been appointed.</p><p>The committee shall issue its final report to Congress and the President within one year after the committee's first meeting.</p>"
        },
        "title": "Establishing the Select Committee on Electoral Reform."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres20.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes\u00a0the House Select Committee on Electoral Reform to examine current methods of electing Members of Congress, consider alternative\u00a0methods of election, and report appropriate recommendations to Congress and the President.</p><p>Specifically, the committee must (1) determine how alternative methods of election would affect the responsiveness, accountability, and functionality of Congress; (2) conduct hearings to take testimony and receive evidence from appropriate expert witnesses; and (3) examine federal barriers to state experimentation with alternative electoral systems.\u00a0The committee must consider alternatives to current methods that include\u00a0adopting multi-member congressional districts with proportional representation;\u00a0adjusting the total number of Members of the House of Representatives; adopting alternative methods of voting (e.g., ranked-choice voting); and holding open and nonpartisan primaries.</p><p>The committee shall be made up of 14 Members of Congress appointed by the Speaker of the House, 7 of whom shall be appointed in consultation with the minority leader. The committee's co-chairs shall be designated by the Speaker and minority leader, respectively.\u00a0The resolution provides that the committee must hold its first meeting within 30 days after all of its members have been appointed.</p><p>The committee shall issue its final report to Congress and the President within one year after the committee's first meeting.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hres20"
    },
    "title": "Establishing the Select Committee on Electoral Reform."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes\u00a0the House Select Committee on Electoral Reform to examine current methods of electing Members of Congress, consider alternative\u00a0methods of election, and report appropriate recommendations to Congress and the President.</p><p>Specifically, the committee must (1) determine how alternative methods of election would affect the responsiveness, accountability, and functionality of Congress; (2) conduct hearings to take testimony and receive evidence from appropriate expert witnesses; and (3) examine federal barriers to state experimentation with alternative electoral systems.\u00a0The committee must consider alternatives to current methods that include\u00a0adopting multi-member congressional districts with proportional representation;\u00a0adjusting the total number of Members of the House of Representatives; adopting alternative methods of voting (e.g., ranked-choice voting); and holding open and nonpartisan primaries.</p><p>The committee shall be made up of 14 Members of Congress appointed by the Speaker of the House, 7 of whom shall be appointed in consultation with the minority leader. The committee's co-chairs shall be designated by the Speaker and minority leader, respectively.\u00a0The resolution provides that the committee must hold its first meeting within 30 days after all of its members have been appointed.</p><p>The committee shall issue its final report to Congress and the President within one year after the committee's first meeting.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hres20"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres20ih.xml"
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
      "title": "Establishing the Select Committee on Electoral Reform.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-08T09:18:15Z"
    },
    {
      "title": "Establishing the Select Committee on Electoral Reform.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T09:05:17Z"
    }
  ]
}
```
