# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4942?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4942
- Title: Quantum Encryption Readiness and Resilience Act
- Congress: 119
- Bill type: HR
- Bill number: 4942
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-09-18T20:15:01Z
- Update date including text: 2025-09-18T20:15:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4942",
    "number": "4942",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Quantum Encryption Readiness and Resilience Act",
    "type": "HR",
    "updateDate": "2025-09-18T20:15:01Z",
    "updateDateIncludingText": "2025-09-18T20:15:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "MI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NC"
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
      "sponsorshipDate": "2025-09-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4942ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4942\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Subramanyam (for himself, Mr. McGuire , Ms. Stevens , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the Subcommittee on the Economic and Security Implications of Quantum Information Science to submit reports on mitigating the cybersecurity and national security risks posed by certain quantum computers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Encryption Readiness and Resilience Act .\n#### 2. Reports on mitigating the cybersecurity and national security risks posed by certain quantum computers\n##### (a) Initial report\nNot later than one year after the date of the enactment of this Act, the Subcommittee on the Economic and Security Implications of Quantum Information Science established under section 105 of the National Quantum Initiative Act ( 15 U.S.C. 8814a ) shall carry out the following:\n**(1)**\nConduct an assessment of each of the following:\n**(A)**\nThe capabilities and progress of the United States, relative to other countries, with respect to the following:\n**(i)**\nDeveloping a cryptographically-relevant quantum computer.\n**(ii)**\nAdopting security and preparedness measures, including post-quantum cryptography, to mitigate the cybersecurity and national security risks posed by such computer.\n**(B)**\nThe progress of private sector entities and public sector entities in the United States toward adopting such measures, including the progress toward implementing the guidance under section 4 of the Quantum Computing Cybersecurity Preparedness Act ( 6 U.S.C. 1526 ).\n**(2)**\nIdentify the sectors of the economy most vulnerable to such risks.\n**(3)**\nBased upon such assessments and such identification, develop a plan to mitigate such risks, including by carrying out the following:\n**(A)**\nFacilitating collaboration between agencies and departments of the Federal Government.\n**(B)**\nFacilitating the exchange of information between such private sector entities and public sector entities.\n**(C)**\nForming partnerships between the Federal Government and such private sector entities.\n**(D)**\nIdentifying such measures that such private sector entities and public sector entities may adopt.\n**(E)**\nSupporting such exchange and the adoption of such measures, including by identifying actions, including piloting projects, providing technical assistance, and publishing cyber hygiene guidance for such private sector entities, that such agencies and departments may carry out to support such exchange and adoption.\n**(4)**\nDevelop guidelines for determining whether a quantum computer is a cryptographically-relevant quantum computer.\n**(5)**\nSubmit to the appropriate committees of Congress a report in classified or unclassified form, as appropriate, that includes information relating to the following:\n**(A)**\nThe assessments conducted under paragraph (1).\n**(B)**\nThe sectors identified under paragraph (2).\n**(C)**\nThe plan developed under paragraph (3).\n**(D)**\nThe guidelines developed under paragraph (4).\n**(E)**\nRecommendations for the following:\n**(i)**\nA timetable to implement such plan.\n**(ii)**\nPolicies to implement such plan that require legislation.\n**(iii)**\nPolicies to implement such plan that do not require legislation.\n##### (b) Subsequent reports\nNot later than one year after the report under subsection (a) is submitted and annually thereafter for four years, the Subcommittee referred to in such subsection shall submit to Congress a report in classified or unclassified form, as appropriate, that includes information relating to the progress of private sector entities and public sector entities in the United States toward adopting the measures described in such subsection.\n##### (c) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress has the meaning given such term in section 2 of the National Quantum Initiative Act ( 15 U.S.C. 8801 ).\n**(2) Classical computer; post-quantum cryptography; quantum computer**\nThe terms classical computer , post-quantum cryptography , and quantum computer have the meanings given such terms in section 3 of the Quantum Computing Cybersecurity Preparedness Act ( 6 U.S.C. 1526 note).\n**(3) Cryptographically-relevant quantum computer**\nThe term cryptographically-relevant quantum computer means a quantum computer with the ability to compromise a cryptographic system that a classical computer is unable to compromise.",
      "versionDate": "2025-08-08",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-18T20:15:01Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4942ih.xml"
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
      "title": "Quantum Encryption Readiness and Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quantum Encryption Readiness and Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Subcommittee on the Economic and Security Implications of Quantum Information Science to submit reports on mitigating the cybersecurity and national security risks posed by certain quantum computers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:26Z"
    }
  ]
}
```
