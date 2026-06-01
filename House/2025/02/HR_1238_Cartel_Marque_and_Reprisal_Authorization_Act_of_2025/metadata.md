# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1238
- Title: Cartel Marque and Reprisal Authorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1238
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-01-20T16:35:54Z
- Update date including text: 2026-01-20T16:35:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1238",
    "number": "1238",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Cartel Marque and Reprisal Authorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-20T16:35:54Z",
    "updateDateIncludingText": "2026-01-20T16:35:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:07:20Z",
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
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1238ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1238\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Burchett (for himself and Mr. Messmer ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize the President of the United States to issue letters of marque and reprisal with respect to acts of aggression against the United States by a member of a cartel, or a member of a cartel-linked organization, or any conspirator associated with a cartel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cartel Marque and Reprisal Authorization Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nArticle I, Section 8 of the Constitution grants the Congress the power to grant letters of marque and reprisal to punish, deter, and prevent the acts of aggression and depredations and other acts of war committed by cartel conspirators.\n**(2)**\nCartels present an unusual and extraordinary threat to national security and foreign policy of the United States.\n#### 3. Issuance of letters of marque and reprisal\n##### (a) Authority of President\nThe President of the United States is authorized and requested to commission, under officially issued letters of marque and reprisal, so many of privately armed and equipped persons and entities as, in the judgment of the President, the service may require, with suitable instructions to the leaders thereof, to employ all means reasonably necessary to seize outside the geographic boundaries of the United States and its territories the person and property of any individual who the President determines is a member of a cartel, a member of a cartel-linked organization, or a conspirator associated with a cartel or a cartel-linked organization, who is responsible for an act of aggression against the United States.\n##### (b) Security Bonds\nNo letter of marque and reprisal shall be issued by the President without requiring the posting of a security bond in such amount as the President shall determine is sufficient to ensure that the letter be executed according to the terms and conditions thereof.\n##### (c) Definition of cartel\nIn this section, the term cartel means an organization that\u2014\n**(1)**\nis described in section 1 of the executive order titled Designating Cartels And Other Organizations As Foreign Terrorist Organizations and Specially Designated Global Terrorists and dated January 20, 2025; or\n**(2)**\nis a transnational criminal organization under the meaning given that term in section 3003(5) of the Public Law 118\u201350 ( 21 U.S.C. 2341(5) ).",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-12-18",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to authorize the President of the United States to issue letters of marque and reprisal with respect to acts of aggression against the United States by a member of a cartel, or a member of a cartel-linked organization, or any conspirator associated with a cartel, and for other purposes.",
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
        "name": "International Affairs",
        "updateDate": "2025-05-07T16:15:37Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1238ih.xml"
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
      "title": "Cartel Marque and Reprisal Authorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cartel Marque and Reprisal Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the President of the United States to issue letters of marque and reprisal with respect to acts of aggression against the United States by a member of a cartel, or a member of a cartel-linked organization, or any conspirator associated with a cartel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:04Z"
    }
  ]
}
```
