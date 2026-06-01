# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1698
- Title: Law Enforcement Protection and Privacy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1698
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-03-10T08:05:28Z
- Update date including text: 2026-03-10T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1698",
    "number": "1698",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Law Enforcement Protection and Privacy Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:28Z",
    "updateDateIncludingText": "2026-03-10T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:05:10Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KS"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IN"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TN"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TN"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-08",
      "state": "OH"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "AL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "GA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "WI"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1698ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1698\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Higgins of Louisiana (for himself, Mr. Weber of Texas , Mr. Babin , Mr. Schmidt , Mr. Fleischmann , Mr. Collins , Mr. Gill of Texas , Mr. Rutherford , Mr. Harris of Maryland , and Mr. Messmer ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide accountability for unlawful disclosures of firearm trace data in the Firearms Trace System database, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Law Enforcement Protection and Privacy Act of 2025 .\n#### 2. Amendment to FOIA\nSection 552(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (8), by striking or at the end;\n**(2)**\nin paragraph (9), by striking the period and inserting ; or ; and\n**(3)**\nby inserting after paragraph (9) the following new paragraph:\n(10) contents of the Firearm Trace System database maintained by the National Trace Center of the Bureau of Alcohol, Tobacco, Firearms, and Explosives, or any information required to be kept by licensees pursuant to section 923(g) of title 18 or reported pursuant to paragraph (3) or (7) of such section. .\n#### 3. Unauthorized disclosures by agencies not part of the Federal Government\n##### (a) Fines for disclosures contrary to Federal law\nThe Attorney General shall fine a State, local, tribal, or foreign entity the following amount if the Attorney General determines that the entity made a disclosure of protected information in violation of the covered disclosure statute or any other applicable Federal law after the date of the enactment of this Act:\n**(1)**\n$10,000, for the first violation by the entity or a violation by the entity occurring more than 3 years after the most recent violation by the entity.\n**(2)**\n$25,000, for any other violation by the entity.\n##### (b) Loss of access for 1 year after multiple violations\nThe Attorney General may not disclose protected information to an entity fined under subsection (a)(2), for 1 year after the date of the imposition of the fine.\n##### (c) Enforcement of fine by civil action\nThe Attorney General may bring an action in a court of competent jurisdiction to enforce or collect payment of a fine imposed under subsection (a).\n##### (d) Assessment of fines\nIn assessing fines under this section, the Attorney General shall impose a fine for each disclosure of each individual piece of protected information in violation of the covered disclosure statute.\n#### 4. Private right of action for unauthorized disclosures of protected information\n##### (a) In general\nAny entity with a license under section 923 of title 18, United States Code, adversely affected or aggrieved by a disclosure of protected information in violation of the covered disclosure statute or any other applicable Federal law by a Federal agency or a local, tribal, or foreign entity may bring an action in a court of competent jurisdiction against the agency or entity for remedies available under this section.\n##### (b) Waiver and abrogation of sovereign immunity\nSovereign immunity shall not be a defense in an action under this section.\n##### (c) Remedies\nAn entity that prevails on a violation alleged in a claim under this section shall be entitled to\u2014\n**(1)**\nthe greater of\u2014\n**(A)**\ntriple the amount of damages suffered by the entity, including damages resulting from loss of business income or harm to the reputation of the entity; or\n**(B)**\n$25,000, for each disclosure of each individual piece of protected information in violation of the covered disclosure statute;\n**(2)**\nsuch punitive damages as the court may allow; and\n**(3)**\na reasonable attorney\u2019s fee and court costs.\n#### 5. Other remedies; severability\n##### (a) Other remedies\nThis Act shall not be interpreted to preclude any other remedy available under law.\n##### (b) Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance is held by a court to be invalid or unconstitutional, no other such provision, amendment, or application shall be affected thereby.\n#### 6. Definitions\nIn this Act:\n**(1) Covered disclosure statute**\nThe term covered disclosure statute means the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses in the Department of Justice Appropriations Act, 2012 (title II of division B of the Consolidated and Further Continuing Appropriations Act, 2012; 18 U.S.C. 923 note), or successor law.\n**(2) Federal agency**\nThe term Federal agency has the meaning given the term in section 2671 of title 28, United States Code.\n**(3) Local entity**\nThe term local entity means a city, county, municipal corporation, or other unit of government that is a political subdivision, and not an arm, of a State.\n**(4) Protected information**\nThe term protected information means the following:\n**(A)**\nThe contents, or a portion thereof, of the Firearms Trace System database maintained by the National Trace Center of the Bureau of Alcohol, Tobacco, Firearms, and Explosives.\n**(B)**\nThe information required to be kept by licensees pursuant to section 923(g) or reported pursuant to paragraph (3) or (7) of such section.",
      "versionDate": "2025-02-27",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-09-02T17:55:44Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-09-02T17:55:40Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-02T17:55:29Z"
          },
          {
            "name": "Freedom of information",
            "updateDate": "2025-09-02T17:55:35Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-09-02T17:55:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-19T17:46:31Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1698ih.xml"
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
      "title": "Law Enforcement Protection and Privacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Law Enforcement Protection and Privacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide accountability for unlawful disclosures of firearm trace data in the Firearms Trace System database, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:22Z"
    }
  ]
}
```
