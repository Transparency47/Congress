# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1149
- Title: POWER Act
- Congress: 119
- Bill type: HR
- Bill number: 1149
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-03-11T17:11:33Z
- Update date including text: 2025-03-11T17:11:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1149",
    "number": "1149",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "POWER Act",
    "type": "HR",
    "updateDate": "2025-03-11T17:11:33Z",
    "updateDateIncludingText": "2025-03-11T17:11:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1149ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1149\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require retail electric utilities to notify electric consumers of rate increases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Wallets from Excessive Rates Act or the POWER Act .\n#### 2. Notification requirements for planned rate increases\n##### (a) Public Notification and Justification Requirement\n**(1) Notification to electric consumers**\nA retail electric utility that intends to increase any rate applicable to electric consumers shall, in accordance with this subsection, provide notification to electric consumers that will be impacted by the rate increase at least 30 days prior to implementing the rate increase.\n**(2) Content of Notification**\nA notification provided under paragraph (1) shall include the following:\n**(A)**\nA clear statement of the percentage of the rate increase.\n**(B)**\nA detailed breakdown of the reasons and justifications for the rate increase.\n**(C)**\nAn explanation of how the increased rate will impact the average electric consumer\u2019s bill.\n**(D)**\nInformation on how electric consumers can provide feedback or file a complaint regarding the rate increase.\n**(3) Methods of Notification**\nA retail electric utility shall provide notification under paragraph (1) using multiple communication channels to ensure, to the extent feasible, that all impacted electric consumers are provided such notification, including by providing notification by direct mail or email to such electric consumers, posting the notification on the retail electric utility\u2019s official website, and publishing the notification in local newspapers and other local media outlets.\n**(4) Penalties for Non-Compliance**\n**(A) In general**\nA retail electric utility that violates or fails or refuses to comply with the notification requirement under paragraph (1)\u2014\n**(i)**\nshall be subject to a civil penalty in an amount not to exceed $10,000; and\n**(ii)**\nmay not implement the applicable rate increase until such notification requirement is met.\n**(B) Assessment**\nA penalty under subparagraph (A) shall be assessed by the Federal Energy Regulatory Commission after notice and opportunity for public hearing. In determining the amount of such a penalty, the Commission shall take into consideration the nature and seriousness of the violation, failure, or refusal and the efforts of the retail electric utility to remedy the violation, failure, or refusal in a timely manner.\n##### (b) Department of Energy Notification Requirement\n**(1) Notification**\nA retail electric utility shall submit to the Secretary of Energy a notification of any planned rate increase of 5 percent or more for any rate applicable to electric consumers, at least 60 days prior to the implementation of such rate increase.\n**(2) Content of notification**\nA notification submitted under paragraph (1) shall include\u2014\n**(A)**\nidentification of the percentage by which the rate will be increased;\n**(B)**\na comprehensive justification for such rate increase, including cost drivers and financial impact;\n**(C)**\nan assessment of the potential impacts on electric consumers; and\n**(D)**\nany proposed mitigation measures to be taken by the retail electric utility.\n**(3) Pre-implementation review by DOE**\nThe Secretary of Energy shall\u2014\n**(A)**\nupon receiving a notification under this subsection, review the justification described in paragraph (2)(B); and\n**(B)**\nnot later than 30 days after receiving a notification under this subsection, publish a report on the Secretary\u2019s findings regarding the applicable planned rate increase, including\u2014\n**(i)**\nan assessment of the potential impacts on electric consumers; and\n**(ii)**\nany recommendations\u2014\n**(I)**\nfor adjustments to the planned rate increase;\n**(II)**\non ways to mitigate the impacts of the rate increase on electric consumers, including\u2014\n**(aa)**\nphasing in price increases; and\n**(bb)**\nfinancial aid options for electric consumers; and\n**(III)**\nfor how the retail electric utility can improve or increase efficiency to avoid future rate increases.\n**(4) Monitoring by DOE**\nThe Secretary of Energy shall, after a rate increase described in paragraph (1) is implemented, monitor the impacts of such rate increase on the market and on electric consumers to evaluate if the rate increase has had the impacts described in paragraph (3)(B) and if further action is needed.\n##### (c) Definitions\nIn this section:\n**(1) Electric consumer**\nThe term electric consumer has the meaning given such term in section 3(5) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602(5) ).\n**(2) Electric utility**\nThe term electric utility has the meaning given such term in section 3(4) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602(4) ).\n**(3) Retail electric utility**\nThe term retail electric utility means an electric utility that sells electric energy for purposes other than resale.",
      "versionDate": "2025-02-07",
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
        "name": "Energy",
        "updateDate": "2025-03-11T17:11:33Z"
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
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1149ih.xml"
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
      "title": "POWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Wallets from Excessive Rates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require retail electric utilities to notify electric consumers of rate increases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:18:22Z"
    }
  ]
}
```
