# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/723?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/723
- Title: Protect American Election Administration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 723
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-06-13T18:05:42Z
- Update date including text: 2025-06-13T18:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/723",
    "number": "723",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001053",
        "district": "4",
        "firstName": "Tom",
        "fullName": "Rep. Cole, Tom [R-OK-4]",
        "lastName": "Cole",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Protect American Election Administration Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-13T18:05:42Z",
    "updateDateIncludingText": "2025-06-13T18:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:00:45Z",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NY"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "KS"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OK"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr723ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 723\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Cole (for himself, Ms. Foxx , Mr. Ellzey , Ms. Tenney , Mr. Zinke , Mr. Carter of Texas , and Mr. Mann ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to prohibit a State from receiving or using funds or certain donations from private entities for the administration of an election for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect American Election Administration Act of 2025 .\n#### 2. Prohibition against the receipt or use of funds or certain donations from private entities\n##### (a) Requirements\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307, respectively; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Prohibition against the receipt or use of funds or certain donations from private entities for election administration (a) In general A State may not solicit, receive, or expend any payment or donation of funds, property, or personal services from a private entity for the purpose of the administration of an election for Federal office, including any programs with respect to voter education, voter outreach, and voter registration. (b) Exception This section shall not apply with respect to the acceptance and use by a State of a donation from a private entity of space to be used for a polling place or an early voting site in the State. .\n##### (b) Conforming amendment relating to enforcement\nSection 401 of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 ) is amended by striking 303, and 304 and inserting 303, 304, and 305 .\n##### (c) Clerical amendment\nThe table of contents of such Act is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to sections 306 and 307, respectively; and\n**(2)**\nby inserting after the item relating to section 304 the following new item:\nSec. 305. Prohibition against the receipt or use of funds or certain donations from private entities for election administration. .\n##### (d) Effective date\nThe amendment made by this section shall apply with respect to any election for Federal office held after the date of the enactment of this Act.",
      "versionDate": "2025-01-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Charitable contributions",
            "updateDate": "2025-06-13T18:05:42Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-06-13T18:05:33Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-13T18:05:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-01T20:51:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr723",
          "measure-number": "723",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr723v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect American Election Administration Act of </strong><strong>2025</strong></p><p>This bill generally prohibits a state from soliciting, receiving, or expending any payment or donation of funds, property, or personal services from a private entity for the purpose of administering a federal election. For example, the bill prohibits the use of these payments or donations for programs related to voter education, outreach, and registration.</p><p>The prohibition shall not apply to a state's acceptance and use of a private entity's donation of space to be used for a polling place or an early voting site.</p>"
        },
        "title": "Protect American Election Administration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr723.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect American Election Administration Act of </strong><strong>2025</strong></p><p>This bill generally prohibits a state from soliciting, receiving, or expending any payment or donation of funds, property, or personal services from a private entity for the purpose of administering a federal election. For example, the bill prohibits the use of these payments or donations for programs related to voter education, outreach, and registration.</p><p>The prohibition shall not apply to a state's acceptance and use of a private entity's donation of space to be used for a polling place or an early voting site.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr723"
    },
    "title": "Protect American Election Administration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect American Election Administration Act of </strong><strong>2025</strong></p><p>This bill generally prohibits a state from soliciting, receiving, or expending any payment or donation of funds, property, or personal services from a private entity for the purpose of administering a federal election. For example, the bill prohibits the use of these payments or donations for programs related to voter education, outreach, and registration.</p><p>The prohibition shall not apply to a state's acceptance and use of a private entity's donation of space to be used for a polling place or an early voting site.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr723"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr723ih.xml"
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
      "title": "Protect American Election Administration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect American Election Administration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to prohibit a State from receiving or using funds or certain donations from private entities for the administration of an election for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:49Z"
    }
  ]
}
```
