# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5889
- Title: Eviction Helpline Act
- Congress: 119
- Bill type: HR
- Bill number: 5889
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-03-19T08:06:45Z
- Update date including text: 2026-03-19T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5889",
    "number": "5889",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Eviction Helpline Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:06:45Z",
    "updateDateIncludingText": "2026-03-19T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:03:50Z",
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
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5889ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5889\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Pressley introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo create a hotline to provide eviction-related assistance.\n#### 1. Short title\nThis Act may be cited as the Eviction Helpline Act .\n#### 2. Eviction information\n##### (a) Hotline\nThe Secretary shall, not later than 1 year after the date of the enactment of this Act, establish a hotline to provide assistance with regard to eviction-related matters to tenants of covered federally assisted rental dwelling units.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section such sums as may be necessary for fiscal year 2026 and each fiscal year thereafter.\n#### 3. Definitions\n##### (a)\nFor purposes of this Act:\n**(1) Assistance**\nThe term assistance means any grant, loan, subsidy, contract, cooperative agreement, or other form of financial assistance, but such term does not include the insurance or guarantee of a loan, mortgage, or pool of loans or mortgages.\n**(2) Covered federally assisted rental dwelling unit**\nThe term covered federally assisted rental dwelling unit means a residential dwelling unit that\u2014\n**(A)**\nis made available for rental; and\n**(B)**\n**(i)**\nfor which assistance is provided, or that is part of a housing project for which assistance is provided, under any program administered by the Secretary of Housing and Urban Development, including\u2014\n**(I)**\nthe public housing program under the United States Housing Act of 1937 21 ( 42 U.S.C. 1437 et seq. );\n**(II)**\nthe program for rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f );\n**(III)**\nthe HOME Investment Partnerships program under title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. );\n**(IV)**\ntitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. );\n**(V)**\nthe Housing Trust Fund program under section 1338 of the Housing and Community Development Act of 1992 ( 12 U.S.C. 4568 );\n**(VI)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q );\n**(VII)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 );\n**(VIII)**\nthe AIDS Housing Opportunities program under subtitle D of title VIII of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12901 et seq. );\n**(IX)**\nthe program for Native American housing under the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ); and\n**(X)**\nthe program for housing assistance for Native Hawaiians under title VIII of the Native American Housing Assistance and Self-Determination Act of 1996 7 ( 25 U.S.C. 4221 et seq. ); or\n**(ii)**\nis a property, or is on or in a property, that has a federally backed mortgage loan or federally backed multifamily mortgage loan, as 11 such terms are defined in section 4024(a) of the CARES Act ( 15 U.S.C. 9058(a) ).\n**(3) Secretary**\nThe term Secretary means Secretary of Housing and Urban Development.",
      "versionDate": "2025-10-31",
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
        "updateDate": "2025-11-19T14:21:38Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5889ih.xml"
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
      "title": "Eviction Helpline Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eviction Helpline Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To create a hotline to provide eviction-related assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:18:16Z"
    }
  ]
}
```
