# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4505
- Title: Export Controls Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 4505
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-05-22T17:35:27Z
- Update date including text: 2026-05-22T17:35:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 41 - 3.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 41 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4505",
    "number": "4505",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Export Controls Enforcement Act",
    "type": "HR",
    "updateDate": "2026-05-22T17:35:27Z",
    "updateDateIncludingText": "2026-05-22T17:35:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 41 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
            "date": "2026-04-22T20:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-17T13:00:20Z",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "MI"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "AS"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "AZ"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "RI"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4505ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4505\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Kamlager-Dove (for herself, Mr. Huizenga , Mr. Meeks , and Mr. Shreve ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo strengthen enforcement of United States export controls by increasing the number of export control officers of the Bureau of Industry and Security of the Department of Commerce who are stationed in foreign regions.\n#### 1. Short title\nThis Act may be cited as the Export Controls Enforcement Act .\n#### 2. Findings and sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Bureau of Industry and Security of the Department of Commerce (hereinafter the Bureau ) uses end-use checks to verify that controlled items exported from the United States are used in accordance with United States license requirements and the Export Administration Regulations (parts 730\u2013774 of title 15, Code of Federal Regulations) and each other export control policy under the administrative jurisdiction of the Bureau.\n**(2)**\nThe Bureau\u2019s export control officers conduct end-use checks in foreign regions to ensure that persons to a transaction comply with such requirements and regulations and do not divert controlled items to unauthorized users.\n**(3)**\nThe Bureau\u2019s export control officers are also responsible for liaising with governments and the private sector on the export controls policies under the administrative jurisdiction of the Bureau.\n**(4)**\nInconclusive or failed end-use checks can lead the Bureau to inaccurately added persons to watch lists, deny export privileges, or take enforcement or criminal action.\n**(5)**\nIn 2024, the Bureau processed over 45,000 license applications valued at over $500,000,000,000.\n**(6)**\nIn fiscal year 2024, the Bureau\u2019s export control officers conducted over 1,400 end-use checks in 60 countries.\n**(7)**\nAs of 2025, the Bureau has only 11 export control officers in foreign regions, with individual officers often covering multiple countries, and dozens of countries where no officer is assigned to them.\n##### (b) Senses of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nend-use checks are critical for verifying the persons to a transaction, assessing the risk of unauthorized use or diversion of controlled items, and determining whether such items are being used according to United States regulations and licenses; and\n**(2)**\nthe United States needs more export control officers stationed in foreign regions to effectively prevent and catch illegal diversion of United States technologies and adequately enforce the export controls policies under the administrative jurisdiction of the Bureau.\n#### 3. Export control officer program\n##### (a) Establishment\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Commerce, acting through the Under Secretary for Industry and Security, shall establish for a period of 5 years an Export Control Officer Program (hereinafter the Program ) to station not less than 20 export control officers at United States diplomatic or consular posts.\n**(2) Program Director**\n**(A) Appointment**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Commerce shall appoint, from among the full-time equivalent employees of the Department of Commerce, a Director to lead the Program.\n**(B) Responsibilities**\nThe Director shall be responsible for overseeing the hiring of the export control officers in the Program and coordinating with the Secretary of State to strategically station the officers in a manner that ensures geographic coverage for every region of the world.\n##### (b) Duties\nEach export control officer within the Program shall fulfill, within the geographic region the officer is stationed, the following duties:\n**(1)**\nManaging and conducting end-use checks with persons involved in transactions of items subject to the export controls policies under the administrative jurisdiction of the Bureau, to improve the scope and effectiveness of such checks.\n**(2)**\nInforming and advising United States diplomatic or consular posts on the export controls policies under the administrative jurisdiction of the Bureau.\n**(3)**\nPerforming industry outreach to enhance compliance with the export controls policies under the administrative jurisdiction of the Bureau.\n**(4)**\nLiaising with foreign governments to enhance cooperation and coordination with the United States with respect to the export control policies under the administrative jurisdiction of the Bureau and the enforcement practices of the Bureau.\n**(5)**\nSharing information with the Bureau\u2019s officials regarding the enforcement challenges, trends, and priorities of the Bureau.\n**(6)**\nIdentifying the best targets with respect to who the Bureau should conduct end-use checks on.",
      "versionDate": "2025-07-17",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T16:41:03Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4505ih.xml"
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
      "title": "Export Controls Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Export Controls Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen enforcement of United States export controls by increasing the number of export control officers of the Bureau of Industry and Security of the Department of Commerce who are stationed in foreign regions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:34:02Z"
    }
  ]
}
```
