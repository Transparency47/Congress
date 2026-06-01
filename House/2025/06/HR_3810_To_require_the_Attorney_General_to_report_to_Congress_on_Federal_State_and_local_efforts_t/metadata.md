# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3810?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3810
- Title: SKIM Act
- Congress: 119
- Bill type: HR
- Bill number: 3810
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2026-02-05T09:06:57Z
- Update date including text: 2026-02-05T09:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3810",
    "number": "3810",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000480",
        "district": "20",
        "firstName": "Vince",
        "fullName": "Rep. Fong, Vince [R-CA-20]",
        "lastName": "Fong",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "SKIM Act",
    "type": "HR",
    "updateDate": "2026-02-05T09:06:57Z",
    "updateDateIncludingText": "2026-02-05T09:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:05:45Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "NC"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "NY"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "OH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NE"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
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
      "sponsorshipDate": "2026-02-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3810ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3810\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Fong (for himself, Mr. Valadao , Mrs. Kim , and Mr. McDowell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Attorney General to report to Congress on Federal, State, and local efforts to combat access device fraud, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Klepto-card and Identity Misuse Act or the SKIM Act .\n#### 2. Sentencing guidelines\nNot later than 30 days after the date of enactment of this Act, the United States Sentencing Commission shall revise of the United States Sentencing Commission Guidelines Manual\u2014\n**(1)**\nin section 2B1.1(b)(11) to provide that\u2014\n**(A)**\nthe baseline increase described in that paragraph shall be an increase by 4 levels; and\n**(B)**\nif the resulting offense level is less than level 14, the offense shall be increased to level 14; and\n**(2)**\nin the notes related to the application of subsection (b) of section 2B1.1, that in a case involving 10 or more counterfeit access devices or unauthorized access devices, loss includes any unauthorized charges made with any such counterfeit access device or unauthorized access device in any amount.\n#### 3. Report to Congress\n##### (a) Report to congress\nNot later than 90 days after the date of the enactment of this Act, the Attorney General, in coordination with the Secretary of Homeland Security, shall submit to the appropriate congressional committees a report on the coordinated efforts of the Department of Homeland Security and Department of Justice, along with State and local law enforcement agencies to prevent, investigate, prosecute, and sentence fraud offenses involving the use of access devices.\n##### (b) Contents\nThe report under this section shall include the following:\n**(1)**\nAn assessment of cooperative operations of Federal and State law enforcement agencies to identify and prosecute fraud involving the use of access devices under subsections (a)(1), (2), (3), (4), and (8), and (b)(2) of section 1029 of title 18, United States Code.\n**(2)**\nAn assessment of technologies and techniques used by perpetrators of fraud using counterfeit access devices, which may facilitate such fraud or prevent its detection by law enforcement personnel.\n**(3)**\nFor the one-year period preceding the report, the number of requests for assistance that State or local law enforcement agencies made to the Department of Justice or the Department of Homeland Security related to fraud involving the use of counterfeit access devices, including the number of such requests for which the Department of Justice or the Department of Homeland Security provided assistance, and the number of such request for which neither agency provided assistance.\n**(4)**\nStates and counties in which fraud involving the use of counterfeit access devices remains unaddressed or of particular concern to the Secretary and Attorney General.\n**(5)**\nLegislative recommendations for cooperation between Federal and State law enforcement agencies to address such fraud.\n**(6)**\nRecommendations on best practices for State and local law enforcement agencies and business owners to combat such fraud.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe terms access device and counterfeit access device have the meaning given such terms in section 1029 of title 18, United States Code.\n**(2)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on the Judiciary of the House of Representatives;\n**(B)**\nthe Committee on the Judiciary of the Senate;\n**(C)**\nthe Committee on Homeland Security of the House of Representatives; and\n**(D)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate.",
      "versionDate": "2025-06-06",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-27T13:25:43Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3810ih.xml"
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
      "title": "SKIM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SKIM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Klepto-card and Identity Misuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Attorney General to report to Congress on Federal, State, and local efforts to combat access device fraud, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:21Z"
    }
  ]
}
```
