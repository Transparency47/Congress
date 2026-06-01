# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/600
- Title: WHO is Accountable Act
- Congress: 119
- Bill type: HR
- Bill number: 600
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-03-11T08:06:50Z
- Update date including text: 2025-03-11T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/600",
    "number": "600",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "WHO is Accountable Act",
    "type": "HR",
    "updateDate": "2025-03-11T08:06:50Z",
    "updateDateIncludingText": "2025-03-11T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:01:35Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "KS"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr600ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 600\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Arrington (for himself, Mr. Crenshaw , Mr. Estes , and Mr. Steube ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization.\n#### 1. Short title\nThis Act may be cited as the WHO is Accountable Act .\n#### 2. Prohibition on use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization\n##### (a) In general\nNotwithstanding any other provision of law, no funds available to any Federal department or agency may be used to seek membership by the United States in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization until such time as the Secretary of State certifies to Congress that the World Health Organization meets the conditions described in subsection (b).\n##### (b) Conditions described\nThe conditions described in this subsection are the following:\n**(1)**\nThe World Health Organization has adopted meaningful reforms to ensure that humanitarian assistance is not politicized and is to be provided to those with the most need.\n**(2)**\nThe World Health Organization is not under the control or significant malign influence of the Chinese Communist Party.\n**(3)**\nThe World Health Organization is not involved in a coverup of the Chinese Communist Party\u2019s response to the COVID\u201319 pandemic.\n**(4)**\nThe World Health Organization grants observer status to Taiwan.\n**(5)**\nThe World Health Organization does not divert humanitarian or medical supplies to Iran, North Korea, or Syria.\n**(6)**\nThe World Health Organization has put in place mechanisms to increase transparency and accountability in its operations and eliminate waste, fraud, and abuse.\n**(7)**\nThe World Health Organization has ceased all funding for, engagement in, and messaging with respect to certain controversial and politically charged issues that are non-germane to the World Health Organization\u2019s directive, including\u2014\n**(A)**\nso-called gender identity and harmful rhetoric relating to gender affirming care ;\n**(B)**\nclimate change; and\n**(C)**\naccess to abortion.\n**(8)**\nThe World Health Organization has agreed that as a condition of membership by the United States in the World Health Organization, no directive issued by the World Health Organization may be considered to be legally binding on any United States citizen or individual State.",
      "versionDate": "2025-01-22",
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
        "updateDate": "2025-02-21T13:00:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr600",
          "measure-number": "600",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr600v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>WHO is Accountable Act</strong></p><p>This bill prohibits the use of federal funds to seek U.S. membership in the World Health Organization (WHO), or to make contributions to the WHO, until the Department of State makes certain certifications to Congress.</p><p>Specifically, these prohibitions shall apply until the State Department certifies that the WHO has met certain conditions, including that the WHO (1) has adopted reforms to ensure that humanitarian assistance is not politicized; (2) is not under the control of the Chinese Communist Party (CCP) and is not involved in a cover-up of the CCP's response to the COVID-19 pandemic; (3) has granted observer status to Taiwan; and (4) has ceased engagement on certain issues, such as climate change, access to abortion, and gender identity.</p>"
        },
        "title": "WHO is Accountable Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr600.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>WHO is Accountable Act</strong></p><p>This bill prohibits the use of federal funds to seek U.S. membership in the World Health Organization (WHO), or to make contributions to the WHO, until the Department of State makes certain certifications to Congress.</p><p>Specifically, these prohibitions shall apply until the State Department certifies that the WHO has met certain conditions, including that the WHO (1) has adopted reforms to ensure that humanitarian assistance is not politicized; (2) is not under the control of the Chinese Communist Party (CCP) and is not involved in a cover-up of the CCP's response to the COVID-19 pandemic; (3) has granted observer status to Taiwan; and (4) has ceased engagement on certain issues, such as climate change, access to abortion, and gender identity.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr600"
    },
    "title": "WHO is Accountable Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>WHO is Accountable Act</strong></p><p>This bill prohibits the use of federal funds to seek U.S. membership in the World Health Organization (WHO), or to make contributions to the WHO, until the Department of State makes certain certifications to Congress.</p><p>Specifically, these prohibitions shall apply until the State Department certifies that the WHO has met certain conditions, including that the WHO (1) has adopted reforms to ensure that humanitarian assistance is not politicized; (2) is not under the control of the Chinese Communist Party (CCP) and is not involved in a cover-up of the CCP's response to the COVID-19 pandemic; (3) has granted observer status to Taiwan; and (4) has ceased engagement on certain issues, such as climate change, access to abortion, and gender identity.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr600"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr600ih.xml"
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
      "title": "WHO is Accountable Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WHO is Accountable Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:32Z"
    }
  ]
}
```
