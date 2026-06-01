# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8699
- Title: Safe Transit for All Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8699
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-22T08:07:26Z
- Update date including text: 2026-05-22T08:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8699",
    "number": "8699",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safe Transit for All Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:26Z",
    "updateDateIncludingText": "2026-05-22T08:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "IN"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8699ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8699\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Min (for himself, Ms. Norton , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require certain recipients of Federal assistance for public transit systems to establish a program to collect data on passenger harassment on public transit systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Transit for All Act of 2026 .\n#### 2. Inclusion of assaults on transit passengers in public transportation safety program\n##### (a) Public transportation agency safety plan\nSection 5329(d) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (I)(ii) by striking the period and inserting ; and ; and\n**(B)**\nby adding at the end the following:\n(J) in the case of a recipient receiving assistance under section 5307 that is serving an urbanized area with a population of 200,000 or more, a program to collect data on street harassment on public transit systems targeted at passengers, including\u2014 (i) establishing accessible digital and in-person reporting mechanisms to collect data from passengers who have experienced or witnessed an incident of street harassment on a public transit system operated by the recipient, including the ability to collect data on\u2014 (I) the frequency, type, location, and time of the incident experienced or witnessed by the passenger, including whether such street harassment was verbal harassment, a physical assault, or a sexual assault; (II) the demographic information of the passenger or passengers that experienced the incident, including race, ethnicity, religion, age, disability, income, primary language, sex, and sexual orientation; (III) the actual or perceived characteristics that may have served as the basis for the incident; and (IV) the impact of the incident on the passenger, including whether and in what way street harassment affects the use of public transit by the passenger; (ii) collecting data and conducting outreach in multiple languages to understand safety concerns and experiences of passengers with limited English language proficiency; (iii) in a timely manner after data is collected pursuant to clauses (i) and (ii), publishing on a publicly available website the data collected, excluding any personally identifiable information; and (iv) establishing protocols for responding to reports of street harassment received through the reporting mechanisms established in clause (i). ; and\n**(2)**\nby adding at the end the following:\n(6) Definition of street harassment In this subsection, the term street harassment means any word, gesture, or other action directed at an individual because of an actual or perceived personal characteristic of the individual, including a characteristic protected under title VI or VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) or the Age Discrimination in Employment Act of 1967 ( 29 U.S.C. 621 et seq. ), in a public place, without the consent of the individual, in which the individual experiences such word, gesture, or action as intimidating or threatening to the safety of the individual. .\n##### (b) National transit database\nSection 5335 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (2) by striking and ;\n**(B)**\nin paragraph (3) by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(4) any data on street harassment of passengers collected by the recipient pursuant to section 5329(d). .",
      "versionDate": "2026-05-07",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-20T20:20:18Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8699ih.xml"
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
      "title": "Safe Transit for All Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Transit for All Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require certain recipients of Federal assistance for public transit systems to establish a program to collect data on passenger harassment on public transit systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:34Z"
    }
  ]
}
```
