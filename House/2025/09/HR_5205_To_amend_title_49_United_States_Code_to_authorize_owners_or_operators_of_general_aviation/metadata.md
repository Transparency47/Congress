# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5205
- Title: Aircraft Noise Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 5205
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-10-07T08:05:34Z
- Update date including text: 2025-10-07T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-09 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-09 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5205",
    "number": "5205",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Aircraft Noise Reduction Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:34Z",
    "updateDateIncludingText": "2025-10-07T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-09T21:42:03Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "WA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "HI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5205ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5205\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Neguse (for himself, Mr. Khanna , Ms. Jayapal , Mr. Moulton , Mr. Case , Mr. Levin , and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to authorize owners or operators of general aviation airports to impose certain restrictions relating to aircraft noise, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aircraft Noise Reduction Act .\n#### 2. Authority of general aviation airports to restrict flights for purposes of implementing aircraft noise limitations\n##### (a) In general\nSubchapter II of chapter 475 of title 49, United States Code, is amended by adding at the end the following:\n47535. Authority of general aviation airports to restrict flights for purposes of implementing aircraft noise limitations (a) In general Notwithstanding any other provision of this chapter, for purposes of implementing aircraft noise limitations, the Administrator of the Federal Aviation Administration shall consult with an owner or operator of a general aviation airport, upon request by such owner or operator, to provide for reasonable adjustments to air traffic and training patterns of noncommercial charter flights so long as such adjustments do not otherwise violate law. (b) Community input In implementing reasonable accommodations under subsection (a), an owner or operator of a general aviation airport and the Administrator shall take into account input received from individuals or entities in communities surrounding the airport. (c) Federal funding No Federal funds, including a grant under this chapter, may be withheld from, withdrawn from, or denied to a general aviation airport based solely on an activity carried out by an owner or operator of such airport under this section. (d) Emergencies The Administrator may reject or temporarily restrict an accommodation under subsection (a), as necessary, in the case of an emergency. (e) Definition of general aviation airport In this section, the term general aviation airport means a noncertified airport covered by part 139 of title 14, Code of Federal Regulations. .\n##### (b) Analysis\nThe analysis for subchapter II of chapter 475 of title 49, United States Code, is amended by adding at the end the following:\n47535. Authority of general aviation airports to restrict flights for purposes of implementing aircraft noise limitations. .\n##### (c) Regulatory updates\nThe Secretary of Transportation shall issue such regulations as are necessary to update part 150 and part 161 of title 14, Code of Federal Regulations, to allow the owners and operators of general aviation airports to implement effective noise abatement measures, as determined appropriate by such owners and operators.",
      "versionDate": "2025-09-08",
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
        "updateDate": "2025-09-23T17:48:52Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5205ih.xml"
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
      "title": "Aircraft Noise Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aircraft Noise Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-12T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to authorize owners or operators of general aviation airports to impose certain restrictions relating to aircraft noise, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T06:48:23Z"
    }
  ]
}
```
