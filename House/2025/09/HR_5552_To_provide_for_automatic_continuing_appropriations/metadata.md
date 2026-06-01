# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5552
- Title: Eliminate Shutdowns Act
- Congress: 119
- Bill type: HR
- Bill number: 5552
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2025-12-05T21:47:18Z
- Update date including text: 2025-12-05T21:47:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-23 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-23 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5552",
    "number": "5552",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Eliminate Shutdowns Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:47:18Z",
    "updateDateIncludingText": "2025-12-05T21:47:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-23T13:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "WI"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "OH"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "KS"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "UT"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5552ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5552\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Johnson of South Dakota (for himself and Mr. Steil ) introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for automatic continuing appropriations.\n#### 1. Short title\nThis Act may be cited as the Eliminate Shutdowns Act .\n#### 2. Automatic continuing appropriations\n##### (a) In general\nSubchapter I of chapter 13 of title 31, United States Code, is amended by adding at the end the following:\n1311. Automatic continuing appropriations (a) For purposes of this section\u2014 (1) the term lapse in appropriations means a time period during which\u2014 (A) the applicable full-year appropriation Act for a program, project, or activity has not been enacted for the current fiscal year; (B) the program, project, or activity was provided funding in the preceding applicable appropriation Act; and (C) no continuing appropriation Act is in effect for such program, project, or activity; and (2) the term preceding applicable appropriation Act means\u2014 (A) the most recent continuing appropriation Act enacted; or (B) if no continuing appropriation Act has been enacted for the current fiscal year, the most recent applicable full-year appropriation Act (including a full-year continuing appropriation Act) enacted for the immediately preceding fiscal year (excluding any supplemental appropriation Act). (b) (1) On and after the first day of each fiscal year, if a lapse in appropriations occurs with respect to a program, project, or activity, there are appropriated such sums as may be necessary, at the rate for operations as provided in the preceding applicable appropriation Acts under the authorities and conditions provided in such Acts, for continuing programs, projects or activities (including the costs of direct loans and loan guarantees) that were conducted under such Acts and for which appropriations, funds, or other authorities were made available in such Acts. (2) (A) Appropriations and funds made available and authority granted under paragraph (1) shall be available for a period of 14 calendar days. (B) If, at the end of the first 14 calendar-day period during which appropriations and funds are made available and authority is granted under paragraph (1), and the end of every 14 calendar-day period thereafter, a lapse in appropriations with respect to a program, project, or activity continues, the appropriations and funds made available and authority granted under paragraph (1) with respect to the program, project, or activity shall be extended for an additional 14 calendar-day period. (3) For entitlements and other mandatory payments whose budget authority was provided for in preceding applicable appropriation Acts, under a law other than this section providing full-year continuing appropriations for the preceding fiscal year, or under this section, and for activities under the Food and Nutrition Act of 2008, appropriations and funds made available for a fiscal year under paragraph (1) shall be at the rate necessary to maintain program levels under current law, and under the authority and conditions provided in the preceding applicable appropriation Act. (c) Appropriations and funds made available, and authority granted, for any fiscal year pursuant to this section for a program, project, or activity shall be available, in accordance with subsection (b), for the period\u2014 (1) beginning on the first day of any lapse in appropriations during such fiscal year; and (2) ending on the date of enactment of an appropriation Act for such fiscal year with respect to the account for such program, project, or activity (whether or not such Act provides appropriations for such program, project, or activity) or a continuing appropriation Act providing funding for the program, project, or activity, as applicable. (d) Expenditures made for a program, project, or activity for any fiscal year pursuant to this section shall be charged to the applicable appropriation, fund, or authorization whenever an appropriation Act for such fiscal year with respect to the account for a program, project, or activity or a law making continuing appropriations until the end of such fiscal year for such program, project, or activity is enacted. (e) Appropriations and funds made available by, or authority granted pursuant to, this section may be used without regard to the time limitations for submission and approval of apportionments set forth in section 1513 of this, but nothing in this section shall be construed to waive any other provision of law governing the apportionment of funds. (f) Notwithstanding any other provision of this section, except for subsection (c), for those programs that would otherwise have high initial rates of operation or complete distribution of appropriations at the beginning of the applicable fiscal year because of distributions of funding to States, foreign countries, grantees, or others, such high initial rates of operation or complete distribution shall not be made, and no grants shall be awarded for such programs funded by this section that would impinge on final funding prerogatives. (g) This section shall be implemented so that only the most limited funding action of that permitted under this section shall be taken in order to provide for continuation of programs, projects and activities. (h) This section shall not apply to a program, project, or activity during a lapse in appropriations if any other provision of law (other than an authorization of appropriations or an appropriation Act for a prior fiscal year making carryover funds available)\u2014 (1) makes an appropriation, makes funds available, or grants authority for such program, project, or activity to continue for such period; or (2) specifically provides that no appropriation shall be made, no funds shall be made available, or no authority shall be granted for such program, project, or activity to continue for such period. (i) (1) Subject to paragraph (2), the head of an agency may, with the approval of the Office of Management and Budget, transfer funds made available to such agency for an appropriation account pursuant to this section to any other appropriation account of such agency. (2) Not more than 5 percent of any appropriation account may be transferred to another appropriation account under paragraph (1). (3) The authority provided by this subsection to transfer appropriated funds\u2014 (A) may be used only to provide funds for items relating to activities necessary for a program, project, or activity that has a higher priority than the programs, projects, or activities carried out using amounts from the accounts from which the funds are transferred; and (B) may not be used to provide funds for an item for which Congress has specifically denied funds. (4) The head of an agency executing a transfer under this subsection shall promptly notify the Committee on Appropriations of the Senate and the Committee on Appropriations of the House of Representatives of any transfer of funds to or from any appropriation. (j) No appropriation of funds made available or authority granted pursuant to this section shall be used to initiate or resume any program, project or activity for which appropriations, funds, or other authority were specifically prohibited during the previous fiscal year under the appropriation Act. .\n##### (b) Clerical amendment\nThe table of sections for chapter 13 of title 31, United States Code, is amended by inserting after the item relating to section 1310 the following:\n1311. Automatic continuing appropriations. .\n#### 3. Budgetary effects\n##### (a) Classification of budgetary effects\nThe budgetary effects of this Act and the amendments made by this Act shall be estimated as if this Act and the amendments made by this Act are discretionary appropriation Acts for purposes of section 251 of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901 ).\n##### (b) Baseline\nFor purposes of calculating the baseline under section 257 of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 907 ), the provision of budgetary resources under section 1311 of title 31, United States Code, as added by this Act, for an account shall be considered to be a continuing appropriation in effect for such account for less than the entire current year.\n##### (c) Enforcement of discretionary spending limits\n**(1) In general**\nFor purposes of enforcing the discretionary spending limits under section 251(a) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(a) ), the budgetary resources made available under section 1311 of title 31, United States Code, as added by this Act, shall be considered part-year appropriations for purposes of section 251(a)(4) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(a)(4) ).\n**(2) Report**\nIf a report under section 254(f) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 904(f) ) is required during a lapse in appropriations, the due date of such report shall be the later of the date specified in section 251(a)(1) of such Act ( 2 U.S.C. 901(a)(1) ) or 30 calendar days after the first day of the lapse in appropriations.\n#### 4. Effective date\nThis Act and the amendments made by this Act shall take effect on September 30, 2025.",
      "versionDate": "2025-09-23",
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
        "actionDate": "2025-09-04",
        "text": "Referred to the Committee on Appropriations, and in addition to the Committees on Rules, House Administration, Oversight and Government Reform, and the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5130",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prevent Government Shutdowns Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2721",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prevent Government Shutdowns Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-29",
        "text": "Motion by Senator Thune to reconsider the vote by which cloture on the motion to proceed to S. 2806 was not invoked (Record Vote No. 533) made in Senate."
      },
      "number": "2806",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eliminate Shutdowns Act",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-10-06T16:47:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-23",
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
          "measure-id": "id119hr5552",
          "measure-number": "5552",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-23",
          "originChamber": "HOUSE",
          "update-date": "2025-10-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5552v00",
            "update-date": "2025-10-06"
          },
          "action-date": "2025-09-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Eliminate Shutdowns Act</strong></p><p>This bill provides continuing appropriations to prevent a government shutdown if the appropriations bills for a fiscal year have not been enacted before the fiscal year begins and continuing appropriations are not in effect.</p><p>Specifically, the bill provides appropriations at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p>"
        },
        "title": "Eliminate Shutdowns Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5552.xml",
    "summary": {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate Shutdowns Act</strong></p><p>This bill provides continuing appropriations to prevent a government shutdown if the appropriations bills for a fiscal year have not been enacted before the fiscal year begins and continuing appropriations are not in effect.</p><p>Specifically, the bill provides appropriations at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p>",
      "updateDate": "2025-10-06",
      "versionCode": "id119hr5552"
    },
    "title": "Eliminate Shutdowns Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate Shutdowns Act</strong></p><p>This bill provides continuing appropriations to prevent a government shutdown if the appropriations bills for a fiscal year have not been enacted before the fiscal year begins and continuing appropriations are not in effect.</p><p>Specifically, the bill provides appropriations at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p>",
      "updateDate": "2025-10-06",
      "versionCode": "id119hr5552"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5552ih.xml"
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
      "title": "Eliminate Shutdowns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminate Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for automatic continuing appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:21Z"
    }
  ]
}
```
