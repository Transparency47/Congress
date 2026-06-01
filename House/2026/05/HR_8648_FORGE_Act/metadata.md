# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8648
- Title: FORGE Act
- Congress: 119
- Bill type: HR
- Bill number: 8648
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-14T08:08:25Z
- Update date including text: 2026-05-14T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8648",
    "number": "8648",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "FORGE Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:25Z",
    "updateDateIncludingText": "2026-05-14T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
        "item": {
          "date": "2026-05-04T14:31:45Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "MA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8648ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8648\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Baird (for himself and Mr. Keating ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish in the Department of State a Foundational Infrastructure for Responsible Use of Small Modular Reactor Technology program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Framework for Oversight of Responsible Global Energy Act or the FORGE Act .\n#### 2. Establishment of Foundational Infrastructure for Responsible Use of Small Modular Reactor Technology program\n##### (a) In general\nThere is established within the Department of State a Foundational Infrastructure for Responsible Use of Small Modular Reactor Technology program (hereafter in this section referred to as the FIRST program ).\n##### (b) Program functions\nThe Under Secretary for Arms Control and International Security, or the designee of the Under Secretary, shall manage the FIRST program, which shall\u2014\n**(1)**\npromote responsible deployment of civil nuclear energy internationally that benefits United States economic and national security interests;\n**(2)**\nadvocate, through relevant bilateral and multilateral diplomatic engagements and forums, for civil nuclear energy projects, technology, and products sourced or exported from United States businesses;\n**(3)**\nengage in diplomacy with partner governments on prioritizing the highest safety, security, and nonproliferation standards as requirements for civil nuclear reactor deployment decisions, including with regard to small modular reactor infrastructure, technology, and products;\n**(4)**\nprovide consultation to partner countries regarding best practices in the field of licensing, legal, and regulatory frameworks for the importation or adoption of United States nuclear reactor infrastructure, technology, or products;\n**(5)**\nprovide early-stage commercial project development support, including feasibility and engineering studies, that are critical to launching United States commercial civil nuclear projects abroad and ensure fair market access for United States businesses relative to state-backed competitors; and\n**(6)**\ncooperate with partner countries in the areas of training programs, technical resource sharing, and potential coordination of codes and standards to support the facilitation of small modular reactor fleet deployment.\n##### (c) Report\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the Under Secretary for Arms Control and International Security, or the designee of such Under Secretary, shall provide to the appropriate congressional committees a report that includes\u2014\n**(A)**\ndetails on the implementation of the FIRST program;\n**(B)**\na description of FIRST program diplomatic outreach and activities, including bilateral and multilateral engagements that promote activities described in subsection (b);\n**(C)**\nthe list of current contributing partners of the FIRST program;\n**(D)**\ndetails relating to potential or ongoing cooperation with contributing partners of the FIRST program related to program activities described in subsection (b);\n**(E)**\na description of engagements and activities conducted by the Department of State to promote and expand the FIRST program to additional potential contributing partners;\n**(F)**\na description of FIRST program-related engagements with United States businesses in the civil nuclear sector; and\n**(G)**\na description of funds expended on FIRST program-related activities, including programming that uses funds from Nonproliferation, Anti-Terrorism, Demining, and Related Programs and related funding sources within the Department.\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex submitted separately from the unclassified portion.\n##### (d) Briefing\nNot later than 120 days after the date of the enactment of this Act, and on a triannual basis thereafter, the Under Secretary for Arms Control and International Security, or the designee of the Under Secretary, shall provide to the appropriate congressional committees a briefing that includes the information required in subsection (c).\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of the Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate.\n**(2) United States business**\nThe term United States business has the meaning given such term in section 2304 of the Export Enhancement Act of 1988 ( 15 U.S.C. 4724 ).\n##### (f) Sunset\nThis section shall terminate on June 8, 2034.",
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
        "updateDate": "2026-05-08T20:31:46Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8648ih.xml"
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
      "title": "FORGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FORGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Framework for Oversight of Responsible Global Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish in the Department of State a Foundational Infrastructure for Responsible Use of Small Modular Reactor Technology program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:34Z"
    }
  ]
}
```
