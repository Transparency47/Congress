# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6666
- Title: HIRRE Prosecutors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6666
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-03-28T08:06:19Z
- Update date including text: 2026-03-28T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6666",
    "number": "6666",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HIRRE Prosecutors Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:19Z",
    "updateDateIncludingText": "2026-03-28T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:06:10Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NE"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CO"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6666ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6666\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Panetta (for himself, Mr. Bacon , Mr. Neguse , Mr. Kennedy of New York , Mr. Goldman of New York , Mr. David Scott of Georgia , Mr. Ciscomani , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to establish a single grant program to make grants to hire prosecutors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Improve Recruitment and Retention Efforts for Prosecutors Act of 2025 or as the HIRRE Prosecutors Act of 2025 .\n#### 2. Authority to make grants for prosecutors\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall establish a program (in this Act referred to as the Program ) to assist a State, territory, unit of local government, or tribal government in hiring prosecutors.\n##### (b) Grant authority\nIn carrying out the Program, the Attorney General may award a grant on a competitive basis in accordance with this section.\n##### (c) Eligible recipients\nThe Attorney General may award a grant under the Program each year to a prosecutor's office of a State, territory, unit of local government, or tribal government that submits an application pursuant to subsection (d).\n##### (d) Application\nTo be eligible for a grant under the Program, an eligible recipient shall submit to the Attorney General an application in such form, at such time, and containing such information as the Attorney General determines to be appropriate.\n##### (e) Eligible projects\nGrant funds awarded under the Program may only be used to hire, retain, and train prosecutors or support staff for a prosecutor's office of a State, territory, unit of local government, or tribal government.\n##### (f) Use of components\nThe Attorney General may use any component of the Department of Justice in carrying out this section.\n##### (g) Preferential consideration of applications for certain grants\nIn awarding grants under this section, the Attorney General may give preferential consideration to an application\u2014\n**(1)**\nto hire and train new prosecutors or support staff for a prosecutor's office of a State, territory, unit of local government, or tribal government;\n**(2)**\nto rehire prosecutors who have been laid off as a result of State, territory, unit of local government, or tribal government budget reductions; and\n**(3)**\nfrom a jurisdiction representing a tribal, remote, or rural area, as defined in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n##### (h) Federal share\n**(1) Federal share**\nThe Federal share of the cost of a project assisted with a grant under the Program shall not exceed 75 percent.\n**(2) Waiver**\nThe Attorney General may waive the 25 percent matching requirement under paragraph (1) upon making a determination that a waiver is equitable in view of the financial circumstances affecting the ability of the eligible recipient to meet that requirement.\n**(3) Nonsupplanting requirement**\nFunds made available under the Program shall not be used to supplant State or local funds, or, in the case of Indian tribal governments, funds awarded by the Bureau of Indian Affairs, but shall be used to increase the amount of funds that would, in the absence of Federal funds received under the Program, be made available from State or local sources, or in the case of Indian tribal governments, from funds supplied by the Bureau of Indian Affairs.\n**(4) Non-Federal costs**\n**(A) In general**\nA State or unit of local or tribal government may use assets received through the assets forfeiture equitable sharing program.\n**(B) Indian tribal governments**\nFunds appropriated by Congress for the activities of any agency of an Indian tribal government or the Bureau of Indian Affairs performing prosecutorial functions on any Indian lands may be used to provide the non-Federal share of the cost of programs or projects funded under this section.\n##### (i) Performance evaluation\n**(1) Monitoring components**\nEach project funded by a grant under the Program shall contain a monitoring component, including the systematic identification and collection of data about activities, accomplishments, and programs undertaken pursuant to the Program.\n**(2) Evaluation components**\nThe Attorney General shall evaluate each project funded by a grant under the Program, individually or as part of a national evaluation.\n**(3) Periodic review and reports**\nThe Attorney General may require a project funded under the Program to submit to the Attorney General the results of the monitoring component and evaluation under paragraphs (1) and (2), respectively, as well as any other information as the Attorney General deems necessary.\n**(4) Revocation or suspension of funding**\nIf the Attorney General determines, as a result of evaluation under this subsection, or otherwise, that a grant under the Program is not in substantial compliance with the terms and requirements of the Program, the Attorney General may revoke or suspend funding of that grant, in whole or in part.\n##### (j) General regulatory authority\nThe Attorney General may promulgate regulations and guidelines to carry out this section.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to carry out the Program $10,000,000 for each of the fiscal years 2026 through 2030.",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3438",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HIRRE Prosecutors Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-08T15:07:12Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6666ih.xml"
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
      "title": "HIRRE Prosecutors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HIRRE Prosecutors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Improve Recruitment and Retention Efforts for Prosecutors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General to establish a single grant program to make grants to hire prosecutors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:21Z"
    }
  ]
}
```
