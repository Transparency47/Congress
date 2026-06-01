# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/756
- Title: 287(g) Program Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 756
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-10-11T08:05:21Z
- Update date including text: 2025-10-11T08:05:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/756",
    "number": "756",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "287(g) Program Protection Act",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:21Z",
    "updateDateIncludingText": "2025-10-11T08:05:21Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
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
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
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
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "OK"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "SC"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "VA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "WI"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr756ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 756\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Cloud (for himself, Mr. Roy , Mr. Ogles , Mr. Babin , Mr. Harris of Maryland , Ms. Tenney , Mr. Biggs of Arizona , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 287(g) of the Immigration and Nationality Act to clarify congressional intent with respect to agreements under such section, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 287(g) Program Protection Act .\n#### 2. Clarification of congressional intent\nSection 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking the Attorney General may enter and all that follows through the period at the end and inserting the following: the Secretary of Homeland Security shall enter into a written agreement with a State, or any political subdivision of a State, upon request of the State or political subdivision, pursuant to which law enforcement officers of the State or subdivision, who are determined by the Secretary to be qualified to perform a function of an immigration officer in relation to the investigation, apprehension, or detention of aliens in the United States (including the transportation of such aliens across State lines to detention centers), may carry out such function at the expense of the State or political subdivision. No request from a bona fide State or political subdivision or bona fide law enforcement agency shall be denied absent a compelling reason, and the Secretary shall notify the Congress and publish in the Federal Register an explanation for those reasons at least 180 days in advance of making final the denial. No limit on the number of agreements under this subsection may be imposed. The Secretary shall process requests for such agreements with all due haste, and in no case shall more than 90 days elapse from the date the request is made until the agreement is consummated. For purposes of this subsection, any reference to a political subdivision shall be construed to include any law enforcement or corrections agency of the political subdivision. ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary ;\n**(3)**\nby redesignating paragraphs (2) through (10) as paragraphs (5) through (13), respectively;\n**(4)**\nby inserting after paragraph (1) the following:\n(2) An agreement under this subsection shall accommodate a requesting State or political subdivision with respect to the enforcement model or combination of models, and shall accommodate a patrol model, task force model, jail model, any combination thereof, or any other reasonable model the State or political subdivision believes is best suited to the immigration enforcement needs of its jurisdiction. (3) No Federal program or technology directed broadly at identifying inadmissible or deportable aliens shall substitute for such agreements, including those establishing a jail model, and shall operate in addition to any agreement under this subsection. (4) (A) No agreement under this subsection may be terminated absent a compelling reason. (B) (i) The Secretary shall provide a State or political subdivision written notice of intent to terminate at least 180 days prior to date of intended termination, and the notice shall fully explain the grounds for termination, along with providing evidence substantiating the Secretary\u2019s allegations. (ii) In order to determine whether the requirements of this paragraph have been satisfied, the State or political subdivision shall have the right\u2014 (I) to appeal the decision of the Secretary to an administrative law judge for a hearing and decision; or (II) to bring a civil action in an appropriate court of jurisdiction. (C) The agreement shall remain in full effect during the course of any and all legal proceedings. ; and\n**(5)**\nin paragraph (6) (as redesignated), by adding at the end the following: The Secretary of Homeland Security shall implement uniform training requirements for law enforcement officers who are, or will be, performing a function of an immigration officer under this subsection. The training requirements shall align with Federal Law Enforcement Training Center standards for training under this subsection (as in effect of the date of the enactment of this sentence). .\n#### 3. Funding\nSection 286(r) of the Immigration and Nationality Act ( 8 U.S.C. 1356(r) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking Breached Bond/Detention Fund and inserting Breached Bond/Detention/287 (g) Fund ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary of Homeland Security ;\n**(3)**\nin paragraph (1), by striking Breached Bond/Detention and inserting Breached Bond/Detention/287(g) ;\n**(4)**\nin paragraph (2), by striking Department of Justice and inserting Department of Homeland Security ; and\n**(5)**\nin paragraph (3)\u2014\n**(A)**\nin clause (i), by striking , and at the end and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iv) for expenses associated with administering section 287(g). .\n#### 4. Requirements on Secretary\n##### (a) Annual performance report\nNot later than December 31 of the first fiscal year that begins after the date of the enactment of this Act, and not later than December 31 of each year thereafter, the Secretary of Homeland Security shall publish an annual performance report on the program under section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) that includes at least the following information:\n**(1)**\nThe number of aliens apprehended and screened by law enforcement through the program.\n**(2)**\nThe number of aliens removed from the United States as a result of the program.\n**(3)**\nThe number of aliens described in paragraph (1) who were not removed and an explanation for why they were not removed.\n**(4)**\nThe methods being used to conduct oversight of each law enforcement agency participating under the program.\n**(5)**\nThe number of law enforcement agencies in compliance with the program\u2019s training requirements.\n**(6)**\nThe number of complaints filed against law enforcement agencies claiming they did not comply their written agreement entered into under such section.\n**(7)**\nThe number of law enforcement agencies that had such written agreement terminated.\n**(8)**\nThe reasons for such termination.\n##### (b) Annual recruitment plan\nNot later than December 31 of the first fiscal year that begins after the date of the enactment of this Act, and not later than December 31 of each year thereafter, the Secretary of Homeland Security shall publish an annual recruitment plan with respect to the program under section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) that includes at least the following information:\n**(1)**\nAnnual goals for the next five years for recruitment of new States and political subdivisions of States to participate in the program.\n**(2)**\nThe number of new States and political subdivisions of States participating in the program each year.\n**(3)**\nA description of the outreach to States and political subdivisions of States conducted for the program and the other methods used to achieve recruitment goals.\n**(4)**\nThe number of requests for agreements received, approved, denied, and pending approval.\n##### (c) Rulemaking\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security shall publish a notice of rulemaking with respect to the training requirements under section 287(g)(6) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g)(6) ), as added by section 2(5).",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-03-01T17:01:48Z"
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
          "measure-id": "id119hr756",
          "measure-number": "756",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr756v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>287(g) Program Protection Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to allow qualified state and local law enforcement agencies to perform certain immigration enforcement activities if the agency requests such authority. DHS may refuse to grant the request only if there is a compelling reason.</p><p>Currently, DHS is authorized to grant such authority but is not required to do so.</p><p>DHS must annually report on (1) the performance of these enforcement activities, and (2) the plans to expand these activities to additional states and localities.</p>"
        },
        "title": "287(g) Program Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr756.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>287(g) Program Protection Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to allow qualified state and local law enforcement agencies to perform certain immigration enforcement activities if the agency requests such authority. DHS may refuse to grant the request only if there is a compelling reason.</p><p>Currently, DHS is authorized to grant such authority but is not required to do so.</p><p>DHS must annually report on (1) the performance of these enforcement activities, and (2) the plans to expand these activities to additional states and localities.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr756"
    },
    "title": "287(g) Program Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>287(g) Program Protection Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to allow qualified state and local law enforcement agencies to perform certain immigration enforcement activities if the agency requests such authority. DHS may refuse to grant the request only if there is a compelling reason.</p><p>Currently, DHS is authorized to grant such authority but is not required to do so.</p><p>DHS must annually report on (1) the performance of these enforcement activities, and (2) the plans to expand these activities to additional states and localities.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr756"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr756ih.xml"
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
      "title": "287(g) Program Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "287(g) Program Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 287(g) of the Immigration and Nationality Act to clarify congressional intent with respect to agreements under such section, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:27Z"
    }
  ]
}
```
