# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3060?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3060
- Title: No Biometric Barriers to Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3060
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-10-07T08:05:23Z
- Update date including text: 2025-10-07T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3060",
    "number": "3060",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "No Biometric Barriers to Housing Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:23Z",
    "updateDateIncludingText": "2025-10-07T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "VT"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3060ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3060\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Ms. Clarke of New York (for herself, Ms. Pressley , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit the use of biometric recognition technology in certain federally assisted dwelling units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Biometric Barriers to Housing Act of 2025 .\n#### 2. Prohibition on biometric identification technology\n##### (a) In general\nAt any time after the expiration of the 1-year period beginning on the date of the enactment of this Act, an owner of a covered federally assisted rental dwelling unit, may not use, or authorize the use of, facial recognition technology, physical biometric recognition technology, or remote biometric recognition technology in such dwelling unit or in any building or grounds containing such dwelling unit for the purposes of surveillance or any other use that has an adverse effect on the ability of a tenant to fairly access affordable housing that is free from bias and discrimination.\n##### (b) Definitions\nFor the purposes of this Act:\n**(1) Assistance**\nThe term assistance means any grant, loan, subsidy, contract, cooperative agreement, or other form of financial assistance, but such term does not include the insurance or guarantee of a loan, mortgage, or pool of loans or mortgages.\n**(2) Covered federally assisted rental dwelling unit**\nThe term covered federally assisted rental dwelling unit means a residential dwelling unit that is made available for rental and for which assistance is provided, or that is part of a housing project for which assistance is provided, under\u2014\n**(A)**\nthe public housing program under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. );\n**(B)**\nthe program for rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f );\n**(C)**\nthe HOME Investment Partnerships program under title II of the Cranton-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. );\n**(D)**\ntitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. );\n**(E)**\nthe Housing Trust Fund program under section 1338 of the Housing and Community Development Act of 1992 (12 U.S.C 4568);\n**(F)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q );\n**(G)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 );\n**(H)**\nthe AIDS Housing Opportunities program under subtitle D of title VIII of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12901 et seq. );\n**(I)**\nthe program for Native American housing under the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ); and\n**(J)**\nthe program for housing assistance for Native Hawaiians under title VIII of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4221 et seq. ).\n**(3) Facial recognition technology**\nThe term facial recognition technology means technology which facilitates or otherwise enables an automated or semi-automated process that assists in identifying an individual based on the physical characteristics of an individual\u2019s face, or that logs characteristics of an individual\u2019s face, head, or body to infer emotion, associations, activities, or the location of an individual.\n**(4) Owner**\nThe term owner means any private person or entity, including a cooperative, an agency of the Federal Government, or a public housing agency, having the legal right to lease or sublease dwelling units.\n**(5) Physical biometric recognition technology**\nThe term physical biometric recognition technology means technology which facilitates or otherwise enables an automated or semi-automated process that assists in identifying an individual or capturing information about an individual based on the characteristics of an individual\u2019s DNA, fingerprints, palmprints, iris, or retina.\n**(6) Remote biometric recognition technology**\nThe term remote biometric recognition technology means technology which facilitates or otherwise enables an automated or semi-automated process that assists in identifying an individual or capturing information about an individual based on the characteristics of an individual\u2019s gait, voice, or other immutable characteristic ascertained from a distance, or that logs such characteristics to infer emotion, associations, activities, or the location of an individual.\n#### 3. Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Secretary of Housing and Urban Development shall submit to the Committee on Financial Services of the House of Representative and the Committee on Banking, Housing, and Urban Affairs of the Senate and make available to the public on the website of the Department, a report that describes\u2014\n**(1)**\nany known usage of facial recognition technology, physical biometric recognition technology, or remote biometric recognition technology in any covered federally assisted dwelling unit during the 5 years preceding the date of enactment of this Act;\n**(2)**\nany known adverse effects for tenants associated with any use of the technology described in paragraph (1);\n**(3)**\nthe impact of such technology on the residents of such covered federally assisted rental dwelling units;\n**(4)**\nthe purpose of installing such technologies in such covered federally assisted rental dwelling units;\n**(5)**\ndemographic information about the residents of each covered federally assisted rental dwelling unit where such usage occurred and demographic information about the area surrounding such unit; and\n**(6)**\nthe potential impacts on vulnerable communities, including persons protected under the Fair Housing Act of 1968, of additional usage of facial recognition technology, physical biometric recognition technology, or remote biometric recognition technology in covered federally assisted rental dwelling units, including impacts on resident privacy, civil rights, and fair housing.",
      "versionDate": "2025-04-29",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-21T14:08:35Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3060ih.xml"
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
      "title": "No Biometric Barriers to Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Biometric Barriers to Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of biometric recognition technology in certain federally assisted dwelling units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:24Z"
    }
  ]
}
```
