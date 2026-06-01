# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4419?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4419
- Title: AV Accessibility Act
- Congress: 119
- Bill type: HR
- Bill number: 4419
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-09-11T08:06:40Z
- Update date including text: 2025-09-11T08:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4419",
    "number": "4419",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "AV Accessibility Act",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:40Z",
    "updateDateIncludingText": "2025-09-11T08:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-16T17:01:24Z",
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
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4419ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4419\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Stanton (for himself and Mr. Mast ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prohibit a State from issuing a motor vehicle operator\u2019s license for the operation or use of an ADS-equipped vehicle operating at Level 4 or Level 5 in a manner that discriminates on the basis of disability.\n#### 1. Short title\nThis Act may be cited as the Autonomous Vehicle Accessibility Act or the AV Accessibility Act .\n#### 2. Definitions\nIn this Act:\n**(1) Disability**\nThe term disability has the meaning given the term in section 12102 of title 42, United States Code.\n**(2) Public transportation**\nThe term public transportation has the meaning given the term in section 5302 of title 49, United States Code.\n**(3) Ride-hail ads-equipped vehicle**\nThe term ride-hail ADS-equipped vehicle means an ADS-equipped vehicle that is\u2014\n**(A)**\noffered for pre-arranged transportation services for compensation, using an online-enabled application or electronic platform to connect passengers with vehicles; and\n**(B)**\ndispatched in driverless operation.\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(5) SAE-defined terms**\nThe terms ADS-equipped vehicle , dispatch , Level 4 , Level 5 , and driverless operation have the meanings given such terms in the document titled SAE International Recommended Practice J3016, published in April 2021, or by a revision of that such document subsequently adopted by the Secretary.\n#### 3. Licensing\nIn accordance with title II of the Americans with Disabilities Act ( 42 U.S.C. 12132 ), a State shall not issue a motor vehicle operator\u2019s license for the operation or use of an ADS-equipped vehicle operating at Level 4 or Level 5 in a manner that discriminates on the basis of disability against a qualified individual with a disability.\n#### 4. Accessible infrastructure study\nThe Secretary shall seek to enter into an agreement with the National Academies to conduct a study to\u2014\n**(1)**\ndetermine changes to public transportation infrastructure that would improve the ability of individuals with disabilities to find, access, and use ride-hail ADS-equipped vehicles, including during pickup and dropoff; and\n**(2)**\nidentify options to simplify safe access of ride-hail ADS-equipped vehicles, such as non-visual access for individuals with disabilities, including the consideration of\u2014\n**(A)**\ntechnological solutions for dynamic curb management;\n**(B)**\nsidewalk and roadway design;\n**(C)**\ndedicated pick-up and drop-off zones;\n**(D)**\ncurb extension;\n**(E)**\ninfrastructure design; and\n**(F)**\nother factors that can better enable individuals with disabilities to safely locate, enter, use, and exit ride-hail ADS-equipped vehicles during pickup and dropoff.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated $5,000,000 to carry out section 4, to be available until expended.",
      "versionDate": "2025-07-15",
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
        "updateDate": "2025-09-10T16:47:51Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4419ih.xml"
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
      "title": "AV Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AV Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T11:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Autonomous Vehicle Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T11:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a State from issuing a motor vehicle operator's license for the operation or use of an ADS-equipped vehicle operating at Level 4 or Level 5 in a manner that discriminates on the basis of disability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T11:48:18Z"
    }
  ]
}
```
