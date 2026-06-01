# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1973?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1973
- Title: No Pay for Congress During Default or Shutdown Act
- Congress: 119
- Bill type: HR
- Bill number: 1973
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-11-13T09:05:32Z
- Update date including text: 2025-11-13T09:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1973",
    "number": "1973",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "No Pay for Congress During Default or Shutdown Act",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:32Z",
    "updateDateIncludingText": "2025-11-13T09:05:32Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-03-10T16:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-10T16:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "PA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NH"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "HI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1973ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1973\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Vindman (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reduce the annual rate of pay of Members of Congress if the public debt limit is reached or a Government shutdown occurs during a year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Pay for Congress During Default or Shutdown Act .\n#### 2. Requiring reduction of pay of Members of Congress if public debt limit is reached\n##### (a) Reduction of Pay for Each Day of Government Shutdown\n**(1) In general**\nIf on any day during a year the public debt limit is reached, the annual rate of pay applicable under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ) with respect to each Member of Congress for the year shall be reduced by an amount equal to the product of\u2014\n**(A)**\nan amount equal to one day\u2019s worth of pay under such annual rate; and\n**(B)**\nthe number of 24-hour periods during which the public debt limit is reached.\n**(2) Effective date**\nThis subsection shall apply with respect to days occurring after the date of the regularly scheduled general election for Federal office held in November 2026.\n##### (b) Special rule for One Hundred Nineteenth Congress\n**(1) Holding Salaries in Escrow**\nIf on any day during the One Hundred Nineteenth Congress the public debt limit is reached, the payroll administrator of that House of Congress shall\u2014\n**(A)**\nwithhold from the payments otherwise required to be made with respect to a pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(i)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ), and\n**(ii)**\nthe number of 24-hour periods during which the public debt limit is reached which occur during the pay period; and\n**(B)**\ndeposit in an escrow account all amounts withheld under subparagraph (A).\n**(2) Release of amounts at end of the Congress**\nIn order to ensure that this subsection is carried out in a manner that shall not vary the compensation of Members of Congress in violation of the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this subsection on the last day of the One Hundred Nineteenth Congress.\n**(3) Exception for days occurring after general election**\nThis subsection does not apply with respect to any day during the One Hundred Nineteenth Congress which occurs after the date of the regularly scheduled general election for Federal office held in November 2026.\n##### (c) Determination of reaching of public debt limit\nFor purposes of this section, the public debt limit shall be considered to be reached if the Federal Government is unable to make payments or meet obligations because the public debt limit under section 3101 of title 31, United States Code, has been reached.\n#### 3. Requiring reduction of pay of Members of Congress if Government shutdown occurs\n##### (a) Reduction of pay for each day of Government shutdown\n**(1) In general**\nIf on any day during a year a Government shutdown is in effect, the annual rate of pay applicable under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ) with respect to each Member of Congress for the year shall be reduced by an amount equal to the product of\u2014\n**(A)**\nan amount equal to one day\u2019s worth of pay under such annual rate; and\n**(B)**\nthe number of 24-hour periods during which the Government shutdown is in effect.\n**(2) Effective date**\nThis subsection shall apply with respect to days occurring after the date of the regularly scheduled general election for Federal office held in November 2026.\n##### (b) Special rule for One Hundred Nineteenth Congress\n**(1) Holding salaries in escrow**\nIf on any day during the One Hundred Nineteenth Congress a Government shutdown is in effect, the payroll administrator of that House of Congress shall\u2014\n**(A)**\nwithhold from the payments otherwise required to be made with respect to a pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(i)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(ii)**\nthe number of 24-hour periods during which the Government shutdown is in effect which occur during the pay period; and\n**(B)**\ndeposit in an escrow account all amounts withheld under subparagraph (A).\n**(2) Release of amounts at end of the Congress**\nIn order to ensure that this subsection is carried out in a manner that shall not vary the compensation of Senators or Representatives in violation of the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this subsection on the last day of the One Hundred Nineteenth Congress.\n**(3) Exception for days occurring after general election**\nThis subsection does not apply with respect to any day during the One Hundred Nineteenth Congress which occurs after the date of the regularly scheduled general election for Federal office held in November 2026.\n##### (c) Determination of Government shutdown\nFor purposes of this section, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 4. Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this Act.\n#### 5. Definitions\n##### (a) Member of Congress\nIn this Act, the term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ).\n##### (b) Payroll administrator\nIn this Act, the payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this Act; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this Act.",
      "versionDate": "2025-03-10",
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
        "name": "Congress",
        "updateDate": "2025-03-26T12:31:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr1973",
          "measure-number": "1973",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-10-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1973v00",
            "update-date": "2025-10-01"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Pay for Congress During Default or Shutdown Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress for any day that the public debt limit is reached or there is a government shutdown.</p><p>During the 119th Congress, any salary earned by Members during these events must be held in escrow and released on the last day of that Congress. For subsequent Congresses, a Member shall not be paid for any day that these events occur. (Some exceptions apply.)</p>"
        },
        "title": "No Pay for Congress During Default or Shutdown Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1973.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pay for Congress During Default or Shutdown Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress for any day that the public debt limit is reached or there is a government shutdown.</p><p>During the 119th Congress, any salary earned by Members during these events must be held in escrow and released on the last day of that Congress. For subsequent Congresses, a Member shall not be paid for any day that these events occur. (Some exceptions apply.)</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr1973"
    },
    "title": "No Pay for Congress During Default or Shutdown Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pay for Congress During Default or Shutdown Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress for any day that the public debt limit is reached or there is a government shutdown.</p><p>During the 119th Congress, any salary earned by Members during these events must be held in escrow and released on the last day of that Congress. For subsequent Congresses, a Member shall not be paid for any day that these events occur. (Some exceptions apply.)</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr1973"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1973ih.xml"
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
      "title": "No Pay for Congress During Default or Shutdown Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Pay for Congress During Default or Shutdown Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the annual rate of pay of Members of Congress if the public debt limit is reached or a Government shutdown occurs during a year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T06:18:24Z"
    }
  ]
}
```
