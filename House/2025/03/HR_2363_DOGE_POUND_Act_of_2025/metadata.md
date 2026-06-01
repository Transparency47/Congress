# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2363
- Title: DOGE POUND Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2363
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-05-14T14:07:55Z
- Update date including text: 2025-05-14T14:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2363",
    "number": "2363",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "DOGE POUND Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-14T14:07:55Z",
    "updateDateIncludingText": "2025-05-14T14:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:02:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "LA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2363ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2363\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Ms. DeGette (for herself, Mr. Goldman of New York , Mr. Carter of Louisiana , Ms. Pressley , and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the authorization of certain individuals to access certain systems containing individually identifiable health information.\n#### 1. Short title\nThis Act may be cited as the Data Of Government health Entities must be Protected from Overreach by Unelected Nonsecure Disruption Act of 2025 or the DOGE POUND Act of 2025 .\n#### 2. Prohibiting the authorization of certain individuals to access certain systems containing individually identifiable health information\n##### (a) In general\nNotwithstanding any other provision of law, no individual may be authorized to use, exercise administrative control over, or otherwise access any specified system (as defined in subsection (d)), or any data from any such system, unless\u2014\n**(1)**\nsuch individual is an officer, employee, or contractor of the Department of Health and Human Services who\u2014\n**(A)**\nwas otherwise eligible to access such system or data prior to January 20, 2025; and\n**(B)**\ncontinued to be otherwise eligible to access such system or data between January 20, 2025, and the date of access to such system or data; or\n**(2)**\nin the case of an individual not described in paragraph (1)\u2014\n**(A)**\nsuch individual holds a security clearance at the appropriate level with respect to such system or data and such clearance was granted pursuant to the procedures established under section 801 of the National Security Act of 1947 ( 50 U.S.C. 3161 );\n**(B)**\nsuch individual\u2019s access to such system or data, or use thereof, does not constitute a violation of section 208 of title 18, United States Code (determined after the application of subsection (b));\n**(C)**\nsuch individual is not a special Government employee (as defined in section 202 of title 18, United States Code);\n**(D)**\nsuch individual\u2019s current continuous service in the civil service (as that term is defined in section 2101 of title 5, United States Code) as of the date of such access is for a period of at least 1 year;\n**(E)**\nsuch individual has completed any required training or compliance procedures with respect to privacy laws and cybersecurity and national security regulations and best practices; and\n**(F)**\nsuch individual has signed a written ethics agreement with either the Department of Health and Human Services or the Office of Government Ethics.\n##### (b) Application of penalties\n**(1) In general**\nWhoever knowingly\u2014\n**(A)**\nuses, exercises administrative control over, or otherwise accesses any system or data described in subsection (a) in violation of such subsection, or\n**(B)**\nauthorizes the use, exercise of administrative control over, or other access to any system or data described in subsection (a) in violation of such subsection,\nshall be imprisoned not more than 5 years or fined under title 18, United States Code, or both.\n**(2) Statute of limitations**\nNotwithstanding section 3282 of title 18, United States Code, no person shall be prosecuted, tried, or punished for any offense under this subsection unless the indictment is found or the information is instituted not later than 10 years after the date on which the offense was committed.\n##### (c) Reports on unauthorized use\nThe Inspector General of the Department of Health and Human Services shall investigate, and submit a report to Congress on such investigation, each instance of unauthorized use or other access of any specified system. Any such report shall be submitted not later than 30 days after any such instance and shall include\u2014\n**(1)**\na detailed description of the unauthorized use or access, including any actions the individual carried out;\n**(2)**\na risk assessment of any threat to privacy, national security, cybersecurity, or the integrity of the applicable system as a result of such unauthorized use or access; and\n**(3)**\na detailed description of any stopped payments during the unauthorized use or access.\n##### (d) Specified system\nFor purposes of this section, the term specified system means any system maintained by the Department of Health and Human Services that contains individually identifiable health information (as defined in section 1171(6) of the Social Security Act ( 42 U.S.C. 1320d(6) )).",
      "versionDate": "2025-03-26",
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
        "name": "Commerce",
        "updateDate": "2025-05-14T14:07:55Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2363ih.xml"
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
      "title": "DOGE POUND Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DOGE POUND Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Of Government health Entities must be Protected from Overreach by Unelected Nonsecure Disruption Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the authorization of certain individuals to access certain systems containing individually identifiable health information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:21Z"
    }
  ]
}
```
