# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8430
- Title: Federal and State Food Safety Information Sharing Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8430
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-14T08:08:02Z
- Update date including text: 2026-05-14T08:08:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8430",
    "number": "8430",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Federal and State Food Safety Information Sharing Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:02Z",
    "updateDateIncludingText": "2026-05-14T08:08:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:01:00Z",
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
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "OH"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DC"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CT"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8430ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8430\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Ms. Ross (for herself and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to authorize the Secretary of Health and Human Services to share food safety information with State, local, Tribal, and Territorial authorities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal and State Food Safety Information Sharing Act of 2026 .\n#### 2. Sharing food safety information with State, local, Tribal, and Territorial authorities\n##### (a) In general\nSection 708 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379 ) is amended by adding at the end the following:\n(d) Sharing food safety information with State, local, Tribal, and Territorial authorities (1) Authorization Notwithstanding section 301(j) and any other law, regulation, or policy, the Secretary may share, with a State, local, Tribal, or Territorial authority with counterpart functions related to the protection of public health, unredacted information in the possession of the Food and Drug Administration relating to any of the following: (A) Foodborne illness surveillance data. (B) Laboratory sampling testing information. (C) Inspectional information and results. (D) Distribution lists for recalls and outbreaks. (E) Consumer complaints. (F) Any other information the Secretary determines will assist such authority in protecting the public. (2) Timing The Secretary may share information pursuant to paragraph (1) as soon as is reasonably practicable. (3) Limitation on further disclosure A State, local, Tribal, or Territorial authority in receipt of information provided by the Secretary under this subsection shall not further disclose such information without permission of the Food and Drug Administration unless such authority determines that disclosure of such information is necessary to contain a foodborne illness outbreak, carry out a recall, or carry out other State enforcement activities. (4) Effect of subsection Nothing in this subsection affects the ability of the Secretary to enter into any written agreement authorized by other provisions of law to share confidential information. .\n##### (b) Conforming amendment\nThe first sentence of section 301(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(j) ) is amended\u2014\n**(1)**\nby striking The and inserting Except as provided in section 708(d), the ; and\n**(2)**\nby striking the second period at the end.\n#### 3. Grants to enhance food safety\n##### (a) In general\nSection 1009 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 399 ) is amended\u2014\n**(1)**\nin subsection (d)(1), by striking 3 years and inserting 5 years ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nby striking 3 years and inserting 5 years ; and\n**(B)**\nby amending the second sentence to read as follows: In the event the Secretary conducts a program evaluation, funding in subsequent years of the grant, where applicable, shall be contingent on a successful program evaluation by the Secretary after the first year of the grant. .\n##### (b) Applicability\nThe amendments made by subsection (a) apply only with respect to grants awarded under section 1009 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 399 ) on or after the date of the enactment of this Act.",
      "versionDate": "2026-04-22",
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
        "name": "Health",
        "updateDate": "2026-04-28T20:23:58Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8430ih.xml"
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
      "title": "Federal and State Food Safety Information Sharing Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal and State Food Safety Information Sharing Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to authorize the Secretary of Health and Human Services to share food safety information with State, local, Tribal, and Territorial authorities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:30Z"
    }
  ]
}
```
