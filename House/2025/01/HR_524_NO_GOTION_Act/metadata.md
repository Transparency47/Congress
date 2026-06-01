# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/524
- Title: NO GOTION Act
- Congress: 119
- Bill type: HR
- Bill number: 524
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-05-11T13:15:13Z
- Update date including text: 2026-05-11T13:15:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/524",
    "number": "524",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "NO GOTION Act",
    "type": "HR",
    "updateDate": "2026-05-11T13:15:13Z",
    "updateDateIncludingText": "2026-05-11T13:15:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "ME"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MI"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr524ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 524\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Moolenaar (for himself, Mr. LaHood , Mr. Golden of Maine , Mr. Bergman , Mr. Huizenga , Mr. Walberg , Mr. Barrett , Mr. James , Mr. Bost , Ms. Malliotakis , Ms. Tenney , Mr. Cline , Mr. Kelly of Pennsylvania , Mr. Rouzer , Mr. Schweikert , Mr. Allen , Mr. Newhouse , Mr. Finstad , Mr. Murphy , Mr. Dunn of Florida , Mr. Gimenez , Mr. Ellzey , and Mr. Palmer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny certain green energy tax benefits to companies connected to certain countries of concern.\n#### 1. Short title\nThis Act may be cited as the No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act .\n#### 2. Denial of green energy tax benefits to companies connected to countries of concern\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n7531. Denial of green energy tax benefits to companies connected to countries of concern (a) In general In the case of any disqualified company, this title shall be applied without regard to sections 30C, 40, 40A, 40B, 45, 45Q, 45U, 45V, 45W, 45X, 45Y, 45Z, 48, 48C, 48E, 179D, 6426(c), 6426(d), 6426(e), and 6427(e). (b) Disqualified company For purposes of this section\u2014 (1) In general The term disqualified company means\u2014 (A) any entity created or organized in, or controlled (in the aggregate) by, one or more countries of concern, and (B) any entity controlled (in the aggregate) by one or more entities described in paragraph (1). (2) Countries of concern The term countries of concern means the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, or the Democratic People\u2019s Republic of Korea. (3) Control The term control has the meaning given such term under section 954(d)(3), determined by treating the rules of section 958(a)(2) as applying to both foreign and domestic corporations, partnerships, trusts, and estates. .\n##### (b) Clerical amendment\nThe table of sections for chapter 77 of such Code is amended by adding at the end the following new item:\nSec. 7531. Denial of green energy tax benefits to companies connected to countries of concern. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-16",
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
        "name": "Taxation",
        "updateDate": "2025-02-19T20:04:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr524",
          "measure-number": "524",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr524v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits an entity that is created in, organized in, or controlled (in the aggregate) by China, Russia, Iran, or North Korea, or an entity controlled (in the aggregate) by one or more of such entities, from claiming multiple energy-related federal tax credits and incentives.</p><p>Specifically, the bill prohibits such entities from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>"
        },
        "title": "NO GOTION Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr524.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits an entity that is created in, organized in, or controlled (in the aggregate) by China, Russia, Iran, or North Korea, or an entity controlled (in the aggregate) by one or more of such entities, from claiming multiple energy-related federal tax credits and incentives.</p><p>Specifically, the bill prohibits such entities from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr524"
    },
    "title": "NO GOTION Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits an entity that is created in, organized in, or controlled (in the aggregate) by China, Russia, Iran, or North Korea, or an entity controlled (in the aggregate) by one or more of such entities, from claiming multiple energy-related federal tax credits and incentives.</p><p>Specifically, the bill prohibits such entities from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr524"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr524ih.xml"
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
      "title": "NO GOTION Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NO GOTION Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny certain green energy tax benefits to companies connected to certain countries of concern.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:26Z"
    }
  ]
}
```
