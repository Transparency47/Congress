# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6925
- Title: Kennedy Center Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 6925
- Origin chamber: House
- Introduced date: 2025-12-23
- Update date: 2026-02-03T09:06:02Z
- Update date including text: 2026-02-03T09:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-23: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-23: Introduced in House

## Actions

- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-23",
    "latestAction": {
      "actionDate": "2025-12-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6925",
    "number": "6925",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Kennedy Center Protection Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:06:02Z",
    "updateDateIncludingText": "2026-02-03T09:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-23",
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
      "actionDate": "2025-12-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-23",
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
          "date": "2025-12-23T17:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:45:49Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
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
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CT"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "AZ"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
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
      "sponsorshipDate": "2026-01-06",
      "state": "DC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NJ"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6925ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6925\nIN THE HOUSE OF REPRESENTATIVES\nDecember 23, 2025 Mrs. McClain Delaney (for herself, Mr. Larson of Connecticut , Mrs. Hayes , and Mrs. Grijalva ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the removal of any signage or other identification from the John F. Kennedy Center for the Performing Arts that differs from the designation John F. Kennedy Center for the Performing Arts , as designated under section 3 of the John F. Kennedy Center Act ( 20 U.S.C. 76i ), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kennedy Center Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress established the National Cultural Center in 1958 to present musical programs, lectures, and other arts programs for youth and the elderly.\n**(2)**\nOur 35th President, John Fitzgerald Kennedy was particularly devoted to the advancement of the performing arts within the United States.\n**(3)**\nCongress statutorily renamed the National Cultural Center the John F. Kennedy Center for the Performing Arts in 1964 following President Kennedy\u2019s untimely death.\n**(4)**\nOn February 7, 2025, President Trump announced his intention to terminate members of the Kennedy Center and appoint himself as chair, an unprecedented action.\n**(5)**\nOn December 18, 2025, it was announced that the Board of Trustees of the John F. Kennedy Center for the Performing Arts voted unanimously to rename the Center The Donald J. Trump and John F. Kennedy Center for the Performing Arts .\n**(6)**\nCongress itself established the Kennedy Center and its Board of Trustees, and such a vote of the Board is clearly beyond its statutory authority.\n**(7)**\nThe renaming of any Federal building for a sitting President signals a slide towards authoritarianism.\n**(8)**\nCongress itself retains sole authority to rename the John F. Kennedy Center for the Performing Arts through statute.\n#### 3. John F. Kennedy Center for the Performing Arts\n##### (a) In general\nThe reported vote of the Trustees of the John F. Kennedy Center for the Performing Arts on December 18, 2025, renaming the Center as the Donald J. Trump and John F. Kennedy Center for the Performing Arts is hereby void.\n##### (b) Removal\nNot later than 1 day after the date of enactment of this Act, the Trustees of the John F. Kennedy Center for the Performing Arts shall remove any signage or other identification from the John F. Kennedy Center for the Performing Arts that differs from the designation John F. Kennedy Center for the Performing Arts , as designated under section 3 of the John F. Kennedy Center Act ( 20 U.S.C. 76i ).\n##### (c) References\nAny reference in a law, map, regulation, document, paper, publication, signage, or other record of the United States to the John F. Kennedy Center for the Performing Arts changed after the vote described in subsection (a) shall return to the name John F. Kennedy Center for the Performing Arts .\n##### (d) Restriction on Board authority\nSection 5 of the John F. Kennedy Center Act ( 20 U.S.C. 76k ) is amended by adding at the end the following:\n(h) Restrictions on Board authority The Board may not undertake any vote or proposal or authorize any action to rename the John F. Kennedy Center for the Performing Arts. .\n##### (e) Reporting on funds used\nNot later than 30 days after the date of enactment of this Act, the Trustees of the John F. Kennedy Center for the Performing Arts shall submit to Congress a report detailing any public or private funds used to install, alter, or implement the change in the name of the John F. Kennedy Center for the Performing Arts.",
      "versionDate": "2025-12-23",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2026-01-27T13:24:14Z"
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
      "date": "2025-12-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6925ih.xml"
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
      "title": "Kennedy Center Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kennedy Center Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the removal of any signage or other identification from the John F. Kennedy Center for the Performing Arts that differs from the designation \"John F. Kennedy Center for the Performing Arts\", as designated under section 3 of the John F. Kennedy Center Act (20 U.S.C. 76i), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T09:18:24Z"
    }
  ]
}
```
