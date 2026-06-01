# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/711
- Title: Honoring the victims of Hurricane Helene and expressing condolences and support for the affected communities in western North Carolina, specifically North Carolina's 11th Congressional District, 1 year after the hurricane made landfall in the State on September 27, 2024.
- Congress: 119
- Bill type: HRES
- Bill number: 711
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2025-10-07T08:05:29Z
- Update date including text: 2025-10-07T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-15: Submitted in House

## Actions

- 2025-09-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/711",
    "number": "711",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Honoring the victims of Hurricane Helene and expressing condolences and support for the affected communities in western North Carolina, specifically North Carolina's 11th Congressional District, 1 year after the hurricane made landfall in the State on September 27, 2024.",
    "type": "HRES",
    "updateDate": "2025-10-07T08:05:29Z",
    "updateDateIncludingText": "2025-10-07T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-15",
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
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-09-15T16:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-16T21:44:32Z",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres711ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 711\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Edwards (for himself, Ms. Foxx , Ms. Ross , Mr. Murphy , Ms. Adams , Mr. Harrigan , Mr. McDowell , Mr. Moore of North Carolina , Mr. Knott , Mr. Rouzer , and Mr. Hudson ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nHonoring the victims of Hurricane Helene and expressing condolences and support for the affected communities in western North Carolina, specifically North Carolina\u2019s 11th Congressional District, 1 year after the hurricane made landfall in the State on September 27, 2024.\nThat the House of Representatives\u2014\n**(1)**\nhonors the memory of those who lost their lives as a result of Hurricane Helene;\n**(2)**\nextends its deepest condolences to the families of the victims and to all individuals and communities who continue to suffer in the storm\u2019s aftermath;\n**(3)**\nrecognizes and expresses gratitude for the heroic efforts of first responders, volunteers, and local leaders who have risked their lives to save others and begin the process of recovery;\n**(4)**\naffirms its commitment to supporting the people and communities impacted by Hurricane Helene through disaster relief, recovery, and rebuilding efforts; and\n**(5)**\nencourages the appropriate executive branch agencies to continue to partner with Congress to accelerate recovery of the communities affected by Hurricane Helene.",
      "versionDate": "2025-09-15",
      "versionType": "IH"
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
        "name": "Emergency Management",
        "updateDate": "2025-09-24T17:21:07Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres711ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring the victims of Hurricane Helene and expressing condolences and support for the affected communities in western North Carolina, specifically North Carolina's 11th Congressional District, 1 year after the hurricane made landfall in the State on September 27, 2024.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:22Z"
    },
    {
      "title": "Honoring the victims of Hurricane Helene and expressing condolences and support for the affected communities in western North Carolina, specifically North Carolina's 11th Congressional District, 1 year after the hurricane made landfall in the State on September 27, 2024.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T08:05:35Z"
    }
  ]
}
```
