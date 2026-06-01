# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5108
- Title: Stop Greenlighting Driver Licenses for Illegal Immigrants Act
- Congress: 119
- Bill type: HR
- Bill number: 5108
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-05-22T08:07:50Z
- Update date including text: 2026-05-22T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5108",
    "number": "5108",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Stop Greenlighting Driver Licenses for Illegal Immigrants Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:50Z",
    "updateDateIncludingText": "2026-05-22T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:00:45Z",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "LA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
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
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AZ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "WI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5108ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5108\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mr. Arrington (for himself, Ms. Mace , Mr. Donalds , Mr. Higgins of Louisiana , Mr. Weber of Texas , Mr. Babin , Mr. Fine , Mr. Biggs of Arizona , Mr. Nehls , Mr. Tiffany , Mr. Haridopolos , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo restrict certain Federal grants for States that grant driver licenses to illegal immigrants and fail to share information about criminal aliens with the Federal Government.\n#### 1. Short title\nThis Act may be cited as the Stop Greenlighting Driver Licenses for Illegal Immigrants Act .\n#### 2. Definitions\nIn this Act:\n**(1) Edward Byrne Memorial Justice Assistance Grant Program funds**\nThe term Edward Byrne Memorial Justice Assistance Grant Program funds \u2014\n**(A)**\nmeans a grant under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ); and\n**(B)**\nincludes a grant made directly to a unit of local government within a State under section 505(d) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10156(d) ).\n**(2) Immigration enforcement information**\nThe term immigration enforcement information means\u2014\n**(A)**\ninformation relating to the citizenship or immigration status of any individual; and\n**(B)**\nthe date, time, and location of the release of any individual from detention, jail, or a prison facility.\n**(3) State**\nThe term State has the meaning given the term in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n#### 3. Edward Byrne Memorial Justice Assistance grant restriction for States that fail to comply with Federal immigration law\n##### (a) Prohibition\nThe following States shall be subject to subsection (b):\n**(1)**\nAny State that issues a driver license to an individual who does not have proof of United States citizenship or lawful presence in the United States.\n**(2)**\nAny State that prohibits or restricts a local or State government entity or official from collecting or sending to or receiving from the Department of Homeland Security immigration enforcement information.\n##### (b) Penalty\nA State described in subsection (a) shall\u2014\n**(1)**\nin the case of a State described in subsection (a)(1), not later than 30 days after the date on which a driver license is issued to an individual who does not have proof of United States citizenship or lawful presence in the United States, return to the Treasury of the United States any unobligated Edward Byrne Memorial Justice Assistance Grant Program funds;\n**(2)**\nin the case of a State described in subsection (a)(2), not later than 30 days after the date of enactment of this Act, return to the Treasury of the United States any unobligated Edward Byrne Memorial Justice Assistance Grant Program funds; and\n**(3)**\nbe ineligible to receive Edward Byrne Memorial Justice Assistance Grant Program funds until the date on which the State institutes a law or policy that\u2014\n**(A)**\nprohibits the issuance of a driver license to an individual who does not have proof of United States citizenship or lawful presence in the United States; and\n**(B)**\npermits a local or State government entity or official to collect and send to and receive from the Department of Homeland Security immigration enforcement information.",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2774",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Greenlighting Driver Licenses for Illegal Immigrants Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-09-23T17:02:17Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5108ih.xml"
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
      "title": "Stop Greenlighting Driver Licenses for Illegal Immigrants Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Greenlighting Driver Licenses for Illegal Immigrants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict certain Federal grants for States that grant driver licenses to illegal immigrants and fail to share information about criminal aliens with the Federal Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:23Z"
    }
  ]
}
```
