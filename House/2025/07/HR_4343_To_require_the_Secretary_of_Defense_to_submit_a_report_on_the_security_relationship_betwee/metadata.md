# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4343?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4343
- Title: United States-Greece Security Cooperation Reporting Act
- Congress: 119
- Bill type: HR
- Bill number: 4343
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-02-25T09:06:17Z
- Update date including text: 2026-02-25T09:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4343",
    "number": "4343",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "United States-Greece Security Cooperation Reporting Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:17Z",
    "updateDateIncludingText": "2026-02-25T09:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-10T15:04:20Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-08",
      "state": "TN"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "DE"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "OH"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
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
      "sponsorshipDate": "2026-01-07",
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
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4343ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4343\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Meng (for herself, Mr. Bilirakis , Ms. Titus , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Defense to submit a report on the security relationship between the United States and the Hellenic Republic, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Greece Security Cooperation Reporting Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States and the Hellenic Republic share a longstanding and robust security relationship, rooted in shared democratic values, mutual strategic interests, and joint membership in the North Atlantic Treaty Organization (NATO).\n**(2)**\nThe United States-Greece Mutual Defense Cooperation Agreement (MDCA), updated on October 14, 2021, reflects the deepening defense partnership between the two countries and enhances the United States ability to operate across the Eastern Mediterranean, Southeastern Europe, Eastern Europe, and the Middle East.\n**(3)**\nThe Hellenic Republic occupies a strategically vital geographic position that supports regional security, energy diversification, and efforts to counter malign influence.\n**(4)**\nUnited States military investments and activities at key locations in Greece, such as Alexandroupolis, Larisa, Stefanovikio, and Souda Bay, have contributed to improved United States and NATO interoperability, operational flexibility, and deterrence posture.\n**(5)**\nThe Port of Alexandroupolis has emerged as a critical logistical hub for the United States and NATO, enabling the rapid deployment of forces and equipment to Eastern and Southeastern Europe and beyond.\n**(6)**\nNaval Support Activity (NSA) Souda Bay is one of the most strategically important United States naval facilities in the Eastern Mediterranean and helps support forward-deployed operations, maritime security, and the defense of multiple theaters, including Eastern and Southeastern Europe.\n**(7)**\nSubtitle B of title XIII of division A of the National Defense Authorization Act for Fiscal Year 2022 ( Public Law 117\u201381 ), known as the United States-Greece Defense and Interparliamentary Partnership Act of 2021, mandated a framework to further strengthen bilateral defense cooperation, expand joint training opportunities, and promote interparliamentary engagement.\n**(8)**\nOngoing instability and increased geopolitical competition highlight the need for continued assessment and adaptation of the United States military posture and security cooperation with Greece.\n#### 3. Report on the security relationship between the United States and the Hellenic Republic\n##### (a) Report\nNot later than 120 days after the date of enactment of this Act, the Secretary of Defense, in coordination with the Commander of United States European Command, shall jointly submit to the appropriate congressional committees a report on the security relationship between the United States and the Hellenic Republic.\n##### (b) Report contents\nThe report required under subsection (a) shall include the following:\n**(1)**\nA description of the basing rights granted to the United States under the updated United States-Greece Mutual Defense Cooperation Agreement (MDCA), signed October 14, 2021.\n**(2)**\nA description of United States activities and investment on the bases covered in the MDCA since such date.\n**(3)**\nA project of investments needed in association with United States basing rights at Alexandroupolis.\n**(4)**\nAn analysis of the potential for additional bases or expanded United States military presence in the Hellenic Republic, particularly on Greek islands.\n**(5)**\nAn assessment of the status of the security cooperation mandated pursuant to subtitle B of title XIII of division A of the National Defense Authorization Act of Fiscal Year 2022 ( Public Law 117\u201381 ; relating to the United States-Greece Defense and Interparliamentary Partnership Act of 2021).\n##### (c) Definition\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nThe House Armed Services Committee; or\n**(2)**\nThe Senate Armed Services Committee.",
      "versionDate": "2025-07-10",
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
        "updateDate": "2025-07-29T22:08:26Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4343ih.xml"
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
      "title": "United States-Greece Security Cooperation Reporting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States-Greece Security Cooperation Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Defense to submit a report on the security relationship between the United States and the Hellenic Republic, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:24Z"
    }
  ]
}
```
