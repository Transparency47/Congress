# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2049
- Title: NTIA Policy and Cybersecurity Coordination Act
- Congress: 119
- Bill type: S
- Bill number: 2049
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-12-03T13:34:03Z
- Update date including text: 2025-12-03T13:34:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2049",
    "number": "2049",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "NTIA Policy and Cybersecurity Coordination Act",
    "type": "S",
    "updateDate": "2025-12-03T13:34:03Z",
    "updateDateIncludingText": "2025-12-03T13:34:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T15:44:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "WV"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "UT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2049is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2049\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Hickenlooper (for himself, Mrs. Capito , Mr. Curtis , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the National Telecommunications and Information Administration Organization Act to establish the Office of Policy Development and Cybersecurity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NTIA Policy and Cybersecurity Coordination Act .\n#### 2. Policy development and cybersecurity\n##### (a) Office of Policy Development and Cybersecurity\nPart A of title I of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 901 et seq. ) is amended by adding at the end the following:\n106. Office of Policy Development and Cybersecurity (a) Establishment There shall be within the NTIA an office to be known as the Office of Policy Development and Cybersecurity (in this section referred to as the Office ). (b) Associate Administrator The head of the Office shall be an Associate Administrator for Policy Development and Cybersecurity (in this section referred to as the Associate Administrator ), who shall report to the Assistant Secretary. (c) Duties (1) In general The Associate Administrator shall oversee and conduct national communications and information policy analysis and development for the internet and communications technologies. (2) Particular duties In carrying out paragraph (1), the Office shall\u2014 (A) develop, analyze, and advocate for market-based policies that promote innovation, competition, consumer access, digital inclusion, workforce development, and economic growth in the communications, media, and technology markets; (B) conduct studies, as delegated by the Assistant Secretary or required by Congress, on how individuals in the United States access and use the internet, wireline and wireless telephony, mass media, other digital services, and video services; (C) coordinate transparent, consensus-based, multistakeholder processes to create guidance for and to support the development and implementation of cybersecurity and privacy policies with respect to the internet and other communications networks; (D) promote increased collaboration between security researchers and providers of communications services and software system developers; (E) perform such duties as the Assistant Secretary considers appropriate relating to the program for preventing future vulnerabilities established under section 8(a) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1607(a) ); (F) advocate for policies that promote the security and resilience to cybersecurity incidents of communications networks while fostering innovation, including policies that promote secure communications network supply chains; (G) at the direction of the Assistant Secretary, present security of the digital economy and infrastructure and cybersecurity policy efforts before the Commission, Congress, and elsewhere; (H) provide advice and assistance to the Assistant Secretary in carrying out the policy responsibilities of the NTIA with respect to cybersecurity policy matters, including the evaluation of the impact of cybersecurity matters pending before the Commission, other Federal agencies, and Congress; (I) in addition to the duties described in subparagraph (H), perform such other duties regarding the policy responsibilities of the NTIA with respect to cybersecurity policy matters as the Assistant Secretary considers appropriate; (J) develop policies to accelerate innovation and commercialization with respect to advances in technological understanding of communications technologies; (K) identify barriers to trust, security, innovation, and commercialization with respect to communications technologies, including access to capital and other resources, and ways to overcome such barriers; (L) provide public access to relevant data, research, and technical assistance on innovation and commercialization with respect to communications technologies, consistent with the protection of classified information; (M) strengthen collaboration on and coordination of policies relating to innovation and commercialization with respect to communications technologies, including policies focused on the needs of small businesses and rural communities\u2014 (i) within the Department of Commerce; (ii) between the Department of Commerce and State government agencies, as appropriate; and (iii) between the Department of Commerce and the Commission or any other Federal agency the Assistant Secretary determines to be necessary; and (N) solicit and consider feedback from small and rural communications service providers, as appropriate. .\n##### (b) Transitional rules\n**(1) Redesignation of Associate Administrator; continuation of service**\n**(A) Redesignation**\nThe position of Associate Administrator for Policy Analysis and Development at the NTIA is redesignated as the position of Associate Administrator for Policy Development and Cybersecurity.\n**(B) Continuation of service**\nThe individual serving as Associate Administrator for Policy Analysis and Development at the NTIA on the day before the date of enactment of this Act shall become, as of such date of enactment, the Associate Administrator for Policy Development and Cybersecurity.\n**(2) NTIA defined**\nIn this subsection, the term NTIA means the National Telecommunications and Information Administration.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-15",
        "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1766",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NTIA Policy and Cybersecurity Coordination Act",
      "type": "HR"
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
        "updateDate": "2025-07-07T13:37:39Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2049is.xml"
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
      "title": "NTIA Policy and Cybersecurity Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NTIA Policy and Cybersecurity Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Telecommunications and Information Administration Organization Act to establish the Office of Policy Development and Cybersecurity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:22Z"
    }
  ]
}
```
