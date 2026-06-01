# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6298?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6298
- Title: Safe and Affordable Transit Act
- Congress: 119
- Bill type: HR
- Bill number: 6298
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2026-01-24T09:06:23Z
- Update date including text: 2026-01-24T09:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-26 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-26 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6298",
    "number": "6298",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000483",
        "district": "30",
        "firstName": "Laura",
        "fullName": "Rep. Friedman, Laura [D-CA-30]",
        "lastName": "Friedman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safe and Affordable Transit Act",
    "type": "HR",
    "updateDate": "2026-01-24T09:06:23Z",
    "updateDateIncludingText": "2026-01-24T09:06:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-26",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
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
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-26T18:28:23Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
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
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6298ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6298\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Ms. Friedman (for herself and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to provide for grants to certain urbanized areas for operating costs relating to crime prevention and security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe and Affordable Transit Act .\n#### 2. Operating grants for crime prevention and security\n##### (a) Crime prevention and security\nSection 5321 of title 49, United States Code, is amended\u2014\n**(1)**\nby striking The Secretary and inserting (a) In general.\u2014 The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Operating grants for urbanized areas (1) In general The Secretary may make grants for operating activities for public transportation systems to any entity eligible to receive funds under section 5307, notwithstanding the population requirement under section (a)(1)(D) of such section. (2) Eligible activities Funds made available under this subsection may be used for the following: (A) Hiring additional officers to police on public transportation and transit stations, including the immediate vicinity of stations. (B) Contracting with local police departments to increase officer presence on public transportation and transit stations. (C) Physical infrastructure upgrades that promote public transportation passenger and operator safety (including monitoring devices, operator shields, and other infrastructure changes). (3) Authorization of appropriations There is authorized to be appropriated $50,000,000 for each of fiscal years 2026 through 2030 to carry out this subsection. .\n##### (b) Study required\nThe Secretary of Transportation shall enter into an agreement with Transportation Research Board of the National Academies, to conduct and submit to Congress, in consultation with labor organizations representing frontline transit workers, a study on crime prevention by transit agencies that includes\u2014\n**(1)**\nwhat such agencies are doing to prevent crime;\n**(2)**\nwhat tactics have been successful in deterring crime;\n**(3)**\nwhat tactics have been unsuccessful in deterring crime; and\n**(4)**\nbest practices for transit agencies to reduce crime within public transportation systems.",
      "versionDate": "2025-11-25",
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
        "updateDate": "2025-12-10T18:22:37Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6298ih.xml"
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
      "title": "Safe and Affordable Transit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe and Affordable Transit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to provide for grants to certain urbanized areas for operating costs relating to crime prevention and security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:33:27Z"
    }
  ]
}
```
