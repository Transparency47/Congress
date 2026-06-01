# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4499?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4499
- Title: ALERT Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4499
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-21T20:14:44Z
- Update date including text: 2026-05-21T20:14:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4499",
    "number": "4499",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "ALERT Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T20:14:44Z",
    "updateDateIncludingText": "2026-05-21T20:14:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-12",
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
        "item": [
          {
            "date": "2026-05-12T13:52:41Z",
            "name": "Referred To"
          },
          {
            "date": "2026-05-12T13:52:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4499is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4499\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Tillis (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to require the Secretary of Health and Human Services to expand and enhance the National Healthcare Safety Network to establish real-time infectious disease and public health surveillance capabilities across nursing homes in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advanced Long-term care Early Response Technology Act of 2026 or the ALERT Act of 2026 .\n#### 2. National network of real-time infectious disease and public health surveillance in nursing homes\nPart B of title III of the Public Health Service Act is amended by inserting after section 319M (42 U.S.C. 247d\u2013f) the following:\n319N. Enhancement of National Healthcare Safety Network for real-time surveillance in nursing homes (a) In general Not later than 180 days after the date of enactment of the Advanced Long-term care Early Response Technology Act of 2026 , the Secretary, acting through the Director of the Centers for Disease Control and Prevention (referred to in this section as the Secretary ), shall carry out a 5-year program to expand and enhance the National Healthcare Safety Network (referred to in this section as the NHSN ) to establish real-time infectious disease and public health surveillance capabilities across nursing homes in the United States. (b) Contracting authority (1) In general The Secretary may enter into one or more contracts with an eligible entity to develop, implement, and operate the technological and analytic infrastructure necessary to provide real-time surveillance and rapid notification capabilities under the NHSN. (2) Eligibility To be eligible to enter into a contract with the Secretary under paragraph (1), an entity\u2014 (A) shall be located in, or shall be a subsidiary of an entity that is located in, the United States; (B) shall have, and shall maintain for the period of the contract, HITRUST r2 certification (or a successor certification); (C) shall not be an electronic medical records company; and (D) shall demonstrate experience in establishing and operating a public health surveillance network that monitors infectious diseases or other public health threats at the State or local level. (c) Required capabilities Any contract entered into under subsection (b) shall\u2014 (1) ensure that the infrastructure developed pursuant to the contract is capable of\u2014 (A) providing real-time monitoring of emerging infectious diseases and other public health threats among nursing homes nationwide; (B) integrating with, and enhancing, the reporting systems of the NHSN; (C) establishing a central hub of epidemiologists and other public health professionals to support rapid identification of outbreaks; (D) providing for immediate notification to appropriate Federal, State, and local health authorities; and (E) supporting the implementation of a staffed care management program that skilled nursing facilities may opt into; (2) ensure appropriate privacy protections for individual patient data; and (3) prohibit the use of data collected or generated under the contract for regulatory compliance or enforcement purposes unless expressly authorized by law. (d) HIPAA and data protections The entity awarded a contract under subsection (b)\u2014 (1) shall be treated as a covered entity (as defined in section 160.103 of title 45, Code of Federal Regulations (or successor regulations)) for purposes of the privacy regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996; and (2) shall comply with all applicable Federal privacy and security requirements. (e) Study and report At the end of the period of the program described in subsection (a), the Secretary shall conduct, and submit to Congress a report that describes the results of, a study on\u2014 (1) the effectiveness of the enhanced NHSN system in monitoring infectious diseases and public health threats in nursing homes; (2) the impact of the enhanced NHSN system on hospitalization rates and patient outcomes; and (3) recommendations regarding continuation or expansion of the program under this section. (f) Authorization of appropriations To carry out this section, there is authorized to be appropriated such sums as may be necessary for each of fiscal years 2027 through 2031. .\n#### 3. Supporting of real-time infections disease and public health surveillance network for nursing homes\nSection 1115A(b)(2)(B) of the Social Security Act ( 42 U.S.C. 1315a(b)(2)(B) ) is amended by adding at the end the following new clause:\n(xxviii) Supporting the adoption by the National Healthcare Safety Network of technology to improve infectious disease surveillance in nursing homes that\u2014 (I) has capabilities for immediate detection and reporting of infectious disease outbreaks; (II) facilitates coordinated responses with local, State, and Federal public health authorities; and (III) enables nursing homes to participate in a staffed care management program to improve resident health outcomes. .",
      "versionDate": "2026-05-12",
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
        "name": "Health",
        "updateDate": "2026-05-21T20:14:44Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4499is.xml"
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
      "title": "ALERT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ALERT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T02:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advanced Long-term care Early Response Technology Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T02:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to require the Secretary of Health and Human Services to expand and enhance the National Healthcare Safety Network to establish real time infectious disease and public health surveillance capabilities across nursing homes in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:26Z"
    }
  ]
}
```
