# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8665
- Title: Allied Defense Sales Act
- Congress: 119
- Bill type: HR
- Bill number: 8665
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-14T08:08:15Z
- Update date including text: 2026-05-14T08:08:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 1.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8665",
    "number": "8665",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Allied Defense Sales Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:15Z",
    "updateDateIncludingText": "2026-05-14T08:08:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 44 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
        "item": [
          {
            "date": "2026-05-13T15:29:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-04T14:31:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "SC"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8665ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8665\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Zinke (for himself and Mr. Bera ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the implementation of a strategy to encourage foreign partners to participate in the foreign military sales and direct commercial sales processes on a multinational basis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Allied Defense Sales Act .\n#### 2. Strategy and report on multinational procurement from the United States\n##### (a) Strategy\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall implement a strategy to encourage foreign partners to participate in the foreign military sales and direct commercial sales processes on a multinational basis. Such strategy shall incorporate existing efforts by the Department of State to\u2014\n**(1)**\nsurvey interest in participating in such multinational procurement processes among potentially eligible countries;\n**(2)**\nidentify countries and partners who may be eligible to serve as the lead purchase coordinator for a multinational procurement process, and potential incentives for their participation as lead coordinator;\n**(3)**\nreview pathways for participation in foreign military sales or direct commercial sales processes for countries determined to be ineligible for foreign military financing loans;\n**(4)**\nidentify challenges and solutions for the Department in carrying out such processes in accordance with the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ), including applicable end-use monitoring, technical assistance agreements, and license filing requirements;\n**(5)**\nidentify ways to provide for expedited license authorizations, sales other than for programs of record, and other potential efforts to increase speed and ease enhanced use of multinational procurement processes;\n**(6)**\ndetailing the benefits of multinational procurement processes to the national security interest, including enhanced military interoperability and strengthening the domestic industrial base; and\n**(7)**\nidentify opportunities to develop and promote exportable defense articles and services, including for purposes of supporting the AUKUS partnership.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter for 3 years, the Secretary shall submit to the appropriate congressional committees a report on the strategy required by subsection (a) and its implementation. Such report shall also include\u2014\n**(1)**\nan update on the development and implementation of the initial strategy during the period following the most recent prior submission of such report (if any);\n**(2)**\na description of challenges faced in the implementation of the strategy;\n**(3)**\na description of all efforts the Department has undertaken to overcome such challenges;\n**(4)**\na list and description of any potential legislative changes necessary to fully implement a multinational procurement process for foreign military sales and direct commercial sales; and\n**(5)**\na description of efforts to promote exportable defense articles and services specifically for use in multinational procurement processes, including those supporting the AUKUS partnership.\n##### (c) Form\nThe report required by subsection (b) shall be submitted in unclassified form and may include a classified annex.\n##### (d) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate;\n**(2)**\nthe term AUKUS partnership means the enhanced trilateral security partnership between Australia, the United Kingdom, and the United States announced in September 2021; and\n**(3)**\nthe term multinational procurement process refers to a process by which defense articles or services are sold by the United States to a lead foreign nation, with the intent that the articles or services so sold will subsequently be retransferred to a previously identified group of participating countries, or to countries identified by reference to a qualifying multilateral partnership agreement, such as a cross-servicing agreement described in section 2350 of title 10, United States Code.",
      "versionDate": "2026-05-04",
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
        "name": "International Affairs",
        "updateDate": "2026-05-08T20:32:02Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8665ih.xml"
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
      "title": "Allied Defense Sales Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Allied Defense Sales Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the implementation of a strategy to encourage foreign partners to participate in the foreign military sales and direct commercial sales processes on a multinational basis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:33Z"
    }
  ]
}
```
