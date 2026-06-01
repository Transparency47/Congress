# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2558
- Title: The National Quantum Cybersecurity Migration Strategy Act of 2025.
- Congress: 119
- Bill type: S
- Bill number: 2558
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-09-18T20:15:41Z
- Update date including text: 2025-09-18T20:15:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2558",
    "number": "2558",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "The National Quantum Cybersecurity Migration Strategy Act of 2025.",
    "type": "S",
    "updateDate": "2025-09-18T20:15:41Z",
    "updateDateIncludingText": "2025-09-18T20:15:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-30T23:08:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2558is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2558\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Peters (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Subcommittee on the Economic and Security Implications of Quantum Information Science to assess possible migration by Federal agencies to post-quantum cryptography, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the The National Quantum Cybersecurity Migration Strategy Act of 2025. .\n#### 2. Definitions\nIn this Act:\n**(1) Cryptography**\nThe term cryptography has the meaning given such term in the National Institute of Standards and Technology Special Publication 1800\u201321B (relating to mobile device security) and the National Institute of Standards and Technology Special Publication 800\u201359 (relating to guidelines for identifying an information system as a national security system).\n**(2) Classical computer**\nThe term classical computer means a device that accepts digital data and manipulates the data based on a program or sequence of instructions for how such data is to be processed, and that encodes information in binary.\n**(3) Quantum computer**\nThe term quantum computer means a computer that uses the collective properties of quantum states, such as superposition, interference, and entanglement, to perform calculations.\n**(4) Post-Quantum Cryptography**\nThe term post-quantum cryptography means cryptographic algorithms or methods that are not specifically vulnerable to attacks by either a quantum computer or classical computer.\n**(5) Critical Infrastructure**\nThe term critical infrastructure has the meaning given that term in section 1016(e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c(e) ).\n**(6) High-impact system**\nThe term high-impact system means a Federal information system that holds sensitive information, the loss of which would be categorized as high impact under Federal Information Processing Standards Publication 199 (relating to standards for security categorization of Federal information and information systems), as in effect on the day before the date of the enactment of this Act.\n**(7) Sector risk management agency**\nThe term sector risk management agency has the meaning given the term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n#### 3. Strategy for Federal agency migration to post-quantum cryptography\n##### (a) Duties of Subcommittee on the Economic and Security Implications of Quantum Information Science\nNot later than 180 days after the date of the enactment of this Act, the Subcommittee on the Economic and Security Implications of Quantum Information Science, as established by section 105 of the National Quantum Initiative Act ( 15 U.S.C. 8814a ), in coordination with the Director of the National Institute of Standards and Technology and in consultation with the Quantum Economic Development Consortium, shall develop a National Quantum Cybersecurity Migration Strategy that includes the following:\n**(1)**\nA definition of a cryptographically relevant quantum computer.\n**(2)**\nRecommended standards for Federal agencies to apply to determine whether a quantum computer meets such definition, including\u2014\n**(A)**\nthe characteristics of such computers; and\n**(B)**\nthe particular point at which such computers are capable of attacking real world cryptographic systems that classical computers are unable to attack.\n**(3)**\nAn assessment of the urgency for migration to post-quantum cryptography for each Federal agency relative to\u2014\n**(A)**\nthe critical functions of each agency; and\n**(B)**\nthe risk each agency faces should a cryptographically relevant quantum computer attack a system operated by the agency.\n**(4)**\nPerformance measures for migration to post-quantum cryptography to be used by each Federal agency for each of the following 4 stages of migration:\n**(A)**\nPreparation for migration to post-quantum cryptography.\n**(B)**\nEstablishment of a baseline understanding of the data inventory.\n**(C)**\nPlanning and execution of post-quantum cryptographic solutions, including ensuring that data at rest and in motion is subject to appropriate protections.\n**(D)**\nMonitoring and evaluation of migration success and assessment of cryptographic security.\n**(5)**\nA plan for evaluating and monitoring entities that are at high risk of quantum cryptographic attacks, including entities determined to be providers of critical infrastructure.\n##### (b) Post-Quantum pilot program\nNot later than 180 days after the date of the enactment of this Act, the Subcommittee on the Economic and Security Implications of Quantum Information Science shall establish a post-quantum pilot program that requires each sector risk management agency to upgrade not less than one high-impact system to post-quantum cryptography not later than January 1, 2027.\n##### (c) Duties of the Office of Electronic Government\nNot later than 180 days after the date of the enactment of this Act, the Administrator of the Office of Electronic Government, in coordination with the Subcommittee on the Economic and Security Implications of Quantum Information Science, shall\u2014\n**(1)**\nsurvey the heads of Federal agencies for information relating to the cost of migration to post-quantum cryptography by the Federal agencies, including estimates for the personnel, equipment, and time needed to fully implement post-quantum cryptography, in alignment with the National Quantum Cybersecurity Migration Strategy developed pursuant to subsection (a);\n**(2)**\nverify that the information provided under paragraph (1) is realistic and fiscally sound;\n**(3)**\nidentify the funding and resources necessary for Federal agencies to carry out the migration to post-quantum cryptography; and\n**(4)**\nadvise on how Federal agencies should encourage the adoption of post-quantum cryptography by the private sector.\n##### (d) Report to Congress\nNot later than 1 year after the date of the enactment of this Act, the Director of the Office of Management and Budget and the Subcommittee on the Economic and Security Implications of Quantum Information Science shall jointly submit to Congress a report detailing their findings with respect to the post-quantum migration assessments required under subsection (a)(3), the pilot program established pursuant to subsection (b), and the survey on associated costs of executing the migration required by subsection (c)(1).\n##### (e) Assessment by Comptroller General\nNot later than 1 year after the development of the National Quantum Cybersecurity Migration Strategy under subsection (a), and annually thereafter, the Comptroller General of the United States shall submit to Congress an assessment, using the performance measures described in subsection (a)(4), of the progress made by each Federal agency in migrating to post-quantum cryptography.",
      "versionDate": "2025-07-30",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-18T20:15:41Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2558is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "The National Quantum Cybersecurity Migration Strategy Act of 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "The National Quantum Cybersecurity Migration Strategy Act of 2025.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Subcommittee on the Economic and Security Implications of Quantum Information Science to assess possible migration by Federal agencies to post-quantum cryptography, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:38Z"
    }
  ]
}
```
